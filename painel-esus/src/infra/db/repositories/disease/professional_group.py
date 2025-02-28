from typing import List


class ProfessionalsGroup():
    professionals_map = {
        "2516": 'ASSISTENTE SOCIAL',
        "2232": 'CIRURGIÃO-DENTISTA',
        "2235": 'ENFERMEIRO',
        "2234": 'FARMACÊUTICO',
        "2236": 'FISIOTERAPEUTA',
        "2238": 'FONOAUDIÓLOGO',
        "225":  'MÉDICO',
        "2237": 'NUTRICIONISTA',
        "2241": 'PROFISSIONAL DA PROFISSIONAL DA EDUCAÇÃO FÍSICA',
        "2515": 'PSICÓLOGO',
        "2239": 'TERAPEUTA OCUPACIONAL',
        # "2263": 'INTEGRATIVA E COMPLEMENTAR',
    }

    def __init__(self):
        self.professionals_dict = {}
        self._create_items()

    def _create_items(self):
        professionals_dict = {
            'MÉDICO': {
                'profissao': 'MÉDICO',
                'totalCount': 0,
                'total': 0
            },
            'CIRURGIÃO-DENTISTA': {
                'profissao': 'CIRURGIÃO-DENTISTA',
                'totalCount': 0,
                'total': 0
            },
            'FARMACÊUTICO': {
                'profissao': 'FARMACÊUTICO',
                'totalCount': 0,
                'total': 0
            },
            'FISIOTERAPEUTA': {
                'profissao': 'FISIOTERAPEUTA',
                'totalCount': 0,
                'total': 0
            },
            'NUTRICIONISTA': {
                'profissao': 'NUTRICIONISTA',
                'totalCount': 0,
                'total': 0
            },
            'FONOAUDIÓLOGO': {
                'profissao': 'FONOAUDIÓLOGO',
                'totalCount': 0,
                'total': 0
            },
            'TERAPEUTA OCUPACIONAL': {
                'profissao': 'TERAPEUTA OCUPACIONAL',
                'totalCount': 0,
                'total': 0
            },
            'PROFISSIONAL DA EDUCAÇÃO FÍSICA': {
                'profissao': 'PROFISSIONAL DA EDUCAÇÃO FÍSICA',
                'totalCount': 0,
                'total': 0
            },
            'PSICÓLOGO': {
                'profissao': 'PSICÓLOGO',
                'totalCount': 0,
                'total': 0
            },
            'ASSISTENTE SOCIAL': {
                'profissao': 'ASSISTENTE SOCIAL',
                'totalCount': 0,
                'total': 0
            },
            'ENFERMEIRO': {
                'profissao': 'ENFERMEIRO',
                'totalCount': 0,
                'total': 0
            },
            
        }
        professionals_dict['OUTROS'] = {
            'profissao': 'OUTROS',
            'totalCount': 0,
            'total': 0
        }
        self.professionals_dict = professionals_dict

    def get_professionals_count(self, cares) -> List:
        keys = list(self.professionals_dict.keys())
        for i, _ in enumerate(cares):
            if i < len(keys):
                self.professionals_dict[keys[i]]["totalCount"] = cares[i]
                self.professionals_dict[keys[i]]["total"] = round(float(cares[i]/cares[-1])*100, 2)
                
        self.professionals_dict = dict(sorted(self.professionals_dict.items()))
        return list(self.professionals_dict.values())
