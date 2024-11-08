# pylint: disable=E0401, W0237,C2801, W0611
import json
from math import e
from typing import Dict

import pandas as pd
from sqlalchemy.ext.declarative import DeclarativeMeta
from src.data.interfaces.city_information_repository import CityInformationRepository
from src.infra.db.entities.equipes import Equipes
from src.infra.db.repositories.sqls import CITY_INFORMATION
from src.infra.db.repositories.sqls import UNITS_LIST
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.settings.connection_local import (
    DBConnectionHandler as LocalDBConnectionHandler,
)


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

    def get_city_info(self, cnes: int = None) -> Dict:
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            res = pd.read_sql_query(CITY_INFORMATION, con=engine)
            return res

    def get_units(self) -> Dict:
        with LocalDBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            res = pd.read_sql_query(UNITS_LIST, con=engine)
            return res

    def get_teams(self, cnes: int = None):
        with LocalDBConnectionHandler() as db_con:
            users = (
                db_con.session.query(Equipes)
                .distinct(Equipes.cidadao_pec, Equipes.codigo_equipe)
                .filter(Equipes.codigo_unidade_saude == cnes)
            ).all()
            return json.loads(json.dumps(list(users), cls=AlchemyEncoder))
