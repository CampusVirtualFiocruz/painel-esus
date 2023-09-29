import re
class AccuteInfection:
    def __init__(self):
        self.label = None
        self.cids = None
        self.ciaps = None

    def get_cidsciaps(self):
        return list(set(self.cids + self.ciaps))

class NonspecificFever(AccuteInfection):
    def __init__(self):
        self.label = 'Febre Inespecífica'
        self.cids = [ 'L18', 'A03', 'R50', 'R508', 'R509', 'M255', 'R520', 'R529', 'B34', 'B349', 'B97', 'M791', 'R53' ]
        self.ciaps = ['L18', 'A03', 'R96', 'L20', 'A01', 'R74', 'A77', 'R33', 'R80', 'R05', 'R08', 'L18', 'R81', 'R02', 'D70']       

class RespiratoryInfections(AccuteInfection):
    def __init__(self):
        self.label = 'Infecção Respiratória'
        self.cids = ['R96', 'R97', 'J459', 'R05', 'R07', 'R08', 'R74', 'R76', 'R77', 'R80', 'R83', 'B342', 'B972', 'J00', 'J02', 'J029', 'J03', 'J039', 'J04', 'J06', 'J09', 'J10', 'J11', 'J111', 'J118', 'R05', 'R43', 'R430', 'R431', 'R432', 'R438', 'U071', 'U072', 'R01', 'R02', 'R81', 'J100', 'J12', 'J13', 'J14', 'J15', 'J158', 'J159', 'J16', 'J17', 'J18', 'J96', 'J960', 'J969', 'U04', 'U049', 'R21', 'J399' ]
        self.ciaps = ['R96', 'R97', 'R96', 'R05', 'R07', 'R08', 'R74', 'R80', 'R82', 'R33', 'A03', 'D01', 'A01', 'R81', 'R02', 'D70', 'A77', 'L18', 'D09', 'R01', 'R21', 'R28' ]

class IntestinalInfections(AccuteInfection):
    def __init__(self):
        self.label = 'Infecção Intestinal'
        self.cids = ['D01', 'D06', 'D10', 'D11', 'R04', 'A08', 'A084', 'A09', 'R11']
        self.ciaps = ['D01', 'D11', 'R04', 'D70', 'D09' ]


class ExanthematousFever(AccuteInfection):
    def __init__(self):
        self.label = 'Febre Exantemática'
        self.cids = ['A77', 'A90', 'S02', 'S29', 'S76', 'A92' ]
        self.ciaps = ['A76', 'S02', 'S29', 'S76', 'A92']

class ClassifyDF:
    def __init__(self, df, list_target):
        self.df = df
        self.list_target = list_target

    def process(self):
        if 'Unnamed: 0' in self.df.columns.to_list():
            self.df.drop(columns=['Unnamed: 0'], inplace=True, errors='ignore')
        self.df['classe'] = None
        def __process(row):
            for item in self.list_target:
                if row.codigo in item.get_cidsciaps():
                    row['classe'] = item.label
            return row
        
        self.df = self.df.apply(lambda x: __process(x), axis=1)