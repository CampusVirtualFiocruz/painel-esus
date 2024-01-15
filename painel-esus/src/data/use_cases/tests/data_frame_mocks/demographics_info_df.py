import pandas as pd
import pytest

@pytest.fixture
def demographics_info_df():
    columns = [
               'co_dim_sexo', 'co_dim_tipo_localizacao', 
               'co_dim_tempo_nascimento', 'co_fat_cidadao_pec'
            ]
    values = [
        [1, 2, '19880528', 1],
        [1, 2, '19570528', 2],
        [1, 2, '19670528', 3],
        [1, 3, '20070528', 4],
        [1, 3, '20220528', 5],
        [2, 2, '19880528', 6],
        [2, 2, '19570528', 7],
        [2, 2, '19770528', 8],
        [2, 3, '20120528', 9],
        [2, 3, '20200528', 10],
    ]
    return pd.DataFrame(columns=columns, data=values)

@pytest.fixture
def demographics_info_df_empty():
    columns = [
               'co_dim_sexo', 'co_dim_tipo_localizacao', 
               'co_dim_tempo_nascimento', 'co_fat_cidadao_pec'
            ]
    values = []
    return pd.DataFrame(columns=columns, data=values)
