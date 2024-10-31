# pylint: disable=duplicate-string-formatting-argument
# pylint: disable=E0401,W0613
from typing import Dict
from typing import List

import pandas as pd
from sqlalchemy import text
from src.data.interfaces.diseases_dashboard import DiseasesDashboardRepositoryInterface
from src.domain.dict_types import DiseaseDashboardTotal
from src.domain.entities.disease import Disease
from src.domain.entities.disease_exams import DiseaseExams
from src.domain.entities.hypertension_complications import HypertensionComplications
from src.domain.entities.imc.imc_model import ImcModel
from src.errors import InvalidArgument
from src.infra.db.repositories.disease.age_groups_location import AgeGroupsLocationDF
from src.infra.db.repositories.disease.professional_group import ProfessionalsGroup
from src.infra.db.repositories.sqls.nominal_list.autoreferido import (
    autorreferidos_check,
)
from src.infra.db.settings.connection_local import DBConnectionHandler

from ..sqls import LISTA_PESOS_ALTURAS
from ..sqls.disease.by_gender import get_patients_by_gender
from ..sqls.disease.by_gender import get_patients_by_location


class DiseasesDashboardLocalRepository(DiseasesDashboardRepositoryInterface):

    def __init__(self, disease: Disease):
        self.disease = disease

    def _find_auto_referido(self, cnes: int = None):
        with DBConnectionHandler().get_engine().connect() as db_con:
            sql = autorreferidos_check(cnes,self.disease.name, self.disease.name)
            sql = text(sql)
            autorreferidos = db_con.execute(sql)
            return list(autorreferidos)
    def faixa_etaria_list(self):
        return [
            "0 a 19 anos",
            "20 a 29 anos",
            "30 a 39 anos",
            "40 a 49 anos",
            "50 a 59 anos",
            "60+ anos",
        ]
    def _total_pacientes(self, cnes: int = None):
        with DBConnectionHandler().get_engine().connect() as db_con:
            cnes_condition = ""
            if cnes is not None and cnes:
                cnes_condition = f' where co_dim_unidade_saude = {cnes}'
            sql = f"select distinct co_fat_cidadao_pec , co_dim_tipo_localizacao from {self.disease.name}  {cnes_condition} ;"
            sql = text(sql)
            pacientes = db_con.execute(sql)
            return list(pacientes)

    def _retrieve_imc_info(self, cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            sql = LISTA_PESOS_ALTURAS(self.disease.name, cnes)
            return pd.read_sql_query(sql, con=engine)

    def _retrieve_procedures(self, cnes: int = None, id_cares: List = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        # if not id_cares:
        #     raise InvalidArgument('ID CARES must be a List')
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            sql = f"select * from {self.disease.name} "
            if cnes:
                sql += f""" where co_dim_unidade_saude = {cnes} """

            sql += "ORDER BY no_cidadao ASC;"
            response = pd.read_sql_query(sql, con=engine)
            return response

    def _retrieve_cares(self, cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            sql = f"select * from {self.disease.name} "
            if cnes:
                sql += f""" where co_dim_unidade_saude = {cnes} """
            sql += ";"
            return pd.read_sql_query(sql, con=engine)

    def get_total(self, cnes: int = None) -> DiseaseDashboardTotal:
        cares = self._retrieve_cares(cnes)
        auto_referido = self._find_auto_referido(cnes)
        total_pacientes = self._total_pacientes(cnes)
        return {
            "total_atendimentos": int(cares["co_seq_fat_atd_ind"].unique().shape[0]),
            "total_pacientes": int(len(total_pacientes)),
            "total_auto_referido": int(len(auto_referido)),
        }

    def get_age_groups_location(self, cnes: int = None) -> Dict:
        with DBConnectionHandler().get_engine().connect() as db_con:
            sql = get_patients_by_location(cnes, self.disease.name)
            sql = text(sql)
            pacientes = list(db_con.execute(sql))
            result = dict()
            def init():
                return {"Rural": 0, "Urbano": 0, "Nao Informado": 0}
            for i in self.faixa_etaria_list():
                result[i] = init()
            for p in pacientes:
                if p[2] not in result:
                    result[p[2]] = init()
                result[p[2]][p[1]] = p[0]

            return result

    def get_age_group_gender(self, cnes: int = None) -> Dict:
        with DBConnectionHandler().get_engine().connect() as db_con:
            sql = get_patients_by_gender(cnes, self.disease.name)
            sql = text(sql)
            pacientes = list(db_con.execute(sql))
            result = dict()
            def init():
                return  {"Feminino": 0, "Masculino": 0}
            for i in self.faixa_etaria_list():
                result[i] = init()
            for p in pacientes:
                if p[2] not in result:
                    result[p[2]] = init()
                result[p[2]][p[1]] = p[0]

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
        cares = self._retrieve_imc_info(cnes)
        imc_model = ImcModel()
        cares.apply(
            lambda x: imc_model.check_presence(
                weight=x["nu_peso"], height=x["nu_altura"]
            ),
            axis=1,
        )

        results = [
            imc_item.statistics_response(cares.shape[0])
            for imc_item in imc_model.get_list()
        ]
        current_total = 0
        for i in results:
            current_total += i[1]["com_consulta_abs"]

        total = cares.shape[0] - current_total
        consultas = 100 * round(float((total) / cares.shape[0]), 2)

        results = results + [
            [
                "Não Informado",
                {
                    "com_consulta": consultas,
                    "com_consulta_abs": int((total)),
                    "limite": "Outros",
                    "sem_consulta": round(100 - consultas, 2),
                    "sem_consulta_abs": cares.shape[0] - (total),
                },
            ]
        ]

        return results

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
        result = list(filter(lambda x: x["nome"] is not None, result))
        for i in result:
            i["idade"] = 0 if i["idade"] is None else i["idade"]

        page_ini = (page - 1) * 20
        page_end = page * 20
        return result[page_ini:page_end]
