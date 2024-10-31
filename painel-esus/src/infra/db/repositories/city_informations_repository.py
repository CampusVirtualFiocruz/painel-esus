# pylint: disable=E0401
from typing import Dict

import pandas as pd
from src.data.interfaces.city_information_repository import CityInformationRepository
from src.infra.db.repositories.sqls import CITY_INFORMATION
from src.infra.db.repositories.sqls import UNITS_LIST
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.settings.connection_local import (
    DBConnectionHandler as LocalDBConnectionHandler,
)


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
