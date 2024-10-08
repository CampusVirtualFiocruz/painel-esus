# pylint: disable=logging-too-many-args
# pylint: disable=line-too-long
# pylint: disable=W0012,R1710, W0611
import urllib.parse
from pprint import pprint

import requests
from sqlalchemy import text
from src.data.interfaces.login_repository import (
    LoginRepository as LoginRepositoryInterface,
)
from src.domain.entities.user_payload import UserPayload
from src.env import env
from src.errors.logging import logging
from src.infra.db.settings.connection import DBConnectionHandler

from .queries.query_sessao import QUERY_SESSAO


class LoginBridgeRepository(LoginRepositoryInterface):

    def check_role(self, response):
        profissional = response["data"]["sessao"]["profissional"]
        acessos = profissional["acessos"]
        lotacoes = profissional["lotacoes"]
        role = None
        roles_adm = [
            "GESTOR_ESTADUAL",
            "GESTOR_MUNICIPAL",
            "ADMINISTRADOR_GERAL",
            "ADMINISTRADOR_MUNICIPAL",
        ]
        cbos_list = [
            "3222",
            "515105",
            "131210",
            "2516",
            "2211 ",
            "2212",
            "2241",
            "2235",
            "2234",
            "2236",
            "2238",
            "225",
            "2237",
            "2232",
            "2515",
            "2239",
        ]
        for acesso in acessos:
            if acesso["tipo"] in roles_adm:
                role = ["admin"]
        cbo_unidade = []
        if role is None:
            for lotacao in lotacoes:
                unidade_saude = lotacao["unidadeSaude"]
                cbo = lotacao["cbo"]
                cbo_unidade.append((cbo["id"], unidade_saude["id"]))

            with DBConnectionHandler().get_engine().connect() as db_con:
                cbos_ids = [cbo[0] for cbo in cbo_unidade]
                list_cbo = ",".join(cbos_ids)
                list_cbo_value = ",".join([f"'{cbo}%'" for cbo in cbos_list])
                sql = f"select co_cbo, co_cbo_2002 from tb_cbo where co_cbo in ({list_cbo}) and co_cbo_2002 like any (array[{list_cbo_value}]);"
                statement = text(sql)
                result = db_con.execute(statement)
                for r in result:
                    for i in cbo_unidade:
                        if i[0] == str(r.co_cbo):
                            return ("user", i[1])

        else:
            return ("admin", None)

    def get_reponse_body(self, session, url, headers, payload):
        return session.request("POST", url, headers=headers, data=payload)

    def post_bridge(self, url, head, query_sessao):
        return requests.request(
            "POST", url, headers=head, data=query_sessao, timeout=30
        )

    def check_credentials(self, username: str, password: str) -> UserPayload:
        session = requests.Session()
        url_login = env.get("BRIDGE_LOGIN_URL", "")
        url = f"{url_login}/api/graphql"
        payload = (
            '{"query":"mutation mutation_login {\\n  login(input: {username: \\"\
                '
            + username
            + '\\", password: \\"'
            + password
            + '\\", force: true}) {\\n    success\\n  }\\n}","variables":{}}'
        )
        headers = {
            "Api-Consumer-Id": "PAINEIS_FIOCRUZ",
            "Content-Type": "application/json",
            "Cookie": "JSESSIONID=87J4pWjfQUVaO3b_lndd1DQE-8hJ3RZzcHes0uFb; XSRF-TOKEN=25038984-1945-43e2-a990-f62709f4eddd",
        }

        response = self.get_reponse_body(session, url, headers, payload)
        if response.text is None:
            return None
        cookie = session.cookies.get_dict()

        response_json = response.json()
        if (
            "errors" in response_json
            and len(response_json["errors"]) > 0
            and not response_json["data"]
        ):
            return None

        if (
            response_json is not None
            and "data" in response_json
            and "login" in response_json["data"]
            and "success" in response_json["data"]["login"]
            and response_json["data"]["login"]["success"]
        ):
            head = {
                "Api-Consumer-Id": "PAINEIS_FIOCRUZ",
                "Content-Type": "application/json",
            }
            head.update({"Cookie": urllib.parse.urlencode(cookie)})
            response = self.post_bridge(url, head, QUERY_SESSAO)
            data = response.json()

            # logging.info('head: {}, nome: {}',
            #              head,
            #              data["data"]["sessao"]["profissional"]["lotacoes"][0]["unidadeSaude"]
            #              )
            if data["data"]["sessao"]:
                profissional = data["data"]["sessao"]["profissional"]
                user = self.check_role(data)
                user_raw_data = UserPayload(
                    username=profissional["nome"],
                    cns=profissional["cns"],
                    uf=profissional["lotacoes"][0]["unidadeSaude"]["endereco"]["uf"][
                        "sigla"
                    ],
                    municipio=profissional["lotacoes"][0]["unidadeSaude"]["endereco"][
                        "uf"
                    ]["nome"],
                    profiles=[user[0]],
                    ubs=user[1],
                )
                return user_raw_data
        return None
