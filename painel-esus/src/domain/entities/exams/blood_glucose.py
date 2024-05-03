from .exams_status import ExamStatus


class BloodGlucose(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = list(set(['0202010473', '0202010295', 'ABEX026']))
        self.label = 'Glicemia'
