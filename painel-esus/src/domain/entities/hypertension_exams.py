# pylint: disable=invalid-name
from typing import Dict, List

from src.domain.entities.exams import (ECG, BloodCount, BloodGlucose,
                                       BloodPressure, Creatinine,
                                       SodiumPotassium, TotalCholesterol,
                                       Urine)

from src.domain.entities.complications import (
    HeartAttack, BrainStroke, KidneyDisease, CoronaryDisease, VascularBrainDisease
)
from .disease_exams import DiseaseExams


class HypertensionExams(DiseaseExams):
    def __init__(self):
        self._res = []
        self.list = [
            BloodPressure(),
            BloodGlucose(),
            Creatinine(),
            Urine(),
            SodiumPotassium(),
            TotalCholesterol(),
            BloodCount(),
            ECG()
        ]

    def check_presence(self, df) -> Dict:

        def __parse(row):
            atd_id = row['co_seq_fat_atd_ind']
            atd_id = str(atd_id)
            if atd_id not in id_maps:
                id_maps[atd_id] = {
                    'requested': set(),
                    'evaluated': set()
                }
            tipo = row['tipo'].strip()
            codigo = row['codigo'].strip()
            if tipo in "Procedimentos Solicitados":
                id_maps[atd_id]['requested'].add(codigo)
            elif tipo in "Procedimentos Avaliados":
                id_maps[atd_id]['evaluated'].add(codigo)

        id_maps = {}
        procedures = df[(df['tipo'] == 'Procedimentos Avaliados') | (
            df['tipo'] == 'Procedimentos Solicitados')]
        procedures.apply(__parse, axis=1)

        for atd_id in id_maps.items():
            item = atd_id[1]
            for exam in self.list:
                exam.check_presence(item['evaluated'], item['requested'])
        response = []
        for exam in self.list:
            response.append({
                'avaliados': exam.evaluated,
                'solicitados': exam.requested,
                'tipo': exam.label
            })
        return response


class HypertensionExamsList(HypertensionExams):
    def __init__(self):
        self._res = []
        self.list = [
            HeartAttack(),
            BrainStroke(),
            KidneyDisease(),
            CoronaryDisease(),
            VascularBrainDisease(),
        ]

class IndividualHypertensionExams(DiseaseExams):
        
    def check_presence(self, df) -> List:
        def __parse(row):
            atd_id = row['co_seq_fat_atd_ind']
            atd_id = str(atd_id)
            if atd_id not in id_maps:
                id_maps[atd_id] = {
                    'nome': row['no_cidadao'],
                    'idade': row['idade'],
                    'requested': set(),
                    'evaluated': set(),
                    'exams_list': HypertensionExamsList()
                }
            tipo = row['tipo'].strip()
            codigo = row['codigo'].strip()
            if tipo in "Procedimentos Solicitados":
                id_maps[atd_id]['requested'].add(codigo)
            elif tipo in "Procedimentos Avaliados":
                id_maps[atd_id]['evaluated'].add(codigo)

        id_maps = {}
        procedures = df[(df['tipo'] == 'Procedimentos Avaliados') | (
            df['tipo'] == 'Procedimentos Solicitados')]
        procedures.apply(__parse, axis=1)

        for id_map in id_maps.items():
            item = id_map[1]
            for exam in item['exams_list'].list:
                exam.check_presence(item['evaluated'], item['requested'])
        response = []
        for id_map in id_maps.items():
            item = id_map[1]
            partial_resp = {
                'nome': item['nome'],
                'idade': item['idade'],
            }
            for exam in item['exams_list'].list:
                partial_resp.update({
                    exam.label: [exam.evaluated, exam.requested]
                })
            response.append(partial_resp)

        return response

