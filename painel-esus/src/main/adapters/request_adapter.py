from typing import Callable

import json

from flask import request as FlaskRequest
from werkzeug.datastructures import MultiDict
from src.presentations.http_types import HttpRequest, HttpResponse


def request_adapter(request: FlaskRequest, controller: Callable) -> HttpResponse:
    http_request = create_request_adapter(request)
    http_response = controller(http_request)
    return http_response


NUMERICOS = {"cnes", "equipe", "page", "itemsPerPage", "size", "limit", "offset"}


def _parametros_seguros(args) -> MultiDict:
    """Os repositorios montam SQL por f-string: nada do usuario chega a eles sem tratar."""
    seguros = MultiDict()
    for chave, valores in args.lists():
        for valor in valores:
            if chave in NUMERICOS:
                if valor.strip().isdigit():
                    seguros.add(chave, valor.strip())
            elif chave == "sort[]":
                try:
                    item = json.loads(valor)
                except ValueError:
                    continue
                if isinstance(item, dict) and str(item.get("field", "")).replace("_", "").isalnum() and item.get("direction", "asc") in ("asc", "desc"):
                    seguros.add(chave, json.dumps({"field": item["field"], "direction": item.get("direction", "asc")}))
            else:
                seguros.add(chave, valor.replace("'", "''"))
    return seguros


def create_request_adapter(request: FlaskRequest) -> HttpRequest:

    body = None
    if request.data:
        body = request.json

    return HttpRequest(
        body=body,
        headers=request.headers,
        query_params=_parametros_seguros(request.args),
        path_params=request.view_args,
        url=request.full_path,
    )
