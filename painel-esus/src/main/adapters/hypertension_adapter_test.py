from pprint import pprint

import pytest
from src.env.conf import env
from src.infra.db.repositories.hypertension_diabetes.hypertension_diabetes_repository import (
    HypertensionDiabetesRepository,
)

from .hypertension_adapter import HypertensionAdapter


@pytest.fixture
def repo_factory():
    return HypertensionDiabetesRepository('hipertensao')


@pytest.fixture
def adapter_factory():
    return HypertensionAdapter()


def test_imc(repo_factory, adapter_factory):
    lista = repo_factory.get_imc()
    result = adapter_factory.get_imc(lista)
    pprint(result)


def test_complications(repo_factory, adapter_factory):
    lista = repo_factory.get_complications(debug=True)
    result = adapter_factory.get_complications(lista)
    pprint(result)


def test_exams(repo_factory, adapter_factory):
    lista = repo_factory.get_exams_count(debug=True)
    result = adapter_factory.get_exams_count(lista)
    # pprint(result)


def test_nominal_list(repo_factory, adapter_factory):
    lista = repo_factory.get_nominal_list(cnes=25)
    pprint(lista)
