# pylint: disable=duplicate-string-formatting-argument
# pylint: disable=E0401,C0301,W0612,W0611
from typing import Dict
from typing import List

import pandas as pd
from src.data.interfaces.diseases_dashboard import DiseasesDashboardRepositoryInterface
from src.domain.dict_types import DiseaseDashboardTotal
from src.domain.entities.disease import Disease
from src.domain.entities.disease_exams import DiseaseExams
from src.domain.entities.hypertension_complications import HypertensionComplications
from src.domain.entities.imc.imc_model import ImcModel
from src.errors import InvalidArgument
from src.infra.db.repositories.disease.age_group_gender import AgeGroupGenderDF
from src.infra.db.repositories.disease.age_groups_location import AgeGroupsLocationDF
from src.infra.db.repositories.disease.professional_group import ProfessionalsGroup
from src.infra.db.repositories.sqls import (
    ATENDIMENTO_INDIVIDUAL_CID_CIAPS_PROCEDIMENTOS,
)
from src.infra.db.repositories.sqls import (
    ATENDIMENTO_INDIVIDUAL_PROCEDIMENTOS_NASCIMENTO,
)
from src.infra.db.repositories.sqls import MAX_DT_ATENDIMENTO_ATENDIMENTO_INDIVIDUAL
from src.infra.db.settings.connection import DBConnectionHandler


class DiseasesDashboardRepository(DiseasesDashboardRepositoryInterface):

    def __init__(self, disease: Disease):
        self.disease = disease

    def update_bases(self):
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            max_date = pd.read_sql_query(
                MAX_DT_ATENDIMENTO_ATENDIMENTO_INDIVIDUAL, con=engine
            )
            max_date = str(max_date["max"].iloc[0])
            disease = self.disease
            cids = ",".join([f"'%%|{i}|%%'" for i in self.disease.target])
            sql = ATENDIMENTO_INDIVIDUAL_CID_CIAPS_PROCEDIMENTOS(cids)
            print(sql)
            # sql += """
            #         where
            #             dt_registro between '{}'::DATE - interval '12 month' and '{}' and codigo in ({})
            #     """.format(
            #     max_date, max_date,
            #     ", ".join([f"'{cid}'" for cid in disease.target])
            # )
            sql += ";"
            ids = (
                pd.read_sql_query(sql, con=engine)["co_seq_fat_atd_ind"]
                .unique()
                .tolist()
            )
            sql = ATENDIMENTO_INDIVIDUAL_CID_CIAPS_PROCEDIMENTOS(cids)
            sql += """
                    where
                        co_seq_fat_atd_ind in ({})
                """.format(
                ", ".join([f"'{id}'" for id in ids])
            )
            return pd.read_sql_query(sql, con=engine)

    def _retrieve_cares(self, cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            max_date = pd.read_sql_query(
                MAX_DT_ATENDIMENTO_ATENDIMENTO_INDIVIDUAL, con=engine
            )
            max_date = str(max_date["max"].iloc[0])
            sql = ATENDIMENTO_INDIVIDUAL_CID_CIAPS_PROCEDIMENTOS
            disease = self.disease

            sql += """
                    where
                        dt_registro between '{}'::DATE - interval '12 month' and '{}' and codigo in ({})
                """.format(
                max_date, max_date, ", ".join(
                    [f"'{cid}'" for cid in disease.target])
            )
            if cnes:
                sql += f""" AND atd.co_dim_unidade_saude = {cnes} """
            sql += ";"
            return pd.read_sql_query(sql, con=engine)

    def _retrieve_procedures(self, cnes: int = None, id_cares: List = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        if not id_cares:
            raise InvalidArgument("ID CARES must be a List")
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            max_date = pd.read_sql_query(
                MAX_DT_ATENDIMENTO_ATENDIMENTO_INDIVIDUAL, con=engine
            )
            max_date = str(max_date["max"].iloc[0])
            sql = ATENDIMENTO_INDIVIDUAL_PROCEDIMENTOS_NASCIMENTO

            sql += """
                    where
                        dt_registro between '{}'::DATE - interval '12 month' and '{}'
                        and co_seq_fat_atd_ind in ({}) 
                """.format(
                max_date, max_date, ", ".join([f"'{id_}'" for id_ in id_cares])
            )
            if cnes:
                sql += f""" AND atd.co_dim_unidade_saude = {cnes} """

            sql += "ORDER BY tfcp.no_cidadao ASC;"
            response = pd.read_sql_query(sql, con=engine)
            return response

    def get_total(self, cnes: int = None) -> DiseaseDashboardTotal:
        cares = self._retrieve_cares(cnes)
        return {
            "total_atendimentos": int(cares["co_seq_fat_atd_ind"].unique().shape[0]),
            "total_pacientes": int(cares["co_fat_cidadao_pec"].unique().shape[0]),
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

    def get_exams_count(
        self, cnes: int = None, exam_disease: DiseaseExams = None
    ) -> Dict:
        cares = self._retrieve_cares(cnes)
        id_cares = cares["co_seq_fat_atd_ind"].unique().tolist()
        procedures = self._retrieve_procedures(cnes, id_cares)
        hypertension = exam_disease
        return hypertension.check_presence(procedures)

    def get_imc(self, cnes: int = None) -> Dict:
        cares = self._retrieve_cares(cnes)
        imc_model = ImcModel()
        cares.apply(
            lambda x: imc_model.check_presence(
                weight=x["nu_peso"], height=x["nu_altura"]
            ),
            axis=1,
        )
        return [
            imc_item.statistics_response(cares.shape[0])
            for imc_item in imc_model.get_list()
        ]

    def get_individual_exams_count(
        self, cnes: int = None, exam_disease: DiseaseExams = None, page=1
    ) -> Dict:
        cares = self._retrieve_cares(cnes)
        id_cares = cares["co_seq_fat_atd_ind"].unique().tolist()
        procedures = self._retrieve_procedures(cnes, id_cares)
        age_group = AgeGroupsLocationDF()
        procedures = age_group.parse_date(procedures)
        hypertension = exam_disease
        result = hypertension.check_presence(procedures)
        page_ini = (page - 1) * 20
        page_end = page * 20
        return result[page_ini:page_end]
