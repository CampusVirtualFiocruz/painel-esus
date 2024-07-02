# pylint: disable=E0401
from datetime import date
from typing import Dict

from pandas import DataFrame
from pandas import Series
from src.infra.db.repositories.enuns import Location


class AgeGroupsLocationDF:
    faixas_dict = {
        '1': '0 a 5 anos',
        '2': '6 a 12 anos',
        '3': '13 a 17 anos',
        '4': '18 a 29 anos',
        '5': '30 a 44 anos',
        '6': '45 a 59 anos',
        '7': '60 + anos'
    }

    def _create_age_groups_items(self) -> Dict:
        return {
            '0 a 5 anos': {
                'Rural': 0,
                'Urbano': 0
            },
            '6 a 12 anos': {
                'Rural': 0,
                'Urbano': 0
            },
            '13 a 17 anos': {
                'Rural': 0,
                'Urbano': 0
            },
            '18 a 29 anos': {
                'Rural': 0,
                'Urbano': 0
            },
            '30 a 44 anos': {
                'Rural': 0,
                'Urbano': 0
            },
            '45 a 59 anos': {
                'Rural': 0,
                'Urbano': 0
            },
            '60 + anos': {
                'Rural': 0,
                'Urbano': 0
            },
        }

    def _calculate_age(self, birth_date) -> int:
        today = date.today()
        age = (
            today.year - birth_date.year -
            ((today.month, today.day) < (birth_date.month, birth_date.day))
        )
        return age

    def parse_date(self, data_frame: DataFrame) -> DataFrame:
        def _calculate_age_fn(_date):
            date_str = str(_date)
            if len(date_str) == 8:
                return self._calculate_age(
                    date(int(str(_date)[:4]),
                         int(str(_date)[4:6]),
                         int(str(_date)[6:8])
                         )
                )
            return 0

        data_frame['idade'] = data_frame['co_dim_tempo_nascimento'].apply(
            _calculate_age_fn)
        return data_frame

    def _hidrate_age_groups(self, row: Series, age_group: Dict) -> None:
        if row['faixas']:
            key = self.faixas_dict[str(row['faixas'])]
            location = row['co_dim_tipo_localizacao']
            value = int(row['qtd'])
            age_group[key][location] = value

    def _parse_age_group(self,
                         data_frame: DataFrame) -> tuple([
                             DataFrame,
                             DataFrame
                         ]):
        data_frame['faixas'] = ''
        mask_faixa1 = (data_frame['idade'] >= 0) & (data_frame['idade'] <= 5)
        data_frame.loc[mask_faixa1, 'faixas'] = '1'

        mask_faixa2 = (data_frame['idade'] >= 6) & (data_frame['idade'] <= 12)
        data_frame.loc[mask_faixa2, 'faixas'] = '2'

        mask_faixa3 = (data_frame['idade'] >= 13) & (data_frame['idade'] <= 17)
        data_frame.loc[mask_faixa3, 'faixas'] = '3'

        mask_faixa4 = (data_frame['idade'] >= 18) & (data_frame['idade'] <= 29)
        data_frame.loc[mask_faixa4, 'faixas'] = '4'

        mask_faixa5 = (data_frame['idade'] >= 30) & (data_frame['idade'] <= 44)
        data_frame.loc[mask_faixa5, 'faixas'] = '5'

        mask_faixa6 = (data_frame['idade'] >= 45) & (data_frame['idade'] <= 59)
        data_frame.loc[mask_faixa6, 'faixas'] = '6'

        mask_faixa7 = data_frame['idade'] >= 60
        data_frame.loc[mask_faixa7, 'faixas'] = '7'

        faixas = data_frame.groupby(
            by=['co_dim_tipo_localizacao', 'faixas']
        ).size().reset_index(name='qtd')

        urbano_value = Location.get_('urbano')
        rural_value = Location.get_('rural')
        nao_informado = Location.get_('nao_informado')
        faixas.loc[
            faixas['co_dim_tipo_localizacao'] == urbano_value,
            'co_dim_tipo_localizacao'] = 'Urbano'
        faixas.loc[
            faixas['co_dim_tipo_localizacao'] == rural_value,
            'co_dim_tipo_localizacao'] = 'Rural'
        faixas.loc[
            faixas['co_dim_tipo_localizacao'] == nao_informado,
            'co_dim_tipo_localizacao'] = 'Não Informado'
        return data_frame, faixas

    def age_group_location(self, data_frame: DataFrame):
        data_frame = self.parse_date(data_frame)
        data_frame = data_frame[data_frame['idade'].notna()]
        data_frame['idade'] = data_frame['idade'].astype(
            str).astype(float).astype(int)
        print('----->', data_frame['co_dim_tipo_localizacao'].unique())

        data_frame, faixas = self._parse_age_group(data_frame)

        result = self._create_age_groups_items()
        faixas.apply(lambda x: self._hidrate_age_groups(x, result), axis=1)
        return result
