from flask import Blueprint
from src.main.composers.demographic_composer import (
    get_age_groups_composer,
    get_child_by_location_area_composer,
    get_diabetes_by_location_area_composer,
    get_elderly_by_location_area_composer,
    get_gender_composer,
    get_hypertension_by_location_area_composer,
    get_ibge_population_composer,
    get_location_area_composer,
    get_total_people_composer,
)
from src.main.server.cache import cache

from .utils import handle_request

demographics_bp = Blueprint("demographics", __name__)


class DemographicPath:
    root_path = "/v1/demographic"
    urls = {
        "age_groups": "/age-groups",
        "gender": "/gender",
        "ibge_population": "/ibge-population",
        "location_area": "/location-area",
        "diabetes_by_location_area": "/location-area/diabetes",
        "hypertension_by_location_area": "/location-area/hypertension",
        "child_by_location_area": "/location-area/child",
        "elderly_by_location_area": "/location-area/elderly",
        "total_people": "/total-people",
    }


demographics = DemographicPath()
URLS = demographics.urls
ROOT = demographics.root_path


# Age groups
@demographics_bp.route(
    f"{ROOT}{URLS['age_groups']}", methods=["GET"], endpoint="age_groups"
)
@demographics_bp.route(
    f"{ROOT}{URLS['age_groups']}/<int:cnes>", methods=["GET"], endpoint="age_groups_id"
)
@cache.cached(query_string=True)
def get_age_groups(cnes=None):
    return handle_request(get_age_groups_composer, cnes=cnes)


# Gender
@demographics_bp.route(f"{ROOT}{URLS['gender']}", methods=["GET"], endpoint="gender")
@demographics_bp.route(
    f"{ROOT}{URLS['gender']}/<int:cnes>", methods=["GET"], endpoint="gender_id"
)
@cache.cached(query_string=True)
def get_gender(cnes=None):
    return handle_request(get_gender_composer, cnes=cnes)


# IBGE Population
@demographics_bp.route(
    f"{ROOT}{URLS['ibge_population']}", methods=["GET"], endpoint="ibge_population"
)
@demographics_bp.route(
    f"{ROOT}{URLS['ibge_population']}/<int:cnes>",
    methods=["GET"],
    endpoint="ibge_population_id",
)
@cache.cached(query_string=True)
def get_ibge_population(cnes=None):
    return handle_request(get_ibge_population_composer, cnes=cnes)


# Location Area
@demographics_bp.route(
    f"{ROOT}{URLS['location_area']}", methods=["GET"], endpoint="location_area"
)
@demographics_bp.route(
    f"{ROOT}{URLS['location_area']}/<int:cnes>",
    methods=["GET"],
    endpoint="location_area_id",
)
@cache.cached(query_string=True)
def get_location_area(cnes=None):
    return handle_request(get_location_area_composer, cnes=cnes)


# Location Area Filters
@demographics_bp.route(
    f"{ROOT}{URLS['diabetes_by_location_area']}",
    methods=["GET"],
    endpoint="diabetes_by_location_area",
)
@demographics_bp.route(
    f"{ROOT}{URLS['diabetes_by_location_area']}/<int:cnes>",
    methods=["GET"],
    endpoint="diabetes_by_location_area_id",
)
@cache.cached(query_string=True)
def get_diabetes_by_location_area(cnes=None):
    return handle_request(get_diabetes_by_location_area_composer, cnes=cnes)


@demographics_bp.route(
    f"{ROOT}{URLS['hypertension_by_location_area']}",
    methods=["GET"],
    endpoint="hypertension_by_location_area",
)
@demographics_bp.route(
    f"{ROOT}{URLS['hypertension_by_location_area']}/<int:cnes>",
    methods=["GET"],
    endpoint="hypertension_by_location_area_id",
)
@cache.cached(query_string=True)
def get_hypertension_by_location_area(cnes=None):
    return handle_request(get_hypertension_by_location_area_composer, cnes=cnes)


@demographics_bp.route(
    f"{ROOT}{URLS['child_by_location_area']}",
    methods=["GET"],
    endpoint="child_by_location_area",
)
@cache.cached(query_string=True)
def get_child_by_location_area():
    return handle_request(get_child_by_location_area_composer)


@demographics_bp.route(
    f"{ROOT}{URLS['elderly_by_location_area']}",
    methods=["GET"],
    endpoint="elderly_by_location_area",
)
@cache.cached(query_string=True)
def get_elderly_by_location_area():
    return handle_request(get_elderly_by_location_area_composer)


# Total people
@demographics_bp.route(
    f"{ROOT}{URLS['total_people']}", methods=["GET"], endpoint="total_people"
)
@demographics_bp.route(
    f"{ROOT}{URLS['total_people']}/<int:cnes>",
    methods=["GET"],
    endpoint="total_people_id",
)
@cache.cached(query_string=True)
def get_total_people(cnes=None):
    return handle_request(get_total_people_composer, cnes=cnes)
