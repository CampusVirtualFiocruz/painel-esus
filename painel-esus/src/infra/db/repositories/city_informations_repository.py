# pylint: disable=E0401, W0237,C2801, W0611
import json
from math import e
from typing import Dict
from webbrowser import get

import duckdb
import pandas as pd
from sqlalchemy.ext.declarative import DeclarativeMeta
from src.data.interfaces.city_information_repository import CityInformationRepository
from src.infra.db.entities.equipes import Equipes
from src.infra.db.repositories.sqls import (
    CITY_INFORMATION,
    UNITS_LIST,
    UNIT_LIST_WITH_PATIENTS,
)
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.settings.connection_local import (
    DBConnectionHandler as LocalDBConnectionHandler,
)
from src.env.conf import getenv

class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # Convert SQLAlchemy model to dictionary
            fields = {}
            for field in [
                x for x in dir(obj) if not x.startswith("_") and x != "metadata"
            ]:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields
        return json.JSONEncoder.default(self, obj)


class CityInformationsRepository(CityInformationRepository):
    
    def __init__(self):
        self.mock_data = getenv("MOCK", False, False) == 'True'
        

    def get_city_info(self, cnes: int = None) -> Dict:
        if self.mock_data:
            return pd.DataFrame(data=[{
                "municipio":"SUSÓPOLIS",
                "cep": 123456,
                "codibge": 2508505,
                "uf": "SUS",
                "estado": "SUS"
                }])
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            res = pd.read_sql_query(CITY_INFORMATION, con=engine)
            return res

    def get_units(self) -> Dict:
        con = duckdb.connect()
        res = con.sql(UNITS_LIST).df()
        if self.mock_data:
            def parse(x):
                x['no_unidade_saude'] = "Unidade de saude {}".format(x['co_seq_dim_unidade_saude'])
                return x            
            res=res.apply(parse, axis=1)
        
        return res

    def get_units_with_patients(self) -> Dict:
        con = duckdb.connect()
        res = con.sql(UNIT_LIST_WITH_PATIENTS).df()
        if self.mock_data:
            def parse(x):
                x['no_unidade_saude'] = "Unidade de saude {}".format(x['co_seq_dim_unidade_saude'])
                return x            
            res=res.apply(parse, axis=1)
        return res

    def get_teams(self, cnes: int = None):
        sql = f""" select 
                    distinct on (co_cidadao, codigo_equipe) 
                    co_fat_cidadao_pec cidadao_pec,
                    co_cidadao co_cidadao,
                    co_dim_unidade_saude codigo_unidade_saude,
                    nome_unidade_saude nome_unidade_saude,
                    codigo_equipe,
                    nome_equipe,
                    nu_ine_vinc_equipe ine,
                    nu_micro_area micro_area
                from 
                read_parquet('./dados/output/cadastro_db.parquet') """

        if cnes is not None:
            sql += f""" where codigo_equipe={cnes} """
        con = duckdb.connect()
        result = con.sql(sql).df()
        if self.mock_data:
            def parse(x):
                x['nome_unidade_saude'] = "Unidade de saude {}".format(x['codigo_unidade_saude'])
                x['nome_equipe'] = "Equipe {}".format(x['codigo_equipe'])
                return x            
            result=result.apply(parse, axis=1)
        result_json = result.to_dict(orient="records")
        return result_json
