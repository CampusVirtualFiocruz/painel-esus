def convert_cnes(request):
    if request.view_args["cnes"]:
        request.view_args["cnes"] = int(request.view_args["cnes"])
    return request
