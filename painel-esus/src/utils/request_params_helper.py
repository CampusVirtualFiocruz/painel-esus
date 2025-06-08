def extract_cnes_equipe(request):
    cnes = (
        int(request.path_params["cnes"])
        if request.path_params and "cnes" in request.path_params
        else None
    )

    equipe_param = request.query_params.get("equipe")
    equipe = int(equipe_param) if equipe_param and equipe_param.isdigit() else None

    return (
        cnes,
        equipe,
    )
