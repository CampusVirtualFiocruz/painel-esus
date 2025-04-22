# pylint: disable=duplicate-string-formatting-argument
# pylint: disable=E0401,W0613
from typing import Dict, List

import duckdb
import pandas as pd
from sqlalchemy import text
from src.data.interfaces.diseases_dashboard import DiseasesDashboardRepositoryInterface
from src.domain.dict_types import DiseaseDashboardTotal
from src.domain.entities.disease import Disease
from src.domain.entities.disease_exams import DiseaseExams
from src.errors import InvalidArgument
from src.infra.db.repositories.disease.age_groups_location import AgeGroupsLocationDF
from src.infra.db.repositories.disease.professional_group import ProfessionalsGroup
from src.infra.db.settings.connection_local import DBConnectionHandler

from ..sqls.disease.auto_referidos import (
    get_autoreferidos,
    get_cares,
    get_complications,
    get_diabetes_exams_count,
    get_hypertension_exams_count,
    get_imc,
    get_professionals,
    get_total_cares,
    get_total_cares_12,
    get_total_patients,
)
from ..sqls.disease.by_gender import get_patients_by_gender, get_patients_by_location


class DiseasesDashboardLocalRepository(DiseasesDashboardRepositoryInterface):

    def __init__(self, disease: Disease):
        self.disease = disease
        self.disease_flag = disease.name == "hipertensao"

    def _find_auto_referido(
        self,
        cnes: int = None,
        equipe: int = None,
    ):
        hipertension_autoreferidos_sql = get_autoreferidos(
            cnes, equipe, self.disease_flag
        )
        con = duckdb.connect()
        autorreferidos = con.sql(hipertension_autoreferidos_sql).fetchone()
        return autorreferidos

    def faixa_etaria_list(self):
        return [
            "0 a 19 anos",
            "20 a 29 anos",
            "30 a 39 anos",
            "40 a 49 anos",
            "50 a 59 anos",
            "60+ anos",
        ]

    def _total_pacientes(self, cnes: int = None, equipe: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        cares_sql = get_total_patients(cnes, equipe, self.disease_flag)
        con = duckdb.connect()
        patients = con.sql(cares_sql).fetchone()
        return patients

    def _retrieve_imc_info(self, cnes: int = None, equipe: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        cares_sql = get_imc(cnes, equipe, self.disease_flag)
        con = duckdb.connect()
        patients = con.sql(cares_sql).fetchall()
        return patients

    def _retrieve_procedures(
        self,
        cnes: int = None,
        id_cares: List = None,
        equipe: int = None,
    ):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        # if not id_cares:
        #     raise InvalidArgument('ID CARES must be a List')
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            sql = f"select * from {self.disease.name} "
            if cnes:
                sql += f""" where co_dim_unidade_saude = {cnes} """
                if equipe and equipe is not None:
                    sql += f""" and co_dim_equipe = {equipe} """

            sql += "ORDER BY no_cidadao ASC;"
            response = pd.read_sql_query(sql, con=engine)
            return response

    def _retrieve_cares(self, cnes: int = None, equipe: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        cares_sql = get_cares(cnes, equipe, self.disease_flag)
        con = duckdb.connect()
        cares = con.sql(cares_sql).fetchone()
        return cares

    def _retrieve_total_cares(self, cnes: int = None, equipe: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        cares_sql = get_total_cares(cnes, equipe, self.disease_flag)
        con = duckdb.connect()
        cares = con.sql(cares_sql).fetchone()
        return cares

    def _retrieve_total_cares_12(self, cnes: int = None, equipe: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        cares_sql = get_total_cares_12(cnes, equipe, self.disease_flag)
        con = duckdb.connect()
        cares = con.sql(cares_sql).fetchone()
        return cares

    def _get_complications(self, cnes: int = None, equipe: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        cares_sql = get_complications(cnes, equipe, self.disease_flag)
        con = duckdb.connect()
        cares = con.sql(cares_sql).fetchone()
        return cares

    def _get_professionals(self, cnes: int = None, equipe: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        cares_sql = get_professionals(cnes, equipe, self.disease_flag)
        con = duckdb.connect()
        cares = con.sql(cares_sql).fetchone()
        return cares

    def _get_exams_count(self, cnes: int = None, equipe: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        if self.disease_flag:
            cares_sql = get_hypertension_exams_count(cnes, equipe)
        else:
            cares_sql = get_diabetes_exams_count(cnes, equipe)
        con = duckdb.connect()
        cares = con.sql(cares_sql).fetchall()
        return cares

    def get_total(self, cnes: int = None, equipe: int = None) -> DiseaseDashboardTotal:
        cares = self._retrieve_total_cares_12(cnes, equipe)
        auto_referido = self._find_auto_referido(cnes, equipe)
        total_pacientes = self._total_pacientes(cnes, equipe)
        return {
            "total_atendimentos": int(cares[0]),
            "total_pacientes": int(total_pacientes[0]),
            "total_auto_referido": int(auto_referido[0]),
        }

    def get_age_groups_location(self, cnes: int = None, equipe: int = None) -> Dict:
        sql = get_patients_by_location(cnes, self.disease.name, equipe)
        con = duckdb.connect()
        pacientes = con.sql(sql).fetchall()
        result = dict()

        def init():
            return {"Rural": 0, "Urbano": 0, "Nao Informado": 0}

        for i in self.faixa_etaria_list():
            result[i] = init()
            for paciente in pacientes:
                if paciente[2] is not None:
                    if paciente[2] not in result:
                        result[paciente[2]] = init()
                    _key = paciente[1].replace("Urbana", "Urbano")

                    result[paciente[2]][_key] = paciente[0]
        return result

    def get_age_group_gender(self, cnes: int = None, equipe: int = None) -> Dict:
        sql = get_patients_by_gender(cnes, self.disease.name, equipe)
        con = duckdb.connect()
        pacientes = con.sql(sql).fetchall()
        result = dict()

        def init():
            return {"Feminino": 0, "Masculino": 0}

        for i in self.faixa_etaria_list():
            result[i] = init()
        for paciente in pacientes:
            if paciente[2] is not None:
                if paciente[2] not in result:
                    result[paciente[2]] = init()
                result[paciente[2]][str(paciente[1]).capitalize()] = paciente[0]
        return result

    def get_complications(self, cnes: int = None, equipe: int = None) -> None:
        cares = self._get_complications(cnes, equipe)

        def init_complications(value, total):
            return {
                "com_consulta": round(value / total, 2)*100,
                "com_consulta_abs": value,
                "sem_consulta": round((total - value) / total, 2)*100,
                "sem_consulta_abs": total - value,
            }

        return [
            {"Infarto Agudo do Miocárdio": init_complications(cares[0], cares[5])},
            {"Acidente Vascular Encefálico": init_complications(cares[1], cares[5])},
            {"Doença renal": init_complications(cares[2], cares[5])},
            {"Doença Coronariana": init_complications(cares[3], cares[5])},
            {"Doença Cerebrovascular": init_complications(cares[4], cares[5])},
        ]

    def get_professionals_count(self, cnes: int = None, equipe: int = None) -> Dict:
        cares = self._get_professionals(cnes, equipe)
        professionals = ProfessionalsGroup()
        return professionals.get_professionals_count(cares)

    def get_exams_count(
        self,
        cnes: int = None,
        equipe: int = None,
        exam_disease: DiseaseExams = None,
    ) -> Dict:
        cares = self._get_exams_count(cnes, equipe)

        condition_map = {
            "1": "sem-solicitacao",
            "2": "aguardando-resultado",
            "3": "resultado-registrado",
            # "4": "nao-informado"
        }

        def init_obj():
            result = dict()
            for condition in condition_map.values():
                result[condition] = 0
            return result

        if self.disease_flag:
            labels = [
                "Glicemia",
                "Creatinina",
                "EAS/EQU (urina rotina)",
                "Sódio",
                "Potássio",
                "Colesterol total",
                "Hemograma",
                "Eletrocardiograma",
            ]
        else:
            labels = [
                "Glicemia",
                "Hemoglobina Glicada",
                "Retinografia",
                "Creatinina",
                "EAS/EQU (urina rotina)",
                "Hemograma",
                "Colesterol total",
            ]
        result = dict()
        for label in labels:
            result[label] = init_obj()
        if len(cares) == 0:
            return result

        for care in cares:
            for idx, val in enumerate(care):
                if val is None:
                    val = 1
                result[labels[idx]][condition_map[str(val)]] += 1

        return result

    def get_imc(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        cares = self._retrieve_imc_info(cnes, equipe)

        imc_labels = {
            "baixo_peso": {"value": "< 18.5", "label": "Baixo Peso"},
            "peso_adequado": {"value": ">= 18.5  e <= 24.9", "label": "Peso Adequado"},
            "excesso_peso": {"value": ">= 25 e <= 29.9", "label": "Excesso de Peso"},
            "obesidade": {"value": " >= 30", "label": "Obesidade"},
            "na_outros": {"value": "outros casos", "label": "Não Informado"},
        }

        def init_obj(label):
            return {
                "com_consulta": 0,
                "com_consulta_abs": 0,
                "limite": label,
                "sem_consulta": 1,
                "sem_consulta_abs": 0,
            }

        result = dict()
        for label in imc_labels.keys():
            result[label] = init_obj(imc_labels[label]["value"])
        for care in cares:
            result[care[0]]["com_consulta"] = round(float(care[1]), 2) * 100
            result[care[0]]["com_consulta_abs"] = int(care[2])
            result[care[0]]["sem_consulta"] = (1 - round(care[1], 2)) * 100
            result[care[0]]["sem_consulta_abs"] = int(care[3] - care[2])

        imc_result = dict()
        for r in result.keys():
            _key = imc_labels[r]["label"]
            _value = result[r]
            imc_result[_key] = [_key, _value]

        return list(imc_result.values())

    def get_individual_exams_count(
        self,
        cnes: int = None,
        equipe: int = None,
        exam_disease: DiseaseExams = None,
        page=1,
    ) -> Dict:
        cares = self._retrieve_cares(cnes, equipe)
        id_cares = cares["co_seq_fat_atd_ind"].unique().tolist()
        procedures = self._retrieve_procedures(cnes, id_cares, equipe)
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
