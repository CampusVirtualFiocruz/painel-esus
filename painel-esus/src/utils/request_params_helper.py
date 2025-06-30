def extract_cnes_equipe(request):
    cnes, equipe = None, None
    if request.path_params and "cnes" in request.path_params:
        cnes = int(request.path_params["cnes"])
    if request.query_params and "equipe" in request.query_params:
        equipe = int(request.query_params["equipe"])
    
    return cnes, equipe