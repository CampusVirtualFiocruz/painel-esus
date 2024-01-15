from .exams_status import ExamStatus


class Creatinine(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = list(set(['0202010317', 'ABEX003']))
        self.label = 'Creatinina'
