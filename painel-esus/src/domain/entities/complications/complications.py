# pylint: disable=E0401
from pandas import DataFrame
import collections

class Complications:
    def __init__(self, cids):
        self.cids = list(set(cids))
        self.total = 0

        self.evaluated_list = set()
        self.requested = set()
        self.evaluated = 0
        self.requested = 0
        self.label = None
        self.exams = []


    def filter_registers(self, data_frame: any) -> any:
        target_df = data_frame[['co_seq_fat_atd_ind', 'tipo', 'codigo']]
        target_df = target_df.drop_duplicates()
        self.total = target_df.shape[0]
        mask = target_df['codigo'].isin(self.cids)
        result_df = target_df.loc[mask]
        return result_df

    def statistics(self, data_frame: DataFrame):
        total_registros = int(data_frame.shape[0])
        com_consulta_abs = float(
            total_registros/self.total)*100 if self.total > 0 else 0
        sem_consulta_abs = float(
            (self.total-total_registros)/self.total)*100 if self.total > 0 else 0
        return {
            'com_consulta': round(com_consulta_abs, 2),
            'com_consulta_abs': total_registros,
            'sem_consulta': round(sem_consulta_abs, 2),
            'sem_consulta_abs': self.total - total_registros
        }


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
