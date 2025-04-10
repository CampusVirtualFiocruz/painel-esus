# pylint: disable=C0103
from src.main.adapters.nominal_list_adapter import IdosoNominalListAdapter


class ElderlyAdapter:

    def total_ubs(self, response):
        
        return {
                'data': 724,
            }
        
    def total_medical_cares(self, response):
        return {
                'data': 643,
            }
    
    def by_gender(self, response):
        return {
                'data': [
            {
                'tag': "60-64-anos",
                'value': {
                'feminino': 20,
                'masculino': 20,
                'indeterminado': 2,
                },
            },
            {
                'tag': "65-69-anos",
                'value': {
                'feminino': 20,
                'masculino': 20,
                'indeterminado': 4,
                },
            },
            ],
        }
        
    def by_race(self, response):
        return {
            'data': [
            {
                'tag': "branca",
                'value': 43.4,
            },
            {
                'tag': "preta",
                'value': 10.2,
            },
            {
                'tag': "amarela",
                'value': 0.4,
            },
            {
                'tag': "parda",
                'value': 45.3,
            },
            {
                'tag': "indigena",
                'value': 0.6,
            },
            {
                'tag': "nao-informado",
                'value': 0.5,
            },
            ],
        }
        
    def two_medical_appointment(self, response):
        return {
            'data': [
            {
                'tag': "duas-mais-consultas",
                'value': 87,
            },
            {
                'tag': "uma-nenhuma-consulta",
                'value': 13,
            },
            ],
        }
        
    def two_height_records(self, response):
        return {
            'data': [
            {
                'tag': "dois-mais-registros",
                'value': 82,
            },
            {
                'tag': "um-nenhum-registro",
                'value': 18,
            },
            ],
        }
        
    def two_acs_visits(self, response):
        return {
            'data': [
            {
                'tag': "duas-mais-visitas",
                'value': 87,
            },
            {
                'tag': "uma-nenhuma-visita",
                'value': 13,
            },
            ],
        }
        
    def creatinine(self, response):
        return {
            'data': [
            {
                'tag': "avaliadas",
                'value': 87,
            },
            {
                'tag': "sem-avaliacao",
                'value': 13,
            },
            ],
        }
        
    def influenza_vaccines(self, response):
    
        return {
            'data': [
            {
                'tag': "vacinadas",
                'value': 87,
            },
            {
                'tag': "nao-vacinadas",
                'value': 13,
            },
            ],
        }
        
    def dentist_appointment(self, response):
        return {
            'data': [
            {
                'tag': "consultadas",
                'value': 87,
            },
            {
                'tag': "sem-consulta",
                'value': 13,
            },
            ],
        }
    
    def ivcf_20(self, response):
        return {
            'data': [
            {
                'tag': "avaliadas",
                'value': 87,
            },
            {
                'tag': "sem-avaliacao",
                'value': 13,
            },
            ],
        }