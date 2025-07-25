import io

from flask import Blueprint, Response, jsonify, request
from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.children_compose import (
    children_acs_visit_until_6m,
    children_acs_visit_until_30d,
    children_appointments_until_2_years,
    children_by_age,
    children_by_race,
    children_dental_appointments_until_12m,
    children_dental_appointments_until_24m,
    children_evaluated_feeding,
    children_first_consult_8d,
    children_get_nominal_list,
    children_get_nominal_list_download,
    children_get_total,
    children_get_total_twelve_months,
    children_high_weight_records,
    children_milestone,
    children_total_medical_cares_composer,
)
from src.main.server.decorators.token_required import extract_token

children_bp = Blueprint("children", __name__)


class ChildrenPath:
    root_path = "/v1/children"
    urls = {
        "get_total": "/total",
        "get_total_twelve_months": "/total-twelve-months",
        "by_age": "/by-age",
        "by_race": "/by-race",
        "total_medical_cares": "/total-medical-cares",
        "first_consult_8d": "/first-consult-8d",
        "appointments_until_2_years": "/appointments-until-2-years",
        "acs_visit_until_30days": "/acs-visit-until-30days",
        "acs_visit_until_6month": "/acs-visit-until-6month",
        "dental_appointment_until_12month": "/dental-appointment-until-12month",
        "dental_appointment_until_24months": "/dental-appointment-until-24months",
        "high_weight_records": "/high-weight-records",
        "milestone": "/milestone",
        "evaluated_feeding": "/evaluated-feeding",
        "get_nominal_list": "/get-nominal-list",
        "get_nominal_list_download": "/get-nominal-list/download",
    }


children_path = ChildrenPath()
urls = children_path.urls


@children_bp.route("/total", methods=["GET"], endpoint="get_total")
@children_bp.route("/total/<int:cnes>", methods=["GET"], endpoint="get_total_id")
def children_get_total_fn(cnes=None):
    try:
        http_response = request_adapter(request, children_get_total())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        return jsonify(http_response.body), http_response.status_code


@children_bp.route(
    "/total-twelve-months", methods=["GET"], endpoint="get_total_twelve_months"
)
@children_bp.route(
    "/total-twelve-months/<int:cnes>",
    methods=["GET"],
    endpoint="get_total_twelve_months_id",
)
def children_get_total_twelve_months_fn(cnes=None):
    try:
        http_response = request_adapter(request, children_get_total_twelve_months())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        return jsonify(http_response.body), http_response.status_code


@children_bp.route("/by-age", methods=["GET"], endpoint="by_age")
@children_bp.route("/by-age/<int:cnes>", methods=["GET"], endpoint="by_age_id")
def children_by_age_fn(cnes=None):
    try:
        http_response = request_adapter(request, children_by_age())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        return jsonify(http_response.body), http_response.status_code


@children_bp.route("/by-race", methods=["GET"], endpoint="by_race")
@children_bp.route("/by-race/<int:cnes>", methods=["GET"], endpoint="by_race_id")
def children_by_race_fn(cnes=None):
    try:
        http_response = request_adapter(request, children_by_race())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        return jsonify(http_response.body), http_response.status_code


@children_bp.route(
    urls["total_medical_cares"], methods=["GET"], endpoint="total_medical_cares"
)
@children_bp.route(
    urls["total_medical_cares"] + "/<cnes>",
    methods=["GET"],
    endpoint="total_medical_cares_id",
)
def children_total_cares(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, children_total_medical_cares_composer()
        )
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        response = jsonify(http_response.body)

    return response, http_response.status_code


@children_bp.route("/first-consult-8d", methods=["GET"], endpoint="first_consult_8d")
@children_bp.route(
    "/first-consult-8d/<int:cnes>", methods=["GET"], endpoint="first_consult_8d_id"
)
def first_consult_8d_fn(cnes=None):
    try:
        http_response = request_adapter(request, children_first_consult_8d())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        return jsonify(http_response.body), http_response.status_code


@children_bp.route(
    "/appointments-until-2-years",
    methods=["GET"],
    endpoint="appointments_until_2_years",
)
@children_bp.route(
    "/appointments-until-2-years/<int:cnes>",
    methods=["GET"],
    endpoint="appointments_until_2_years_id",
)
def appointments_until_2_years(cnes=None):
    try:
        http_response = request_adapter(request, children_appointments_until_2_years())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        return jsonify(http_response.body), http_response.status_code


