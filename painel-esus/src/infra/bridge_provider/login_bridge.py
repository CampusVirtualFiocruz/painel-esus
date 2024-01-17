# pylint: disable=logging-too-many-args
# pylint: disable=line-too-long
from src.env import env
from src.errors.logging import logging
import urllib.parse

import requests

from src.data.interfaces.login_repository import \
    LoginRepository as LoginRepositoryInterface
from src.domain.entities.user_payload import UserPayload

from .queries.query_sessao import QUERY_SESSAO



class LoginBridgeRepository(LoginRepositoryInterface):

    def check_credentials(self, username: str, password: str) -> UserPayload:
        session = requests.Session()
        url = env.get("BRIDGE_LOGIN_URL", "")
        payload = "{\"query\":\"mutation mutation_login {\\n  login(input: {username: \\\""+username + \
            "\\\", password: \\\""+password + \
            "\\\", force: true}) {\\n    success\\n  }\\n}\",\"variables\":{}}"
        headers = {
            'Api-Consumer-Id': 'PAINEIS_FIOCRUZ',
            'Content-Type': 'application/json',
            'Cookie': 'JSESSIONID=87J4pWjfQUVaO3b_lndd1DQE-8hJ3RZzcHes0uFb; XSRF-TOKEN=25038984-1945-43e2-a990-f62709f4eddd'
        }

        response = session.request("POST", url, headers=headers, data=payload)
        if response.text is None:
            return None
        cookie = session.cookies.get_dict()

        response_json = response.json()
        if 'errors' in response_json and len(response_json['errors']) > 0 and not response_json['data']:
            return None

        if response_json is not None and 'data' in response_json and\
            'login' in response_json['data'] and\
            'success' in response_json['data']['login'] and\
                response_json['data']['login']['success']:
            head = {
                'Api-Consumer-Id': 'PAINEIS_FIOCRUZ',
                'Content-Type': 'application/json',
            }
            head.update({"Cookie": urllib.parse.urlencode(cookie)})
            response = requests.request(
                "POST", url, headers=head, data=QUERY_SESSAO, timeout=30)
            data = response.json()
            logging.info('head: {}, nome: {}',
                         head,
                         data["data"]["sessao"]["profissional"]["lotacoes"][0]["unidadeSaude"]
                         )
            if data["data"]["sessao"]:
                profissional = data["data"]["sessao"]["profissional"]
                user_raw_data = UserPayload(
                    username=profissional["nome"],
                    cns=profissional["cns"],
                    uf=profissional["lotacoes"][0]["unidadeSaude"]["endereco"]["uf"]["sigla"],
                    municipio=profissional["lotacoes"][0]["unidadeSaude"]["endereco"]["uf"]["nome"],
                    profiles=['user']
                )
                return user_raw_data
        return None
