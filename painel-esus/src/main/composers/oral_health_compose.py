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
from src.presentations.controllers.oral_health.oral_health_nominal_list import (
    OralHealthNominalListController,
)
from src.presentations.controllers.oral_health.oral_health_total import (
    OralHealthTotalController,
)


def oral_health_get_extraction():
    repository = OralHealthRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetExtractionController(use_case)

    return controller.handle


def oral_health_get_cares_by_gender():
    repository = OralHealthRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetCaresByGenderController(use_case)

    return controller.handle


def oral_health_get_cares_by_race():
    repository = OralHealthRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetCaresByRaceController(use_case)

    return controller.handle


def oral_health_get_first_appointment():
    repository = OralHealthRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetFirstAppointmentController(use_case)

    return controller.handle


def oral_health_get_conclued_treatment():
    repository = OralHealthRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetConcluedTreatmentController(use_case)

    return controller.handle


def oral_health_get_prevention_procedures():
    repository = OralHealthRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetPreventionProceduresController(use_case)

    return controller.handle


def oral_health_get_supervised_brushing():
    repository = OralHealthRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetSupervisedBrushingController(use_case)

    return controller.handle


def oral_health_get_atraumatic_treatment():
    repository = OralHealthRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthGetAtraumaticTreatmentController(use_case)

    return controller.handle

def oral_health_get_nominal_list():
    repository = OralHealthRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthNominalListController(use_case)
    return controller.handle

def oral_health_get_total():
    repository = OralHealthRepository()
    use_case = OralHealthDashboardUseCase(repository)
    controller = OralHealthTotalController(use_case)
    return controller.handle
