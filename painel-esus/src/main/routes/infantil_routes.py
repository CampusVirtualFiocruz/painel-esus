from flask import Blueprint, jsonify, request
from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.children_compose import (
    children_appointments_until_2_years,
    children_by_age,
    children_by_race,
    children_evaluated_feeding,
    children_first_consult_8d,
    children_get_total,
    children_high_weight_records,
    children_milestone,
)

children_bp = Blueprint("children", __name__)


class ChildrenPath:
    root_path = "/v1/children"
    urls = {
        "get_total": "/total",
        "by_age": "/by-age",
        "by_race": "/by-race",
        "first_consult_8d": "/first-consult-8d",
        "appointments_until_2_years": "/appointments-until-2-years",
        "high_weight_records": "/high-weight-records",
        "milestone": "/milestone",
        "children_evaluated_feeding": "/children-evaluated-feeding",
    }


children_path = ChildrenPath()
urls = children_path.urls


@children_bp.route("/total", methods=["GET"], endpoint="get_total")
def children_get_total_fn():
    try:
        http_response = request_adapter(request, children_get_total())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@children_bp.route("/by-age", methods=["GET"], endpoint="by_age")
def children_by_age_fn():
    try:
        http_response = request_adapter(request, children_by_age())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@children_bp.route("/by-race", methods=["GET"], endpoint="by_race")
def children_by_race_fn():
    try:
        http_response = request_adapter(request, children_by_race())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@children_bp.route("/first-consult-8d", methods=["GET"], endpoint="first_consult_8d")
def first_consult_8d_fn():
    try:
        http_response = request_adapter(request, children_first_consult_8d())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@children_bp.route(
    "/appointments-until-2-years",
    methods=["GET"],
    endpoint="appointments_until_2_years",
)
def appointments_until_2_years():
    try:
        http_response = request_adapter(request, children_appointments_until_2_years())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@children_bp.route(
    "/high-weight-records",
    methods=["GET"],
    endpoint="high_weight_records",
)
def high_weight_records():
    try:
        http_response = request_adapter(request, children_high_weight_records())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@children_bp.route(
    "/milestone",
    methods=["GET"],
    endpoint="milestone",
)
def milestone():
    try:
        http_response = request_adapter(request, children_milestone())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@children_bp.route(
    "/children-evaluated-feeding",
    methods=["GET"],
    endpoint="children-evaluated-feeding",
)
def evaluated_feeding():
    try:
        http_response = request_adapter(request, children_evaluated_feeding())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
