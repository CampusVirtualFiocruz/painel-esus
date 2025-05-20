# pylint: disable=W0613
# pylint: disable=E0401,C0301,W0612,W0611
from flask import Blueprint, jsonify, request
from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.oral_health_compose import (
    oral_health_get_atraumatic_treatment,
    oral_health_get_cares_by_gender,
    oral_health_get_cares_by_race,
    oral_health_get_conclued_treatment,
    oral_health_get_extraction,
    oral_health_get_first_appointment,
    oral_health_get_nominal_list,
    oral_health_get_prevention_procedures,
    oral_health_get_supervised_brushing,
    oral_health_get_total,
)
from src.main.server.cache import cache

oral_health_bp = Blueprint("oral_health", __name__)


class OralHealthPath:
    root_path = "/v1/oral-health"
    urls = {
        "get_cares_by_gender": "/get-cares-by-gender",
        "get_extraction": "/get-extraction",
        "get_first_appointment": "/get-first-appointment",
        "get_conclued_treatment": "/get-conclued-treatment",
        "get_group_by_race": "/get-group-by-race",
        "get_prevention_procedures": "/get-prevention-procedures",
        "get_supervised_brushing": "/get-supervised-brushing",
        "get_atraumatic_treatment": "/get-atraumatic-treatment",
        "get_nominal_list": "/get-nominal-list",
        "get_total": "/get-total",
    }


oral_path = OralHealthPath()
urls = oral_path.urls


@oral_health_bp.route(
    f"{urls['get_extraction']}",
    methods=["GET"],
    endpoint="get_extraction",
)
@oral_health_bp.route(
    f"{urls['get_extraction']}/<cnes>",
    methods=["GET"],
    endpoint="get_extraction_id",
)
#@cache.cached()
def oral_health_get_extraction_fn(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, oral_health_get_extraction())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@oral_health_bp.route(
    f"{urls['get_cares_by_gender']}", methods=["GET"], endpoint="get_cares_by_gender"
)
@oral_health_bp.route(
    f"{urls['get_cares_by_gender']}/<cnes>",
    methods=["GET"],
    endpoint="get_cares_by_gender_id",
)
#@cache.cached(query_string=True)
def oral_health_get_cares_by_gender_fn(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, oral_health_get_cares_by_gender())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@oral_health_bp.route(
    f"{urls['get_group_by_race']}", methods=["GET"], endpoint="get_group_by_race"
)
@oral_health_bp.route(
    f"{urls['get_group_by_race']}/<cnes>",
    methods=["GET"],
    endpoint="get_group_by_race_id",
)
#@cache.cached(query_string=True)
def oral_health_get_cares_by_race_fn(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, oral_health_get_cares_by_race())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@oral_health_bp.route(
    f"{urls['get_first_appointment']}",
    methods=["GET"],
    endpoint="get_first_appointment",
)
@oral_health_bp.route(
    f"{urls['get_first_appointment']}/<cnes>",
    methods=["GET"],
    endpoint="get_first_appointment_id",
)
#@cache.cached(query_string=True)
def oral_health_get_first_appointment_fn(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, oral_health_get_first_appointment())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@oral_health_bp.route(
    f"{urls['get_conclued_treatment']}",
    methods=["GET"],
    endpoint="get_conclued_treatment",
)
@oral_health_bp.route(
    f"{urls['get_conclued_treatment']}/<cnes>",
    methods=["GET"],
    endpoint="get_conclued_treatment_id",
)
#@cache.cached(query_string=True)
def oral_health_get_conclued_treatment_fn(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, oral_health_get_conclued_treatment())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
    return response, http_response.status_code


@oral_health_bp.route(
    f"{urls['get_prevention_procedures']}",
    methods=["GET"],
    endpoint="get_prevention_procedures",
)
@oral_health_bp.route(
    f"{urls['get_prevention_procedures']}/<cnes>",
    methods=["GET"],
    endpoint="get_prevention_procedures_id",
)
#@cache.cached(query_string=True)
def oral_health_get_prevention_procedures_fn(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, oral_health_get_prevention_procedures()
        )
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)

        response = jsonify(http_response.body)

    return response, http_response.status_code


@oral_health_bp.route(
    f"{urls['get_supervised_brushing']}",
    methods=["GET"],
    endpoint="get_supervised_brushing",
)
@oral_health_bp.route(
    f"{urls['get_supervised_brushing']}/<cnes>",
    methods=["GET"],
    endpoint="get_supervised_brushing_id",
)
#@cache.cached(query_string=True)
def oral_health_get_supervised_brushing_fn(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, oral_health_get_supervised_brushing())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)

        response = jsonify(http_response.body)

    return response, http_response.status_code


@oral_health_bp.route(
    f"{urls['get_atraumatic_treatment']}",
    methods=["GET"],
    endpoint="get_atraumatic_treatment",
)
@oral_health_bp.route(
    f"{urls['get_atraumatic_treatment']}/<cnes>",
    methods=["GET"],
    endpoint="get_atraumatic_treatment_id",
)
#@cache.cached(query_string=True)
def oral_health_get_atraumatic_treatment_fn(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, oral_health_get_atraumatic_treatment())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)

        response = jsonify(http_response.body)

    return response, http_response.status_code

@oral_health_bp.route(
    f"{urls['get_nominal_list']}",
    methods=["GET"],
    endpoint="get_nominal_list",
)
@oral_health_bp.route(
    f"{urls['get_nominal_list']}/<cnes>",
    methods=["GET"],
    endpoint="get_nominal_list_id",
)
#@cache.cached(query_string=True)
def oral_health_get_nominal_list_fn(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, oral_health_get_nominal_list())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)

        response = jsonify(http_response.body)

    return response, http_response.status_code


@oral_health_bp.route(
    f"{urls['get_total']}",
    methods=["GET"],
    endpoint="get_total",
)
@oral_health_bp.route(
    f"{urls['get_total']}/<cnes>",
    methods=["GET"],
    endpoint="get_total_id",
)
## @cache.cached()
def oral_health_get_total_fn(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, oral_health_get_total())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code
