from flask import Blueprint
from flask import jsonify
from flask import request
from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.children_composer import children_grouping_by_ages_location_composer
from src.main.composers.children_composer import children_grouping_by_gender_composer
from src.main.composers.children_composer import children_grouping_by_location_rate_composer
from src.main.composers.children_composer import children_grouping_by_race_composer
from src.main.composers.children_composer import children_grouping_cares_by_professionals_composer
from src.main.composers.children_composer import children_total_composer

children_bp = Blueprint("children", __name__)


class ChildrenPath:
    root_path = "/v1/children"
    urls = {
        "root": "",
        "total": "/total",
        "group_by_age_location": "/group-by-age-location",
        "group_by_race": "/group-by-race",
        "group_by_gender": "/group-by-gender",
        "grouping_by_location_rate": "/group-by-location-rate",
        "grouping_cares_by_professionals": "/group-cares-by-professionals",
    }


children = ChildrenPath()
urls = children.urls


@children_bp.route(urls["total"], methods=["GET"], endpoint="children_total")
@children_bp.route(urls["total"]+"/<cnes>", methods=["GET"], endpoint="children_total_id")
def children_total():
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, children_total_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code

@children_bp.route(urls["group_by_age_location"], methods=["GET"], endpoint="group_by_age_location")
@children_bp.route(urls["group_by_age_location"]+"/<cnes>", methods=["GET"], endpoint="group_by_age_location_id")
def children_grouping_by_ages_location():
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, children_grouping_by_ages_location_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@children_bp.route(urls["group_by_race"], methods=["GET"], endpoint="group_by_race")
@children_bp.route(
    urls["group_by_race"] + "/<cnes>",
    methods=["GET"],
    endpoint="group_by_race_id",
)
def children_grouping_by_race():
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, children_grouping_by_race_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code

@children_bp.route(urls["group_by_gender"], methods=["GET"], endpoint="group_by_gender")
@children_bp.route(
    urls["group_by_gender"] + "/<cnes>",
    methods=["GET"],
    endpoint="group_by_gender_id",
)
def children_grouping_by_gender():
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, children_grouping_by_gender_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@children_bp.route(urls["grouping_by_location_rate"], methods=["GET"], endpoint="grouping_by_location_rate")
@children_bp.route(
    urls["grouping_by_location_rate"] + "/<cnes>",
    methods=["GET"],
    endpoint="grouping_by_location_rate_id",
)
def children_grouping_by_location_rate():
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, children_grouping_by_location_rate_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@children_bp.route(urls["grouping_cares_by_professionals"], methods=["GET"], endpoint="grouping_cares_by_professionals")
@children_bp.route(
    urls["grouping_cares_by_professionals"] + "/<cnes>",
    methods=["GET"],
    endpoint="grouping_cares_by_professionals_id",
)
def children_grouping_cares_by_professionals():
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, children_grouping_cares_by_professionals_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code
