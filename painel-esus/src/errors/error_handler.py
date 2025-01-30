import asyncio
import datetime
import os

import aiohttp
import jwt
from src.errors.logging import logging
from src.presentations.http_types import HttpResponse

from .types import (
    HttpBadRequestError,
    HttpCredentialsFailError,
    HttpNotFoundError,
    HttpUnprocessableEntityError,
    InvalidIMC,
)

SECRET_KEY = "y)wjkIaV;2~1_xn38_X5Xs*/@=4yX3"

def handle_errors(error: Exception) -> HttpResponse:

    logging.exception(error)
    asyncio.run(send_exception_logs(str(error)))
    if isinstance(error, (HttpNotFoundError, HttpBadRequestError, HttpUnprocessableEntityError,
                          InvalidIMC, HttpCredentialsFailError)):
        # mandar mensagem para logger falando que teve esse erro!
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )



async def send_exception_logs(error):
    try:
        print('==============================>ENTORU NO MÉTODO PARA ENVIAR O LOG: ', error)
        cod_ibge = os.getenv("CIDADE_IBGE", "n/a")
        estado = os.getenv("ESTADO", "n/a")
        version = os.getenv("APPLICATION_VERSION", "n/a")
        base_url = os.getenv("LOG_API", "")
        api_url = f"{base_url}/exception-log"

        payload = {
            "codigoIbge": cod_ibge,
            "estado": estado,
            "version": version,
            "exception": error
        }
        # token = gerar_token(codIbge)
        token = gerar_jwt(cod_ibge, version, estado)
        print('==============================>TOKEN: ', token)
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {token}"}
        print('==============================>ANTES DE ENVIAR: ', api_url)
        async with aiohttp.ClientSession() as session:
            async with session.post(api_url, json=payload, headers=headers) as response:
                if response.status == 201:
                    print("POST enviado com sucesso!")
                else:
                    print(f"Falha no POST: {response.status}, {await response.text()}")

    except Exception as e:
        print(f"Erro no envio do erro: {e}")

def gerar_jwt(cod_ibge, version, estado):
    try:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5)  # Token expira em 1 hora
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return token
    except Exception as e:
        print(f"Erro na tarefa assíncrona: {e}")
