from flask import Blueprint, jsonify, request
from src.main.composers.children_compose import (
    children_get_total,
    children_by_age,
    children_by_race,
    children_first_consult_8d,
    children_appointments_until_2_years,
    children_acs_visit_until_30d,
    children_acs_visit_until_6m,
    children_dental_appointments_until_12m,
    children_dental_appointments_until_24m
)

from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter

children_bp = Blueprint("children", __name__)


class ChildrenPath:
    root_path = "/v1/children"
    urls = {
        "get_total": "/total",
        "by_age": "/by-age",
        "by_race": "/by-race",
        "first_consult_8d": "/first-consult-8d",
        "appointments-until-2-years": "/appointments-until-2-years",
        "acs_visit_until_30days" : "/acs-visit-until-30days", 
        "acs_visit_until_6month" : "/acs-visit-until-6month",
        "dental_appointment_until_12month": "/dental-appointment-until-12month",
        "dental_appointment_until_24months" : "/dental-appointment-until-24months",
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
def first_consult_8d_fn():
    try:
        http_response = request_adapter(request, children_appointments_until_2_years())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@children_bp.route(
    "/acs-visit-until-30days",
    methods=["GET"],
    endpoint="acs_visit_until_30days"
)
def acs_visit_until_30d_fn():
    try:
        http_response = request_adapter(request,  children_acs_visit_until_30d())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
    
@children_bp.route(
    "/acs-visit-until-6month",
    methods=["GET"],
    endpoint="acs_visit_until_6month"
)
def acs_visit_until_6m_fn():
    try:
        http_response = request_adapter(request,  children_acs_visit_until_6m())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@children_bp.route(
    "/dental-appointment-until-12month",
    methods=["GET"],
    endpoint="dental_appointment_until_12month")
def dental_appointment_until_12month_fn():
    try:
        http_response = request_adapter(request, children_dental_appointments_until_12m())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@children_bp.route(
    "/dental-appointment-until-24months",
    methods=["GET"],
    endpoint="dental_appointment_until_24months")
def dental_appointment_until_24months_fn():
    try:
        http_response = request_adapter(request, children_dental_appointments_until_24m())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
    