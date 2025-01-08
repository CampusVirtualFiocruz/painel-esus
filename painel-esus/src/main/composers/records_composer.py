from src.infra.db.repositories.cadastro.records_repository import RecordsRepository
from src.presentations.controllers.cadastros.records_controller import RecordsController

repository = RecordsRepository()
controller = RecordsController(repository)

def get_total_group_composer():
    return controller.get_total_group

def get_cpf_cns_rate():
    return controller.get_cpf_cns_rate

def group_localidade():
    return controller.group_localidade

def group_raca_cor():
    return controller.group_raca_cor

def group_records_by_origin():
    return controller.group_records_by_origin

def group_records_status():
    return controller.group_records_status


def nominal_list():
    return controller.nominal_list


def nominal_list_download():
    return controller.nominal_list_download

def people_who_get_care():
    return controller.people_who_get_care
