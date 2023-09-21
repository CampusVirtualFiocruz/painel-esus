# pylint: disable=invalid-name
from typing import Dict

from src.domain.entities.exams import (ECG, BloodCount, BloodGlucose,
                                       BloodPressure, Creatinine,
                                       SodiumPotassium, TotalCholesterol,
                                       Urine)


class HypertensionExams:
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
            if id not in id_maps:
                id_maps[id] = {
                    'requested': set(),
                    'evaluated': set()
                }
            tipo = row['tipo'].strip()
            codigo = row['codigo'].strip()
            if tipo in "Procedimentos Solicitados":
                id_maps[id]['requested'].add(codigo)
            elif tipo in "Procedimentos Avaliados":
                id_maps[id]['evaluated'].add(codigo)

        id_maps = {}
        procedures = df[(df['tipo'] == 'Procedimentos Avaliados') | (
            df['tipo'] == 'Procedimentos Solicitados')]
        procedures.apply(__parse, axis=1)

        for atd_id in id_maps.items():
            item = id_maps[atd_id]
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
