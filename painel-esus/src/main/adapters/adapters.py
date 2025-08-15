from abc import ABC, abstractmethod
from typing import TypedDict


class TypeTotal(TypedDict):
    data: int = 0

class AbstractAdapter(ABC):

    def _total_hydrate(self):
        return {
            'data': 0
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
            "feminino": 0,
            "masculino": 0,
            "indeterminado": 0,
        }
    def _location_type_hydrate(self):
        return {
            "urbano": self._tag_value_hydrate('urbano'),
            "rural": self._tag_value_hydrate('rural'),
            "nao_informado": self._tag_value_hydrate('nao_informado'),
        },
    @abstractmethod
    def total_adapter(self, response) -> TypeTotal:
        pass

class DemographicAdapter(AbstractAdapter):

    def total_adapter(self, response) -> TypeTotal:
        result = self._total_hydrate()
        if type(response) == list and len(response) > 0:
            response = response[0]

        if response is not None :
            result["data"] = response

        return result

    def location_type_adapter(self, response): pass

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
                result[key] += int(response[k])
        return result
