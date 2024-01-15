from .imc import IMC


class IMCHeighWeight(IMC):
    def __init__(self):
        super().__init__()
        self.imc = 'Excesso de Peso'
        self.label = '25 a 29,9'
        self.min = 25
        self.max = 29.9
