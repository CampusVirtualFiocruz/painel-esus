# pylint: disable=R1718,C0301
from src.domain.entities.disease import Disease


class Cancer(Disease):
    def __init__(self):
        super().__init__()
        self.name = "Cardiopatias reumáticas crônicas"
        self.target = list(
            set([f'C{str(i).rjust(2,"0")}' for i in range(0, 90)]))


class ChronicRheumaticHeartDiseases(Disease):
    def __init__(self):
        super().__init__()
        self.name = "Cardiopatias reumáticas crônicas"
        self.target = list(set([f"I0{i}" for i in range(5, 10)]))


class HypertensiveDiseases(Disease):
    def __init__(self):
        super().__init__()
        self.name = "Doenças hipertensivas"
        self.target = list(set([f"I{i}" for i in range(10, 16)]))


class IschemicHheartDisease(Disease):
    def __init__(self):
        super().__init__()
        self.name = "Cardiopatias isquêmicas"
        self.target = list(set([f"I{i}" for i in range(20, 26)]))


class PulmonaryHeartDisease(Disease):
    def __init__(self):
        super().__init__()
        self.name = "Cardiopatias pulmonares e doenças da circulação pulmonar"
        self.target = list(
            set(
                [[f"I{i}" for i in range(26, 29)]],
            )
        )


class OtherFormsOfHeartDisease(Disease):
    def __init__(self):
        super().__init__()
        self.name = "Outras formas de doença cardíaca"
        self.target = list(
            set(
                [f"I{i}" for i in range(30, 52)],
            )
        )


class CerebrovascularDiseases(Disease):
    def __init__(self):
        super().__init__()
        self.name = "Doenças cerebrovasculares"
        self.target = list(
            set(
                [f"I{i}" for i in range(60, 70)],
            )
        )


class DiseasesOfTheVeins(Disease):
    def __init__(self):
        super().__init__()
        self.name = "Doenças das veias, dos vasos linfáticos e dos gânglios linfáticos, não classificadas noutra posição"
        self.target = list(
            set(
                [f"I{i}" for i in range(80, 90)],
            )
        )


class OtherUnspecifiedDisorders(Disease):
    def __init__(self):
        super().__init__()
        self.name = "Outras afecções não especificadas do aparelho circulatório"
        self.target = list(
            set(
                [f"I{i}" for i in range(80, 90)],
            )
        )


class ChronicDiseasesOfTheLowerRespiratorySystem(Disease):
    def __init__(self):
        super().__init__()
        self.name = "Doenças crônicas do aparelho respiratório inferior"
        self.target = list(
            set(
                [f"J{i}" for i in range(40, 48)],
            )
        )


class LungDiseasesDueToExternalAgents(Disease):
    def __init__(self):
        super().__init__()
        self.name = "Doenças pulmonares devidas a agentes externos"
        self.target = list(
            set(
                [f"J{i}" for i in range(60, 71)],
            )
        )


class OtherRespiratoryDiseases(Disease):
    def __init__(self):
        super().__init__()
        self.name = (
            "Outras doenças respiratórias que afetam principalmente o interstício"
        )
        self.target = list(
            set(
                [f"J{i}" for i in range(80, 85)],
            )
        )


class SuppurativeAndNecroticConditions(Disease):
    def __init__(self):
        super().__init__()
        self.name = "Afecções supurativas e necróticas do trato respiratório inferior"
        self.target = list(
            set(
                [f"J{i}" for i in range(85, 87)],
            )
        )


class OtherPleuralDiseases(Disease):
    def __init__(self):
        super().__init__()
        self.name = "Outras doenças da pleura"
        self.target = list(
            set(
                [f"J{i}" for i in range(90, 95)],
            )
        )


class OtherDiseasesOfTheRespiratorySystem(Disease):
    def __init__(self):
        super().__init__()
        self.name = "Outras doenças do aparelho respiratório"
        self.target = list(
            set(
                [f"J{i}" for i in range(95, 100)],
            )
        )
