from src.domain.entities.disease import Disease


class Hypertension(Disease):
    def __init__(self):
        super().__init__()
        self.name = 'hipertensao'
        self.target = list(set([
            'K86', 'K87', 'W81', 'I10', 'I11', 'I110', 'I119', 'I12',
            'I120', 'I129', 'I13', 'I130', 'I131', 'I132', 'I139', 'I15',
            'I150', 'I151', 'I152', 'I158', 'I159', 'I270', 'I272', 'O10',
            'O100', 'O101', 'O102', 'O103', 'O104', 'O109', 'ABP005'
        ]))
