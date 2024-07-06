# pylint: disable=E0401
import pandas as pd

from .hypertension_exams import HypertensionExams
from .hypertension_exams import IndividualHypertensionExams


def test_hypertension_exams():
    data_frame = pd.DataFrame(columns=[
        'co_seq_fat_atd_ind',
        'codigo', 'tipo', 'co_fat_cidadao_pec'],
        data=[
        [1, 'ABEX026', 'Procedimentos Avaliados', 1],
        [1, 'ABEX026', 'Procedimentos Solicitados', 1]
    ])
    arterial_hypertension_list = HypertensionExams()
    response = arterial_hypertension_list.check_presence(data_frame[[
        'co_seq_fat_atd_ind', 'codigo', 'tipo', 'co_fat_cidadao_pec']])
    print(response)


def test_hypertension_individual_exams():
    data_frame = pd.DataFrame(columns=[
        'co_seq_fat_atd_ind',
        'codigo', 'tipo', 'co_fat_cidadao_pec', 'no_cidadao', 'idade'],
        data=[
        [1, 'ABEX026', 'Procedimentos Avaliados', 1, 'Rosa', '30'],
        [1, 'ABEX026', 'Procedimentos Solicitados', 1, 'Rosa', '30'],
        [2, 'ABEX026', 'Procedimentos Avaliados', 2, 'Verde', '31'],
        [2, 'ABEX026', 'Procedimentos Solicitados', 2, 'Verde', '31'],
    ])
    arterial_hypertension_list = IndividualHypertensionExams()
    response = arterial_hypertension_list.check_presence(data_frame[[
        'co_seq_fat_atd_ind', 'codigo', 'tipo', 'co_fat_cidadao_pec', 'no_cidadao', 'idade']])
    print(response)
