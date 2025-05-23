from src.data.interfaces.oral_health_dashboard_repository import (
    OralHealthDashboardRepositoryInterface,
)
from src.domain.use_cases.oral_health_dashboard_use_case import (
    OralHealthDashboardUseCaseInterface,
)
from src.errors import InvalidArgument


class OralHealthDashboardUseCase(OralHealthDashboardUseCaseInterface):

    def __init__(self, _repository: OralHealthDashboardRepositoryInterface):
        self._repository = _repository

    def get_oral_health_total(self, cnes: int = None, equipe: int = None):
        self.__valid_cnes(cnes)
        response = self._repository.total_ubs(cnes, equipe)
        return response
    
    def get_oral_health_extraction(
        self, cnes: int = None, equipe: int = None, category: str = None
    ):
        self.__valid_cnes(cnes)
        response = self._repository.get_oral_health_extraction(cnes, equipe, category)
        return response

    def get_oral_health_cares_by_gender(
        self, cnes: int = None, equipe: int = None, category: str = None
    ):
        self.__valid_cnes(cnes)
        response = self._repository.get_oral_health_cares_by_gender(
            cnes, equipe, category
        )
        return response

    def get_oral_health_cares_by_race(
        self, cnes: int = None, equipe: int = None, category: str = None
    ):
        self.__valid_cnes(cnes)
        response = self._repository.get_oral_health_cares_by_race(
            cnes, equipe, category
        )
        return response

    def get_oral_health_first_appointment(
        self, cnes: int = None, equipe: int = None, category: str = None
    ):
        self.__valid_cnes(cnes)
        response = self._repository.get_oral_health_first_appointment(
            cnes, equipe, category
        )
        return response

    def get_oral_health_conclued_treatment(
        self, cnes: int = None, equipe: int = None, category: str = None
    ):
        self.__valid_cnes(cnes)
        response = self._repository.get_oral_health_conclued_treatment(
            cnes, equipe, category
        )
        return response

    def oral_health_get_supervised_brushing(
        self, cnes=None, equipe=None, category: str = None
    ):
        self.__valid_cnes(cnes)
        response = self._repository.oral_health_get_supervised_brushing(
            cnes, equipe, category
        )
        return response

    def get_oral_health_prevention_procedures(
        self, cnes=None, equipe=None, category: str = None
    ):
        self.__valid_cnes(cnes)
        response = self._repository.get_oral_health_prevention_procedures(
            cnes, equipe, category
        )
        return response

    def oral_health_get_atraumatic_treatment(
        self, cnes=None, equipe=None, category: str = None
    ):
        self.__valid_cnes(cnes)
        response = self._repository.oral_health_get_atraumatic_treatment(
            cnes, equipe, category
        )
        return response
    
    def donwload_nominal_list(
        self, cnes=None, equipe=None, category: str = None
    ):
        self.__valid_cnes(cnes)
        response = self._repository.donwload_nominal_list(
            cnes, equipe, category
        )
        return response
    
    def find_filter_nominal(
        self,
        cnes: int,
        page: int = 0,
        pagesize: int = 10,
        nome: str = None,
        cpf: str = None,
        equipe: int = None,
        query: str = None,
        sort=[],
        category: str = 'atendidas'
    ):
        self.__valid_cnes(cnes)
        response = self._repository.find_filter_nominal(
            cnes,
            page,
            pagesize,
            nome,
            cpf,
            equipe,
            query,
            sort,
            category
        )
        return response

    def __valid_cnes(self, cnes):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
