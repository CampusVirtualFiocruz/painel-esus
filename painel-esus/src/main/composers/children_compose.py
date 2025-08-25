from src.domain.use_cases.children.children_use_case_impl import ChildrenUseCaseImpl
from src.infra.db.repositories.children.children_repository import ChildrenRepository
from src.presentations.controllers.children.children_controller import (
    ChildrenController,
)

_repository = ChildrenRepository()
_use_case = ChildrenUseCaseImpl(_repository)
_controller = ChildrenController(_use_case, _repository)


def children_get_total():
    return _controller.get_total


def children_get_total_twelve_months():
    return _controller.get_total_twelve_months


def children_by_age():
    return _controller.get_by_age


def children_by_race():
    return _controller.get_by_race


def children_total_medical_cares_composer():
    return _controller.total_medical_cares


def children_first_consult_8d():
    return _controller.get_first_consult_8d


def children_appointments_until_2_years():
    return _controller.get_appointments_until_2_years


def children_acs_visit_until_30d():
    return _controller.get_acs_visit_until_30d


def children_acs_visit_until_6m():
    return _controller.get_acs_visit_until_6m


def children_dental_appointments_until_12m():
    return _controller.get_dental_appointments_until_12m


def children_dental_appointments_until_24m():
    return _controller.get_dental_appointments_until_24m


def children_high_weight_records():
    return _controller.get_high_weight_records


def children_milestone():
    return _controller.get_milestone


def children_evaluated_feeding():
    return _controller.get_evaluated_feeding


def children_get_nominal_list():
    return _controller.get_nominal_list


def children_get_nominal_list_download():
    return _controller.get_nominal_list_download
