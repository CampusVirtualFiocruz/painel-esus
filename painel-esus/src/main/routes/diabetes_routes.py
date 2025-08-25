# pylint: disable=W0613
import io

from flask import Blueprint, Response, jsonify, request
from src.errors.error_handler import handle_errors
from src.infra.requests.factory import send_download_request
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.diabetes_dashboard_composer import (
    diabetes_dashboard_get_age_group_gender,
    diabetes_dashboard_get_by_race,
    diabetes_dashboard_get_complications,
    diabetes_dashboard_get_exams_count,
    diabetes_dashboard_get_imc,
    diabetes_dashboard_get_nominal_list,
    diabetes_dashboard_get_nominal_list_download,
    diabetes_dashboard_get_total,
)
from src.main.server.cache import cache
from src.main.server.decorators.token_required import extract_token
from src.presentations.validators.schema.nominal_list import schema

diabetes_bp = Blueprint("diabetes", __name__)


class DiabetesPath:
    root_path = "/v1/diabetes"
    urls = {
        "total": "/total",
        "by_gender": "/by-gender",
        "imc": "/imc",
        "by_race": "/by-race",
        "complications": "/complications",
        "exams": "/exams",
        "get_nominal_list": "/get-nominal-list",
    }


diabetes = DiabetesPath()
urls = diabetes.urls


@diabetes_bp.route(f"{urls['total']}", methods=["GET"], endpoint="total")
@diabetes_bp.route(f"{urls['total']}/<cnes>", methods=["GET"], endpoint="total_id")
def get_total(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, diabetes_dashboard_get_total())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(
            exception, extract_token(request.headers.get("Authorization"))
        )
        response = jsonify(http_response.body)

    return response, http_response.status_code


@diabetes_bp.route(
    f"{urls['by_gender']}", methods=["GET"], endpoint="get_by_gender"
)
@diabetes_bp.route(
    f"{urls['by_gender']}/<cnes>", methods=["GET"], endpoint="get_age_group_gender_id"
)
def get_age_group_gender(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, diabetes_dashboard_get_age_group_gender()
        )
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(
            exception, extract_token(request.headers.get("Authorization"))
        )
        response = jsonify(http_response.body)

    return response, http_response.status_code


@diabetes_bp.route(f"{urls['imc']}", methods=["GET"], endpoint="get_imc")
@diabetes_bp.route(
    f"{urls['imc']}/<int:cnes>", methods=["GET"], endpoint="get_imc_id"
)
def get_imc(cnes=None):
    if cnes:
        request.view_args["cnes"] = int(request.view_args["cnes"])
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, diabetes_dashboard_get_imc())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(
            exception, extract_token(request.headers.get("Authorization"))
        )
        response = jsonify(http_response.body)

    return response, http_response.status_code


@diabetes_bp.route(
    f"{urls['complications']}", methods=["GET"], endpoint="get_complications"
)
@diabetes_bp.route(
    f"{urls['complications']}/<int:cnes>", methods=["GET"], endpoint="get_complications_id"
)
def get_complications(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, diabetes_dashboard_get_complications()
        )
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(
            exception, extract_token(request.headers.get("Authorization"))
        )
        response = jsonify(http_response.body)

    return response, http_response.status_code


@diabetes_bp.route(f"{urls['exams']}", methods=["GET"], endpoint="get_exams")
@diabetes_bp.route(
    f"{urls['exams']}/<cnes>", methods=["GET"], endpoint="get_exams_id"
)
def get_exams(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, diabetes_dashboard_get_exams_count()
        )
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(
            exception, extract_token(request.headers.get("Authorization"))
        )
        response = jsonify(http_response.body)

    return response, http_response.status_code


@diabetes_bp.route(f"{urls['by_race']}", methods=["GET"], endpoint="get_by_race")
@diabetes_bp.route(
    f"{urls['by_race']}/<cnes>", methods=["GET"], endpoint="get_by_race_id"
)
def get_by_race(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, diabetes_dashboard_get_by_race())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(
            exception, extract_token(request.headers.get("Authorization"))
        )
        response = jsonify(http_response.body)

    return response, http_response.status_code


@diabetes_bp.route(
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
        http_response = request_adapter(
            request, diabetes_dashboard_get_nominal_list()
        )
        return jsonify(http_response.body), 200

    except Exception as exception:
        http_response = handle_errors(
            exception, extract_token(request.headers.get("Authorization"))
        )
        return jsonify(http_response.body), 500



@diabetes_bp.route(
    f"{urls['get_nominal_list']}/download/<cnes>",
    methods=["GET"],
    endpoint="get_nominal_list_id_download",
)
def get_nominal_list_download(cnes=None):
    if cnes:
        request.view_args["cnes"] = int(request.view_args["cnes"])

    http_response = None
    response = None

    try:
        # _validation(request.args.to_dict(), schema)
        response = request_adapter(
            request, diabetes_dashboard_get_nominal_list_download()
        )

        buffer = io.BytesIO()
        response.to_excel(buffer)

        headers = {
            "Content-Disposition": "attachment; filename=lista_nominal.xlsx",
            "Content-type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        }
        send_download_request(
            "Baixando lista nominal de hipertensão.",
            "lista_nominal_hipertensao",
            request,
        )
        return Response(
            buffer.getvalue(),
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers=headers,
        )

    except Exception as exception:
        http_response = handle_errors(
            exception, extract_token(request.headers.get("Authorization"))
        )
        response = jsonify(http_response.body)

    return response, 200
