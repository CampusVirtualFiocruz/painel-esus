from src.main.adapters.request_adapter import HttpRequest


def parse_request(request: HttpRequest):
    cnes, equipe = None, None
    if request.path_params and "cnes" in request.path_params:
        cnes = int(request.path_params["cnes"])
    if request.query_params and "equipe" in request.query_params:
        equipe = int(request.query_params["equipe"])
    return cnes, equipe


def parse_request_nominal_list(request: HttpRequest):
    cnes, equipe, itemsPerPage, page, cpf = None, None, 10, 0, None
    if request.path_params and "cnes" in request.path_params:
        cnes = int(request.path_params["cnes"])
    if request.query_params and "equipe" in request.query_params:
        equipe = int(request.query_params["equipe"])
    if request.query_params and "itemsPerPage" in request.query_params:
        itemsPerPage = int(request.query_params["itemsPerPage"])
    if request.query_params and "page" in request.query_params:
        page = int(request.query_params["page"])
    if request.query_params and "cpf" in request.query_params:
        cpf = int(request.query_params["cpf"])
    return cnes, equipe, itemsPerPage, page, cpf
