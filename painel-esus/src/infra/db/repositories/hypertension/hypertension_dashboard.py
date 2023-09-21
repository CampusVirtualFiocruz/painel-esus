# pylint: disable=duplicate-string-formatting-argument
from typing import Dict

import pandas as pd

from src.data.interfaces.hypertension_dashboard import \
    HypertensionDashboardRepositoryInterface
from src.domain.dict_types import DiseaseDashboardTotal
from src.domain.entities.hypertension import Hypertension
from src.domain.entities.hypertension_complications import \
    HypertensionComplications
from src.domain.entities.hypertension_exams import HypertensionExams
from src.domain.entities.imc.imc_model import ImcModel
from src.errors import InvalidArgument
from src.infra.db.repositories.hypertension.age_group_gender import \
    AgeGroupGenderDF
from src.infra.db.repositories.hypertension.age_groups_location import \
    AgeGroupsLocationDF
from src.infra.db.repositories.hypertension.professional_group import \
    ProfessionalsGroup
from src.infra.db.repositories.sqls import (
    ATENDIMENTO_INDIVIDUAL_CID_CIAPS_NASCIMENTO,
    ATENDIMENTO_INDIVIDUAL_PROCEDIMENTOS_NASCIMENTO,
    MAX_DT_ATENDIMENTO_ATENDIMENTO_INDIVIDUAL)
from src.infra.db.settings.connection_irece import DBConnectionHandler


class HypertensionDashboardRepository(HypertensionDashboardRepositoryInterface):

    def _init_(self):
        pass

    def _retrieve_cares(self, cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            max_date = pd.read_sql_query(
                MAX_DT_ATENDIMENTO_ATENDIMENTO_INDIVIDUAL, con=engine)
            max_date = str(max_date['max'].iloc[0])
            sql = ATENDIMENTO_INDIVIDUAL_CID_CIAPS_NASCIMENTO
            hypertension = Hypertension()

            sql += """
                    where
                        dt_registro between '{}'::DATE - interval '12 month' and '{}' and codigo in ({})
                """.format(
                max_date, max_date,
                ", ".join([f"'{cid}'" for cid in hypertension.target])
            )
            if cnes:
                sql += f""" AND atd.co_dim_unidade_saude = {cnes} """
            sql += ';'
            return pd.read_sql_query(sql, con=engine)

    def _retrieve_procedures(self, cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            max_date = pd.read_sql_query(
                MAX_DT_ATENDIMENTO_ATENDIMENTO_INDIVIDUAL, con=engine)
            max_date = str(max_date['max'].iloc[0])
            sql = ATENDIMENTO_INDIVIDUAL_PROCEDIMENTOS_NASCIMENTO

            sql += """
                    where
                        dt_registro between '{}'::DATE - interval '12 month' and '{}'
                """.format(
                max_date, max_date
            )
            if cnes:
                sql += f""" AND atd.co_dim_unidade_saude = {cnes} """
            sql += ';'
            return pd.read_sql_query(sql, con=engine)

    def get_total(self, cnes: int = None) -> DiseaseDashboardTotal:
        cares = self._retrieve_cares(cnes)
        return {'total': int(
            cares['co_seq_fat_atd_ind'].unique().shape[0]
        )
        }

    def get_age_groups_location(self, cnes: int = None) -> Dict:
        cares = self._retrieve_cares(cnes)
        age_group = AgeGroupsLocationDF()
        result = age_group.age_group_location(cares)
        return result

    def get_age_group_gender(self, cnes: int = None) -> Dict:
        cares = self._retrieve_cares(cnes)
        age_group = AgeGroupGenderDF()
        result = age_group.age_group_gender(cares)
        return result

    def get_complications(self, cnes: int = None) -> None:
        cares = self._retrieve_cares(cnes)
        hypertension_complications = HypertensionComplications(cares)
        statistics = hypertension_complications.compute_statistics()
        return statistics

    def get_professionals_count(self, cnes: int = None) -> Dict:
        cares = self._retrieve_cares(cnes)
        professionals = ProfessionalsGroup()
        return professionals.get_professionals_count(cares)

    def get_exams_count(self, cnes: int = None) -> Dict:
        procedures = self._retrieve_procedures(cnes)
        hypertension = HypertensionExams()
        return hypertension.check_presence(procedures)

    def get_imc(self, cnes: int = None) -> Dict:
        cares = self._retrieve_cares(cnes)
        imc_model = ImcModel()
        cares.apply(lambda x: imc_model.check_presence(
            weight=x['nu_peso'],
            height=x['nu_altura']
        ), axis=1)
        return [
            imc_item.statistics_response(cares.shape[0])
            for imc_item in imc_model.get_list()
        ]
