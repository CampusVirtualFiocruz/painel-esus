import pandas as pd

from .hypertension_exams import HypertensionExams


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
