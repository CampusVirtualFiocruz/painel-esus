from typing import List


class ProfessionalsGroup():
    professionals_map = {
        "225":  'MÉDICOS',
        "2232": 'CIRURGIÕES-DENTISTAS',
        "2234": 'FARMACÊUTICOS',
        "2236": 'FISIOTERAPEUTAS',
        "2237": 'NUTRICIONISTAS',
        "2238": 'FONOAUDIÓLOGOS',
        "2239": 'TERAPEUTAS OCUPACIONAIS',
        "2241": 'EDUCAÇÃO FÍSICA',
        "2263": 'INTEGRATIVA E COMPLEMENTAR',
        "2515": 'PSCICÓLOGOS',
        "2516": 'ASSITENTE SOCIAL',
        "2235": 'ENFERMEIROS'
    }

    def __init__(self):
        self.professionals_dict = {}
        self._create_items()

    def _create_items(self):
        self.professionals_dict = {
            'MÉDICOS': {
                'profissao': 'MÉDICOS',
                'totalCount': 0,
                'total': 0
            },
            'CIRURGIÕES-DENTISTAS': {
                'profissao': 'CIRURGIÕES-DENTISTAS',
                'totalCount': 0,
                'total': 0
            },
            'FARMACÊUTICOS': {
                'profissao': 'FARMACÊUTICOS',
                'totalCount': 0,
                'total': 0
            },
            'FISIOTERAPEUTAS': {
                'profissao': 'FISIOTERAPEUTAS',
                'totalCount': 0,
                'total': 0
            },
            'NUTRICIONISTAS': {
                'profissao': 'NUTRICIONISTAS',
                'totalCount': 0,
                'total': 0
            },
            'FONOAUDIÓLOGOS': {
                'profissao': 'FONOAUDIÓLOGOS',
                'totalCount': 0,
                'total': 0
            },
            'TERAPEUTAS OCUPACIONAIS': {
                'profissao': 'TERAPEUTAS OCUPACIONAIS',
                'totalCount': 0,
                'total': 0
            },
            'EDUCAÇÃO FÍSICA': {
                'profissao': 'EDUCAÇÃO FÍSICA',
                'totalCount': 0,
                'total': 0
            },
            'INTEGRATIVA E COMPLEMENTAR': {
                'profissao': 'INTEGRATIVA E COMPLEMENTAR',
                'totalCount': 0,
                'total': 0
            },
            'PSCICÓLOGOS': {
                'profissao': 'PSCICÓLOGOS',
                'totalCount': 0,
                'total': 0
            },
            'ASSITENTE SOCIAL': {
                'profissao': 'ASSITENTE SOCIAL',
                'totalCount': 0,
                'total': 0
            },
            'ENFERMEIROS': {
                'profissao': 'ENFERMEIROS',
                'totalCount': 0,
                'total': 0
            },
            'OUTROS': {
                'profissao': 'OUTROS',
                'totalCount': 0,
                'total': 0
            },
        }

    def get_professionals_count(self, data_frame) -> List:
        def _parse_professionals(cbo):
            if cbo:
                cbo = str(cbo).strip()
                for cbo_initial in list(self.professionals_map.keys()):
                    if cbo.startswith(cbo_initial):
                        return self.professionals_map[cbo_initial]
            return 'OUTROS'

        data_frame['profissional'] = data_frame['cbo'].apply(
            _parse_professionals)
        data_frame = data_frame[['co_seq_fat_atd_ind', 'profissional']]
        data_frame = data_frame.drop_duplicates()
        result = data_frame.groupby(
            by=['profissional']).size().reset_index(name='qtd')
        total = int(result['qtd'].sum())
        for i in result.iterrows():
            item = {
                'profissao': i[1][0],
                'totalCount': i[1][1],
                'total': round(float(i[1][1]/total)*100, 2)
            }
            self.professionals_dict[i[1][0]] = item
        return list(self.professionals_dict.values())
