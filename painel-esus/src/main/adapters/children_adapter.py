# pylint: disable=C0103,C3001,W0613
from src.main.adapters.nominal_list_adapter import CriancaNominalListAdapter


class ChildrenAdapter:

    def fill_value_age_by_sex(self, _tag):
        return  {"tag": _tag, "value": {"masculino":0, "feminino": 0, "nao-informado":0}}

    def fill_value_age_by_location(self, _tag):
        return {
            "tag": _tag,
            "value": {"urbana": 0, "rural": 0, "nao-informado": 0},
        }

    def tag(self, months):
        if months <=1:
            return ( '1-mes', '1 mês')
        if months > 1:
            return (f"{months}-meses", f"{months} meses")
        return None

    def age_by_gender(self, response):
        result = {}
        for resp in response:
            _tag = self.tag(resp[0])[0]
            if _tag not in result:
                result[_tag] = self.fill_value_age_by_sex(_tag)
            else:
                sex = resp[1].lower()
                value = int(resp[2])
                result[_tag]["value"][sex] = value
        return {"data": list(result.values())}

    def age_by_location(self, response):
        result = {}
        for resp in response:
            _tag = self.tag(resp[0])[0]
            if _tag not in result:
                result[_tag] = self.fill_value_age_by_location(_tag)
            else:
                location = resp[1].lower().replace("zona ","")
                value = int(resp[2])
                result[_tag]["value"][location] = value
        return {"data": list(result.values())}

    def total_cares(self, response):
        result = {
            "total-criancas-cadastradas-2-anos": {
                "data": 0,
            },
            "total-criancas-atendidas-2-anos": {
                "data": 0,
            },
        }
        if len(response) == 0:
            return result 

        for resp in response:
            result["total-criancas-cadastradas-2-anos"]["data"] = int(resp[0])
            result["total-criancas-atendidas-2-anos"]["data"] = int(resp[1])

        return result

    def children_location_rate(self, response):
        result_item = lambda x,y: { "tag": str(x), "value": float(y)}
        if len(response) == 0:
            labels = ["nao-informado", "rural", "urbana"]
            return [result_item(l, 0) for l in labels]
        result=[]
        for r in response:
            tag = r[0].lower().replace("zona ", "").replace("n/i", "nao-informado")
            value = r[2]
            result.append(result_item(tag,value))

        return result

    def children_cares_by_professionals(self, response):
        result_item = lambda x,y: { "tag": str(x), "value": int(y)}
        professional_list = [
            "Assistente Social",
            "Cirurgião Dentista",
            "Enfermeiro",
            "Farmacêutico",
            "Fisioterapeuta",
            "Fonoaudiólogo",
            "Médico",
            "Nutricionista",
            "Professor da Educação Física",
            "Psicólogo",
            "Terapeuta Ocupacional",
            "Outros",
        ]
        result = [ result_item(p, 0) for p in professional_list]

        return result

    def children_group_by_race(self, response):
        result_item = lambda x, y: {"tag": str(x), "value": float(y)}
        result = []
        for r in response:
            tag = r[0]
            value = r[2]
            result.append(result_item(tag, value))
        return result

    def nominal_list(self, response):
        print(response["items"])
        response["items"] = [
            CriancaNominalListAdapter(r).to_dict() for r in response["items"]
        ]
        return response
