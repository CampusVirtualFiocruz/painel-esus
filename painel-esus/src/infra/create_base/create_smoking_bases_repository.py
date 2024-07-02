from sqlalchemy.exc import OperationalError
from sqlalchemy.exc import ResourceClosedError
from src.data.interfaces.create_bases.create_bases_repository import \
    CreateBasesRepositoryInterface
from src.errors import InvalidArgument
from src.errors import NoSuchTableError
from src.errors.logging import logging
from src.infra.db.repositories.smoking.smoking_repository import SmokingRepository
from src.infra.db.repositories.update_bases import UpdateBasesRepository


class CreateSmokingBasesRepository(CreateBasesRepositoryInterface):
    _base = 'atendimento_smoking'

    def __init__(self):
        ...

    def get_base(self):
        return self._base

    def create_base(self):
        if self._base is None:
            raise InvalidArgument('Creation base not passed.')
        try:
            self.destroy_base()
        except NoSuchTableError:
            logging.info(f'Crating {self._base}!')
        repo = SmokingRepository()
        repo.create_database()

    def destroy_base(self):
        if self._base is None:
            raise InvalidArgument('Creation base not passed.')
        try:
            update_base_repository = UpdateBasesRepository()
            update_base_repository.destroy_bases(self._base)
        except (OperationalError, ResourceClosedError) as exc:
            raise NoSuchTableError(
                f'No {self.get_base()} table found') from exc
