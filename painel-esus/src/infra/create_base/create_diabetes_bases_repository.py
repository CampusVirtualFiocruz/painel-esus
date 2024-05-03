from src.domain.entities.diabetes import Diabetes
from src.infra.create_base.create_base_repository import CreateBasesRepository


class CreateDiabetesBasesRepository(CreateBasesRepository):
    _base = 'diabetes'

    def __init__(self) -> None:
        super().__init__(Diabetes())
