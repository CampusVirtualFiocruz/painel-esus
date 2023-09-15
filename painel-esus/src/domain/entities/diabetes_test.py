#pylint: disable=invalid-name
import pandas as pd
from .diabetes import Diabetes

def test_filter_diabetes_success():
    df = pd.DataFrame(columns=['codigo'], data=[['A123'], ['T89'], ['C123'], ['A123']])

    diabetes = Diabetes()
    response = diabetes.filter_registers(df)
    assert response.shape[0] == 1

def test_filter_diabetes_no_result():
    df = pd.DataFrame(columns=['codigo'], data=[['A123'], ['C123'], ['A123']])

    diabetes = Diabetes()
    response = diabetes.filter_registers(df)
    assert response.shape[0] == 0
