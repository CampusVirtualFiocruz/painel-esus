import io

import src.main.composers.records_composer as composer
from flask import Blueprint, Response, jsonify, request
from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter

from .utils import convert_cnes

records_bp = Blueprint("records", __name__)


class RecordsPath:
    root_path = "/v1/cadastros"
    urls = {
        "root": "",
        "total": "/total",
        "cpf_cns_rate": "/cpf_cns_rate",
        "group_by_location": "/group-by-location",
        "group_by_race": "/group-by-race",
        "group_by_origin": "/group-by-origin",
        "group_by_status": "/group-by-status",
        "get_nominal_list": "/get-nominal-list",
        "people_who_get_care": "/people-who-get-care",
    }


record = RecordsPath()
urls = record.urls


@records_bp.route(urls["total"], methods=["GET"], endpoint="records_total")
@records_bp.route(urls["total"]+"/<cnes>", methods=["GET"], endpoint="records_total_id")
def records_total(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, composer.get_total_group_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@records_bp.route(
    urls["cpf_cns_rate"], methods=["GET"], endpoint="records_cpf_cns_rate"
)
@records_bp.route(
    urls["cpf_cns_rate"] + "/<cnes>",
    methods=["GET"],
    endpoint="records_cpf_cns_ratel_id",
)
def records_cpf_cns_rate(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, composer.get_cpf_cns_rate())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@records_bp.route(
    urls["group_by_location"], methods=["GET"], endpoint="records_group_by_location"
)
@records_bp.route(
    urls["group_by_location"] + "/<cnes>",
    methods=["GET"],
    endpoint="records_group_by_locationl_id",
)
def records_group_by_location(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, composer.group_localidade())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@records_bp.route(
    urls["group_by_race"], methods=["GET"], endpoint="records_group_by_race"
)
@records_bp.route(
    urls["group_by_race"] + "/<cnes>",
    methods=["GET"],
    endpoint="records_group_by_racel_id",
)
def records_group_by_race(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, composer.group_raca_cor())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@records_bp.route(
    urls["group_by_origin"], methods=["GET"], endpoint="records_group_by_origin"
)
@records_bp.route(
    urls["group_by_origin"] + "/<cnes>",
    methods=["GET"],
    endpoint="records_group_by_origin_id",
)
def records_group_by_origin(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, composer.group_records_by_origin())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@records_bp.route(
    urls["group_by_status"], methods=["GET"], endpoint="records_group_by_status"
)
@records_bp.route(
    urls["group_by_status"] + "/<cnes>",
    methods=["GET"],
    endpoint="records_group_by_status_id",
)
def records_group_by_status(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, composer.group_records_status())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@records_bp.route(
    urls["people_who_get_care"], methods=["GET"], endpoint="records_people_who_get_care"
)
@records_bp.route(
    urls["people_who_get_care"] + "/<cnes>",
    methods=["GET"],
    endpoint="records_people_who_get_care_id",
)
def records_people_who_get_care(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, composer.people_who_get_care())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@records_bp.route(
    f"{urls['get_nominal_list']}", methods=["GET"], endpoint="get_nominal_list"
)
@records_bp.route(
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
        http_response = request_adapter(request, composer.nominal_list())
        response = jsonify(http_response.body)

    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, 200


@records_bp.route(
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
        response = request_adapter(request, composer.nominal_list_download())
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
