# pylint: disable=E0401
import pandas as pd
from pandas import DataFrame
from src.data.interfaces.oral_health_dashboard_repository import \
    OralHealthDashboardRepositoryInterface
from src.errors import InvalidArgument
from src.infra.db.repositories.sqls.odonto import (
    ALL_CARES_BY_PLACE, CARES_BY_LINE_OF_SERVICE, CARES_BY_OUTCOME,
    CARES_BY_PLACE, CARES_BY_TYPE_OF_SERVICE, CARES_LOCATION_BY_AGE_RANGE,
    CARES_LOCATION_BY_GENDER, EXTRACTION_PROCEDURES_PROPORTION,
    TOTAL_ATENDIMENTOS)
from src.infra.db.settings.connection_local import DBConnectionHandler


class OralHealthDashboardRepository(OralHealthDashboardRepositoryInterface):

    def __init__(self):
        pass

    def get_total(self, cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            total = pd.read_sql_query(TOTAL_ATENDIMENTOS(cnes), con=engine)
            return int(total['total'].iloc[0])

    def get_cares_by_line_of_services(self,  cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            total = pd.read_sql_query(
                CARES_BY_LINE_OF_SERVICE(cnes), con=engine)
            return total

    def get_cares_by_type_of_services(self,  cnes: int = None) -> DataFrame:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            if cnes:
                total = pd.read_sql_query(
                    CARES_BY_TYPE_OF_SERVICE(cnes), con=engine, params={"cnes": cnes})
            else:
                total = pd.read_sql_query(
                    CARES_BY_TYPE_OF_SERVICE(cnes), con=engine)
            return total

    def get_extraction_procedures_proportion(self,  cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            if cnes:
                total = pd.read_sql_query(
                    EXTRACTION_PROCEDURES_PROPORTION(cnes), con=engine, params={"cnes": cnes})
            else:
                total = pd.read_sql_query(
                    EXTRACTION_PROCEDURES_PROPORTION(cnes), con=engine)
            return total

    def get_oral_health_cares_by_age_range(self,  cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            if cnes:
                total = pd.read_sql_query(
                    CARES_LOCATION_BY_AGE_RANGE(cnes), con=engine, params={"cnes": cnes})
            else:
                total = pd.read_sql_query(
                    CARES_LOCATION_BY_AGE_RANGE(cnes), con=engine)
            return total

    def get_oral_health_cares_by_gender(self,  cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            if cnes:
                total = pd.read_sql_query(
                    CARES_LOCATION_BY_GENDER(cnes), con=engine, params={"cnes": cnes})
            else:
                total = pd.read_sql_query(
                    CARES_LOCATION_BY_GENDER(cnes), con=engine)
            return total

    def get_oral_health_cares_by_outcome(self,  cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            if cnes:
                total = pd.read_sql_query(
                    CARES_BY_OUTCOME(cnes), con=engine, params={"cnes": cnes})
            else:
                total = pd.read_sql_query(
                    CARES_BY_OUTCOME(cnes), con=engine)
            return total

    def get_oral_health_cares_by_place(self,  cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            if cnes:
                total = pd.read_sql_query(
                    CARES_BY_PLACE(cnes), con=engine, params={"cnes": cnes})
            else:
                total = pd.read_sql_query(
                    CARES_BY_PLACE(cnes), con=engine)
            return total

    def get_oral_health_all_cares_by_place(self,  cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            if cnes:
                total = pd.read_sql_query(
                    ALL_CARES_BY_PLACE(cnes), con=engine, params={"cnes": cnes})
            else:
                total = pd.read_sql_query(
                    ALL_CARES_BY_PLACE(cnes), con=engine)
            return total
