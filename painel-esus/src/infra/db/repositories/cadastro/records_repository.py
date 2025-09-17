"""Cadastro Individual.

Consultas relacionadas ao cadastro de pessoas (equipe,
localidade, raça/cor, status e outras agregações).

Responsabilidades principais:
- Agregar totais e indicadores do cadastro.
- Agrupar cadastros por localidade, raça/cor, origem e status.
- Fornecer listas nominais paginadas e exportação anonimizadas.

Observações:
- Quando a variável de ambiente ``MOCK=True`` estiver definida, alguns
  fluxos podem retornar dados simulados.
"""
# pylint: disable=R0913,W0611
import json

import duckdb
import pandas as pd
from sqlalchemy import and_, or_
from src.env.conf import getenv
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
from src.infra.db.repositories.sqls.parquet.tb_acompanhamento_vinculo import (
    get_pessoas,
    get_pessoas_sql,
)
from src.infra.db.repositories.utils.str_utils import anonymize_data_frame


class RecordsRepository:
    """Implementa operações de leitura de dados cadastrais."""
    def __init__(self):
        self.mock_data = getenv("MOCK", False, False) == 'True'

    def get_total_group(self, cnes: int = None, equipe: int = None):
        """Retorna total de pessoas cadastradas por agrupamento padrão.

        Parâmetros opcionais cnes e equipe permitem filtrar por
        unidade e equipe.
        """
        con = duckdb.connect()
        sql = get_total_cadastros(cnes, equipe)
        result = con.sql(sql).fetchall()
        return result

    def get_cpf_cns_rate(self, cnes: int = None, equipe: int = None):
        """Retorna taxa de preenchimento de CPF/CNS entre os cadastrados."""
        con = duckdb.connect()
        sql = get_cpf_cns_rate(cnes, equipe)
        result = con.sql(sql).fetchall()
        return result

    def group_localidade(self, cnes: int = None, equipe: int = None):
        """Agrupa cadastros por tipo de localidade."""
        sql = group_localidade(cnes, equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def group_raca_cor(self, cnes: int = None, equipe: int = None):
        """Agrupa cadastros por raça/cor."""
        sql = group_raca_cor(cnes, equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def group_records_by_origin(self, cnes: int = None, equipe: int = None):
        """Agrupa registros pela origem (ex.: e-SUS, importações)."""
        sql = group_records_by_origin(cnes, equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def group_records_status(self, cnes: int = None, equipe: int = None):
        """Agrupa cadastros por status (ativo, atualizado, desatualizado etc.)."""
        sql = group_records_by_status(cnes, equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def people_who_get_care(self, cnes: int = None, equipe: int = None):
        """Retorna agregações de pessoas que recebem atendimento."""
        sql = people_who_get_care(cnes, equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def nominal_list(self, cnes: int = None, equipe: int = None):
        """Lista nominal baseada na origem dos registros."""
        sql = group_records_by_origin(cnes, equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def find_filter_nominal(
        self,
        cnes: int = None,
        page: int = 0,
        pagesize: int = 10,
        nome: str = None,
        cpf: str = None,
        equipe: int = None,
        query:str=None,
        sort=[]
    ):
        """Retorna lista nominal (items e metadados de paginação).

        Parâmetros:
        - cnes, equipe: filtros por unidade e equipe.
        - page, pagesize: paginação.
        - nome, cpf, query: filtros de busca textual (query aplica em
          múltiplas colunas como nome/CPF/CNS).
        - sort: lista de dicts com chaves field e direction.
        """
        page = int(page) if page is not None else 0
        pagesize = int(pagesize) if pagesize is not None else 0

        con = duckdb.connect()
        pessoas_sql = get_pessoas_sql()

        conditions = []
        or_conditions = []

        order = ''
        order_list = []
        mapped_columns = {
            'name': 'nome',
            'cpf':'cpf',
            'cns': 'cns',
            'idade': 'idade',
            'sexo': 'sexo',
            'equipe': 'nome_equipe',
            'micro_area': 'micro_area'
        }

        if cnes is not None and cnes:
            conditions += [f"codigo_unidade_saude = {cnes}"]

        if query is not None and query:
            or_conditions += [
                f"cpf ilike '%{query}%'",
                f"nome ilike '%{query}%'",
                f"cns ilike  '%{query}%'"
            ]
        if equipe is not None and equipe:
            conditions += [ f'codigo_equipe_vinculada = {equipe}']

        where_clause = []
        sql_where, sql, sql_or = "", "", ""

        if len(conditions) > 0:
            sql += " AND ".join(conditions)
            where_clause += [f"({sql})"]

        if len(or_conditions) > 0:
            sql_or += " OR ".join(or_conditions)
            where_clause += [f"({sql_or})"]

        if len(where_clause)>0:
            offset = max(0, page - 1) * pagesize
            limit = pagesize
            sql_where = " AND ".join(where_clause)
            sql_where = f" WHERE {sql_where}"

        if len(sort) > 0:
            for s in sort:
                filter = json.loads(s)
                if filter["field"] not in mapped_columns: continue

                direction = filter['direction'] if 'direction' in filter else'asc'
                columns = mapped_columns[filter["field"]]
                order_list.append( f'{columns} {direction}')
        else:
            order_list = ['nome asc']
        if len(order_list)>0:
            order = 'order by '
            order += ", ".join(order_list)

        users = con.sql(
            pessoas_sql + sql_where + f"  {order} LIMIT {limit} OFFSET {offset} "
        ).df()

        users = users.to_dict(orient="records")
        total = len(con.sql(pessoas_sql + sql_where).fetchall())
        return {
                "itemsCount": total,
                "itemsPerPage": pagesize,
                "page": page,
                "pagesCount": round(total / pagesize),
                "items": users,
            }

    def find_all_download(self, cnes: int = None, equipe: int = None):
        """Gera DataFrame para exportação da lista nominal.

        Os dados sensíveis são anonimizados.
        """
        sql_pessoas = get_pessoas(cnes, equipe)
        sql = f"""
            with pessoas as ({sql_pessoas})
            select
                cidadao_pec,
                co_cidadao,
                raca_cor,
                cpf,
                cns,
                nome,
                STRFTIME( '%d-%m-%Y',data_nascimento) data_nascimento,
                idade,
                sexo,
                telefone,
                STRFTIME( '%d-%m-%Y',  cast(ultima_atualizacao_fci as DATE) ) as ultima_atualizacao_fci,
                case
                    when fci_att_2anos = 0 then 'NÃO'
                    when fci_att_2anos is null then 'NÃO'
                    when fci_att_2anos =1 then 'SIM'
                end as fci_atualizada,
                STRFTIME( '%d-%m-%Y', cast( ultima_atualizacao_fcd as DATE)) as ultima_atualizacao_fcd,
                case
                    when fci_att_2anos = 0 then 'NÃO'
                    when fci_att_2anos is null then 'NÃO'
                    when fci_att_2anos = 1 then 'SIM'
                end as fcd_atualizada,
                tipo_endereco,
                endereco,
                complemento,
                numero,
                bairro,
                cep,
                tipo_localidade,
                nome_unidade_saude,
                nome_equipe,
                micro_area,
                case
                    when acompanhamento = 1 then 'SIM'
                    when acompanhamento = 0 then 'NÃO'
                end as acompanhamento,
                status_cadastro
            from pessoas  """

        con = duckdb.connect()
        response = con.sql(sql).df()
        response = response.apply(anonymize_data_frame, axis=1)
        return response