@children_bp.route(
    "/acs-visit-until-30days", methods=["GET"], endpoint="acs_visit_until_30days"
)
@children_bp.route(
    "/acs-visit-until-30days/<int:cnes>",
    methods=["GET"],
    endpoint="acs_visit_until_30days_id",
)
def acs_visit_until_30d_fn(cnes=None):
    try:
        http_response = request_adapter(request, children_acs_visit_until_30d())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        return jsonify(http_response.body), http_response.status_code


@children_bp.route(
    "/acs-visit-until-6month", methods=["GET"], endpoint="acs_visit_until_6month"
)
@children_bp.route(
    "/acs-visit-until-6month/<int:cnes>",
    methods=["GET"],
    endpoint="acs_visit_until_6month_id",
)
def acs_visit_until_6m_fn(cnes=None):
    try:
        http_response = request_adapter(request, children_acs_visit_until_6m())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        return jsonify(http_response.body), http_response.status_code


@children_bp.route(
    "/dental-appointment-until-12month",
    methods=["GET"],
    endpoint="dental_appointment_until_12month",
)
@children_bp.route(
    "/dental-appointment-until-12month/<int:cnes>",
    methods=["GET"],
    endpoint="dental_appointment_until_12month_id",
)
def dental_appointment_until_12month_fn(cnes=None):
    try:
        http_response = request_adapter(
            request, children_dental_appointments_until_12m()
        )
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        return jsonify(http_response.body), http_response.status_code


@children_bp.route(
    "/dental-appointment-until-24months",
    methods=["GET"],
    endpoint="dental_appointment_until_24months",
)
@children_bp.route(
    "/dental-appointment-until-24months/<int:cnes>",
    methods=["GET"],
    endpoint="dental_appointment_until_24months_id",
)
def dental_appointment_until_24months_fn(cnes=None):
    try:
        http_response = request_adapter(
            request, children_dental_appointments_until_24m()
        )
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        return jsonify(http_response.body), http_response.status_code


@children_bp.route(
    "/high-weight-records",
    methods=["GET"],
    endpoint="high_weight_records",
)
@children_bp.route(
    "/high-weight-records/<int:cnes>",
    methods=["GET"],
    endpoint="high_weight_records_id",
)
def high_weight_records(cnes=None):
    try:
        http_response = request_adapter(request, children_high_weight_records())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        return jsonify(http_response.body), http_response.status_code


@children_bp.route(
    "/milestone",
    methods=["GET"],
    endpoint="milestone",
)
@children_bp.route(
    "/milestone/<int:cnes>",
    methods=["GET"],
    endpoint="milestone_id",
)
def milestone(cnes=None):
    try:
        http_response = request_adapter(request, children_milestone())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        return jsonify(http_response.body), http_response.status_code


@children_bp.route(
    "/evaluated-feeding",
    methods=["GET"],
    endpoint="evaluated_feeding",
)
@children_bp.route(
    "/evaluated-feeding/<int:cnes>",
    methods=["GET"],
    endpoint="evaluated_feeding_id",
)
def evaluated_feeding(cnes=None):
    try:
        http_response = request_adapter(request, children_evaluated_feeding())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        return jsonify(http_response.body), http_response.status_code


@children_bp.route(
    "/get-nominal-list",
    methods=["GET"],
    endpoint="get_nominal_list",
)
@children_bp.route(
    "/get-nominal-list/<int:cnes>",
    methods=["GET"],
    endpoint="get_nominal_list_id",
)
def get_nominal_list(cnes=None):
    try:
        http_response = request_adapter(request, children_get_nominal_list())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        return jsonify(http_response.body), http_response.status_code


@children_bp.route(
    "/get-nominal-list/download",
    methods=["GET"],
    endpoint="get_nominal_list_download",
)
@children_bp.route(
    "/get-nominal-list/download/<int:cnes>",
    methods=["GET"],
    endpoint="get_nominal_list_download_id",
)
def get_nominal_list_download(cnes=None):
    try:
        if cnes is None and "cnes" in request.args:
            try:
                cnes = int(request.args["cnes"])
            except ValueError:
                cnes = None

        controller = children_get_nominal_list_download()
        http_response = request_adapter(request, controller)

        buffer = io.BytesIO()
        http_response.body.to_excel(buffer, index=False)
        buffer.seek(0)

        headers = {
            "Content-Disposition": "attachment; filename=lista_nominal.xlsx",
            "Content-Type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        }

        return Response(
            buffer.getvalue(),
            mimetype=headers["Content-Type"],
            headers=headers,
        )

    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        return jsonify(http_response.body), http_response.status_code
