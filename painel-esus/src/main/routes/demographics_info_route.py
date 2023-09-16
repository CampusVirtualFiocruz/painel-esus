from flask import Blueprint, request, jsonify
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.demographics_info_composer import demographics_info_composer
from src.errors.error_handler import handle_errors

demographics_info_bp = Blueprint("demographics_info", __name__)

#v1/get-demographic-info
@demographics_info_bp.route("/", methods=["GET"])
def get_demographics_info():
    http_response = None
    response = None
    try:
        # user_finder_validator(request)
        http_response = request_adapter(request, demographics_info_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code
