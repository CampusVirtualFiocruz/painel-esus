from src.main.adapters.nominal_list_adapter import CriancaNominalListAdapter


class RecordsAdapter:
    def get_total_group(self, response):
        result =  {
            "total-cadastros-ubs": {
                "data":0,
            },
            "porcentagem-cadastros-atualizados": {
                "data": 0,
            },
        }
        response = response.pop()
        if response[0] is not None:
            result["total-cadastros-ubs"]["data"] = int(response[0])
        if response[1] is not None:
            result["porcentagem-cadastros-atualizados"]["data"] = float(response[1])
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
            result[1]["value"] = float(response[0])
        if response[1] is not None:
            result[0]["value"] = float(response[1])
        return result

    def group_localidade(self, response):
        result = []
        for resp in response:
            tag = resp[0].lower().replace("zona ", "").replace("n/i", "nao-informado")
            result.append({
                "tag":tag,
                "value": float(resp[2])
            })

        return result

    def group_raca_cor(self, response):
        result = []
        for resp in response:
            tag='indefinido'
            if resp[0] is not None:
                tag = resp[0].lower()
            result.append({"tag": tag, "value": float(resp[2])})

        return result

    def group_records_by_origin(self, response):
        result = []
        response=response.pop()
        result = [
            {
                "tag": "fci",
                "value": {
                    "fci": int(response[2]),
                },
            },
            {
                "tag": "pec",
                "value": {
                    "pec": int(response[5]),
                },
            },
            {
                "tag": "recusa",
                "value": {
                    "recusa": int(response[1]),
                },
            },
        ]

        return result

    def records_status(self, response):
        response = response.pop()
        
        return [
            {
                "tag": "ativo",
                "value": float(response[1]),
            },
            {
                "tag": "inconsistente",
                "value": float(response[3]),
            },
        ]

    def nominal_list(self, response):
        response["items"] = [
            CriancaNominalListAdapter(r).to_dict() for r in response["items"]
        ]
        return response
