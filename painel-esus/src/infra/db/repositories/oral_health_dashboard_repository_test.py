from src.infra.db.repositories.oral_health_dashboard_repository import OralHealthDashboardRepository


from .update_bases import UpdateBasesRepository


def test_create_database():
    repo = OralHealthDashboardRepository()
    repo.create_database()
    update_repo = UpdateBasesRepository()
    table = update_repo.check_bases('atendimento_odontologico')
    print(table.shape[0])
    assert table.shape[0] > 0
