from .imc import IMC


class IMCOthers(IMC):
    def __init__(self):
        super().__init__()
        self.imc = 'OUTROS'
        self.label = 'OUTROS'
        self.min = 0.0
        self.max = 0.0
