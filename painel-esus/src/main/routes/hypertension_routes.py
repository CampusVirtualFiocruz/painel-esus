# pylint: disable=W0613
from flask import Blueprint, jsonify, request

from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.hypertension_dashboard_composer import (
    hypertension_dashboard_get_age_group_gender,
    hypertension_dashboard_get_age_groups_location,
    hypertension_dashboard_get_complications,
    hypertension_dashboard_get_exams_count, hypertension_dashboard_get_imc,
    hypertension_dashboard_get_professionals_count,
    hypertension_dashboard_get_total,
    hypertension_dashboard_get_individual_exams_count)


from src.main.server.cache import cache

hypertension_bp = Blueprint("hypertension", __name__)


@hypertension_bp.route('/total', methods=['GET'],
                       endpoint='total')
@hypertension_bp.route('/total/<cnes>', methods=['GET'],
                       endpoint='total_id')
@cache.cached()
def get_total(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, hypertension_dashboard_get_total())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@hypertension_bp.route('/age-group-gender', methods=['GET'],
                       endpoint='get_age_group_gender')
@hypertension_bp.route('/age-group-gender/<cnes>', methods=['GET'],
                       endpoint='get_age_group_gender_id')
@cache.cached()
def get_age_group_gender(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, hypertension_dashboard_get_age_group_gender())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@hypertension_bp.route('/age-group-location', methods=['GET'],
                       endpoint='get_age_group_location')
@hypertension_bp.route('/age-group-location/<cnes>', methods=['GET'],
                       endpoint='get_age_group_location_id')
@cache.cached()
def get_age_group_location(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, hypertension_dashboard_get_age_groups_location())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@hypertension_bp.route('/imc', methods=['GET'],
                       endpoint='get_imc')
@hypertension_bp.route('/imc/<int:cnes>', methods=['GET'],
                       endpoint='get_imc_id')
@cache.cached()
def get_imc(cnes=None):
    if cnes:
        request.view_args['cnes'] = int(request.view_args['cnes'])
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, hypertension_dashboard_get_imc())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@hypertension_bp.route('/complications', methods=['GET'],
                       endpoint='get_complications')
@hypertension_bp.route('/complications/<cnes>', methods=['GET'],
                       endpoint='get_complications_id')
@cache.cached()
def get_complications(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, hypertension_dashboard_get_complications())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@hypertension_bp.route('/exams', methods=['GET'],
                       endpoint='get_exams')
@hypertension_bp.route('/exams/<cnes>', methods=['GET'],
                       endpoint='get_exams_id')
@cache.cached()
def get_exams(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, hypertension_dashboard_get_exams_count())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@hypertension_bp.route('/professionals', methods=['GET'],
                       endpoint='get_professionals')
@hypertension_bp.route('/professionals/<cnes>', methods=['GET'],
                       endpoint='get_professionals_id')
@cache.cached()
def get_professionals(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, hypertension_dashboard_get_professionals_count())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@hypertension_bp.route('/get-hypertensive-list', methods=['GET'],
                       endpoint='get_hypertenses_list')
@hypertension_bp.route('/get-hypertensive-list/<cnes>', methods=['GET'],
                       endpoint='get_hypertenses_list_id')
@cache.cached()
def get_hypertenses_list(cnes=None):
    if cnes:
        request.view_args['cnes'] = int(request.view_args['cnes'])

    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, hypertension_dashboard_get_individual_exams_count())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code
