from flask import Blueprint
from flask import jsonify
from flask import request
from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.demographics_info_composer import demographics_info_composer
from src.main.server.cache import cache

demographics_info_bp = Blueprint("demographics_info", __name__)


class DemographichInfoPath:
    root_path = '/v1/get-demographic-info'
    urls = {
        'root': '',
    }


demographics_info = DemographichInfoPath()
urls = demographics_info.urls


@demographics_info_bp.route(f"{urls['root']}", methods=["GET"],
                            endpoint='get_demographics_info')
@demographics_info_bp.route(f"{urls['root']}/<cnes>", methods=['GET'],
                            endpoint='get_demographics_info_id')
@cache.cached(query_string=True)
def get_demographics_info_fn(cnes=None):
    if cnes:
        request.view_args['cnes'] = int(request.view_args['cnes'])
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, demographics_info_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code
