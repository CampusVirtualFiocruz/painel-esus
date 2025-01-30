import asyncio
import datetime
import os

import aiohttp
import jwt
from flask import Request
from src.presentations.http_types import HttpRequest

SECRET_KEY = "y)wjkIaV;2~1_xn38_X5Xs*/@=4yX3"

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
    asyncio.run(send_authentication_logs())

    return http_request



async def send_authentication_logs():
    try:
        cod_ibge = os.getenv("CIDADE_IBGE", "n/a")
        estado = os.getenv("ESTADO", "n/a")
        version = os.getenv("APPLICATION_VERSION", "n/a")
        base_url = os.getenv("LOG_API", "")
        api_url = f"{base_url}/auth-log"

        payload = {
            "codigoIbge": cod_ibge,
            "estado": estado,
            "version": version
        }
        # token = gerar_token(codIbge)
        token = gerar_jwt(cod_ibge, version, estado)
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {token}"}
        async with aiohttp.ClientSession() as session:
            async with session.post(api_url, json=payload, headers=headers) as response:
                if response.status == 201:
                    print("POST enviado com sucesso!")
                else:
                    print(f"Falha no POST: {response.status}, {await response.text()}")

    except Exception as e:
        print(f"Erro na tarefa assíncrona: {e}")

def gerar_jwt(cod_ibge, version, estado):
    try:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5)  # Token expira em 1 hora
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return token
    except Exception as e:
        print(f"Erro na tarefa assíncrona: {e}")
