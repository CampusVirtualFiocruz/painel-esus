# pylint: disable=R0913,W0611
import duckdb
import json
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
from src.infra.db.repositories.sqls.parquet.tb_acompanhamento_vinculo import (
    get_pessoas,
    get_pessoas_sql,
)
from src.infra.db.settings.connection_local import DBConnectionHandler
from src.env.conf import getenv
from src.main.adapters.nominal_list_adapter import mock_word

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
    def __init__(self):
        self.mock_data = getenv("MOCK", False, False) == 'True'

    def get_total_group(self, cnes: int = None, equipe: int = None):
        con = duckdb.connect()
        sql = get_total_cadastros(cnes, equipe)
        result = con.sql(sql).fetchall()
        return result

    def get_cpf_cns_rate(self, cnes: int = None, equipe: int = None):
        con = duckdb.connect()
        sql = get_cpf_cns_rate(cnes, equipe)
        result = con.sql(sql).fetchall()
        return result

    def group_localidade(self, cnes: int = None, equipe: int = None):
        sql = group_localidade(cnes, equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def group_raca_cor(self, cnes: int = None, equipe: int = None):
        sql = group_raca_cor(cnes, equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def group_records_by_origin(self, cnes: int = None, equipe: int = None):
        sql = group_records_by_origin(cnes, equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def group_records_status(self, cnes: int = None, equipe: int = None):
        sql = group_records_by_status(cnes, equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def people_who_get_care(self, cnes: int = None, equipe: int = None):
        sql = people_who_get_care(cnes, equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def nominal_list(self, cnes: int = None, equipe: int = None):
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
        if self.mock_data:
            def parse(x):
                x['cpf'] = mock_word(x['cpf'], 2)
                x['cns'] = mock_word(x['cns'], 2)
                x['nome'] = mock_word(x['nome'], 3, True)
                x['telefone'] = mock_word(x['telefone'], 2)
                x['endereco'] = mock_word(x['endereco'], 2)
                x['numero'] = mock_word(x['numero'], 2)
                x['cep'] = mock_word(x['cep'], 2)
                x['complemento'] = mock_word(x['complemento'], 2)
                x['bairro'] = mock_word(x['bairro'], 2)
                x['nome_unidade_saude'] = mock_word(x['nome_unidade_saude'], 2)
                x['nome_equipe'] = mock_word(x['nome_equipe'], 2)
                return x            
            response=response.apply(parse, axis=1)
        return response
