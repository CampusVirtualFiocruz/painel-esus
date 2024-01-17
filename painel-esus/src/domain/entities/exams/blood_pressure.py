from .exams_status import ExamStatus


class BloodPressure(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = list(set(['0301100039']))
        self.label = 'Aferição de PA'
