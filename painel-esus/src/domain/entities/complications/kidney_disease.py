from .complications import Complications


class KidneyDisease(Complications):
    def __init__(self):
        super().__init__(['I12', 'I129', 'I13', 'I130', 'I131', 'I132', 'I139', 'N083',
                          'N179', 'N18', 'N180', 'N188', 'N189', 'N19', 'U14', 'U99',
                          'U88', 'U90'])
        self.label = 'Doença renal'
