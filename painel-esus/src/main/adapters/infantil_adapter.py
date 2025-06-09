class InfantilAdapter:

    def total_count_infantil(self, response):
        total = response[0][0] if response else 0
        return {"data": total}

    def by_age_infantil(self, response):
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

    def by_race_infantil(self, response):
        data = []
        for row in response:
            tag, value = row
            data.append(
                {
                    "tag": tag,
                    "value": value,
                }
            )
        return {"data": data}

    def first_consult_8d(self, response):
        data = []
        for row in response:
            tag, value = row
            data.append(
                {
                    "tag": tag,
                    "value": value,
                }
            )
        return {"data": data}

    def appointments_until_2_years(self, response):
        data = []
        for row in response:
            tag, value = row
            data.append(
                {
                    "tag": tag,
                    "value": value,
                }
            )
        return {"data": data}
