"""Adapters de agregação e transformação para Cadastros.

Converte respostas de consultas SQL em estruturas prontas para o frontend,
incluindo totais, percentuais e listas nominais com anonimização.
"""

import datetime
import json

from src.main.adapters.nominal_list_adapter import RecordNominalListAdapter

class RecordsAdapter:
    """Utilitários para montar respostas de Cadastros."""
    def get_total_group(self, response):
        """Agrupa total de cadastros e percentual de atualizados."""
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
        """Percentual de cadastros identificados por CPF/CNS e não identificados."""
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
        """Distribuição por localidade (urbana/rural/não informado)."""
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
        """Distribuição por raça/cor com percentuais e valores absolutos."""
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
        """Totais por origem do cadastro (FCI/PEC/recusa)."""
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
                    "pec": int(response[4] if response[4] is not None else 0),
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
        """Distribuição por status de cadastro."""
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
        """Percentual de acompanhados e não acompanhados."""
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
        """Transforma itens de saída em dicionários anonimizados."""
        response["items"] = [
            RecordNominalListAdapter(r).to_dict() for r in response["items"]
        ]
        return response
