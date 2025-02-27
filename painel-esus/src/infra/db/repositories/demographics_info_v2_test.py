from pprint import pprint

from .demographics_info_v2 import DemographicsInfoV2Repository


def test_get_total():
    repo = DemographicsInfoV2Repository()
    response = repo.get_demographics_info()
    assert response["total"] == 6778
    pprint(response["ageGroups"])

def test_get_total_people():
    repo = DemographicsInfoV2Repository()
    result = repo.get_total_people()
    assert result > 0
    
    result = repo.get_total_people(26, 19)
    assert result > 0

    result = repo.get_total_people(26, 18)
    assert result == 0

def test_get_age_groups():
    repo = DemographicsInfoV2Repository()
    result = repo.get_age_groups(26, 19)
    print(result)


def test_get_by_place():
    repo = DemographicsInfoV2Repository()
    result = repo.get_by_place(26, 19)
    print(result)


def test_get_by_gender():
    repo = DemographicsInfoV2Repository()
    result = repo.get_by_gender(26, 19)
    print(result)
    assert result['feminino'] > 0
    assert result["masculino"] > 0

    result = repo.get_by_gender()
    assert result["feminino"] > 0
    assert result["masculino"] > 0

def test_get_diabetes_location():
    repo = DemographicsInfoV2Repository()
    result = repo.get_diabetes_location()
    print(result)
