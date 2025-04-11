import pandas as pd
import duckdb
import json
from src.infra.db.repositories.elderly.sqls import (
    get_total_ubs,get_medical_cares, get_total_card, by_gender, by_race, medical_appointments, height_records, acs_visits,
    ivcf_20,creatinine,dentist_appointment,influenza_vaccines, get_elderly_base
)
from src.infra.db.settings.connection_local import DBConnectionHandler
from src.env.conf import getenv

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

        order = 'order by '
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
        with DBConnectionHandler() as db_con:
            where_clause = ""
            if cnes is not None and cnes:
                where_clause +=  f' where e.codigo_unidade_saude = {cnes} '
                if equipe is not None and equipe:
                    where_clause +=  f' and e.codigo_equipe = {equipe} '
            response = pd.read_sql_query(
                con=db_con.get_engine(),
                sql=f"""select
                    p.cidadao_pec as codigo_cidadao,
                    p.nome  as nome,
                    p.cns as cns,
                    p.cpf as cpf,
                    p.sexo as sexo,
                    p.raca_cor  as "raca/cor",
                    group_concat(e.micro_area) micro_area,
                    group_concat(e.nome_equipe) nome_equipe,
                    e.nome_unidade_saude,
                    STRFTIME( '%d-%m-%Y',p.data_nascimento) data_nascimento,
                    p.idade ,
                    p.tipo_endereco ,
                    p.endereco || ' ' || p.numero logradouro,
                    p.complemento,
                    p.bairro ,
                    p.cep,
                    p.tipo_localidade ,
                    i.atendimentos_medicos,
                    STRFTIME( '%d-%m-%Y',i.data_ultimo_atendimento_medicos) data_ultimo_atendimento_medicos,
                    i.medicoes_peso_altura , 
                    STRFTIME( '%d-%m-%Y',i.data_ultima_medicao_peso_altura) data_ultima_medicao_peso_altura, 
                    case 
                        when i.indicador_medicoes_peso_altura  = 1 then 'SIM'
                        when i.indicador_medicoes_peso_altura != 1 then 'NÃO'	
                    end indicador_medicoes_peso_altura ,
                    i.imc , 
                    i.categoria_imc , 
                    i.registros_creatinina , 
                    STRFTIME( '%d-%m-%Y',i.data_ultimo_registro_creatinina) data_ultimo_registro_creatinina, 
                    case 
                        when i.indicador_registros_creatinina   = 1 then 'SIM'
                        when i.indicador_registros_creatinina  != 1 then 'NÃO'	
                    end indicador_registros_creatinina  ,
                    case 
                        when i.indicador_visitas_domiciliares_acs   = 1 then 'SIM'
                        when i.indicador_visitas_domiciliares_acs  != 1 then 'NÃO'	
                    end indicador_visitas_domiciliares_acs  ,
                    i.visitas_domiciliares_acs , 
                    STRFTIME( '%d-%m-%Y',i.data_ultima_visita_domiciliar_acs) data_ultima_visita_domiciliar_acs, 
                    i.vacinas_influenza , 
                    STRFTIME( '%d-%m-%Y',i.data_ultima_vacina_influenza) data_ultima_vacina_influenza, 
                    case 
                        when i.indicador_vacinas_influenza   = 1 then 'SIM'
                        when i.indicador_vacinas_influenza  != 1 then 'NÃO'	
                    end indicador_vacinas_influenza  ,
                    i.atendimentos_odontologicos , 
                    STRFTIME( '%d-%m-%Y',i.data_ultimo_atendimento_odontologico) data_ultimo_atendimento_odontologico, 
                    case 
                        when i.indicador_atendimento_odontologico 	   = 1 then 'SIM'
                        when i.indicador_atendimento_odontologico 	  != 1 then 'NÃO'	
                    end indicador_atendimento_odontologico 	  
                from
                    idoso i   join pessoas p on p.cidadao_pec = i.cidadao_pec 
                    left join equipes e on e.cidadao_pec  = p.cidadao_pec 
                {where_clause}
group by p.cidadao_pec	
order by p.nome
                """,
            )
            return response
