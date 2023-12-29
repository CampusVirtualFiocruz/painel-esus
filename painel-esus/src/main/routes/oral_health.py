# pylint: disable=W0613
from flask import Blueprint, jsonify, request
from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.oral_health_compose import (
    oral_health_dashboard_get_cares_by_line_of_services,
    oral_health_dashboard_get_cares_by_type_of_services,
    oral_health_dashboard_get_total, oral_health_get_all_cares_by_place,
    oral_health_get_cares_by_age_range, oral_health_get_cares_by_gender,
    oral_health_get_cares_by_outcome, oral_health_get_cares_by_place,
    oral_health_get_extraction_procedures_proportion)
from src.main.server.cache import cache

oral_health_bp = Blueprint("oral_health", __name__)


@oral_health_bp.route('/total', methods=['GET'],
                      endpoint='total')
@oral_health_bp.route('/total/<cnes>', methods=['GET'],
                      endpoint='total_id')
@cache.cached()
def oral_health_get_total(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, oral_health_dashboard_get_total())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@oral_health_bp.route('/cares-by-line-of-services', methods=['GET'],

                      endpoint='cares_by_line_of_services')
@oral_health_bp.route('/cares-by-line-of-services/<cnes>', methods=['GET'],

                      endpoint='cares_by_line_of_services_id')
@cache.cached()
def oral_health_get_cares_by_line_of_service(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, oral_health_dashboard_get_cares_by_line_of_services())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@oral_health_bp.route('/cares-by-type-of-services', methods=['GET'],
                      endpoint='cares_by_type_of_services')
@oral_health_bp.route('/cares-by-type-of-services/<cnes>', methods=['GET'],
                      endpoint='cares_by_type_of_services_id')
@cache.cached()
def oral_health_get_cares_by_type_of_service(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, oral_health_dashboard_get_cares_by_type_of_services())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@oral_health_bp.route('/get-extraction-procedures-proportion', methods=['GET'],
                      endpoint='get_extraction_procedures_proportion')
@oral_health_bp.route('/get-extraction-procedures-proportion/<cnes>', methods=['GET'],
                      endpoint='get_extraction_procedures_proportion_id')
@cache.cached()
def oral_health_get_extraction_procedures_proportion_fn(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, oral_health_get_extraction_procedures_proportion())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@oral_health_bp.route('/get-cares-by-age-range', methods=['GET'],
                      endpoint='get_cares_by_age_range')
@oral_health_bp.route('/get-cares-by-age-range/<cnes>', methods=['GET'],
                      endpoint='get_cares_by_age_range_id')
@cache.cached()
def oral_health_get_cares_by_age_range_fn(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, oral_health_get_cares_by_age_range())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@oral_health_bp.route('/get-cares-by-gender', methods=['GET'],
                      endpoint='get_cares_by_gender')
@oral_health_bp.route('/get-cares-by-gender/<cnes>', methods=['GET'],
                      endpoint='get_cares_by_gender_id')
@cache.cached()
def oral_health_get_cares_by_gender_fn(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, oral_health_get_cares_by_gender())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@oral_health_bp.route('/get-cares-by-outcome', methods=['GET'],
                      endpoint='get_cares_by_outcome')
@oral_health_bp.route('/get-cares-by-outcome/<cnes>', methods=['GET'],
                      endpoint='get_cares_by_outcome_id')
@cache.cached()
def oral_health_get_cares_by_outcome_fn(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, oral_health_get_cares_by_outcome())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@oral_health_bp.route('/get-cares-by-place', methods=['GET'],
                      endpoint='get_cares_by_place')
@oral_health_bp.route('/get-cares-by-place/<cnes>', methods=['GET'],
                      endpoint='get_cares_by_place_id')
@cache.cached()
def oral_health_get_cares_by_place_fn(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, oral_health_get_cares_by_place())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@oral_health_bp.route('/get-all-cares-by-place', methods=['GET'],
                      endpoint='get_all_cares_by_place')
@oral_health_bp.route('/get-all-cares-by-place/<cnes>', methods=['GET'],
                      endpoint='get_all_cares_by_place_id')
@cache.cached()
def oral_health_get_all_cares_by_place_fn(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, oral_health_get_all_cares_by_place())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code
