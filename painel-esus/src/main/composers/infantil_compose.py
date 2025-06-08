from src.domain.use_cases.infantil.infantil_use_case_impl import InfantilUseCaseImpl
from src.infra.db.repositories.infantil.infantil_repository import InfantilRepository
from src.presentations.controllers.infantil.infantil_controller import (
    InfantilController,
)

_repository = InfantilRepository()
_use_case = InfantilUseCaseImpl(_repository)
_controller = InfantilController(_use_case)


def infantil_get_total():
    return _controller.get_total


def infantil_by_age():
    return _controller.get_by_age
