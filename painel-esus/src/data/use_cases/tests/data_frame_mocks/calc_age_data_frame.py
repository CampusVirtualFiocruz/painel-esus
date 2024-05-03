#pylint: disable=invalid-name
import pandas as pd
import pytest

@pytest.fixture
def calc_age_df():
    df = pd.DataFrame(
        columns=['co_dim_tempo_nascimento'],
        data=[
            ['20220101'],
            ['19880528']
        ]
    )
    return df
