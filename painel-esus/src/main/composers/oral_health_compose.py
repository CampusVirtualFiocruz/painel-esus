from src.data.use_cases.oral_health.oral_health_dashboard import \
    OralHealthDashboardUseCase
from src.infra.db.repositories.odonto.oral_health_dashboard_repository import \
    OralHealthDashboardRepository
from src.presentations.controllers.oral_health import OralHealthGetAllCaresByPlaceController
from src.presentations.controllers.oral_health import OralHealthGetCaresByAgeRangeController
from src.presentations.controllers.oral_health import OralHealthGetCaresByGenderController
from src.presentations.controllers.oral_health import OralHealthGetCaresByLineOfServicesController
from src.presentations.controllers.oral_health import OralHealthGetCaresByOutcomeController
from src.presentations.controllers.oral_health import OralHealthGetCaresByPlaceController
from src.presentations.controllers.oral_health import OralHealthGetCaresByTypeOfServicesController
from src.presentations.controllers.oral_health import OralHealthGetExtractionProceduresProportionController
from src.presentations.controllers.oral_health import OralHealthGetTotalController


def oral_health_dashboard_get_total():
    repository = OralHealthDashboardRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetTotalController(use_case)

    return controller.handle


def oral_health_dashboard_get_cares_by_line_of_services():
    repository = OralHealthDashboardRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetCaresByLineOfServicesController(use_case)

    return controller.handle


def oral_health_dashboard_get_cares_by_type_of_services():
    repository = OralHealthDashboardRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetCaresByTypeOfServicesController(use_case)

    return controller.handle


def oral_health_get_extraction_procedures_proportion():
    repository = OralHealthDashboardRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetExtractionProceduresProportionController(
        use_case)

    return controller.handle


def oral_health_get_cares_by_age_range():
    repository = OralHealthDashboardRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetCaresByAgeRangeController(use_case)

    return controller.handle


def oral_health_get_cares_by_gender():
    repository = OralHealthDashboardRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetCaresByGenderController(use_case)

    return controller.handle


def oral_health_get_cares_by_outcome():
    repository = OralHealthDashboardRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetCaresByOutcomeController(use_case)

    return controller.handle


def oral_health_get_cares_by_place():
    repository = OralHealthDashboardRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetCaresByPlaceController(use_case)

    return controller.handle


def oral_health_get_all_cares_by_place():
    repository = OralHealthDashboardRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetAllCaresByPlaceController(use_case)

    return controller.handle
