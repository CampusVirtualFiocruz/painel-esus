from src.data.interfaces.oral_health_dashboard_repository import \
    OralHealthDashboardRepositoryInterface
from src.presentations.http_types import HttpRequest
from src.presentations.http_types import HttpResponse
from src.presentations.interfaces.controller_interface import \
    ControllerInterface


class OralHealthGetCaresByGenderController(ControllerInterface):

    def __init__(self, use_case: OralHealthDashboardRepositoryInterface):
        self.__use_case = use_case

    def init_response_output(self, _dict, label: str):
        _dict[label] = {
            "label": label,
            "axis": [
                {
                    "label": 'Feminino',
                    "value": 0
                },
                {
                    "label": 'Masculino',
                    "value": 0
                }
            ]
        }
        return _dict

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes = None
        if request.path_params and 'cnes' in request.path_params:
            cnes = int(request.path_params['cnes'])

        response = self.__use_case.get_oral_health_cares_by_gender(cnes)
        response = response.to_dict(orient='records')
        labels = ['0 a 24 meses',
                  '2 a 9 anos',
                  '10 a 19 anos',
                  '20 a 59 anos',
                  '> de 60 anos',]
        response_parsed = {}
        for label in labels:
            self.init_response_output(response_parsed, label)
        for item in response:
            if item['ds_faixa_etaria'] in response_parsed:
                for i in response_parsed[item['ds_faixa_etaria']]['axis']:
                    if i['label'] == item['ds_sexo']:
                        i["value"] = int(item['total'])
            else:
                response_parsed[item['ds_faixa_etaria']] = {
                    "label": item['ds_faixa_etaria'],
                    "axis": [
                        {
                            "label": 'Feminino',
                            "value": 0
                        },
                        {
                            "label": 'Masculino',
                            "value": 0
                        }
                    ]
                }
                for i in response_parsed[item['ds_faixa_etaria']]['axis']:
                    if i['label'] == item['ds_sexo']:
                        i["value"] = int(item['total'])

        return HttpResponse(
            status_code=200,
            body=list(response_parsed.values())
        )
