import io

from flask import Blueprint, Response, jsonify, request
from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.elderly_composer import (
    elderly_acs_visits_composer,
    elderly_by_gender_composer,
    elderly_by_race_composer,
    elderly_creatinine_composer,
    elderly_dentist_appointment_composer,
    elderly_get_nominal_list_composer,
    elderly_get_nominal_list_download_composer,
    elderly_height_records_composer,
    elderly_influenza_vaccines_composer,
    elderly_ivcf_20_composer,
    elderly_medical_appointment_composer,
    elderly_total_card_composer,
    elderly_total_medical_cares_composer,
    elderly_total_ubs_composer,
)
from src.main.server.decorators.token_required import extract_token

elderly_bp = Blueprint('elderly', __name__)


class ElderlyPath:
    root_path = '/v1/elderly'
    urls = {
        'root': '',
        'total_card': '/total-card',
        'total_ubs': '/total-ubs',
        'total_medical_cares': '/total-medical-cares',
        'by_gender': '/by-gender',
        'by_race': '/by-race',
        'two_medical_appointments': '/two-medical-appointments',
        'two_height_records': '/two-height-records',
        'two_acs_visits': '/two-acs-visits',
        'creatinine': '/creatinine',
        'influenza_vaccines': '/influenza-vaccines',
        'dentist_appointment': '/dentist-appointment',
        'ivcf_20': '/ivcf-20',
        'get_nominal_list': '/get-nominal-list' ,      
        'get_nominal_list_download': '/get-nominal-list/download' ,   
    }


elderly = ElderlyPath()
urls = elderly.urls

@elderly_bp.route(urls['total_ubs'], methods=['GET'], endpoint='elderly_total_ubs')
@elderly_bp.route(
    urls['total_ubs'] + '/<cnes>', methods=['GET'], endpoint='elderly_total_ubs_id'
)
def elderly_total_ubs(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_total_ubs_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        response = jsonify(http_response.body)

    return response, http_response.status_code

@elderly_bp.route(urls['total_card'], methods=['GET'], endpoint='elderly_total_card')
@elderly_bp.route(
    urls['total_card'] + '/<cnes>', methods=['GET'], endpoint='elderly_total_card_id'
)
def elderly_total_card(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_total_card_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        response = jsonify(http_response.body)

    return response, http_response.status_code


@elderly_bp.route(urls['total_medical_cares'], methods=['GET'], endpoint='elderly_total_medical_cares')
@elderly_bp.route(
    urls['total_medical_cares'] + '/<cnes>', methods=['GET'], endpoint='elderly_total_medical_cares_id'
)
def elderly_total_cares(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_total_medical_cares_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        response = jsonify(http_response.body)

    return response, http_response.status_code

@elderly_bp.route(urls['by_gender'], methods=['GET'], endpoint='elderly_by_gender')
@elderly_bp.route(
    urls['by_gender'] + '/<cnes>', methods=['GET'], endpoint='elderly_by_gender_id'
)
def elderly_by_gender(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_by_gender_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        response = jsonify(http_response.body)

    return response, http_response.status_code

@elderly_bp.route(urls['by_race'], methods=['GET'], endpoint='elderly_by_race')
@elderly_bp.route(
    urls['by_race'] + '/<cnes>', methods=['GET'], endpoint='elderly_by_race_id'
)
def elderly_by_race(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_by_race_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        response = jsonify(http_response.body)

    return response, http_response.status_code

@elderly_bp.route(urls['two_medical_appointments'], methods=['GET'], endpoint='elderly_medical_appointment')
@elderly_bp.route(
    urls['two_medical_appointments'] + '/<cnes>', methods=['GET'], endpoint='elderly_medical_appointment_id'
)
def elderly_medical_appointment(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_medical_appointment_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        response = jsonify(http_response.body)

    return response, http_response.status_code

@elderly_bp.route(urls['two_height_records'], methods=['GET'], endpoint='elderly_height_records')
@elderly_bp.route(
    urls['two_height_records'] + '/<cnes>', methods=['GET'], endpoint='elderly_height_records_id'
)
def elderly_height_records(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_height_records_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        response = jsonify(http_response.body)

    return response, http_response.status_code

@elderly_bp.route(urls['two_acs_visits'], methods=['GET'], endpoint='elderly_acs_visits')
@elderly_bp.route(
    urls['two_acs_visits'] + '/<cnes>', methods=['GET'], endpoint='elderly_acs_visits_id'
)
def elderly_acs_visits(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_acs_visits_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        response = jsonify(http_response.body)

    return response, http_response.status_code

@elderly_bp.route(urls['creatinine'], methods=['GET'], endpoint='elderly_creatinine')
@elderly_bp.route(
    urls['creatinine'] + '/<cnes>', methods=['GET'], endpoint='elderly_creatinine_id'
)
def elderly_creatinine(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_creatinine_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        response = jsonify(http_response.body)

    return response, http_response.status_code

@elderly_bp.route(urls['influenza_vaccines'], methods=['GET'], endpoint='elderly_influenza_vaccines')
@elderly_bp.route(
    urls['influenza_vaccines'] + '/<cnes>', methods=['GET'], endpoint='elderly_influenza_vaccines_id'
)
def elderly_influenza_vaccines(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_influenza_vaccines_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        response = jsonify(http_response.body)

    return response, http_response.status_code

@elderly_bp.route(urls['dentist_appointment'], methods=['GET'], endpoint='elderly_dentist_appointment')
@elderly_bp.route(
    urls['dentist_appointment'] + '/<cnes>', methods=['GET'], endpoint='elderly_dentist_appointment_id'
)
def elderly_dentist_appointment(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_dentist_appointment_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        response = jsonify(http_response.body)

    return response, http_response.status_code

@elderly_bp.route(urls['ivcf_20'], methods=['GET'], endpoint='elderly_ivcf_20')
@elderly_bp.route(
    urls['ivcf_20'] + '/<cnes>', methods=['GET'], endpoint='elderly_ivcf_20_id'
)
def elderly_ivcf_20(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_ivcf_20_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        response = jsonify(http_response.body)

    return response, http_response.status_code

@elderly_bp.route(urls['get_nominal_list'], methods=['GET'], endpoint='elderly_get_nominal_list')
@elderly_bp.route(
    urls['get_nominal_list'] + '/<cnes>', methods=['GET'], endpoint='elderly_get_nominal_list_id'
)
def elderly_get_nominal_list(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, elderly_get_nominal_list_composer())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        response = jsonify(http_response.body)

    return response, http_response.status_code

@elderly_bp.route(urls['get_nominal_list_download'], methods=['GET'], endpoint='elderly_get_nominal_list_download')
@elderly_bp.route(
    urls['get_nominal_list_download'] + '/<cnes>', methods=['GET'], endpoint='elderly_get_nominal_list_download_id'
)
def elderly_get_nominal_list_download(cnes=None):
    if cnes:
        request.view_args["cnes"] = int(request.view_args["cnes"])

    http_response = None
    response = None

    try:
        response = request_adapter(request, elderly_get_nominal_list_download_composer())
        buffer = io.BytesIO()
        response.to_excel(buffer)

        headers = {
            "Content-Disposition": "attachment; filename=lista_nominal.xlsx",
            "Content-type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        }
        return Response(
            buffer.getvalue(),
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers=headers,
        )

    except Exception as exception:
        http_response = handle_errors(exception, extract_token(request.headers.get("Authorization")))
        response = jsonify(http_response.body)

    return response, 200
