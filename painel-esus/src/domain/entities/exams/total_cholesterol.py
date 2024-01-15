from .exams_status import ExamStatus


class TotalCholesterol(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = list(set(['0202010295']))
        self.label = 'Colesterol total'
