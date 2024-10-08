# pylint: disable=R0913
from typing import Dict

import pandas as pd
from sqlalchemy import or_
from src.infra.db.entities.hipertensao_nominal import HipertensaoNominal
from src.infra.db.settings.connection_local import DBConnectionHandler


class HypertensionNominalListRepository:

    def find_all(self, cnes: int = None) -> Dict:
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session.query(HipertensaoNominal)
                .filter(HipertensaoNominal.co_dim_unidade_saude == cnes)
                .all()
            )
            return users

    def find_all_download(self, cnes: int = None) -> Dict:
        with DBConnectionHandler() as db_con:
            response = pd.read_sql_query(
                con=db_con.get_engine(),
                sql=f"""select co_fat_cidadao_pec as codigo_cidadao,
                                         no_cidadao as nome,
                                         nu_cns as cns,
                                         nu_cpf as cpf,
                                         no_sexo,
                                         no_raca_cor as "raca/cor",
                                         nu_micro_area "micro area",
                                         nu_area "area",
                                         dt_nascimento "data nascimento",
                                         idade,
                                         (no_tipo_logradouro || ' '|| ds_logradouro) "logradouro",
                                         no_bairro "bairro",
                                         nu_numero "numero",
                                         ds_cep "cep",
                                         no_localidade "cidade",
                                         no_uf "estado",
                                         sg_uf "uf",
                                         co_dim_equipe "codigo equipe",
                                         co_dim_unidade_saude "codigo unidade saude",
                                         co_dim_tempo "data atendimento",
                                         cids "cids",
                                         min_date "primeiro atendimento",
                                         ds_tipo_localizacao "tipo localizacao",
                                         equipe "ultima equipe vinculada",
                                         data_ultima_visita_acs,
                                         alerta_visita_acs,
                                         total_consulta_individual_medico,
                                         alerta_total_de_consultas_medico,
                                         ultimo_atendimento_medico,
                                         alerta_ultima_consulta_medico,
                                         ultimo_atendimento_odonto,
                                         alerta_ultima_consulta_odontologica,
                                         ultima_data_afericao_pa,
                                         alerta_afericao_pa,
                                         ultima_data_creatinina,
                                         alerta_creatinina
                                         from hipertensao_nominal where co_dim_unidade_saude like '%{cnes},%' or
                                         co_dim_unidade_saude  like "%{cnes}" order by nome""",
            )
            return response

    def find_by_nome(self, nome: str):
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session.query(HipertensaoNominal)
                .filter(HipertensaoNominal.no_cidadao.ilike(f"%{nome}%"))
                .all()
            )
            return users

    def find_filter(
        self,
        cnes: int,
        page: int = 0,
        pagesize: int = 10,
        nome: str = None,
        cpf: str = None,
    ):
        page = int(page) if page is not None else 0
        pagesize = int(pagesize) if pagesize is not None else 0
        with DBConnectionHandler() as db_con:
            users = db_con.session.query(HipertensaoNominal).distinct(
                HipertensaoNominal.co_fat_cidadao_pec
            )

            users = users.filter(
                or_(
                    HipertensaoNominal.co_dim_unidade_saude.ilike(f"%{cnes},%"),
                    HipertensaoNominal.co_dim_unidade_saude.ilike(f"%{cnes}"),
                )
            )
            if nome is not None:
                users = users.filter(HipertensaoNominal.no_cidadao.ilike(f"%{nome}%"))
            if cpf is not None:
                users = users.filter(HipertensaoNominal.nu_cpf.ilike(f"%{cpf}%"))
            total = users.count()
            users = (
                users.order_by(HipertensaoNominal.no_cidadao)
                .offset(max(0, ((page - 1) * pagesize)))
                .limit(pagesize)
            )

            return {
                "itemsCount": total,
                "itemsPerPage": pagesize,
                "page": page,
                "pagesCount": round(total / pagesize),
                "items": list(users),
            }
