"""Adapter para o módulo Crianças.

Formata respostas de repositórios em estruturas consumíveis pelo frontend:
totais, distribuiçoes por raça/idade/indicadores e lista nominal.
"""
from src.main.adapters.nominal_list_adapter import CriancaNominalListAdapter


class ChildrenAdapter:
    """Converte respostas do domínio Crianças em objetos prontos para UI."""

    def _init_object(self,tag):
        return {
            "tag": tag,
            "value": 0,
        }
    def _sim_nao_labels(self):
        return {
            "sim": self._init_object("sim"),
            "nao": self._init_object("nao"),
            "nao-se-aplica": self._init_object("nao-se-aplica-infantil"),
        }

    def _milestone_label(self):
        return {
            "sim": self._init_object("avaliados"),
            "nao": self._init_object("nao-avaliados"),

        }

    def _race_labels(self):
        return {
        "branca": self._init_object("branca"),
        "preta": self._init_object("preta"),
        "parda": self._init_object("parda"),
        "amarela": self._init_object("amarela"),
        "indigena": self._init_object("indigena"),
        "nao-informado": self._init_object("nao-informado"),
    }

    def total_count_children(self, response):
        """Extrai total de crianças de uma consulta agregada."""
        total = response[0][0] if response else 0
        return {"data": total}

    def total_and_12_months_adapter(self, response):
        """Retorna total acumulado e total dos últimos 12 meses."""
        total = response[0][0] if response else 0
        total_12_meses = response[0][1] if response else 0
        return {
            "total-cadastros": {"data": total},
            "total-atendidas-12-meses": {"data": total_12_meses},
        }

    def total_ubs(self, response):
        """Total de UBS relacionadas ao módulo Crianças."""
        total = 0
        if response is not None and len(response) > 0:
            total = response[0][0]

        return {
            "data": total,
        }

    def _to_tag_value_list(self, response):
        return {"data": [{"tag": tag, "value": value} for tag, value in response]}

    def total_medical_cares(self, response):
        """Total de atendimentos médicos."""
        total = 0
        if response is not None and len(response) > 0:
            total = response[0][0]

        return {
            "data": total,
        }

    def _to_tag_value_from_dict(self, response, dict_label):
        data = dict(dict_label)
        for tag, value in response:
            data[tag]["value"] = value
        return {"data": list(data.values())}

    def by_race_children(self, response):
        return self._to_tag_value_from_dict(response, self._race_labels())

    def first_consult_8d(self, response):
        return self._to_tag_value_from_dict(response, self._sim_nao_labels())

    def appointments_until_2_years(self, response):
        return self._to_tag_value_from_dict(response, self._sim_nao_labels())

    def by_age_children(self, response):
        """Distribuição por faixas etárias e sexo."""
        data = {}
        def _init(i):
            return {
                "tag": i,
                "value": {
                    "feminino": 0,
                    "masculino": 0,
                    "indeterminado": 0,
                    "nao-informado": 0,
                },
            }
        categories = ['0 a 8 dias',
        '9 a 30 dias',
        '1 a 2 meses',
        '2 a 4 meses',
        '4 a 6 meses',
        '6 a 9 meses',
        '9 a 12 meses',
        '12 a 18 meses',
        '18 a 24 meses',
        '24 a 36 meses']
        for i in categories:
            data[i] = _init(i)

        for row in response:
            tag, feminino, masculino, indeterminado, nao_informado = row
            data[tag]= (
                {
                    "tag": tag,
                    "value": {
                        "feminino": feminino,
                        "masculino": masculino,
                        "indeterminado": indeterminado,
                        "nao-informado": nao_informado,
                    },
                }
            )
        data2 = list(data.values())
        # data2.sort(key=lambda d: int(d["tag"].split(" ")[0]))

        return {"data": data2}

    def acs_visit_until_30d(self, response):
        return self._to_tag_value_from_dict(response, self._sim_nao_labels())

    def acs_visit_until_6m(self, response):
        return self._to_tag_value_from_dict(response, self._sim_nao_labels())

    def dental_appointments_until_12m(self, response):
        return self._to_tag_value_from_dict(response, self._sim_nao_labels())

    def dental_appointments_until_24m(self, response):
        return self._to_tag_value_from_dict(response, self._sim_nao_labels())

    def high_weight_records(self, response):
        return self._to_tag_value_from_dict(response, self._sim_nao_labels())

    def milestone(self, response):
        return self._to_tag_value_from_dict(response, self._milestone_label())

    def evaluated_feeding(self, response):
        return self._to_tag_value_from_dict(response, self._milestone_label())

    def nominal_list(self, response):
        return CriancaNominalListAdapter(response)
