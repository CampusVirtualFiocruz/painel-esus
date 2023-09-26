from flask import Blueprint, jsonify, request

from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.diabetes_dashboard_composer import (
    diabetes_dashboard_get_age_group_gender,
    diabetes_dashboard_get_age_groups_location,
    diabetes_dashboard_get_complications,
    diabetes_dashboard_get_exams_count, diabetes_dashboard_get_imc,
    diabetes_dashboard_get_professionals_count,
    diabetes_dashboard_get_total,
    diabetes_dashboard_get_individual_exams_count)


diabetes_bp = Blueprint("diabetes", __name__)


@diabetes_bp.route('/total', methods=['GET'])
def get_total():
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, diabetes_dashboard_get_total())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@diabetes_bp.route('/age-group-gender', methods=['GET'])
def get_age_group_gender():
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, diabetes_dashboard_get_age_group_gender())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@diabetes_bp.route('/age-group-location', methods=['GET'])
def get_age_group_location():
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, diabetes_dashboard_get_age_groups_location())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@diabetes_bp.route('/imc', methods=['GET'])
@diabetes_bp.route('/imc/<int:cnes>', methods=['GET'])
def get_imc(cnes=None):
    if cnes:
        request.view_args['cnes'] = int(request.view_args['cnes'])
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, diabetes_dashboard_get_imc())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@diabetes_bp.route('/complications', methods=['GET'])
def get_complications():
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, diabetes_dashboard_get_complications())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@diabetes_bp.route('/exams', methods=['GET'])
def get_exams():
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, diabetes_dashboard_get_exams_count())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@diabetes_bp.route('/professionals', methods=['GET'])
def get_professionals():
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, diabetes_dashboard_get_professionals_count())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@diabetes_bp.route('/get-diabetes-list', methods=['GET'])
@diabetes_bp.route('/get-diabetes-list/<cnes>', methods=['GET'])
def get_diabetes_list(cnes=None):
    if cnes:
        request.view_args['cnes'] = int(request.view_args['cnes'])

    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, diabetes_dashboard_get_individual_exams_count())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code
