# pylint: disable=E0401
from typing import Dict

from pandas import DataFrame
from pandas import Series
from src.infra.db.repositories.enuns.individual_cares import IndividualCare

from .age_groups_location import AgeGroupsLocationDF


class AgeGroupGenderDF(AgeGroupsLocationDF):
    faixas_dict = {
        '1': "0 a 19 anos",
        '2': "20 a 29 anos",
        '3': "30 a 39 anos",
        '4': "40 a 49 anos",
        '5': "50 a 59 anos",
        '6': "60 + anos",
    }

    def _create_age_groups_items(self) -> Dict:
        return {
            '0 a 19 anos': {
                'Feminino': 0,
                'Masculino': 0
            },
            '20 a 29 anos': {
                'Feminino': 0,
                'Masculino': 0
            },
            '30 a 39 anos': {
                'Feminino': 0,
                'Masculino': 0
            },
            '40 a 49 anos': {
                'Feminino': 0,
                'Masculino': 0
            },
            '50 a 59 anos': {
                'Feminino': 0,
                'Masculino': 0
            },
            '60 + anos': {
                'Feminino': 0,
                'Masculino': 0
            },
        }

    def _parse_age_group(self, data_frame: DataFrame) -> tuple([DataFrame, DataFrame]):
        data_frame['faixas'] = ''
        mask_faixa1 = (data_frame['idade'] >= 0) & (data_frame['idade'] <= 19)
        data_frame.loc[mask_faixa1, 'faixas'] = '1'

        mask_faixa2 = (data_frame['idade'] >= 20) & (data_frame['idade'] <= 29)
        data_frame.loc[mask_faixa2, 'faixas'] = '2'

        mask_faixa3 = (data_frame['idade'] >= 30) & (data_frame['idade'] <= 39)
        data_frame.loc[mask_faixa3, 'faixas'] = '3'

        mask_faixa4 = (data_frame['idade'] >= 40) & (data_frame['idade'] <= 49)
        data_frame.loc[mask_faixa4, 'faixas'] = '4'

        mask_faixa5 = (data_frame['idade'] >= 40) & (data_frame['idade'] <= 49)
        data_frame.loc[mask_faixa5, 'faixas'] = '5'

        mask_faixa6 = data_frame['idade'] >= 60
        data_frame.loc[mask_faixa6, 'faixas'] = '6'

        faixas = data_frame.groupby(
            by=['co_dim_sexo', 'faixas']
        ).size().reset_index(name='qtd')

        masculino_value = IndividualCare.get_('Masculino')
        feminino_value = IndividualCare.get_('Feminino')

        faixas.loc[
            faixas['co_dim_sexo'] == masculino_value,
            'co_dim_sexo'] = 'Masculino'
        faixas.loc[
            faixas['co_dim_sexo'] == feminino_value,
            'co_dim_sexo'] = 'Feminino'
        return data_frame, faixas

    def _hidrate_age_groups(self, row: Series, age_group: Dict) -> None:
        if row['faixas']:
            key = self.faixas_dict[str(row['faixas'])]
            location = row['co_dim_sexo']
            value = int(row['qtd'])
            age_group[key][location] = value

    def age_group_gender(self, data_frame: DataFrame):
        data_frame = self.parse_date(data_frame)
        data_frame, faixas = self._parse_age_group(data_frame)
        result = self._create_age_groups_items()
        faixas.apply(lambda x: self._hidrate_age_groups(x, result), axis=1)
        return result
