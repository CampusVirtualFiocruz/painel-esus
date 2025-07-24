import asyncio
import datetime

import aiohttp
import jwt
import pandas as pd
from src.env.conf import getenv
from src.errors import HttpCredentialsFailError
from src.errors.logging import logging
from src.infra.db.repositories.login_repository import LoginRepository

SECRET_KEY = "y)wjkIaV;2~1_xn38_X5Xs*/@=4yX3"


class ApiLog:

    async def _send_request(self, api_url, payload, headers):
        async with aiohttp.ClientSession() as session:
            async with session.post(api_url, json=payload, headers=headers) as response:
                if response.status == 201 or response.status == 200:
                    logging.info("POST enviado para log com sucesso!")
                else:
                    logging.info(
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
                "cidade": row["NOME DO MUNICIPIO"].values[0],
                "estado": row["UF"].values[0],
            }
        return {
            "cidade": None,
            "estado": None,
        }

    def send_authentication_logs(self, body):
        try:
            cod_ibge = getenv("CIDADE_IBGE", "n/a", False)
            estado = getenv("ESTADO", "n/a", False)
            version = getenv("APPLICATION_VERSION", "n/a", False)
            base_url = getenv("LOG_API", "", False)
            api_url = f"{base_url}/auth-log"
            username = body["username"]
            repo = LoginRepository()
            user = repo.check_cpf_credentials(username)
            cidade = self._get_ibge_data(cod_ibge)
            token = self._gerar_jwt(cod_ibge, version, estado)
            payload = {
                "codigoIbge": cod_ibge,
                "version": version,
                "username": username,
                **cidade,
                **user,
            }
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
            print(payload)
            asyncio.run(self._send_request(api_url, payload, headers))

        except Exception as e:
            logging.exception(f"Erro na tarefa assíncrona: {e}")
            raise HttpCredentialsFailError("Credentials fail.")

    def send_exception_logs(self, error):
        try:
            logging.error(f"Enviando erro para o log: {error}")
            cod_ibge = getenv("CIDADE_IBGE", "n/a", False)
            estado = getenv("ESTADO", "n/a", False)
            version = getenv("APPLICATION_VERSION", "n/a", False)
            base_url = getenv("LOG_API", "", False)
            api_url = f"{base_url}/exception-log"

            payload = {
                "codigoIbge": cod_ibge,
                "estado": estado,
                "version": version,
                "exception": error,
            }
            # token = gerar_token(codIbge)
            token = self._gerar_jwt(cod_ibge, version, estado)

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }

            logging.error(f"Enviando post para {api_url}\n{payload}")

            asyncio.run(self._send_request(api_url, payload, headers))

        except Exception as e:
            logging.exception(f"Erro no envio do erro: {e}")
