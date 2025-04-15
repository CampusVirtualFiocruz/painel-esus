from typing import Dict

from src.data.interfaces.demographic_repository import DemographicIndicatorsInterface
from src.errors import InvalidArgument

from .location_area_repository import LocationAreaRepository


class IndicatorsRepository(DemographicIndicatorsInterface):

    def __init__(self):
        self.location_area_repository = LocationAreaRepository()

    def get_indicators(
        self,
        cnes: int = None,
        equipe: int = None,
    ) -> Dict:
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")

        location_body = self.location_area_repository.get_location_area(cnes, equipe)
        diabetes = self.location_area_repository.get_diabetes_location_area(
            cnes, equipe
        )
        hypertension = self.location_area_repository.get_hypertension_location_area(
            cnes, equipe
        )

        indicators_body = {
            "diabetes": diabetes,
            "hipertensao": hypertension,
            "crianca": {"rural": 0, "urbano": 0, "nao_informado": 0},
            "idosa": {"rural": 0, "urbano": 0, "nao_informado": 0},
            "qualidade": {
                "rural": location_body.get("rural", 0),
                "urbano": location_body.get("urbano", 0),
                "nao_informado": location_body.get("nao_definido", 0),
            },
        }

        return indicators_body
