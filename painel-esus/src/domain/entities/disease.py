

class Disease:

    def __init__(self):
        self.target = []

    def filter_registers(self, data_frame: any)-> any:
        mask = data_frame['codigo'].isin(self.target)
        return data_frame.loc[mask]
