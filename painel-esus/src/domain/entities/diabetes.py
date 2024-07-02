from src.domain.entities.disease import Disease


class Diabetes(Disease):
    def __init__(self):
        super().__init__()
        self.name = "diabetes"
        self.target = list(
            set(
                [
                    "T89",
                    "T90",
                    "W85",
                    "E10",
                    "E100",
                    "E101",
                    "E102",
                    "E103",
                    "E104",
                    "E105",
                    "E106",
                    "E107",
                    "E108",
                    "E109",
                    "E11",
                    "E110",
                    "E111",
                    "E112",
                    "E113",
                    "E114",
                    "E115",
                    "E116",
                    "E117",
                    "E118",
                    "E119",
                    "E12",
                    "E120",
                    "E121",
                    "E122",
                    "E123",
                    "E124",
                    "E125",
                    "E126",
                    "E127",
                    "E128",
                    "E129",
                    "E13",
                    "E130",
                    "E131",
                    "E132",
                    "E133",
                    "E134",
                    "E135",
                    "E136",
                    "E137",
                    "E138",
                    "E139",
                    "E14",
                    "E140",
                    "E141",
                    "E142",
                    "E143",
                    "E144",
                    "E145",
                    "E146",
                    "E147",
                    "E148",
                    "E149",
                    "O24",
                    "O240",
                    "O241",
                    "O242",
                    "O243",
                    "O244",
                    "O249",
                    "P702",
                    "ABP006",
                ]
            )
        )


class DiabeteMellitus(Disease):
    def __init__(self):
        super().__init__()
        self.name = "diabetes mellitus"
        self.target = list(
            set(
                [
                    "E10",
                    "E11",
                    "E12",
                    "E13",
                    "E14",
                ],
            )
        )
