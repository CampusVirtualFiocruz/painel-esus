# pylint: disable=invalid-name
# pylint: disable=E0401
import pandas as pd

from .diabetes import Diabetes


def test_filter_diabetes_success():
    df = pd.DataFrame(columns=['co_seq_fat_atd_ind', 'tipo', 'codigo'], data=[
        [1, '1', 'A123'], [2, '1', 'T89'], [3, '1', 'C123'], [4, '1', 'A123']
    ])

    diabetes = Diabetes()
    response = diabetes.filter_registers(df)
    assert response.shape[0] == 1


def test_filter_diabetes_success_with_duplicate_entries():
    df = pd.DataFrame(columns=['co_seq_fat_atd_ind', 'tipo', 'codigo'], data=[
        [1, '1', 'A123'],
        [2, '1', 'T89'],
        [2, '1', 'T89'],
        [3, '1', 'C123'],
        [4, '1', 'A123'],
    ])

    diabetes = Diabetes()
    response = diabetes.filter_registers(df)
    assert response.shape[0] == 1


def test_filter_diabetes_no_result():
    df = pd.DataFrame(columns=['co_seq_fat_atd_ind', 'tipo', 'codigo'], data=[
        [1, '1', 'A123'], [2, '1', 'C123'], [3, '1', 'A123']
    ])

    diabetes = Diabetes()
    response = diabetes.filter_registers(df)
    assert response.shape[0] == 0
