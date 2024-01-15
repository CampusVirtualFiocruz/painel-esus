from src.presentations.interfaces.controller_interface import \
    ControllerInterface
from src.data.interfaces.oral_health_dashboard_repository import \
    OralHealthDashboardRepositoryInterface
from src.presentations.http_types import HttpRequest, HttpResponse


class OralHealthGetCaresByOutcomeController(ControllerInterface):

    def __init__(self, use_case: OralHealthDashboardRepositoryInterface):
        self.__use_case = use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        cnes = None
        if request.path_params and 'cnes' in request.path_params:
            cnes = int(request.path_params['cnes'])

        response = self.__use_case.get_oral_health_cares_by_outcome(cnes)
        response = response.to_dict(orient='records')
        response_parsed = []
        total = 0
        for i in response:
            total += i['total']
            response_parsed.append({
                "label": i["label"],
                "value": int(i["total"]),
                "percent": 0
            })
        for i in response_parsed:
            i["percent"] = round(float(i["value"]/total)*100, 2)
        return HttpResponse(
            status_code=200,
            body=list(sorted(response_parsed,
                      key=lambda x: x["percent"], reverse=True))
        )
