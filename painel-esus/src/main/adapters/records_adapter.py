from src.main.adapters.nominal_list_adapter import RecordNominalListAdapter


class RecordsAdapter:
    def get_total_group(self, response):
        result = {
            "total-cadastros-ubs": {
                "data": 0,
            },
            "porcentagem-cadastros-atualizados": {
                "data": 0,
            },
        }
        response = response.pop()
        if response[0] is not None:
            result["total-cadastros-ubs"]["data"] = int(response[0])
        if response[1] is not None:
            result["porcentagem-cadastros-atualizados"]["data"] = (
                float(response[1]) * 100
            )
        return result

    def get_cpf_cns_rate(self, response):
        result = [
            {
                "tag": "sem-cpf-cnf",
                "value": 0,
            },
            {
                "tag": "cadastros-identificados-por-cpf-cns",
                "value": 0,
            },
        ]
        response = response.pop()
        if response[0] is not None:
            result[1]["value"] = float(response[0] if response[0] is not None else 0)
        if response[1] is not None:
            result[0]["value"] = float(response[1] if response[1] is not None else 0)
        return result

    def group_localidade(self, response):
        result = []
        for resp in response:
            if resp[0] is None:
                tag = "nao-informado"
            else:
                tag = (
                    resp[0].lower().replace("zona ", "").replace("n/i", "nao-informado")
                )
            result.append({"tag": tag, "value": float(resp[1])})

        return result

    def group_raca_cor(self, response):
        result = []
        for resp in response:
            tag = "indefinido"
            if resp[0] is not None:
                tag = resp[0].lower()
            result.append(
                {
                    "tag": tag,
                    "percent": float(resp[2] if response[2] is not None else 0),
                    "value": float(resp[1] if response[1] is not None else 0),
                }
            )

        return result

    def group_records_by_origin(self, response):
        result = []
        response = response.pop()
        result = [
            {
                "tag": "fci",
                "value": {
                    "fci": int(response[2] if response[2] is not None else 0),
                },
            },
            {
                "tag": "pec",
                "value": {
                    "pec": int(response[5] if response[5] is not None else 0),
                },
            },
            {
                "tag": "recusa",
                "value": {
                    "recusa": int(response[1] if response[1] is not None else 0),
                },
            },
        ]

        return result

    def records_status(self, response):
        result = []
        label_map = {
            "cadastro_completo": "Cadastro Completo",
            "cadastro_incompleto": "Cadastro Incompleto",
            "pessoa_ident_nao_cadastrada": "Pessoa não cadastrada",
            "outro": "Outro",
        }
        return [
            {
                "tag": label_map[resp[0]],
                "value": float(resp[1]),
            }
            for resp in response
        ]

    def people_who_get_care(self, response):
        result = []
        label_map = {
            "0": "Não Acompanhados",
            "1": "Acompanhados",
        }
        return [
            {
                "tag": label_map[str(resp[0])],
                "value": float(resp[1]),
            }
            for resp in response
        ]

    def nominal_list(self, response):
        print(response)
        response["items"] = [
            RecordNominalListAdapter(r).to_dict() for r in response["items"]
        ]
        return response
