from flask import jsonify, request
from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter


def convert_cnes(request):
    if request.view_args["cnes"]:
        request.view_args["cnes"] = int(request.view_args["cnes"])
    return request


def handle_request(composer, **path_args):
    try:
        args = request.args.to_dict()
        args.update(path_args)
        http_response = request_adapter(request, composer())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
