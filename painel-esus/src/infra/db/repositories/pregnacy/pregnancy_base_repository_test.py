import pandas as pd
from .pregnancy_base_repository import PregnancyBaserepository
from src.domain.entities.pregnancy import Pregnants
from datetime import datetime


def test_list_pregnacy():
    repo = PregnancyBaserepository(Pregnants())
    result = repo.get_pregnancy_list()
    result.to_csv('/tmp/pregnants.csv')
    print(result)


def test_parse_height():
    data = [
        {
            "nu_altura": 175,
            "co_fat_cidadao_pec": 1
        },
        {
            "nu_altura": None,
            "co_fat_cidadao_pec": 1
        },
        {
            "nu_altura": None,
            "co_fat_cidadao_pec": 1
        },
        {
            "nu_altura": None,
            "co_fat_cidadao_pec": 1
        },
        {
            "nu_altura": None,
            "co_fat_cidadao_pec": 1
        },
        {
            "nu_altura": None,
            "co_fat_cidadao_pec": 1
        },
        {
            "nu_altura": None,
            "co_fat_cidadao_pec": 1
        },
        {
            "nu_altura": 174,
            "co_fat_cidadao_pec": 2
        },
    ]
    data_df = pd.DataFrame(data)
    repo = PregnancyBaserepository(Pregnants())
    result = repo.fill_height(data_df)
    for i in result[result['co_fat_cidadao_pec'] == 1].iterrows():
        altura = int(i[1]['nu_altura'])
        assert altura == 175
    for i in result[result['co_fat_cidadao_pec'] == 2].iterrows():
        altura = int(i[1]['nu_altura'])
        assert altura == 174


def test_parse_dum():
    data = [
        {
            "co_dim_tempo_dum": 20190404,
            "co_fat_cidadao_pec": 1
        },
        {
            "co_dim_tempo_dum": 20200124,
            "co_fat_cidadao_pec": 1
        },
        {
            "co_dim_tempo_dum": 20200323,
            "co_fat_cidadao_pec": 1
        },
        {
            "co_dim_tempo_dum": 30001231,
            "co_fat_cidadao_pec": 1
        },
        {
            "co_dim_tempo_dum": 30001231,
            "co_fat_cidadao_pec": 1
        },
        {
            "co_dim_tempo_dum": 30001231,
            "co_fat_cidadao_pec": 1
        },
        {
            "co_dim_tempo_dum": 30001231,
            "co_fat_cidadao_pec": 1
        },
        {
            "co_dim_tempo_dum": 20190404,
            "co_fat_cidadao_pec": 2
        },
    ]
    data_df = pd.DataFrame(data)

    expeced = {
        '1': [
            pd.Timestamp('2019-04-04'),
            pd.Timestamp('2020-03-23'),
            pd.Timestamp('2020-03-23'),
            pd.Timestamp('2019-04-04'),
            pd.Timestamp('2019-04-04'),
            pd.Timestamp('2019-04-04'),
            pd.Timestamp('2019-04-04'),
            pd.Timestamp('2019-04-04')
        ]
    }
    repo = PregnancyBaserepository(Pregnants())
    result = repo.fill_dum(data_df)
    for idx, i in enumerate(result[result['co_fat_cidadao_pec'] == 1].iterrows()):
        altura = i[1]['dum']
        assert altura == expeced['1'][idx]

    result.to_csv('/tmp/pregnants_parse.csv')
