# pylint: disable=E0401
import pandas as pd

from .coronary_disease import CoronaryDisease


def test_coronary_filter():
    data_frame = pd.DataFrame(columns=['co_seq_fat_atd_ind', 'tipo', 'codigo'], data=[
        [1, '1', 'A123'], [2, '1', 'B123'], [3, '1', 'C123'], [4, '1', 'A123'], [5, '1', 'A123']])
    disease = CoronaryDisease()
    disease.cids = ['A123']
    response = disease.filter_registers(data_frame)
    response = response.drop_duplicates()
    print(disease.statistics(response))
    assert response.shape[0] == 3
    assert disease.total == 5
