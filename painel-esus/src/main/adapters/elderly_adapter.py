# pylint: disable=C0103

class ElderlyAdapter:

    def _fill_disease_value(self, tag, value, is_float=False):
        return {
            "tag": str(tag),
            "value": {
                "total": float(value) if is_float else int(value)
            }
        }

    def _fill_single_values(self, tag, value, is_float=False):
        return {"tag": str(tag), "value": float(value) if is_float else int(value)}

    def _fill_location_values(self, tag, ):
        return {
                "tag": tag,
                "value": {
                    "urbana": 0,
                    "rural": 0,
                    "nao-informado": 0,
                },
            }

    def _fill_gender_values(
        self,
        tag,
    ):
        return {
            "tag": tag,
            "value": {
                "feminino": 0,
                "masculino": 0,
            },
        }

    def total(self, response):
        result = {
            "total-ubs": {
                "data": 0,
            }
        }
        response=response.pop()
        result["total-ubs"]["data"] = int(response[0])
        if len(response) > 1 and response[1] is not None:
            result["total-atendidas"] = { "data": int(response[1])}
        if len(response) > 2 and response[2] is not None:
            result["total-atendidas"] = { "data": int(response[2])}

        return result

    def age_location(self, response):
        result = {}

        for r in response:
            category = r[0].lower().replace("zona ","").replace("n/i", "nao-informado")
            tag = r[1].replace(" ", "-")
            if tag not in result:
                result[tag] = self._fill_location_values(tag)
            result[tag]["value"][category] = int(r[2])

        return list(result.values())

    def group_by_race(self, response):
        result = []
        for r in response:
            result.append(
                self._fill_single_values(r[0].lower(), r[2],True)
            ) 
        return result

    def group_by_gender(self, response):
        result = {}
        for r in response:
            category = r[0].lower().strip()
            tag = r[1].replace(" ", "-").strip()
            if tag not in result:
                result[tag] = self._fill_gender_values(tag)

            result[tag]["value"][category] = int(r[2])

        return list(result.values())

    def influenza_rate(self, response):
        result = []
        response = response.pop()

        r0, r1 = int(response[0]) , int(response[1])
        total = r0+r1
        atendidas = float(r0 / total) if total > 0 else 0 
        n_atentiddas = float(r1 / total) if total > 0 else 0 
        result.append(
            self._fill_single_values("vacinadas", atendidas, True)
        )
        result.append(
            self._fill_single_values("nao-vacinadas", n_atentiddas, True)
        )

        return result

    def odonto_rate(self, response):
        result = []
        response = response.pop()
        r0, r1 = int(response[0]) , int(response[1])
        total = r0+r1
        atendidas = float(r0 / total) if total > 0 else 0 
        n_atentiddas = float(r1 / total) if total > 0 else 0 
        result.append(
            self._fill_single_values("atendidas", atendidas, True)
        )
        result.append(
            self._fill_single_values("nao-atendidas", n_atentiddas, True)
        )

        return result

    def total_hipertension_diabetes(self, response):
        result = []
        response = response.pop()
        result.append(self._fill_disease_value("hipertensao", response[0]))
        result.append(self._fill_disease_value("diabetes", response[1]))
        result.append(
            self._fill_disease_value("hipertensao-diabetes-associadas", response[2])
        )
        return result
