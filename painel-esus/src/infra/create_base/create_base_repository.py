from sqlalchemy.exc import OperationalError, ResourceClosedError
from src.data.interfaces.create_bases.create_bases_repository import \
    CreateBasesRepositoryInterface
from src.domain.entities.disease import Disease
from src.errors import InvalidArgument, NoSuchTableError
from src.infra.db.repositories.disease.diseases_dashboard import \
    DiseasesDashboardRepository
from src.infra.db.repositories.update_bases import UpdateBasesRepository

from ...domain.entities.disease import Disease


class CreateBasesRepository(CreateBasesRepositoryInterface):
    _base = None

    def __init__(self, disease: Disease = None) -> None:
        self.__disease = disease

    def get_base(self):
        return self._base

    def create_base(self):
        if self._base is None:
            raise InvalidArgument('Creation base not passed.')
        if self.__disease is None:
            raise InvalidArgument('Disease instance not passed.')
        hypertension_repository = DiseasesDashboardRepository(self.__disease)
        cares = hypertension_repository.update_bases()
        update_base_repository = UpdateBasesRepository()
        update_base_repository.update_bases(cares, self._base)

    def destroy_base(self):
        if self._base is None:
            raise InvalidArgument('Creation base not passed.')
        try:
            update_base_repository = UpdateBasesRepository()
            update_base_repository.destroy_bases(self._base)
        except (OperationalError, ResourceClosedError) as exc:
            raise NoSuchTableError(
                f'No {self.get_base()} table found') from exc
