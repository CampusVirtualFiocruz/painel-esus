from .complications import Complications


class HeartAttack(Complications):
    def __init__(self):
        super().__init__(['I21', 'I21.0', 'I21.1', 'I21.2',  'I21.3', 'I21.4', 'I21.9',
                         'I210', 'I211', 'I212', 'I213', 'I214', 'I219'])
        self.label = 'Infarto Agudo do Miocárdio'
