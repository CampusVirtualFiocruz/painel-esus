from unittest.mock import patch

from src.data.use_cases.demographic.get_age_groups import GetAgeGroupsUseCase
from src.data.use_cases.demographic.get_gender import GetGenderUseCase
from src.infra.db.repositories.demographic.age_groups_repository import (
    AgeGroupsRepository,
)
from src.infra.db.repositories.demographic.gender_repository import GenderRepository


def test_age_groups():
    repository = AgeGroupsRepository()
    use_case = GetAgeGroupsUseCase(repository)
    print(use_case.get_age_groups())

def test_gender():
    repository = GenderRepository()
    use_case = GetGenderUseCase(repository)

    return_value = {"feminino": 2, "indeterminado": 1, "masculino": 2, 'nao_informado': 1, None: 1}

    with patch(
        "src.infra.db.repositories.demographic.gender_repository.GenderRepository.get_gender",
        return_value=return_value
    ):
        result = use_case.get_gender(25)
        assert result['feminino'] == 2
        assert result["masculino"] == 2
        assert result["indeterminado"] == 3
