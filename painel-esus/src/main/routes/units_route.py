from flask import Blueprint
from flask import jsonify
from flask import request
from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.city_informations_composer import get_teams_composer
from src.main.composers.city_informations_composer import get_units_composer
from src.main.server.cache import cache

units_bp = Blueprint("units", __name__)
teams_bp = Blueprint("teams", __name__)


class UnitsPath:
    root_path = '/v1/get-units'
    urls = {
        'root': '',
    }


class TeamsPath:
    root_path = "/v1/get-teams/"
    urls = {
        "root": "",
    }


units = UnitsPath()
urls = UnitsPath.urls

teams = TeamsPath()


@units_bp.route(urls["root"], endpoint="get_units", methods=["GET"])
@units_bp.route(
    urls["root"] + "/<cnes>", endpoint="get_units_id", methods=["GET"]
)
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


@teams_bp.route(teams.urls["root"] , endpoint="get_teams", methods=["GET"])
@teams_bp.route(teams.urls["root"] + "/<cnes>", endpoint="get_teams_id", methods=["GET"])
@cache.cached()
def teams_list(cnes=None):
    http_response = None
    response = None
    if cnes and cnes is not None and cnes != 'undefined':
        request.view_args["cnes"] = int(request.view_args["cnes"])
    else:
        request.view_args["cnes"] = None
    try:
        http_response = request_adapter(request, get_teams_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code
