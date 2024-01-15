import pytest
from src.errors import NoSuchTableError
from src.infra.create_base.create_oral_health_bases_repository import \
    CreateOralHealthBasesRepository
from src.infra.db.repositories.update_bases import UpdateBasesRepository


def test_oral_health_bases_no_base_exists():
    oral_base = CreateOralHealthBasesRepository()
    update_base = UpdateBasesRepository()
    try:
        oral_base.destroy_base()
        update_base.check_table_exists(
            base_table=oral_base.get_base())
    except NoSuchTableError:
        pass

    with pytest.raises(NoSuchTableError):
        oral_base.destroy_base()

    with pytest.raises(NoSuchTableError):
        update_base.check_bases(
            base_table=oral_base.get_base())


def test_oral_health_bases_base():
    oral_base = CreateOralHealthBasesRepository()
    oral_base.create_base()

    update_base = UpdateBasesRepository()
    result = update_base.check_bases(
        base_table=oral_base.get_base())
    assert result.shape[0] > 0
