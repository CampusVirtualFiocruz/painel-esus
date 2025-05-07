import duckdb

from src.data.use_cases.oral_health.oral_health_use_case import (
    OralHealthDashboardUseCase,
)
from src.infra.db.repositories.oral_health.oral_health_repository import (
    OralHealthRepository,
)
from src.presentations.controllers.oral_health import (
    OralHealthGetCaresByGenderController,
)
from src.presentations.controllers.oral_health.oral_health_get_atraumatic_treatment import (
    OralHealthGetAtraumaticTreatmentController,
)
from src.presentations.controllers.oral_health.oral_health_get_cares_by_race import (
    OralHealthGetCaresByRaceController,
)
from src.presentations.controllers.oral_health.oral_health_get_conclued_treatment import (
    OralHealthGetConcluedTreatmentController,
)
from src.presentations.controllers.oral_health.oral_health_get_extraction import (
    OralHealthGetExtractionController,
)
from src.presentations.controllers.oral_health.oral_health_get_first_appointment import (
    OralHealthGetFirstAppointmentController,
)
from src.presentations.controllers.oral_health.oral_health_get_prevention_procedures import (
    OralHealthGetPreventionProceduresController,
)
from src.presentations.controllers.oral_health.oral_health_get_supervised_brushing import (
    OralHealthGetSupervisedBrushingController,
)


def oral_health_get_extraction():
    session = duckdb.connect()
    repository = OralHealthRepository(session)
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetExtractionController(use_case)

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


def oral_health_get_first_appointment():
    session = duckdb.connect()
    repository = OralHealthRepository(session)
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetFirstAppointmentController(use_case)

    return controller.handle


def oral_health_get_conclued_treatment():
    session = duckdb.connect()
    repository = OralHealthRepository(session)
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetConcluedTreatmentController(use_case)

    return controller.handle


def oral_health_get_prevention_procedures():
    session = duckdb.connect()
    repository = OralHealthRepository(session)
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetPreventionProceduresController(use_case)

    return controller.handle


def oral_health_get_supervised_brushing():
    session = duckdb.connect()
    repository = OralHealthRepository(session)
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetSupervisedBrushingController(use_case)

    return controller.handle


def oral_health_get_atraumatic_treatment():
    session = duckdb.connect()
    repository = OralHealthRepository(session)
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetAtraumaticTreatmentController(use_case)

    return controller.handle
