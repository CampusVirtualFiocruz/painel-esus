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


class OralHealthPath:
    root_path = '/v1/oral-health'
    urls = {
        'total': '/total',
        'cares_by_line_of_services': '/cares-by-line-of-services',
        'cares_by_type_of_services': '/cares-by-type-of-services',
        'get_extraction_procedures_proportion': '/get-extraction-procedures-proportion',
        'get_cares_by_age_range': "/get-cares-by-age-range",
        'get_cares_by_gender': '/get-cares-by-gender',
        'get_cares_by_outcome': '/get-cares-by-outcome',
        'get_cares_by_place': '/get-cares-by-place',
        'get_all_cares_by_place': '/get-all-cares-by-place'
    }


oral_path = OralHealthPath()
urls = oral_path.urls


@oral_health_bp.route(urls['total'], methods=['GET'],
                      endpoint='total')
@oral_health_bp.route(f"{urls['total']}/<cnes>", methods=['GET'],
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


@oral_health_bp.route(f"{urls['cares_by_line_of_services']}", methods=['GET'],

                      endpoint='cares_by_line_of_services')
@oral_health_bp.route(f"{urls['cares_by_line_of_services']}/<cnes>", methods=['GET'],

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


@oral_health_bp.route(f"{urls['cares_by_type_of_services']}", methods=['GET'],
                      endpoint='cares_by_type_of_services')
@oral_health_bp.route(f"{urls['cares_by_type_of_services']}/<cnes>", methods=['GET'],
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


@oral_health_bp.route(f"{urls['get_extraction_procedures_proportion']}", methods=['GET'],
                      endpoint='get_extraction_procedures_proportion')
@oral_health_bp.route(f"{urls['get_extraction_procedures_proportion']}/<cnes>", methods=['GET'],
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


@oral_health_bp.route(f"{urls['get_cares_by_age_range']}", methods=['GET'],
                      endpoint='get_cares_by_age_range')
@oral_health_bp.route(f"{urls['get_cares_by_age_range']}/<cnes>", methods=['GET'],
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


@oral_health_bp.route(f"{urls['get_cares_by_gender']}", methods=['GET'],
                      endpoint='get_cares_by_gender')
@oral_health_bp.route(f"{urls['get_cares_by_gender']}/<cnes>", methods=['GET'],
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


@oral_health_bp.route(f"{urls['get_cares_by_outcome']}", methods=['GET'],
                      endpoint='get_cares_by_outcome')
@oral_health_bp.route(f"{urls['get_cares_by_outcome']}/<cnes>", methods=['GET'],
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


@oral_health_bp.route(f"{urls['get_cares_by_place']}", methods=['GET'],
                      endpoint='get_cares_by_place')
@oral_health_bp.route(f"{urls['get_cares_by_place']}/<cnes>", methods=['GET'],
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


@oral_health_bp.route(f"{urls['get_all_cares_by_place']}", methods=['GET'],
                      endpoint='get_all_cares_by_place')
@oral_health_bp.route(f"{urls['get_all_cares_by_place']}/<cnes>", methods=['GET'],
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
