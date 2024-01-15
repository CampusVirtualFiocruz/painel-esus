from .complications import Complications


class Neuropathy(Complications):
    def __init__(self):
        super().__init__(['G57', 'G578', 'G579', 'G58', 'G590', 'G598', 'G61', 'G628',
                          'G629', 'G63', 'G632', 'G633'])
        self.label = 'Neuropatia'
