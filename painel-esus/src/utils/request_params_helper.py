def extract_cnes_equipe(request):
    cnes_param = request.query_params.get("cnes")
    cnes = int(cnes_param) if cnes_param and cnes_param.isdigit() else None

    equipe_param = request.query_params.get("equipe")
    equipe = int(equipe_param) if equipe_param and equipe_param.isdigit() else None

    return cnes, equipe
