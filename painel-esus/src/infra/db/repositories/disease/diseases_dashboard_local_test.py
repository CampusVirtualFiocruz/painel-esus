from src.domain.entities.hypertension import Hypertension

from .diseases_dashboard_local import DiseasesDashboardLocalRepository

hipertension = Hypertension()
repo = DiseasesDashboardLocalRepository(hipertension)

def test_total_pacientes():
    total = repo.get_total()
    print(total)

def test_get_age_groups_location():
    total = repo.get_age_groups_location(26,19)
    print(total)


def test_get_age_group_gender():
    total = repo.get_age_group_gender(26, 19)
    print(total)


def test_get_complications():
    total = repo.get_complications(26, 19)
    print(total)


def test_get_professionals_count():
    total = repo.get_professionals_count()
    print(total)


def test_get_exams_count():
    total = repo.get_exams_count()
    print(total)

def test_get_imc():
    total = repo.get_imc()
    print(total)
