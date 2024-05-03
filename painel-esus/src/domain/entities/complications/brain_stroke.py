from .complications import Complications


class BrainStroke(Complications):
    def __init__(self):
        super().__init__(['I64'])
        self.label = 'Acidente Vascular Encefálico'
