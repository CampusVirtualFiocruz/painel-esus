import pytest
from src.errors import NoSuchTableError
from src.infra.create_base.create_diabetes_bases_repository import \
    CreateDiabetesBasesRepository
from src.infra.db.repositories.update_bases import UpdateBasesRepository


def test_create_diabetes_base_no_base_exists():
    diabetes_base = CreateDiabetesBasesRepository()
    update_base = UpdateBasesRepository()
    try:
        diabetes_base.destroy_base()
        update_base.check_table_exists(base_table=diabetes_base.get_base())
    except NoSuchTableError:
        pass

    with pytest.raises(NoSuchTableError):
        diabetes_base.destroy_base()

    with pytest.raises(NoSuchTableError):
        update_base.check_table_exists(
            base_table=diabetes_base.get_base())


def test_create_diabetes_base():
    diabetes_base = CreateDiabetesBasesRepository()
    diabetes_base.create_base()

    update_base = UpdateBasesRepository()
    result = update_base.check_bases(
        base_table=diabetes_base.get_base())
    assert result.shape[0] > 0
