from .exams_status import ExamStatus


class BloodCount(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = list(set(['0202020380', 'ABEX028']))
        self.label = 'Hemograma'
