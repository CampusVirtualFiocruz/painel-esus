from .exams_status import ExamStatus


class GlycatedHemoglobin(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = list(set(['0202010503', 'ABEX008']))
        self.label = 'Hemoglobina glicada'
