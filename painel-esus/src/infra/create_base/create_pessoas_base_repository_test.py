from .create_pessoas_base_repository import CreateStatusRecordsRepository


def test_create_status():
    repo = CreateStatusRecordsRepository()
    repo.create_base()