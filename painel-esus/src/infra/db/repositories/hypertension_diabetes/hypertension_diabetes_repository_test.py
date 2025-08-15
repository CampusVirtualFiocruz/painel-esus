from pprint import pprint
from typing import Literal, Union

import pytest

from .hypertension_diabetes_repository import HypertensionDiabetesRepository


@pytest.fixture
def factory():
    return HypertensionDiabetesRepository("diabetes")

def test_exam_table(factory):
    table = factory.get_exams_count()
    # pprint(table)

def test_imc(factory):
    table = factory.get_imc()
    # pprint(table)


def test_complications(factory):
    table = factory.get_complications(None, None, True)
    # pprint(list(zip(table[0],table[1][0])))


def test_total(factory):
    table = factory.get_total()
    pprint(table)
