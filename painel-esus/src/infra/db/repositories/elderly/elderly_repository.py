import pandas as pd
import duckdb
import json
from src.infra.db.repositories.elderly.sqls import (
    get_total_ubs,get_medical_cares, get_total_card, by_gender, by_race, medical_appointments, height_records, acs_visits,
    ivcf_20,creatinine,dentist_appointment,influenza_vaccines, get_elderly_base,nominal_download)
from src.infra.db.settings.connection_local import DBConnectionHandler
from src.env.conf import getenv
from src.main.adapters.nominal_list_adapter import mock_word

class ElderlyRepository:
    def __init__(self):
        self.mock_data = getenv("MOCK", False, False) == 'True'

    def total_ubs(self, cnes: int = None, equipe: int = None):
        sql = get_total_ubs(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result
        
    def total_card(self, cnes: int = None, equipe: int = None):
            sql = get_total_card(cnes,equipe)
            con = duckdb.connect()
            result = con.sql(sql).fetchall()
            return result
            

    def total_medical_cares(self, cnes: int = None, equipe: int = None):
        sql = get_medical_cares(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result
    
    def by_gender(self, cnes: int = None, equipe: int = None):
        sql = by_gender(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        if len(result) > 0 and '100' in result[0][0]: 
            result = [list(result[2:])+list(result[:2]) ][0]
        return result
    
    def by_race(self, cnes: int = None, equipe: int = None):
        sql = by_race(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result
    
    def medical_appointment(self, cnes: int = None, equipe: int = None):
        sql = medical_appointments(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result
    
    def height_records(self, cnes: int = None, equipe: int = None):
        sql = height_records(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result
    
    def acs_visits(self, cnes: int = None, equipe: int = None):
        sql = acs_visits(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result
    
    def creatinine(self, cnes: int = None, equipe: int = None):
        sql = creatinine(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result
    
    def dentist_appointment(self, cnes: int = None, equipe: int = None):
        sql = dentist_appointment(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result
    
    def ivcf_20(self, cnes: int = None, equipe: int = None):
        sql = ivcf_20(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result
    
    def influenza_vaccines(self, cnes: int = None, equipe: int = None):
        sql = influenza_vaccines(cnes,equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result
    
    
    def find_filter_nominal(
        self,
        cnes: int,
        page: int = 0,
        pagesize: int = 10,
        nome: str = None,
        cpf: str = None,
        equipe: int = None,
        query: str = None,
        sort=[]
    ):
        page = int(page) if page is not None else 0
        pagesize = int(pagesize) if pagesize is not None else 0
        con = duckdb.connect()
        pessoas_sql = get_elderly_base()
        conditions = []
        or_conditions = []

        if cnes is not None and cnes:
            conditions += [f"codigo_unidade_saude = {cnes}"]

        if query is not None and query:
            or_conditions += [
                f"cpf ilike '%{query}%'",
                f"nome ilike '%{query}%'",
                f"cns ilike  '%{query}%'",
            ]
        if equipe is not None and equipe:
            conditions += [f"codigo_equipe = {equipe}"]

        where_clause = []
        sql_where, sql, sql_or = "", "", ""

        if len(conditions) > 0:
            sql += " AND ".join(conditions)
            where_clause += [f"({sql})"]

        if len(or_conditions) > 0:
            sql_or += " OR ".join(or_conditions)
            where_clause += [f"({sql_or})"]

        if len(where_clause) > 0:
            offset = max(0, page - 1) * pagesize
            limit = pagesize
            sql_where = " AND ".join(where_clause)
            sql_where = f" WHERE {sql_where}"
        if len(where_clause)>0:
            offset = max(0, page - 1) * pagesize
            limit = pagesize
            sql_where = " AND ".join(where_clause)
            sql_where = f" WHERE {sql_where}"

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
            pessoas_sql
            + sql_where
            + f"  {order} LIMIT {limit} OFFSET {offset} "
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
        sql = nominal_download(cnes,equipe)
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
