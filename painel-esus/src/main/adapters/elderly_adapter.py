"""Adapter para o módulo Idosos.

Formata respostas de repositórios em estruturas consumíveis pelo frontend:
estruturas prontas para o frontend e também adapta listas nominais.
"""

# pylint: disable=C0103
from src.main.adapters.nominal_list_adapter import IdosoNominalListAdapter
from pprint import pprint

class ElderlyAdapter:
    """Formata resultados do domínio Idosos para consumo na UI."""

    def total_ubs(self, response):
        """Retorna total numérico de UBS aplicável ao módulo Idosos."""
        total= 0
        if response is not None and len(response) > 0:
            total = response[0][0]

        return {
                'data': total,
            }

    def total_card(self, response):
        """Mapeia distribuição por localidade (urbana/rural/NI)."""
        result = {"data": [
            { "tag": "urbana", "value": 0},
            { "tag": "rural", "value": 0},
            # { "tag": "periurbana", "value": 0},
            { "tag": "nao_informado", "value": 0},
        ]}
        idx = {
            'urbana': 0,
            'rural': 1,
        #    'periurbana': 2
            }

        for resp in response:
            if resp[0] is not None and resp[1] is not None:
                if str(resp[0]).lower() in idx:
                    key = idx[str(resp[0]).lower()]
                    result['data'][key]['value'] = resp[1]
                else:
                    key = len(result['data'])-1
                    result['data'][key]['value'] = resp[1]

        return result


    def total_medical_cares(self, response):
        """Total de atendimentos médicos com idosos."""
        total= 0
        if response is not None and len(response) > 0:
            total = response[0][0]

        return {
                'data': total,
            }

    def by_gender(self, response):
        """Distribuição por sexo para faixas etárias padronizadas."""
        result = { "data": [] }
        map_ = {}
        for resp in response:
            if resp[0] is not None and resp[1] is not None and resp[2] is not None:
                if resp[0] not in map_:
                    map_[resp[0]] = {
                        'feminino': 0,
                        'masculino': 0,
                        'indeterminado': 0
                    }

                map_[resp[0]][str(resp[1]).lower()] = resp[2]

        for key in map_.keys():
            _key = key.replace("a","-")
            _key += '-anos'
            _key = _key.replace("100m-is-anos", "100-ou-mais")
            value ={
                "tag": _key,
                "value": map_[key]
            }
            result["data"].append(value)


        return result

    def by_race(self, response):
        """Distribuição por raça/cor padronizada para o módulo Idosos."""
        result = { "data": [
            { 'tag':'branca', 'value': 0},
            { 'tag':'preta', 'value': 0},
            { 'tag':'parda', 'value': 0},
            { 'tag':'amarela', 'value': 0},
            { 'tag':'indigena', 'value': 0},
            ]
        }
        map_ = {
            'branca': 0,
            'preta': 1,
            'parda': 2,
            'amarela': 3,
            'indigena': 4,
        }
        for resp in response:
            if resp[0] is not None and resp[1] is not None:
                key = str(resp[0]).lower()
                result["data"][map_[key]]["value"] =  resp[1]

        return result



    def two_medical_appointment(self, response):
        """Distribuição de pessoas com <2 ou >=2 consultas médicas em 12 meses."""
        result = {"data": [
            { "tag": "uma-nenhuma-consulta", "value": 0},
            { "tag": "duas-mais-consultas", "value": 0},
        ]}
        for resp in response:
            if resp[0] is not None and resp[1] is not None:
                if resp[0] == 0:
                    result['data'][0]['value'] = resp[1]
                else:
                    result['data'][1]['value'] = resp[1]

        return result

    def two_height_records(self, response):
        """Distribuição de pessoas com <2 ou >=2 registros de peso/altura."""
        result = {"data": [
            { "tag": "um-nenhum-registro", "value": 0},
            { "tag": "dois-mais-registros", "value": 0},
        ]}
        for resp in response:
            if resp[0] is not None and resp[1] is not None:
                if resp[0] == 0:
                    result['data'][0]['value'] = resp[1]
                else:
                    result['data'][1]['value'] = resp[1]

        return result

    def two_acs_visits(self, response):
        """Distribuição de pessoas com <2 ou >=2 visitas ACS."""
        result = {"data": [
            { "tag": "uma-nenhuma-visita", "value": 0},
            { "tag": "duas-mais-visitas", "value": 0},
        ]}
        for resp in response:
            if resp[0] is not None and resp[1] is not None:
                if resp[0] == 0:
                    result['data'][0]['value'] = resp[1]
                else:
                    result['data'][1]['value'] = resp[1]

        return result

    def creatinine(self, response):
        """Proporção com/sem avaliação de creatinina."""
        result = {"data": [
            { "tag": "sem-avaliacao", "value": 0},
            { "tag": "avaliadas", "value": 0},
        ]}
        for resp in response:
            if resp[0] is not None and resp[1] is not None:
                if resp[0] == 0:
                    result['data'][0]['value'] = resp[1]
                else:
                    result['data'][1]['value'] = resp[1]

        return result


    def influenza_vaccines(self, response):
        """Proporção de vacinação contra influenza."""
        result = {"data": [
            { "tag": "nao-vacinadas", "value": 0},
            { "tag": "vacinadas", "value": 0},
        ]}
        for resp in response:
            if resp[0] is not None and resp[1] is not None:
                if resp[0] == 0:
                    result['data'][0]['value'] = resp[1]
                else:
                    result['data'][1]['value'] = resp[1]

        return result


    def dentist_appointment(self, response):
        """Proporção com/sem consulta odontológica na APS."""
        result = {"data": [
            { "tag": "sem-consulta", "value": 0},
            { "tag": "consultadas", "value": 0},
        ]}
        for resp in response:
            if resp[0] is not None and resp[1] is not None:
                if resp[0] == 0:
                    result['data'][0]['value'] = resp[1]
                else:
                    result['data'][1]['value'] = resp[1]

        return result


    def ivcf_20(self, response):
        """Proporção com/sem avaliação IVCF-20."""
        result = {"data": [
            { "tag": "sem-avaliacao", "value": 0},
            { "tag": "avaliadas", "value": 0},
        ]}
        for resp in response:
            if resp[0] is not None and resp[1] is not None:
                if resp[0] == 0:
                    result['data'][0]['value'] = resp[1]
                else:
                    result['data'][1]['value'] = resp[1]

        return result

    def nominal_list(self, response):
        """Adapter para lista nominal de idoso."""
        return IdosoNominalListAdapter(response)
