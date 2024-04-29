from typing import Dict

import pandas as pd
from datetime import timedelta

from src.infra.db.settings.connection import DBConnectionHandler
from src.domain.entities.disease import Disease
from .sqls.pregnancy_base import PREGNANCY_BASE
from src.infra.db.repositories.sqls import (
    MAX_DT_ATENDIMENTO_ATENDIMENTO_INDIVIDUAL)


class PregnancyBaserepository():

    def __init__(self, disease: Disease):
        self.disease = disease

    def get_pregnancy_list(self, cnes: int = None) -> Dict:
        with DBConnectionHandler() as db_con:
            engine = db_con.get_engine()
            max_date = pd.read_sql_query(
                MAX_DT_ATENDIMENTO_ATENDIMENTO_INDIVIDUAL, con=engine)
            max_date = str(max_date['max'].iloc[0])

            sql = PREGNANCY_BASE
            sql += """
                    where
                        dt_registro between '{}'::DATE - interval '12 month' and '{}' and codigo in ({})
                """.format(
                max_date, max_date,
                ", ".join([f"'{cid}'" for cid in self.disease.target])
            )

            res = pd.read_sql_query(PREGNANCY_BASE, con=engine)
            return res

    def fill_height(self, df):
        columns = df.columns.tolist()

        if False in [i in columns for i in ['nu_altura', 'co_fat_cidadao_pec']]:
            raise Exception('nu_altura e co_fat_cidadao_pec não presentes.')

        height = df.groupby(['co_fat_cidadao_pec'])[
            'nu_altura'].mean().reset_index()

        for h in height.iterrows():
            mask = df['co_fat_cidadao_pec'] == h[1]['co_fat_cidadao_pec']
            df.loc[mask, ['nu_altura']] = h[1]['nu_altura']
        return df

    def _choose_sum(self, row):
        time_dum = row['co_dim_tempo_dum']
        dum_294 = row['dum_294']
        min = row['minima_dum']
        max = row['maxima_dum']

        current_time = time_dum if not pd.isnull(time_dum) else dum_294

        if current_time is not None:
            if current_time > dum_294:
                print("MAX", max)
                return max
            else:
                return min

    def fill_dum(self, data_df):
        time_pregnancy = 294
        columns = data_df.columns.tolist()
        cidadao_pec = 'co_fat_cidadao_pec'
        tempo_dum = 'co_dim_tempo_dum'

        if False in [i in columns for i in [tempo_dum, cidadao_pec]]:
            raise Exception(
                f'{tempo_dum} e {cidadao_pec} não presentes.')

        data_df[tempo_dum] = pd.to_datetime(
            data_df[tempo_dum], format='%Y%m%d', errors='coerce')

        data_df['dum'] = data_df[tempo_dum]

        maxima_dum = data_df.groupby([cidadao_pec])[
            tempo_dum].max().reset_index()
        minima_dum = data_df.groupby([cidadao_pec])[
            tempo_dum].min().reset_index()

        for h in data_df[cidadao_pec].unique().tolist():

            mask = data_df[cidadao_pec] == h
            mask_min_dum = minima_dum[cidadao_pec] == h
            mask_max_dum = maxima_dum[cidadao_pec] == h

            min_dum = minima_dum[mask_min_dum][tempo_dum].iloc[0]
            max_dum = maxima_dum[mask_max_dum][tempo_dum].iloc[0]

            data_df.loc[mask, 'minima_dum'] = min_dum
            data_df.loc[mask, 'maxima_dum'] = max_dum
            data_df.loc[mask, 'dum_294'] = min_dum + timedelta(time_pregnancy)

        data_df['dum'] = data_df.apply(lambda x: self._choose_sum(x), axis=1)
        return data_df
