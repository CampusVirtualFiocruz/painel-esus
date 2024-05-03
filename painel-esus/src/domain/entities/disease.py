

class Disease:

    def __init__(self):
        self.target = []

    def filter_registers(self, data_frame: any) -> any:
        target_df = data_frame
        target_df = target_df.drop_duplicates()
        mask = target_df['codigo'].isin(self.target)
        return target_df.loc[mask]
