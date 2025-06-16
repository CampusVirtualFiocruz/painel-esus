class ChildrenAdapter:
    def total_count_children(self, response):
        total = response[0][0] if response else 0
        return {"data": total}

    def _to_tag_value_list(self, response):
        return {"data": [{"tag": tag, "value": value} for tag, value in response]}

    def by_race_children(self, response):
        return self._to_tag_value_list(response)

    def first_consult_8d(self, response):
        return self._to_tag_value_list(response)

    def appointments_until_2_years(self, response):
        return self._to_tag_value_list(response)

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
        return {"data": data}
    
    def acs_visit_until_30d(self, response):
        return self._to_tag_value_list(response)
    
    def acs_visit_until_6m(self, response):
        return self._to_tag_value_list(response)

    def dental_appointments_until_12m(self, response):
        return self._to_tag_value_list(response)
    
    def dental_appointments_until_24m(self, response):
        return self._to_tag_value_list(response)
    
   