from flask import Request

from src.presentations.http_types import HttpRequest


def request_login_adapter(request: Request) -> HttpRequest:

    body = None
    if request.data:
        body = request.json

    http_request = HttpRequest(
        body=body,
        headers=request.headers,
        query_params=request.args,
        path_params=request.view_args,
        url=request.full_path
    )

    return http_request
