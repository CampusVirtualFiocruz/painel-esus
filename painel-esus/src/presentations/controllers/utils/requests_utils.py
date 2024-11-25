from src.main.adapters.request_adapter import HttpRequest


def parse_request(request: HttpRequest):
    cnes, equipe = None, None
    if request.path_params and "cnes" in request.path_params:
        cnes = int(request.path_params["cnes"])
    if request.query_params and "equipe" in request.query_params:
        equipe = int(request.query_params["equipe"])
    return cnes, equipe
