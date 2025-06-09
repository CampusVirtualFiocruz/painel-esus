from flask import Blueprint, jsonify, request

from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.infantil_compose import (
    infantil_get_total,
    infantil_by_age,
    infantil_by_race,
    infantil_first_consult_8d,
    infantil_appointments_until_2_years,
)

infantil_bp = Blueprint("infantil", __name__)


class InfantilPath:
    root_path = "/v1/children"
    urls = {
        "get_total": "/total",
        "by_age": "/by-age",
        "by_race": "/by-race",
        "first_consult_8d": "/first-consult-8d",
        "appointments-until-2-years": "/appointments-until-2-years",
    }


infantil_path = InfantilPath()
urls = infantil_path.urls


@infantil_bp.route("/total", methods=["GET"], endpoint="get_total")
def infantil_get_total_fn():
    try:
        http_response = request_adapter(request, infantil_get_total())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@infantil_bp.route("/by-age", methods=["GET"], endpoint="by_age")
def infantil_by_age_fn():
    try:
        http_response = request_adapter(request, infantil_by_age())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@infantil_bp.route("/by-race", methods=["GET"], endpoint="by_race")
def infantil_by_race_fn():
    try:
        http_response = request_adapter(request, infantil_by_race())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@infantil_bp.route("/first-consult-8d", methods=["GET"], endpoint="first_consult_8d")
def first_consult_8d_fn():
    try:
        http_response = request_adapter(request, infantil_first_consult_8d())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@infantil_bp.route(
    "/appointments-until-2-years",
    methods=["GET"],
    endpoint="appointments_until_2_years",
)
def first_consult_8d_fn():
    try:
        http_response = request_adapter(request, infantil_appointments_until_2_years())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
