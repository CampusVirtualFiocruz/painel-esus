# pylint: disable=invalid-name
# pylint: disable=E0401
import pandas as pd
from .hypertension import Hypertension


def test_filter_hypertension_success():
    df = pd.DataFrame(columns=['codigo'], data=[
                      ['A123'], ['I11'], ['C123'], ['A123']])

    hypertension = Hypertension()
    response = hypertension.filter_registers(df)
    assert response.shape[0] == 1


def test_filter_hypertension_no_result():
    df = pd.DataFrame(columns=['codigo'], data=[['A123'], ['C123'], ['A123']])

    hypertension = Hypertension()
    response = hypertension.filter_registers(df)
    assert response.shape[0] == 0
