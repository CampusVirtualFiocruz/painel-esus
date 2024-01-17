# pylint: disable=invalid-name
# pylint: disable=E0401
import pandas as pd
from .pregnancy import Pregnants


def test_filter_pregnancy_success():
    df = pd.DataFrame(columns=['codigo'], data=[
                      ['A123'], ['O264'], ['C123'], ['A123']])

    pregnancy = Pregnants()
    response = pregnancy.filter_registers(df)
    assert response.shape[0] == 1


def test_filter_pregnancy_no_result():
    df = pd.DataFrame(columns=['codigo'], data=[['A123'], ['C123'], ['A123']])

    pregnancy = Pregnants()
    response = pregnancy.filter_registers(df)
    assert response.shape[0] == 0
