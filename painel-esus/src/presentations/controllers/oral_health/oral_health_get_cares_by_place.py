from src.data.interfaces.oral_health_dashboard_repository import \
    OralHealthDashboardRepositoryInterface
from src.presentations.http_types import HttpRequest, HttpResponse
from src.presentations.interfaces.controller_interface import \
    ControllerInterface


class OralHealthGetCaresByPlaceController(ControllerInterface):

    def __init__(self, use_case: OralHealthDashboardRepositoryInterface):
        self.__use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes = None
        if request.path_params and 'cnes' in request.path_params:
            cnes = int(request.path_params['cnes'])

        response = self.__use_case.get_oral_health_cares_by_place(cnes)
        response = response.to_dict(orient='records')
        response_parsed = {}
        for item in response:
            if item['ds_local_atendimento'] in response_parsed:
                for i in response_parsed[item['ds_local_atendimento']]['axis']:
                    if i['label'] == item['ds_local_atendimento']:
                        i["value"] = int(item['total'])
            else:
                response_parsed[item['ds_local_atendimento']] = {
                    "label": item['ds_local_atendimento'],
                    "axis": [
                        {
                            "label": '',
                            "value": int(item['total'])
                        }
                    ]
                }

        return HttpResponse(
            status_code=200,
            body=list(response_parsed.values())
        )
