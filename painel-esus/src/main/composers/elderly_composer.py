from src.infra.db.repositories.elderly.elderly_repository import ElderlyRepository
from src.presentations.controllers.elderly.elderly_controller import ElderlyController

repository = ElderlyRepository()
controller = ElderlyController(repository)

def elderly_total_composer():
    return controller.total

def elderly_group_by_age_location_composer():
    return controller.grouping_by_ages_location

def elderly_group_by_race_composer():
    return controller.grouping_by_race

def elderly_group_by_gender_composer():
    return controller.grouping_by_gender

def elderly_imc_rate_composer():
    return controller.grouping_imc_rate

def elderly_influenza_rate_composer():
    return controller.grouping_influenza_rate

def elderly_odonto_rate_composer():
    return controller.grouping_odonto_rate

def elderly_hipertesnion_diabetes_rate_composer():
    return controller.grouping_total_disease_related


def elderly_get_nominal_list():
    return controller.get_nominal_list
