from src.infra.db.repositories.children.children_repository import ChildrenRepository
from src.presentations.controllers.children.children_controller import (
    ChildrenController,
)

repository = ChildrenRepository()
controller = ChildrenController(repository)

def children_total_composer():
    return controller.total

def children_grouping_by_ages_location_composer():
    return controller.grouping_by_ages_location

def children_grouping_by_race_composer():
    return controller.grouping_by_race

def children_grouping_by_gender_composer():
    return controller.grouping_by_gender

def children_grouping_by_location_rate_composer():
    return controller.grouping_by_location_rate

def children_grouping_cares_by_professionals_composer():
    return controller.grouping_cares_by_professionals

def children_get_nominal_list():
    return controller.get_nominal_list

def children_get_nominal_list_download():
    return controller.get_nominal_list_download
