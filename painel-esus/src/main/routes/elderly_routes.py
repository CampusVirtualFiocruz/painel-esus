import io

from flask import Blueprint, Response, jsonify, request
from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.elderly_composer import (
    elderly_get_nominal_list,
    elderly_get_nominal_list_download,
    elderly_group_by_age_location_composer,
    elderly_group_by_gender_composer,
    elderly_group_by_imc,
    elderly_group_by_race_composer,
    elderly_hipertesnion_diabetes_rate_composer,
    elderly_imc_rate_composer,
    elderly_influenza_rate_composer,
    elderly_odonto_rate_composer,
    elderly_total_composer,
)

elderly_bp = Blueprint("elderly", __name__)


class ElderlyPath:
    root_path = "/v1/elderly"
    urls = {
        "root": "",
        "total": "/total",
        "group_by_age_location": "/group-by-age-location",
        "group_by_gender": "/group-by-gender",
        "group_by_race": "/group-by-race",
        "group_by_imc": "/group-by-imc",
        "grouping_by_imc_rate": "/group-by-imc-rate",
        "grouping_by_influenza_rate": "/group-by-influenza-rate",
        "grouping_by_odonto_rate": "/group-by-odonto-rate",
        "grouping_hipertesnion_diabetes_rate": "/group-hipertesnion-diabetes-rate",
        "get_nominal_list": "/get-nominal-list",
    }


elderly = ElderlyPath()
urls = elderly.urls


@elderly_bp.route(urls["total"], methods=["GET"], endpoint="elderly_total")
@elderly_bp.route(
    urls["total"] + "/<cnes>", methods=["GET"], endpoint="elderly_total_id"
)
def elderly_total(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_total_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@elderly_bp.route(
    urls["group_by_age_location"], methods=["GET"], endpoint="group_by_age_location"
)
@elderly_bp.route(
    urls["group_by_age_location"] + "/<cnes>",
    methods=["GET"],
    endpoint="group_by_age_location_id",
)
def elderly_grouping_by_ages_location(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, elderly_group_by_age_location_composer()
        )
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@elderly_bp.route(urls["group_by_race"], methods=["GET"], endpoint="group_by_race")
@elderly_bp.route(
    urls["group_by_race"] + "/<cnes>",
    methods=["GET"],
    endpoint="group_by_race_id",
)
def elderly_grouping_by_race(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_group_by_race_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@elderly_bp.route(urls["group_by_gender"], methods=["GET"], endpoint="group_by_gender")
@elderly_bp.route(
    urls["group_by_gender"] + "/<cnes>",
    methods=["GET"],
    endpoint="group_by_gender_id",
)
def elderly_grouping_by_gender(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_group_by_gender_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@elderly_bp.route(
    urls["grouping_by_imc_rate"],
    methods=["GET"],
    endpoint="grouping_by_imc_rate",
)
@elderly_bp.route(
    urls["grouping_by_imc_rate"] + "/<cnes>",
    methods=["GET"],
    endpoint="grouping_by_imc_rate_id",
)
def elderly_grouping_by_imc_rate(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_imc_rate_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@elderly_bp.route(
    urls["grouping_by_influenza_rate"],
    methods=["GET"],
    endpoint="grouping_by_influenza_rate",
)
@elderly_bp.route(
    urls["grouping_by_influenza_rate"] + "/<cnes>",
    methods=["GET"],
    endpoint="grouping_by_influenza_rate_id",
)
def elderly_grouping_by_influenza_rate(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, elderly_influenza_rate_composer()
        )
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@elderly_bp.route(
    urls["grouping_by_odonto_rate"],
    methods=["GET"],
    endpoint="grouping_by_odonto_rate",
)
@elderly_bp.route(
    urls["grouping_by_odonto_rate"] + "/<cnes>",
    methods=["GET"],
    endpoint="grouping_by_odonto_rate_id",
)
def elderly_grouping_by_odonto_rate(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_odonto_rate_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@elderly_bp.route(
    urls["grouping_hipertesnion_diabetes_rate"],
    methods=["GET"],
    endpoint="grouping_hipertesnion_diabetes_rate",
)
@elderly_bp.route(
    urls["grouping_hipertesnion_diabetes_rate"] + "/<cnes>",
    methods=["GET"],
    endpoint="grouping_hipertesnion_diabetes_rate_id",
)
def elderly_grouping_hipertesnion_diabetes_rate(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_hipertesnion_diabetes_rate_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@elderly_bp.route(
    urls["group_by_imc"],
    methods=["GET"],
    endpoint="group_by_imc",
)
@elderly_bp.route(
    urls["group_by_imc"] + "/<cnes>",
    methods=["GET"],
    endpoint="group_by_imc_id",
)
def elderly_group_by_imc(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_imc_rate_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@elderly_bp.route(
    f"{urls['get_nominal_list']}", methods=["GET"], endpoint="get_nominal_list"
)
@elderly_bp.route(
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
        http_response = request_adapter(request, elderly_get_nominal_list())
        response = jsonify(http_response.body)

    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, 200


@elderly_bp.route(
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
        response = request_adapter(request, elderly_get_nominal_list_download())
        print(response.head())
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
