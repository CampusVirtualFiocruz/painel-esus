from flask import Blueprint, request, jsonify
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.city_informations_composer import city_informations_composer
from src.errors.error_handler import handle_errors

city_informations_bp = Blueprint("city_informations", __name__)


@city_informations_bp.route('', methods=['GET'])
def city():
    print('CITY INFO')
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, city_informations_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code
