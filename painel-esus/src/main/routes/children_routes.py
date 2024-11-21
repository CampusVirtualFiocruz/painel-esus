from flask import Blueprint, Response, jsonify, request
from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.children_composer import (
    children_get_nominal_list,
    children_get_nominal_list_download,
    children_grouping_by_ages_location_composer,
    children_grouping_by_gender_composer,
    children_grouping_by_location_rate_composer,
    children_grouping_by_race_composer,
    children_grouping_cares_by_professionals_composer,
    children_total_composer,
)

children_bp = Blueprint("children", __name__)
import io


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
        "get_nominal_list": "/get-nominal-list",
    }


children = ChildrenPath()
urls = children.urls


@children_bp.route(urls["total"], methods=["GET"], endpoint="children_total")
@children_bp.route(urls["total"]+"/<cnes>", methods=["GET"], endpoint="children_total_id")
def children_total(cnes=None):
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
def children_grouping_by_ages_location(cnes=None):
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
def children_grouping_by_race(cnes=None):
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
def children_grouping_by_gender(cnes=None):
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
def children_grouping_by_location_rate(cnes=None):
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
def children_grouping_cares_by_professionals(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, children_grouping_cares_by_professionals_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@children_bp.route(
    f"{urls['get_nominal_list']}", methods=["GET"], endpoint="get_nominal_list"
)
@children_bp.route(
    f"{urls['get_nominal_list']}/<cnes>",
    methods=["GET"],
    endpoint="get_nominal_list_id",
)
def get_nominal_list(cnes=None):
    if cnes:
        request.view_args["cnes"] = int(request.view_args["cnes"])

    http_response = None
    response = None

    try:
        # _validation(request.args.to_dict(), schema)
        http_response = request_adapter(request, children_get_nominal_list())
        response = jsonify(http_response.body)

    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, 200


@children_bp.route(
    f"{urls['get_nominal_list']}/download/<cnes>",
    methods=["GET"],
    endpoint="get_nominal_list_id_download",
)
# @cache.cached(query_string=True)
def get_nominal_list_download(cnes=None):
    if cnes:
        request.view_args["cnes"] = int(request.view_args["cnes"])

    http_response = None
    response = None

    try:
        # _validation(request.args.to_dict(), schema)
        response = request_adapter(request, children_get_nominal_list_download())
        buffer = io.BytesIO()
        response.to_excel(buffer)

        headers = {
            "Content-Disposition": "attachment; filename=lista_nominal.xlsx",
            "Content-type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        }
        return Response(
            buffer.getvalue(),
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers=headers,
        )

    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, 200
