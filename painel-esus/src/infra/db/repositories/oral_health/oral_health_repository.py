import json
import duckdb
from src.data.interfaces.oral_health_dashboard_repository import (
    OralHealthDashboardRepositoryInterface,
)
from .sqls.oral_health_queries import (
    by_gender,
    by_race,
    first_appointment,
    conclued_treatment,
    extraction,
    prevention_procedures,
    atraumatic_treatment,
    supervised_brushing,
    oral_healt_base_sql
)


class OralHealthRepository(OralHealthDashboardRepositoryInterface):
    def __init__(self,):
        self.session = duckdb.connect()

    def get_oral_health_cares_by_gender(
        self, cnes=None, equipe=None, category: str = None
    ):
        sql = by_gender(cnes, equipe, category)
        return self.session.execute(sql).fetchall()

    def get_oral_health_cares_by_race(
        self, cnes=None, equipe=None, category: str = None
    ):
        sql = by_race(cnes, equipe, category)
        return self.session.execute(sql).fetchall()

    def get_oral_health_first_appointment(
        self, cnes=None, equipe=None, category: str = None
    ):
        sql = first_appointment(cnes, equipe, category)
        return self.session.execute(sql).fetchall()

    def get_oral_health_conclued_treatment(self, cnes=None, equipe=None, category=None):
        sql = conclued_treatment(cnes, equipe, category)
        return self.session.execute(sql).fetchall()

    def get_oral_health_extraction(self, cnes=None, equipe=None, category=None):
        sql = extraction(cnes, equipe, category)
        return self.session.execute(sql).fetchall()

    def get_oral_health_prevention_procedures(
        self, cnes=None, equipe=None, category=None
    ):
        sql = prevention_procedures(cnes, equipe, category)
        return self.session.execute(sql).fetchall()

    def oral_health_get_atraumatic_treatment(
        self, cnes=None, equipe=None, category=None
    ):
        sql = atraumatic_treatment(cnes, equipe, category)
        return self.session.execute(sql).fetchall()

    def oral_health_get_supervised_brushing(
        self, cnes=None, equipe=None, category=None
    ):
        sql = supervised_brushing(cnes, equipe, category)
        return self.session.execute(sql).fetchall()
    
    def find_filter_nominal(
        self,
        cnes: int,
        page: int = 0,
        pagesize: int = 10,
        nome: str = None,
        cpf: str = None,
        equipe: int = None,
        query: str = None,
        sort=[],
        category: str = 'atendidas'
    ):
        page = int(page) if page is not None else 0
        pagesize = int(pagesize) if pagesize is not None else 0
        con = duckdb.connect()
        oral_health = oral_healt_base_sql()
        conditions = []
        or_conditions = []

        print(cnes, equipe)
        print('-----')
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
            oral_health
            + sql_where
            + f"  {order} LIMIT {limit} OFFSET {offset} "
        ).df()

        users = users.to_dict(orient="records")
        total = len(con.sql(oral_health + sql_where).fetchall())
        print( oral_health + sql_where )
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

