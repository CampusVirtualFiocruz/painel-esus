from pprint import pprint

from src.data.use_cases.smoking.smoking_use_case import SmokingUseCase
from src.infra.db.repositories.smoking.smoking_repository import \
    SmokingRepository
from src.presentations.controllers.smoking import FollowedSmokedPeopleProportionController


def test_followed_smoked_people_proportion():
    repository = SmokingRepository()
    use_case = SmokingUseCase(repository)
    controller = FollowedSmokedPeopleProportionController(use_case)

    response = controller.action()
    response = {"data": response.to_dict(orient='records')}

    pprint(response, indent=4)
