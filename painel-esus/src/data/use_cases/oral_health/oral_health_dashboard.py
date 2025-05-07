from src.data.interfaces.oral_health_dashboard_repository import \
    OralHealthDashboardRepositoryInterface
from src.domain.use_cases.oral_health_dashboard_use_case import \
    OralHealthDashboardUseCaseInterface
from src.errors import InvalidArgument


class OralHealthDashboardUseCase(OralHealthDashboardUseCaseInterface):

    def __init__(self, _repository: OralHealthDashboardRepositoryInterface):
        self._repository = _repository

    def get_total(self, cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        response = self._repository.get_total(cnes)
        return response

    def get_cares_by_line_of_services(self,  cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        response = self._repository.get_cares_by_line_of_services(cnes=cnes)
        return response

    def get_cares_by_type_of_services(self,  cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        response = self._repository.get_cares_by_type_of_services(cnes)
        return response

    def get_extraction_procedures_proportion(self,  cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        response = self._repository.get_extraction_procedures_proportion(cnes)
        return response

    def get_oral_health_cares_by_age_range(self,  cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        response = self._repository.get_oral_health_cares_by_age_range(cnes)
        return response

    def get_oral_health_cares_by_gender(self,  cnes: int = None, equipe: int = None, category: str = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        response = self._repository.get_oral_health_cares_by_gender(cnes, equipe, category)
        return response

    def get_oral_health_cares_by_race(self,  cnes: int = None, equipe: int = None, category: str = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        response = self._repository.get_oral_health_cares_by_race(cnes, equipe, category)
        return response

    def get_oral_health_first_appointment(self,  cnes: int = None, equipe: int = None, category: str = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        response = self._repository.get_oral_health_first_appointment(cnes, equipe, category)
        return response

    def get_oral_health_cares_by_outcome(self,  cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        response = self._repository.get_oral_health_cares_by_outcome(cnes)
        return response

    def get_oral_health_cares_by_place(self,  cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        response = self._repository.get_oral_health_cares_by_place(cnes)
        return response

    def get_oral_health_all_cares_by_place(self, cnes: int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument('CNES must be int')
        response = self._repository.get_oral_health_all_cares_by_place(cnes)
        return response
