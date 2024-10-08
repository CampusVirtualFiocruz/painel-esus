from pprint import pprint

from .demographics_info_v2 import DemographicsInfoV2Repository


def test_get_total():
    repo = DemographicsInfoV2Repository()
    response = repo.get_demographics_info()
    assert response["total"] == 6778
    pprint(response["ageGroups"])
