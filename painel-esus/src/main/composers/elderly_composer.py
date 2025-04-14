from src.infra.db.repositories.elderly.elderly_repository import ElderlyRepository
from src.presentations.controllers.elderly.elderly_controller import ElderlyController

repository = ElderlyRepository()
controller = ElderlyController(repository)

def elderly_ivcf_20_composer():
    return controller.ivcf_20

def elderly_dentist_appointment_composer():
    return controller.dentist_appointment

def elderly_influenza_vaccines_composer():
    return controller.influenza_vaccines

def elderly_creatinine_composer():
    return controller.creatinine

def elderly_acs_visits_composer():
    return controller.acs_visits

def elderly_height_records_composer():
    return controller.height_records

def elderly_medical_appointment_composer():
    return controller.medical_appointment

def elderly_by_race_composer():
    return controller.by_race

def elderly_by_gender_composer():
    return controller.by_gender

def elderly_total_medical_cares_composer():
    return controller.total_medical_cares

def elderly_total_ubs_composer():
    return controller.total_ubs

def elderly_total_card_composer():
    return controller.total_card

def elderly_get_nominal_list_composer():
    return controller.get_nominal_list

def elderly_get_nominal_list_download():
    return controller.get_nominal_list_download
