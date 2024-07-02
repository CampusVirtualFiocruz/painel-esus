from src.infra.db.repositories.smoking.smoking_repository import SmokingRepository


def test_create_base():
    repo = SmokingRepository()
    data = repo.create_database()
    print(data.head())
