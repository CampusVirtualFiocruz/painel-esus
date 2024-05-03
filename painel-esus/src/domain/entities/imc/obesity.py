from .imc import IMC


class IMCObesity(IMC):
    def __init__(self):
        super().__init__()
        self.imc = 'Obesidade'
        self.label = '> 30'
        self.min = 30
        self.max = 9999
