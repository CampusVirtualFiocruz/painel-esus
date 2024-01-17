from .complications import Complications


class OcclusiveArterialDisease(Complications):
    def __init__(self):
        super().__init__(['I73', 'I738', 'I739'])
        self.label = 'Doença Arterial Oclusiva'
