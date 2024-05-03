from src.infra.db.repositories.odonto.oral_health_builder_base import \
    OralHealthBuilderBaseRepository
from src.infra.db.repositories.update_bases import UpdateBasesRepository


def test_create_database():
    repo = OralHealthBuilderBaseRepository()
    repo.create_database()
    update_repo = UpdateBasesRepository()
    table = update_repo.check_bases('atendimento_odontologico')
    print(table.shape[0])
    assert table.shape[0] > 0
