# pylint: disable=invalid-name,R0913
import datetime
import logging
import os
from functools import wraps
from typing import List

import jwt
from flask import Request, jsonify, request
from src.errors import HttpBadTokenError
from src.errors.logging import logging
from src.main.adapters.request_adapter import HttpResponse


def _dentro_do_escopo(payload) -> bool:
    """Administrador ve tudo; os demais, a propria unidade e os numeros gerais, nunca lista nominal de outra unidade."""
    perfis = payload.get("profiles") or []
    if perfis == "admin" or "admin" in perfis:
        return True
    ubs = payload.get("ubs")
    if not isinstance(ubs, int):
        return False
    cnes = (request.view_args or {}).get("cnes")
    if cnes is None:
        return "nominal" not in request.path
    return str(cnes) == str(ubs)


def login_required(f):
    """So exige token valido: serve ao que acontece antes da escolha do perfil."""
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            check_token(request)
        except Exception:
            return jsonify({"message": "Token is missing or invalid."}), 401
        return f(*args, **kwargs)

    return decorated


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        response = HttpResponse(body=None, status_code=0)
        try:
            payload = check_token(request)
            if not _dentro_do_escopo(payload):
                return jsonify({"message": "Access not allowed for this profile."}), 403
            return f(*args, **kwargs)
        except HttpBadTokenError as exc:
            response.body = {"message": "Bad token was given."}
            response.status_code = exc.status_code
            logging.exception(exc)
        except IndexError as exc:
            response.body = {"message": "Token is missing."}
            response.status_code = 401
            logging.exception(exc)
        except Exception as exc:
            response.body = {"message": "Bearer token malformed."}
            logging.exception(exc)
            response.status_code = 401
        return jsonify(response.body), response.status_code

    decorated.__name__ = f.__name__
    return decorated


def extract_token(token: str):
    auth_header = token
    if auth_header:
        return auth_header.split(" ")[1]
    raise HttpBadTokenError("Bad Token")


def check_token_str(_request: str) -> HttpResponse:
    auth_header = _request
    if auth_header:
        return validate_token(auth_header)

    raise HttpBadTokenError("Token is missing")


def check_token(_request: Request) -> HttpResponse:
    auth_header = _request.headers.get("Authorization")
    if auth_header:
        auth_token = auth_header.split(" ")[1]
        if not auth_token:
            raise HttpBadTokenError("Bad Token")
        return validate_token(auth_token)

    raise HttpBadTokenError("Token is missing")


def validate_token(auth_token: str):
    return jwt.decode(
        auth_token, os.environ["SECRET_TOKEN"], algorithms=["HS256"]
    )


def generate_token(
    name: str,
    cns: str,
    uf: str,
    municipio: str,
    profiles: List[str] = None,
    ubs: int = None,
    equipe: int=None,
    lotacoes: List[dict] = None
) -> str:
    return jwt.encode(
        {
            "lotacoes": lotacoes,
            "username": name,
            "cns": cns,
            "uf": uf,
            "municipio": municipio,
            "profiles": profiles,
            "equipe": equipe,
            "ubs": ubs,
            "exp": datetime.datetime.now() + datetime.timedelta(hours=12),
        },
        os.environ["SECRET_TOKEN"],
        algorithm="HS256",
    )
