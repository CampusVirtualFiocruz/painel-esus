from src.infra.db.repositories.hypertension_diabetes.hypertension_diabetes_repository import (
    HypertensionDiabetesRepository,
)
from src.presentations.controllers.hypertension.hypertension_controller import (
    HypertensionController,
)

repository = HypertensionDiabetesRepository('hipertensao')

def hypertension_dashboard_get_total():

    controller = HypertensionController(repository)

    return controller.get_total


def hypertension_dashboard_get_age_group_gender():
    controller = HypertensionController(repository)

    return controller.get_by_gender


def hypertension_dashboard_get_complications():
    controller = HypertensionController(repository)

    return controller.get_complications


def hypertension_dashboard_get_exams_count():
    controller = HypertensionController(repository)

    return controller.get_exams_table


def hypertension_dashboard_get_imc():
    controller = HypertensionController(repository)

    return controller.get_imc


def hypertension_dashboard_get_by_race():
    controller = HypertensionController(repository)

    return controller.get_by_race


def hypertension_dashboard_get_nominal_list():
    controller = HypertensionController(repository)
    return controller.get_nominal_list
    


def hypertension_dashboard_get_nominal_list_download():
    controller = HypertensionController(repository)
    return controller.get_nominal_list_download
    