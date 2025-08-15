from collections import defaultdict


class BaseDashboardAdapter:

    def group_count_binary(self, response, tag_zero, tag_nonzero):
        return {
            "data": [
                {"tag": tag_zero, "value": sum(r[1] for r in response if r[0] == 0)},
                {"tag": tag_nonzero, "value": sum(r[1] for r in response if r[0] != 0)},
            ]
        }

    def group_gender_age(self, response):
        result = defaultdict(
            lambda: {"feminino": 0, "masculino": 0, "indeterminado": 0}
        )

        for sexo, faixa_etaria, total in response:
            if not (sexo and faixa_etaria and total is not None):
                continue
            sexo = sexo.lower()
            if sexo not in result[faixa_etaria]:
                continue
            result[faixa_etaria][sexo] += total

        return {
            "data": [
                {"tag": self.__format_faixa_etaria(faixa_etaria), "value": valores}
                for faixa_etaria, valores in result.items()
            ]
        }

    def group_race(self, response):
        base_tags = ["branca", "preta", "parda", "amarela", "indigena", "nao-informado"]
        result = {"data": [{"tag": tag, "value": 0} for tag in base_tags]}
        idx = {tag: i for i, tag in enumerate(base_tags)}

        for raca, total in response:
            tag = str(raca).lower() if raca else "nao-informado"
            if tag in idx:
                result["data"][idx[tag]]["value"] = total

        return result

    def __format_faixa_etaria(self, faixa: str) -> str:
        mapping = {
            "0a1": "menos-1-ano",
            "1a4": "1-4-anos",
            "5a9": "5-9-anos",
            "10a14": "10-14-anos",
            "15a19": "15-19-anos",
            "20a29": "20-29-anos",
            "30a39": "30-39-anos",
            "40a49": "40-49-anos",
            "50a59": "50-59-anos",
            "60a64": "60-64-anos",
            "65a69": "65-69-anos",
            "70a74": "70-74-anos",
            "75a79": "75-79-anos",
            "80+": "80-ou-mais",
        }
        faixa = faixa.lower().strip()
        return mapping.get(faixa, faixa)
