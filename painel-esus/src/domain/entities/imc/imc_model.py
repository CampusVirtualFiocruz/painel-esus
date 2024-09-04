from typing import List

from src.errors import InvalidIMC

from .high_weight import IMCHeighWeight
from .imc import IMC
from .low_weight import IMCLowWeight
from .normal import IMCNormal
from .obesity import IMCObesity
from .others import IMCOthers


class ImcModel():

    def __init__(self):
        self.list = [
            IMCLowWeight(),
            IMCNormal(),
            IMCHeighWeight(),
            IMCObesity(),
        ]
        self.other = IMCOthers()

    def check_presence(self, weight, height):
        errors = set()
        for imc_item in self.list:
            try:
                imc_item.check_presence(weight, height)
            except (InvalidIMC, ZeroDivisionError):
                if (weight, height) not in errors:
                    errors.add((weight, height))
                    self.other.total += 1

    def get_list(self) -> List[IMC]:
        return self.list
