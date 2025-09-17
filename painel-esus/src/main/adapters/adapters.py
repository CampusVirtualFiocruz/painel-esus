"""Adapters base para formatar respostas para o frontend.

Os adapters aqui definidos transformam resultados brutos em estruturas
padronizadas, reduzindo acoplamento entre as camadas de dados e apresentação.
"""
from abc import ABC, abstractmethod
from typing import TypedDict

from src.utils.ibge import get_ibge_total


class TypeTotal(TypedDict):
    data: int = 0

class AbstractAdapter(ABC):
    """Base para adapters com utilitários de hidratação/formatação."""

    def _total_hydrate(self):
        return {
            "total": self._tag_value_hydrate("total"),
            "ibgePopulation": self._tag_value_hydrate("ibgePopulation"),
        }

    def _tag_value_hydrate(self, tag: str):
        return {
            'tag':tag,
            'value': 0,
        }

    def _pyramid_item_hydrate(self,tag: str):
        return {
          'tag': tag,
          'value': {
            'urbano': 0,
            'rural': 0,
            "nao-informado": 0,
          },
        }

    def _pyramid_hidrate(self):
        labels = [
            "100 ou mais","95 a 99 anos","90 a 94 anos","85 a 89 anos","80 a 84 anos","75 a 79 anos","70 a 74 anos","65 a 69 anos","60 a 64 anos","55 a 59 anos","50 a 54 anos","45 a 49 anos","40 a 44 anos","35 a 39 anos","30 a 34 anos","25 a 29 anos","20 a 24 anos","15 a 19 anos","10 a 14 anos","5 a 9 anos","0 a 4 anos",
        ]
        result = dict()
        for side in ['left','right']:
            for label in labels:
                result[side] = result.get(side, {})
                result[side][label] = result[side].get(label, {})
                result[side][label] = self._pyramid_item_hydrate(label)

        return result

    def _gender_hidrate(self):
        return {
            "feminino": self._tag_value_hydrate('feminino'),
            "masculino": self._tag_value_hydrate('masculino'),
            "indeterminado": self._tag_value_hydrate('indeterminado'),
        }
    def _location_type_hydrate(self):
        return {
            "urbano": self._tag_value_hydrate('urbano'),
            "rural": self._tag_value_hydrate('rural'),
            "nao_informado": self._tag_value_hydrate('nao_informado')
        }
    @abstractmethod
    def total_adapter(self, response) -> TypeTotal:
        pass

class DemographicAdapter(AbstractAdapter):
    """Adapter de Demografia para totais, tipos de localidade, pirâmide etária e sexo."""

    def total_adapter(self, response) -> TypeTotal:
        result = self._total_hydrate()
        if type(response) == list and len(response) > 0:
            response = response[0]

        if response is not None :
            result["total"]['value'] = response

        result["ibgePopulation"]["value"] = get_ibge_total()
        return [ k for k in result.values() ]

    def location_type_adapter(self, response):
        label_map = {
            "rural": "rural",
            "não informado": "nao_informado",
            "urbana": "urbano",
            "urbano": "urbano",
        }
        result = self._location_type_hydrate()
        if type(response) == dict and len(response) > 0:
            for item in response.keys():
                if item not in result:
                    result["nao_informado"]["value"] = response[item]
                else:
                    key = label_map.get(item[0].lower(), "nao_informado")
                    result[item]["value"] = response[item]
        elif type(response) == list and len(response) > 0:
            for item in response:
                if item[0] is None:
                    result["nao_informado"]["value"] = int(item[1])
                else:
                    key = label_map.get(item[0].lower(), "nao_informado")
                    result[key]["value"] = int(item[1])

        return list(result.values())

    def age_group_pyramid(self, response):
        result = self._pyramid_hidrate()
        side_map = {"Masculino":'left', 'Feminino': 'right' }
        location_map = {
            "urbano": "urbano",
            "rural": "rural",
            "nao informado": "nao-informado"
        }
        if type(response) == list and len(response) > 0:
            for resp in response:
                key_side = side_map.get(resp[0], None)
                key_gender = location_map.get(resp[2].lower(), "nao informado")
                if not key_side:
                    continue
                if resp[1] in result[key_side]:
                    result[key_side][resp[1]]["value"][key_gender] = resp[3]

        return { resp: list(result[resp].values()) for resp in result.keys() }

    def gender_apadter(self, response):
        result = self._gender_hidrate()
        if type(response) == dict:
            for k in response.keys():
                key = k
                if k not in result:
                    key = "indeterminado"

                result[key]['value'] = int(response[k])
        return [ k for k in result.values() ]
