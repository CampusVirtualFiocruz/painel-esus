# pylint: disable=invalid-name,R0913
import datetime
import logging
import os
from functools import wraps
from typing import List

import jwt
from flask import jsonify
from flask import Request
from flask import request
from src.errors import HttpBadTokenError
from src.main.adapters.request_adapter import HttpResponse

logging.basicConfig(level=logging.DEBUG)

SECRET_PASS = "OM3VpHNkEsKA"


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        response = HttpResponse(body=None, status_code=0)
        try:
            check_token(request)
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
        auth_token, os.getenv("SECRET_TOKEN", SECRET_PASS), algorithms=["HS256"]
    )


def generate_token(
    name: str,
    cns: str,
    uf: str,
    municipio: str,
    profiles: List[str] = None,
    ubs: int = None,
) -> str:
    return jwt.encode(
        {
            "username": name,
            "cns": cns,
            "uf": uf,
            "municipio": municipio,
            "profiles": profiles,
            "ubs": ubs,
            "exp": datetime.datetime.now() + datetime.timedelta(hours=12),
        },
        os.getenv("SECRET_TOKEN", SECRET_PASS),
        algorithm="HS256",
    )
