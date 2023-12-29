from flask import Blueprint, request, jsonify
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.city_informations_composer import get_units_composer
from src.errors.error_handler import handle_errors

from src.main.server.cache import cache
units_bp = Blueprint("units", __name__)


@units_bp.route('', methods=['GET'])
@cache.cached()
def units_list():
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, get_units_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code
