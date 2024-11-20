from src.infra.db.repositories.children.children_repository import ChildrenRepository
from src.presentations.controllers.children.children_controller import (
    ChildrenController,
)


def children_total_composer():
    repository = ChildrenRepository()
    controller = ChildrenController(repository)

    return controller.total

def children_grouping_by_ages_location_composer():
    repository = ChildrenRepository()
    controller = ChildrenController(repository)

    return controller.grouping_by_ages_location

def children_grouping_by_race_composer():
    repository = ChildrenRepository()
    controller = ChildrenController(repository)

    return controller.grouping_by_race

def children_grouping_by_gender_composer():
    repository = ChildrenRepository()
    controller = ChildrenController(repository)

    return controller.grouping_by_gender


def children_grouping_by_location_rate_composer():
    repository = ChildrenRepository()
    controller = ChildrenController(repository)

    return controller.grouping_by_location_rate


def children_grouping_cares_by_professionals_composer():
    repository = ChildrenRepository()
    controller = ChildrenController(repository)

    return controller.grouping_cares_by_professionals
