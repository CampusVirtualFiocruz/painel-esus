import pytest
from src.errors import NoSuchTableError
from src.infra.create_base.create_hypertension_bases_repository import \
    CreateHypertensionBasesRepository
from src.infra.db.repositories.update_bases import UpdateBasesRepository


def test_create_hypertension_base_no_base_exists():
    hypertension_base = CreateHypertensionBasesRepository()
    update_base = UpdateBasesRepository()
    try:
        hypertension_base.destroy_base()
        update_base.check_table_exists(
            base_table=hypertension_base.get_base())
    except NoSuchTableError:
        pass

    with pytest.raises(NoSuchTableError):
        hypertension_base.destroy_base()

    with pytest.raises(NoSuchTableError):
        update_base.check_table_exists(
            base_table=hypertension_base.get_base())


def test_create_hypertension_base():
    hypertension_base = CreateHypertensionBasesRepository()
    hypertension_base.create_base()

    update_base = UpdateBasesRepository()
    result = update_base.check_table_exists(
        base_table=hypertension_base.get_base())
    assert result.shape[0] > 0
