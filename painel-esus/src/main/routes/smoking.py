# pylint: disable=W0613,line-too-long
from flask import Blueprint
from flask import jsonify
from flask import request
from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.smoking_composer import followed_smoked_people_proportion
from src.main.composers.smoking_composer import (
    proportion_of_dental_consultations_among_smokers,
)
from src.main.composers.smoking_composer import risk_factors_proportion_by_dant
from src.main.composers.smoking_composer import smokers_by_age
from src.main.composers.smoking_composer import smokers_by_education
from src.main.composers.smoking_composer import smokers_by_sex
from src.main.server.cache import cache

smoking_bp = Blueprint("smoking", __name__)


class SmokingPath:
    root_path = "/v1/smoking"
    urls = {
        "followed-smoked-people-proportion": "/followed-smoked-people-proportion",
        "risk-factors-proportion-by-dant": "/risk-factors-proportion-by-dant",
        "smokers-by-age": "/smokers-by-age",
        "proportion-of-dental-consultations-among-smokers": "/proportion-of-dental-consultations-among-smokers",
        "smokers-by-sex": "/smokers-by-sex",
        "smokers-by-education": "/smokers-by-education",
    }


oral_path = SmokingPath()
urls = oral_path.urls


@smoking_bp.route(
    urls["followed-smoked-people-proportion"],
    methods=["GET"],
    endpoint="followed-smoked-people-proportion",
)
@smoking_bp.route(
    f"{urls['followed-smoked-people-proportion']}/<cnes>",
    methods=["GET"],
    endpoint="followed-smoked-people-proportion_id",
)
@cache.cached()
def smoking_followed_smoked_people_proportion(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, followed_smoked_people_proportion())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@smoking_bp.route(
    f"{urls['risk-factors-proportion-by-dant']}",
    methods=["GET"],
    endpoint="risk-factors-proportion-by-dant",
)
@smoking_bp.route(
    f"{urls['risk-factors-proportion-by-dant']}/<cnes>",
    methods=["GET"],
    endpoint="risk-factors-proportion-by-dant_id",
)
@cache.cached()
def smoking_risk_factors_proportion_by_dant(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, risk_factors_proportion_by_dant())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@smoking_bp.route(
    f"{urls['smokers-by-age']}", methods=["GET"], endpoint="smokers-by-age"
)
@smoking_bp.route(
    f"{urls['smokers-by-age']}/<cnes>", methods=["GET"], endpoint="smokers-by-age_id"
)
@cache.cached()
def smoking_smokers_by_age(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, smokers_by_age())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@smoking_bp.route(
    f"{urls['proportion-of-dental-consultations-among-smokers']}",
    methods=["GET"],
    endpoint="proportion-of-dental-consultations-among-smokers",
)
@smoking_bp.route(
    f"{urls['proportion-of-dental-consultations-among-smokers']}/<cnes>",
    methods=["GET"],
    endpoint="proportion-of-dental-consultations-among-smokers_id",
)
@cache.cached()
def smoking_proportion_of_dental_consultations_among_smokers(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(
            request, proportion_of_dental_consultations_among_smokers()
        )
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@smoking_bp.route(
    f"{urls['smokers-by-sex']}", methods=["GET"], endpoint="smokers-by-sex"
)
@smoking_bp.route(
    f"{urls['smokers-by-sex']}/<cnes>", methods=["GET"], endpoint="smokers-by-sex_id"
)
@cache.cached()
def smoking_smokers_by_sex(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, smokers_by_sex())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@smoking_bp.route(
    f"{urls['smokers-by-education']}", methods=["GET"], endpoint="smokers-by-education"
)
@smoking_bp.route(
    f"{urls['smokers-by-education']}/<cnes>",
    methods=["GET"],
    endpoint="smokers-by-education_id",
)
@cache.cached()
def smoking_smokers_by_education(cnes=None):
    http_response = None
    response = None
    try:
        http_response = request_adapter(request, smokers_by_education())
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code
