from .exams_status import ExamStatus


class SodiumPotassium(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = list(set(['0202010635', '0202010600']))
        self.label = 'Sódio e potássio'
