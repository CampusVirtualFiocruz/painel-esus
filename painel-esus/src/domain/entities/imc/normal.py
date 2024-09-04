from .imc import IMC


class IMCNormal(IMC):
    def __init__(self):
        super().__init__()
        self.imc = 'Peso Adequado'
        self.label = '18,5 a 24,9'
        self.min = 18.5
        self.max = 24.9
