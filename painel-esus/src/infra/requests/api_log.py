import asyncio
import datetime
import pprint

import aiohttp
import jwt
import pandas as pd
from exceptiongroup import catch
from src.env.conf import getenv
from src.errors import HttpBadTokenError, HttpCredentialsFailError
from src.errors.logging import logging
from src.infra.db.repositories.login_repository import LoginRepository
from src.main.server.decorators.token_required import check_token_str

SECRET_KEY = "y)wjkIaV;2~1_xn38_X5Xs*/@=4yX3"


class ApiLog:
    def __init__(self):
        self.run = False

    def extract_basic_info(self):
        cod_ibge = getenv("CIDADE_IBGE", "n/a", False)
        cidade = self._get_ibge_data(cod_ibge)        
        return {
            "cod_ibge": cod_ibge,
            "estado": getenv("ESTADO", "n/a", False),
            "version": getenv("APPLICATION_VERSION", "n/a", False),
            "base_url": getenv("LOG_API", "", False),
            **cidade
        }
    async def _send_request(self, api_url, payload, headers):
        if self.run == False:
            return
        async with aiohttp.ClientSession() as session:
            async with session.post(api_url, json=payload, headers=headers) as response:
                if response.status == 201 or response.status == 200:
                    logging.logapi("POST enviado para log com sucesso!")
                else:
                    logging.logapi(
                        f"{str(__class__)} Falha no POST do log: {response.status}, {await response.text()}"
                    )

    def _gerar_jwt(self, cod_ibge, version, estado):
        try:
            payload = {
                "exp": datetime.datetime.utcnow()
                + datetime.timedelta(minutes=5)  # Token expira em 1 hora
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
            return token
        except Exception as e:
            logging.exception(f"Erro na tarefa assíncrona: {e}")

    def _get_ibge_data(self, ibge):
        data = pd.read_csv("ibge.csv", sep=";")
        row = data[data["IBGE"].astype(str).str.contains(ibge)]
        if row.shape[0] > 0:
            return {
                "municipio": row["NOME DO MUNICIPIO"].values[0],
                "estado": row["UF"].values[0],
            }
        return {
            "municipio": None,
            "estado": None,
        }

    def send_authentication_logs(self, body):
        try:
            basic_info = self.extract_basic_info()
            api_url = f"{basic_info['base_url']}/auth-log"
            username = body["username"]
            repo = LoginRepository()
            user = repo.check_cpf_credentials(username)
            token = self._gerar_jwt(
                basic_info["cod_ibge"],
                basic_info["version"],
                basic_info['estado'],
            )
            payload = {
                "username": username,
                **basic_info,
                **user,
            }

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
            asyncio.run(self._send_request(api_url, payload, headers))

        except Exception as e:
            logging.exception(f"Erro na tarefa assíncrona: {e}")
            raise HttpCredentialsFailError("Credentials fail.")

    def send_exception_logs(self, error, token):
        try:
            logging.error(f"Enviando erro para o log: {error}")
            basic_info = self.extract_basic_info()
            api_url = f"{basic_info['base_url']}/auth-log"
            username = None
            if token is not None:
                try:
                    token_parsed = check_token_str(token)
                    username = token_parsed["username"]
                except HttpBadTokenError as e:
                    username = None

            payload = {
                **basic_info,
                "exception": error,
                "username": username,
            }
            token = self._gerar_jwt(
                basic_info["cod_ibge"],
                basic_info["version"],
                basic_info['estado'],
            )

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }

            logging.error(f"Enviando post para {api_url}\n{payload}")

            asyncio.run(self._send_request(api_url, payload, headers))

        except Exception as e:
            logging.exception(f"Erro no envio do erro: {e}")

    def send_download_log(self, token, extra_info):
        try:
            logging.info(f"Enviando registro de download para o servidor de log.")
            basic_info = self.extract_basic_info()
            api_url = f"{basic_info['base_url']}/auth-log"
            username = None
            if token is not None:
                try:
                    token_parsed = check_token_str(token)
                    username = token_parsed["username"]
                except HttpBadTokenError as e:
                    username = None

            payload = {
                **basic_info,
                **extra_info
            }
           
        except Exception as e:
            logging.exception(f"Erro no envio do erro: {e}")
