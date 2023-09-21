from pprint import pprint

from src.presentations.validators.dashboard_validator import (
    age_group_gender_validator, age_group_location_validator,
    hypertension_complications, professionals_count)

from .hypertension_dashboard import HypertensionDashboardRepository


def test_get_age_groups_location():
    repo = HypertensionDashboardRepository()
    response = repo.get_age_groups_location()
    assert age_group_location_validator(response)


def test_get_age_groups_gender():
    repo = HypertensionDashboardRepository()
    response = repo.get_age_group_gender()
    assert age_group_gender_validator(response)


def test_professionals_count():
    repo = HypertensionDashboardRepository()
    response = repo.get_professionals_count()
    assert professionals_count({'data': response})
    pprint(response, indent=4)


def test_get_complications():
    repo = HypertensionDashboardRepository()
    response = repo.get_complications()
    pprint(response, indent=4)
    assert hypertension_complications({'data': response})


def test_get_exams_count():
    repo = HypertensionDashboardRepository()
    response = repo.get_exams_count()
    pprint(response, indent=4)


def test_get_imc():
    repo = HypertensionDashboardRepository()
    response = repo.get_imc()
    pprint(response, indent=4)
