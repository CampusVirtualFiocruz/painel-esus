from .complications import Complications


class VascularBrainDisease(Complications):
    def __init__(self):
        super().__init__(['G46', 'G468', 'I67', 'I678',
                          'I679', 'I68', 'I688', 'I69', 'I699'])
        self.label = 'Doença Cerebrovascular'
