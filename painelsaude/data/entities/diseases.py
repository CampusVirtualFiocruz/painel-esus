class Disease:
    
    def __init__(self):
        self.match = []
        self.complications =[
            'I73',
            'G57',
            'H360',
            'G46',
            'I24',
            'I64',
            'I21'           
        ]

    def check(self, row):
        if any(word in field for field in row for word in self.match):
            return True
        return False
    
    def check_str(self, row: str):
        for i in row:
            i = i.replace("|","")
            if self.check(i):
                return True
        
            

class Hipertensao(Disease):
    
    def __init__(self):
        super().__init__()        
        self.ciaps = ['K86','K87','W81']
        self.cids = ['I10','I11','I110','I119','I12','I120','I129','I13','I130','I131','I132','I139','I15','I150','I151','I152','I158','I159','I270','I272','O10','O100','O101','O102','O103',
         'O104','O109','ABP005']
        self.match = self.ciaps + self.cids
        

class Diabetes(Disease):
    def __init__(self):
        super().__init__()
        self.ciaps = ['T89','T90','W85','E10']
        self.cids = ['E100','E101','E102','E103','E104','E105','E106','E107','E108','E109','E11','E110','E111','E112','E113','E114','E115','E116','E117','E118','E119','E12','E120',
         'E121','E122','E123','E124','E125','E126','E127','E128','E129','E13','E130','E131','E132','E133','E134','E135','E136','E137','E138','E139','E14','E140','E141','E142','E143','E144','E145',
         'E146','E147','E148','E149','O24','O240','O241','O242','O243','O244','O249','P702','ABP006']
        self.match = self.cids + self.ciaps
      