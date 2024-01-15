from typing import Dict
import pytest
from src.data.interfaces.demographics_info import DemographicsInfoRepository

class DemographicsInfoRepositoryStub(DemographicsInfoRepository):

    def get_demographics_info(self, cnes: int = None) -> Dict:
        return {
                    "total":12325,
                    "ageGroups":{
                        "Feminino":{
                            "0 a 5 anos":{
                                "Rural":5,
                                "Urbano":11
                            },
                            "6 a 12 anos":{
                                "Rural":2,
                                "Urbano":7
                            },
                            "13 a 17 anos":{
                                "Rural":1,
                                "Urbano":12
                            },
                            "18 a 29 anos":{
                                "Rural":110,
                                "Urbano":935
                            },
                            "30 a 44 anos":{
                                "Rural":336,
                                "Urbano":2970
                            },
                            "45 a 59 anos":{
                                "Rural":291,
                                "Urbano":2417
                            },
                            "60 + anos":{
                                "Rural":364,
                                "Urbano":1820
                            }
                        },
                        "Masculino":{
                            "0 a 5 anos":{
                                "Rural":0,
                                "Urbano":23
                            },
                            "6 a 12 anos":{
                                "Rural":0,
                                "Urbano":9
                            },
                            "13 a 17 anos":{
                                "Rural":0,
                                "Urbano":5
                            },
                            "18 a 29 anos":{
                                "Rural":31,
                                "Urbano":251
                            },
                            "30 a 44 anos":{
                                "Rural":157,
                                "Urbano":702
                            },
                            "45 a 59 anos":{
                                "Rural":140,
                                "Urbano":798
                            },
                            "60 + anos":{
                                "Rural":203,
                                "Urbano":725
                            }
                        }
                    },
                    "locationArea":{
                        "rural":1640,
                        "urbano":10685
                    },
                    "gender":{
                        "feminino":9281,
                        "masculino":3044
                    },
                    "indicators":{
                        "diabetes":{
                            "rural":25,
                            "urbano":197
                        },
                        "gestantes":{
                            "rural":16,
                            "urbano":165
                        },
                        "hipertensao":{
                            "rural":89,
                            "urbano":654
                        }
                    }
            }

@pytest.fixture
def demographics_info_mock():
    return DemographicsInfoRepositoryStub()
