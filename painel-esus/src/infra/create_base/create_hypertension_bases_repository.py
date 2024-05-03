from src.domain.entities.hypertension import Hypertension
from src.infra.create_base.create_base_repository import CreateBasesRepository


class CreateHypertensionBasesRepository(CreateBasesRepository):
    _base = 'hipertensao'

    def __init__(self) -> None:
        super().__init__(Hypertension())
