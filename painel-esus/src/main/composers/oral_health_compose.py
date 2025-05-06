from src.data.use_cases.oral_health.oral_health_dashboard import \
    OralHealthDashboardUseCase
from src.infra.db.repositories.oral_health.oral_health_repository import \
    OralHealthRepository
from src.presentations.controllers.oral_health import OralHealthGetAllCaresByPlaceController
from src.presentations.controllers.oral_health import OralHealthGetCaresByAgeRangeController
from src.presentations.controllers.oral_health import OralHealthGetCaresByGenderController
from src.presentations.controllers.oral_health import OralHealthGetCaresByLineOfServicesController
from src.presentations.controllers.oral_health import OralHealthGetCaresByOutcomeController
from src.presentations.controllers.oral_health import OralHealthGetCaresByPlaceController
from src.presentations.controllers.oral_health import OralHealthGetCaresByTypeOfServicesController
from src.presentations.controllers.oral_health import OralHealthGetExtractionProceduresProportionController
from src.presentations.controllers.oral_health import OralHealthGetTotalController

import duckdb

from src.presentations.controllers.oral_health.oral_health_get_cares_by_race import OralHealthGetCaresByRaceController


def oral_health_dashboard_get_total():
    repository = OralHealthRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetTotalController(use_case)

    return controller.handle


def oral_health_dashboard_get_cares_by_line_of_services():
    repository = OralHealthRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetCaresByLineOfServicesController(use_case)

    return controller.handle


def oral_health_dashboard_get_cares_by_type_of_services():
    repository = OralHealthRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetCaresByTypeOfServicesController(use_case)

    return controller.handle


def oral_health_get_extraction_procedures_proportion():
    repository = OralHealthRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetExtractionProceduresProportionController(
        use_case)

    return controller.handle


def oral_health_get_cares_by_age_range():
    repository = OralHealthRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetCaresByAgeRangeController(use_case)

    return controller.handle


def oral_health_get_cares_by_gender():
    session = duckdb.connect()
    repository = OralHealthRepository(session)
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetCaresByGenderController(use_case)

    return controller.handle


def oral_health_get_cares_by_race():
    session = duckdb.connect()
    repository = OralHealthRepository(session)
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetCaresByRaceController(use_case)

    return controller.handle


def oral_health_get_cares_by_outcome():
    repository = OralHealthRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetCaresByOutcomeController(use_case)

    return controller.handle


def oral_health_get_cares_by_place():
    repository = OralHealthRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetCaresByPlaceController(use_case)

    return controller.handle


def oral_health_get_all_cares_by_place():
    repository = OralHealthRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetAllCaresByPlaceController(use_case)

    return controller.handle
