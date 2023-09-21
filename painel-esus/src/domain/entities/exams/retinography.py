from .exams_status import ExamStatus


class Retinography(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = list(set(['0211060178', 'ABEX013']))
        self.label = 'Retinografia'
