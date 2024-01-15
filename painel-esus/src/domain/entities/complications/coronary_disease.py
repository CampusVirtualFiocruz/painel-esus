from .complications import Complications


class CoronaryDisease(Complications):
    def __init__(self):
        super().__init__(['I24', 'I248', 'I249', 'I25', 'I251', 'I258', 'I259', 'I518',
                          'I519', 'I110', 'I119', 'I130', 'I132', 'I50', 'I500', 'I509'])
        self.label = 'Doença Coronariana'
