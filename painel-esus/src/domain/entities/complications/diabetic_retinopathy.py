from .complications import Complications


class DiabeticRetinopathy(Complications):
    def __init__(self):
        super().__init__(['H360', 'F83'])
        self.label = 'Retinopatia diabética'
