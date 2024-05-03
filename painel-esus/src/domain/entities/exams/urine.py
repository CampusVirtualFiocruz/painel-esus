from .exams_status import ExamStatus


class Urine(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = list(set(['0202010017', 'ABEX027']))
        self.label = 'EAS/EQU (urina rotina)'
