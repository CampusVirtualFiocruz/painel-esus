from .imc import IMC


class IMCLowWeight(IMC):
    def __init__(self):
        super().__init__()
        self.imc = 'Baixo Peso'
        self.label = '< 18,5'
        self.min = 1
        self.max = 18.5
