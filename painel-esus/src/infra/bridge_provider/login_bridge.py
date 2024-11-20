# pylint: disable=logging-too-many-args
# pylint: disable=line-too-long
# pylint: disable=W0012,R1710, W0611, C0103,W0622
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

    def get_ubs_id(self, id):
        sql = f"""select co_seq_dim_unidade_saude co_dim_unidade_saude from tb_unidade_saude tus join tb_dim_unidade_saude tdus on tus.nu_cnes = tdus.nu_cnes  where co_seq_unidade_saude = {id};	"""
        with DBConnectionHandler().get_engine().connect() as db_con:
            statement = text(sql)
            result = db_con.execute(statement)
            result = next(result)
            return result[0] if len(result) > 0 else id

    def check_role(self, acesso):
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
        if acesso["tipo"] in roles_adm:
            role = ["admin"]
        cbo_unidade = []
        if role is None:
            unidade_saude = acesso["unidadeSaude"]
            cbo = acesso["cbo"]["id"]
            cbo_unidade.append((cbo, unidade_saude["id"]))

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
                            # ubs_id = self.get_ubs_id(i[1])
                            equipe_id = None
                            if "equipe" in acesso and acesso['equipe'] is not None:
                                equipe_id = acesso["equipe"]["id"]
                            return ("user", i[1], equipe_id)

        else:
            return ("admin", None, None)

    def get_equipe_id(self, id):
        with DBConnectionHandler().get_engine().connect() as db_con:
            statement = text(f'select tde.co_seq_dim_equipe  from tb_equipe te join tb_dim_equipe tde on te.nu_ine = tde.nu_ine where te.co_seq_equipe = {id}')
            result = db_con.execute(statement)
            for r in result:
                return r.co_seq_dim_equipe
        return None

    def get_unit_id(self, id):
        with DBConnectionHandler().get_engine().connect() as db_con:
            statement = text(
                f"select co_seq_dim_unidade_saude from tb_unidade_saude tus join tb_dim_unidade_saude tdus on tdus.nu_cnes = tus.nu_cnes where tus.co_seq_unidade_saude = {id}"
            )
            result = db_con.execute(statement)
            for r in result:
                return r.co_seq_dim_unidade_saude
        return None

    def get_reponse_body(self, session, url, headers, payload):
        return session.request("POST", url, headers=headers, data=payload)

    def post_bridge(self, url, head, query_sessao):
        return requests.request(
            "POST", url, headers=head, data=query_sessao, timeout=30
        )

    def get_profiles(self, response):
        acessos = response["lotacoes"]
        def format_entity( id, name):
            if id is not None and name is not None:
                return {
                    "id": id,
                    "nome": name
                }
            return None

        profiles = []
        for acesso in acessos:
            ubs = None
            equipe = None
            if not acesso['ativo']:
                continue
            if acesso["unidadeSaude"] is not None:
                id = self.get_unit_id(acesso["unidadeSaude"]["id"])
                ubs = format_entity(id, acesso["unidadeSaude"]["nome"])
            if acesso["equipe"] is not None:
                equipe_id = self.get_equipe_id(acesso["equipe"]["id"])
                equipe = format_entity(equipe_id, acesso["equipe"]["nome"])

            profiles.append({
                "tipo": acesso["tipo"],
                "profissao": acesso["cbo"]["nome"],
                "cbo": acesso["cbo"]["cbo2002"],
                "id": acesso["cbo"]["id"],
                "ubs": ubs,
                "equipe": equipe
            })

        return profiles

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
        print('iniciando....')
        response = self.get_reponse_body(session, url, headers, payload)
        print(response)
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

            if data["data"]["sessao"]:
                profissional = data["data"]["sessao"]["profissional"]
                profiles = self.get_profiles(profissional)
                if len(profiles) > 1:
                    user_raw_data = UserPayload(
                        username=profissional["nome"],
                        cns=profissional["cns"],
                        uf=profissional["lotacoes"][0]["unidadeSaude"]["endereco"]["uf"][
                            "sigla"
                        ],
                        municipio=profissional["lotacoes"][0]["unidadeSaude"]["endereco"][
                            "uf"
                        ]["nome"],
                        profiles=profiles,
                        ubs="waiting for chosing",
                    )
                    return user_raw_data
                if len(profiles) == 1:
                    user = self.check_role(profissional['lotacoes'][0])  
                    equipe = None
                    if profiles[0]["equipe"] is not None:
                        equipe = profiles[0]["equipe"]["id"]
                    user_raw_data = UserPayload(
                        username=profissional["nome"],
                        cns=profissional["cns"],
                        uf=profissional["lotacoes"][0]["unidadeSaude"]["endereco"][
                            "uf"
                        ]["sigla"],
                        municipio=profissional["lotacoes"][0]["unidadeSaude"][
                            "endereco"
                        ]["uf"]["nome"],
                        profiles=[profiles[0]],
                        ubs=(profiles[0]["ubs"]["id"] if user is not None else None),
                        equipe=equipe,
                    )
                    return user_raw_data
        return None
