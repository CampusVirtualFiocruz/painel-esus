# pylint: disable=E0401
from pandas import DataFrame


class Complications:
    def __init__(self, cids):
        self.cids = list(set(cids))
        self.total = 0

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
