# pylint: disable=R0913,W0611
import pandas as pd
from sqlalchemy import and_, or_
from src.infra.db.entities.equipes import Equipes
from src.infra.db.entities.pessoas import Pessoas
from src.infra.db.repositories.cadastro.sqls import (
    get_cpf_cns_rate,
    get_total_cadastros,
    group_localidade,
    group_raca_cor,
    group_records_by_origin,
    group_records_by_status,
    people_who_get_care,
)
from src.infra.db.settings.connection_local import DBConnectionHandler

columns = [
    Pessoas.co_cidadao,
    Pessoas.raca_cor,
    Pessoas.cpf,
    Pessoas.cns,
    Pessoas.nome,
    Pessoas.nome_social,
    Pessoas.data_nascimento,
    Pessoas.idade,
    Pessoas.sexo,
    Pessoas.identidade_genero,
    Pessoas.telefone,
    Pessoas.ultima_atualizacao_cidadao,
    Pessoas.diferenca_ultima_atualizacao_cidadao,
    Pessoas.ultima_atualizacao_fcd,
    Pessoas.diferenca_ultima_atualizacao_fcd,
    Pessoas.tipo_endereco,
    Pessoas.endereco,
    Pessoas.complemento,
    Pessoas.numero,
    Pessoas.bairro,
    Pessoas.cep,
    Pessoas.tipo_localidade,
    Pessoas.acompanhamento,
    Pessoas.status_cadastro,
    Pessoas.alerta_status_cadastro,
    Pessoas.alerta,
    Equipes.nome_unidade_saude,
    Equipes.nome_equipe,
    Equipes.micro_area,
]

class RecordsRepository:

    def get_total_group(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = get_total_cadastros(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def get_cpf_cns_rate(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = get_cpf_cns_rate(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def group_localidade(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = group_localidade(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def group_raca_cor(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = group_raca_cor(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def group_records_by_origin(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = group_records_by_origin(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def group_records_status(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = group_records_by_status(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def people_who_get_care(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = people_who_get_care(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def nominal_list(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = group_records_by_origin(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_filter_nominal(
        self,
        cnes: int = None,
        page: int = 0,
        pagesize: int = 10,
        nome: str = None,
        cpf: str = None,
        equipe: int = None,
        query:str=None
    ):
        page = int(page) if page is not None else 0
        pagesize = int(pagesize) if pagesize is not None else 0
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session.query(*columns)
                .distinct(Pessoas.cidadao_pec)
                .join(
                    Equipes,
                    and_(
                        Equipes.cidadao_pec == Pessoas.cidadao_pec,
                        Equipes.codigo_equipe == Pessoas.codigo_equipe_vinculada,
                        Equipes.codigo_unidade_saude == Pessoas.codigo_unidade_saude
                    ),
                )
            )
            conditions = []
            or_conditions = []

            if cnes is not None and cnes:
                conditions+=[ Pessoas.codigo_unidade_saude == cnes]

            if query is not None and query:
                or_conditions += [
                    Pessoas.cpf.ilike(f"%{query}%"),
                    Pessoas.nome.ilike(f"%{query}%"),
                    Pessoas.cns.ilike(f"%{query}%"),
                ]
            if equipe is not None and equipe:
                # users = users.filter(Equipes.codigo_equipe == equipe)
                conditions += [Pessoas.codigo_equipe_vinculada == equipe]
            if len(conditions) > 0:
                users = users.filter(*conditions)

            if len(or_conditions) > 0:
                users = users.filter(or_(*or_conditions))
            users = users.group_by(Pessoas.cidadao_pec)
            total = users.count()
            users = (
                users.order_by(Pessoas.nome)
                .offset(max(0, page - 1) * pagesize)
                .limit(pagesize)
            )
            print(list(users))
            return {
                "itemsCount": total,
                "itemsPerPage": pagesize,
                "page": page,
                "pagesCount": round(total / pagesize),
                "items": list(users),
            }

    def find_all_download(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler() as db_con:
            where_clause = ""
            if cnes is not None and cnes:
                where_clause += f" where pessoas.codigo_unidade_saude = {cnes} "
                if equipe is not None and equipe:
                    where_clause += f" and pessoas.codigo_unidade_saude = {equipe} "
            sql = f"""select 
                pessoas.cidadao_pec,
                pessoas.co_cidadao,
                pessoas.raca_cor,
                pessoas.cpf,
                pessoas.cns,
                pessoas.nome,
                pessoas.nome_social,
                STRFTIME( '%d-%m-%Y',pessoas.data_nascimento) data_nascimento,
                pessoas.idade,
                pessoas.sexo,
                pessoas.identidade_genero,
                pessoas.telefone,
                STRFTIME( '%d-%m-%Y',pessoas.ultima_atualizacao_cidadao) ultima_atualizacao_cidadao,
                case 
                    when pessoas.diferenca_ultima_atualizacao_cidadao > 24 then 'NÃO'
                    when pessoas.diferenca_ultima_atualizacao_cidadao is null then 'NÃO'
                    when pessoas.diferenca_ultima_atualizacao_cidadao <= 24 then 'SIM'
                end fci_atualizada,
                STRFTIME( '%d-%m-%Y',pessoas.ultima_atualizacao_fcd) ultima_atualizacao_fcd,
                case 
                    when pessoas.diferenca_ultima_atualizacao_fcd > 24 then 'NÃO'
                    when pessoas.diferenca_ultima_atualizacao_fcd is null then 'NÃO'
                    when pessoas.diferenca_ultima_atualizacao_fcd <= 24 then 'SIM'
                end fcd_atualizada,
                pessoas.tipo_endereco,
                pessoas.endereco,
                pessoas.complemento,
                pessoas.numero,
                pessoas.bairro,
                pessoas.cep,
                pessoas.tipo_localidade,
                equipes.nome_unidade_saude,
                equipes.nome_equipe,
                equipes.micro_area,
                case 
                    when pessoas.acompanhamento = 1 then "SIM"
                    when pessoas.acompanhamento = 0 then "NÃO"
                end acompanhamento,
                pessoas.status_cadastro
            from pessoas 
                left join equipes on pessoas.cidadao_pec = equipes.cidadao_pec and pessoas.codigo_equipe_vinculada = equipes.codigo_equipe and pessoas.codigo_unidade_saude = equipes.codigo_unidade_saude
            {where_clause}
            order by equipes.micro_area desc """
            response = pd.read_sql_query(
                con=db_con.get_engine(),
                sql=sql,
            )
            return response
