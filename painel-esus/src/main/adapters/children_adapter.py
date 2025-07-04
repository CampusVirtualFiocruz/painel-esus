from src.main.adapters.nominal_list_adapter import CriancaNominalListAdapter


class ChildrenAdapter:

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
            "nao-se-aplica": self._init_object("nao-se-aplica-infantil"),
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
        total = response[0][0] if response else 0
        return {"data": total}

    def total_and_12_months_adapter(self, response):
        total = response[0][0] if response else 0
        total_12_meses = response[0][1] if response else 0
        return {
            "total-cadastros": {"data": total},
            "total-atendidas-12-meses": {"data": total_12_meses},
        }

    def total_ubs(self, response):
        total = 0
        if response is not None and len(response) > 0:
            total = response[0][0]

        return {
            "data": total,
        }

    def _to_tag_value_list(self, response):
        return {"data": [{"tag": tag, "value": value} for tag, value in response]}

    def total_medical_cares(self, response):
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
        data = []
        for row in response:
            tag, feminino, masculino, indeterminado, nao_informado = row
            data.append(
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

        data.sort(key=lambda d: int(d["tag"].split(" ")[0]))

        return {"data": data}

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
