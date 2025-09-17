"""Adapters para hipertensão e diabetes.

Formata respostas de repositórios em estruturas consumíveis pelo frontend:
totais, IMC, complicações, por sexo/raça.
"""

from collections import defaultdict

from src.main.adapters.base.base_dashboard_adapter import BaseDashboardAdapter


class HypertensionAdapter(BaseDashboardAdapter):
    """Adapter de Hipertensão."""
    def __init__(self):
        super().__init__()
        self.columns = [
            "glicemia",
            "creatinina",
            "eas_equ",
            "sodio",
            "potassio",
            "colesterol",
            "hemograma",
            "eletro",
        ]
    def __init(self, tag):
        """Cria estrutura padrão de bloco com rótulo e valores binários."""
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
                                "value": 1,
                            },
                        ],
                    },
                })

    def get_total(self, response):
        """Repasse direto do agregado de totais já estruturado no repositório."""
        return response

    def get_by_gender(self, response):
        """Agrupamento por sexo e faixa etária."""
        return self.group_gender_age(response)

    def get_by_race(self, response):
        """Agrupamento por raça/cor."""
        return self.group_race(response)

    def get_exams_count(self, response):
        """Contagem do status de exames solicitados/pendentes/registrados por tipo."""
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

        columns = self.columns
        print(columns)
        result = {}
        result_map = {
            "1": "sem-solicitacao",
            "2": "aguardando-resultado",
            "3": "resultado-registrado",
        }
        for i in columns:
            result = { **result, **__init(i)}
        for idx, res in enumerate(response):
            for idx2, i in enumerate(res):
                key = columns[idx2]
                if idx2 < len(res):
                    result_key = result_map[str(i)]
                    result[key]['value'][result_key]+=1
        return list(result.values())

    def get_imc(self, response):
        """Distribuição de IMC com valores percentuais e binários por classe."""
        imc_mapped = {}
        for i in [
            "baixo-peso",
            "peso-adequado",
            "excesso-peso",
            "obesidade",
            "nao-informado",
        ]:
            imc_mapped = {
                **imc_mapped,
                **self.__init(i)
            }
        for res in response:
            key = res[0].replace("_", "-")
            if key not in imc_mapped:
                key = "nao-informado"

            imc_mapped[key]['value'] = float(res[1])
            imc_mapped[key]["data"][0]["value"] = float(res[1])
            imc_mapped[key]["data"][1]["value"] = 1 - float(res[1])

        return list(imc_mapped.values())

    def get_complications(self, response):
        """Percentual de complicações associadas dividido em blocos binários."""
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

        for idx, res in enumerate(response[0]):
            if idx < len(response[0])-1:
                percent = 0
                key = columns[idx]
                percent = round(float(res) / float(response[0][-1]), 3)
                imc_mapped[key]["value"] = percent
                imc_mapped[key]["data"][0]["value"] = percent
                imc_mapped[key]["data"][1]["value"] = 1 - percent

        return list(imc_mapped.values())

class DiabetesAdapter(HypertensionAdapter):
    def __init__(self):
        super().__init__()
        self.columns = [
            "glicemia",
            "hemob_glica",
            "retino",
            "creatinina",
            "eas_equ",
            "hemograma",
            "colesterol",
        ]
