from pprint import pprint

import pytest

from src.domain.entities.hypertension import Hypertension
from src.domain.entities.hypertension_exams import HypertensionExams
from src.presentations.validators.dashboard_validator import (
    age_group_gender_validator, age_group_location_validator,
    hypertension_complications, professionals_count)

from .diseases_dashboard import DiseasesDashboardRepository


@pytest.fixture
def hypertension_factory():
    return Hypertension()


@pytest.mark.usefixtures('hypertension_factory')
def test_get_age_groups_location(hypertension_factory):
    repo = DiseasesDashboardRepository(hypertension_factory)
    response = repo.get_age_groups_location()
    assert age_group_location_validator(response)


@pytest.mark.usefixtures('hypertension_factory')
def test_get_age_groups_gender(hypertension_factory):
    repo = DiseasesDashboardRepository(hypertension_factory)
    response = repo.get_age_group_gender()
    assert age_group_gender_validator(response)


@pytest.mark.usefixtures('hypertension_factory')
def test_professionals_count(hypertension_factory):
    repo = DiseasesDashboardRepository(hypertension_factory)
    response = repo.get_professionals_count()
    assert professionals_count({'data': response})
    pprint(response, indent=4)


@pytest.mark.usefixtures('hypertension_factory')
def test_get_complications(hypertension_factory):
    repo = DiseasesDashboardRepository(hypertension_factory)
    response = repo.get_complications()
    pprint(response, indent=4)
    assert hypertension_complications({'data': response})


@pytest.mark.usefixtures('hypertension_factory')
def test_get_exams_count(hypertension_factory):
    repo = DiseasesDashboardRepository(hypertension_factory)
    hypertension_exams = HypertensionExams()
    response = repo.get_exams_count(exam_disease=hypertension_exams)
    pprint(response, indent=4)


@pytest.mark.usefixtures('hypertension_factory')
def test_get_imc(hypertension_factory):
    repo = DiseasesDashboardRepository(hypertension_factory)
    response = repo.get_imc()
    pprint(response, indent=4)
