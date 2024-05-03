# pylint: disable=E0401
from pandas import DataFrame

from .complications import (BrainStroke, CoronaryDisease, HeartAttack,
                            KidneyDisease, VascularBrainDisease)


class HypertensionComplications:
    targets = [
        HeartAttack(),
        BrainStroke(),
        KidneyDisease(),
        CoronaryDisease(),
        VascularBrainDisease(),
    ]

    def __init__(self, data_frame: DataFrame):
        self.data_frame = data_frame

    def compute_statistics(self):
        response = []
        for target in self.targets:
            result = target.filter_registers(self.data_frame.copy())
            response.append({target.label: target.statistics(result)})
        return response
