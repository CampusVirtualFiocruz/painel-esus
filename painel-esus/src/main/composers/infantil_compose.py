from src.domain.use_cases.infantil.infantil_use_case_impl import InfantilUseCaseImpl
from src.infra.db.repositories.infantil.infantil_repository import InfantilRepository
from src.presentations.controllers.infantil.infantil_controller import (
    InfantilController,
)


def infantil_get_total():
    repository = InfantilRepository()
    use_case = InfantilUseCaseImpl(repository)
    controller = InfantilController(use_case)
    return controller.get_total
