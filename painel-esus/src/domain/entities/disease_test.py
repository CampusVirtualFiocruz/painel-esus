# pylint: disable=invalid-name
# pylint: disable=E0401
import pandas as pd

from src.domain.entities.disease import Disease


def test_disease_filter_success():

    df = pd.DataFrame(columns=['codigo'], data=[
                      ['A123'], ['B123'], ['C123'], ['A123']])
    disease = Disease()
    disease.target = ['A123']
    response = disease.filter_registers(df)
    assert response.shape[0] == 1

    disease.target = ['B123']
    response = disease.filter_registers(df)
    assert response.shape[0] == 1


def test_disease_filter_not_found():

    df = pd.DataFrame(columns=['codigo'], data=[
                      ['A123'], ['B123'], ['C123'], ['A123']])
    disease = Disease()
    disease.target = ['D123']
    response = disease.filter_registers(df)
    assert response.shape[0] == 0
