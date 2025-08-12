from collections import defaultdict

from src.main.adapters.base.base_dashboard_adapter import BaseDashboardAdapter


class HypertensionAdapter(BaseDashboardAdapter):
    def __init(self, tag):
            return ({
                    tag: {
                        "tag": tag,
                        "value": 0,
                        "data": [
                            {
                                "tag": "possui",
                                "value": 0,
                            },
                            {
                                "tag": "nao-possui",
                                "value": 0,
                            },
                        ],
                    },
                })

    
    def get_total(self, response):

        return response

    def get_by_gender(self, response):
        return self.group_gender_age(response)

    def get_by_race(self, response):

        return self.group_race(response)

    def get_exams_count(self, response):
        def __init(tag):
            return ({
                tag: {
                    'tag': tag.replace("_","-"),
                    'value': {
                        "sem-solicitacao": 0,
                        "aguardando-resultado": 0,
                        "resultado-registrado": 0,
                    }
                }
            }
            )

        columns = [
            "glicemia",
            "creatinina",
            "eas_equ",
            "sodio",
            "potassio",
            "colesterol",
            "hemograma",
            "eletro",
        ]
        result = {}
        result_map = {
            "1": "sem-solicitacao",
            "2": "aguardando-resultado",
            "3": "resultado-registrado",
        }
        for i in columns:
            result = { **result, **__init(i)}

        for idx, res in enumerate(response):
            if idx < len(res):
                key = columns[idx]
                for _, i in enumerate(res):
                    result_key = result_map[str(i)]
                    result[key]['value'][result_key]+=1

        return list(result.values())

    def get_imc(self, response):
        imc_mapped = {}
        for i in [
            "baixo-peso",
            "peso-adequado",
            "excesso-peso",
            "obesidade",
            "nao-informado",
            "na-outros",
        ]:
            imc_mapped = {
                **imc_mapped,
                **self.__init(i)
            }
        for res in response:
            key = res[0].replace("_", "-")
            imc_mapped[key]['value'] = float(res[1])
            imc_mapped[key]["data"][0]["value"] = float(res[1])
            imc_mapped[key]["data"][1]["value"] = 1 - float(res[1])

        return list(imc_mapped.values())

    def get_complications(self, response):
        imc_mapped = {}
        columns = [
            "infarto-agudo",
            "acidente-vascular",
            "renal",
            "coronariana",
            "cerebrovascular",
        ]
        for i in columns:
            imc_mapped = {**imc_mapped, **self.__init(i)}

        for idx, res in enumerate(response):
            key = columns[idx]
            percent = round(float(res[1]) / float(res[-1]), 3)
            imc_mapped[key]["value"] = percent
            imc_mapped[key]["data"][0]["value"] = percent
            imc_mapped[key]["data"][1]["value"] = 1 - percent

        return list(imc_mapped.values())
