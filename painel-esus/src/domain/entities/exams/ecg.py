from .exams_status import ExamStatus


class ECG(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = list(set(['0211020036']))
        self.label = 'Eletrocardiograma'
