from flask import Blueprint
from flask import jsonify
from flask import request
from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.city_informations_composer import city_informations_composer

city_informations_bp = Blueprint("city_informations", __name__)


class CityInfoPath:
    root_path = '/v1/city-informations'
    urls = {
        'root': '',
    }


city_info = CityInfoPath()
urls = city_info.urls


@city_informations_bp.route(urls['root'], methods=['GET'])
def city():
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
