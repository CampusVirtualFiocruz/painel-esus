import collections


class ExamStatus:
    def __init__(self):
        self.evaluated_list = set()
        self.requested = set()
        self.evaluated = 0
        self.requested = 0
        self.label = None
        self.exams = []

    def __repr__(self):
        return f'{self.label}: evaluated: {self.evaluated}\trequested: {self.requested}'

    def intersect(self, list1, list2):
        intersection = collections.Counter(list1) & collections.Counter(list2)
        return list(intersection.elements())

    def check_presence(self, _eval, _resquest):
        """Verify if there how many exams were requested and not evaluated

        Args:
            _eval ([str]): List of evaluated exams
            _resquest ([str]): List of requested exams
        """
        exams = self.exams
        evaluated_procedures_presence = self.intersect(exams, list(_eval))
        requested_procedures_presence = self.intersect(exams, list(_resquest))
        # - if the exam code did't present on requested and evaluated column
        # plus one on requested pendency
        if len(requested_procedures_presence) == 0 and len(evaluated_procedures_presence) == 0:
            self.requested += 1
        elif len(requested_procedures_presence) > 0 and len(evaluated_procedures_presence) == 0:
            # - if the exam code were present on requested column but not
            # in evaluated column, plus one on evaluated pendency
            self.evaluated += 1
