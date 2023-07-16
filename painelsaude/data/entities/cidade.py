class Cidade:
    
    def __init__(self,
                 co_municipio: int,
                 no_municipio:str, 
                 co_ibge: str,
                 no_uf: str,
                 sg_uf: str) -> None:
        self.co_municipio = co_municipio
        self.no_municipio = no_municipio
        self.co_ibge = co_ibge
        self.no_uf = no_uf
        self.sg_uf = sg_uf
        
    def to_dict(self):
        cidade = {
            "co_municipio": self.co_municipio,
            "no_municipio": self.no_municipio,
            "co_ibge": self.co_ibge,
            "no_uf": self.no_uf,
            "sg_uf": self.sg_uf,
        }
        return cidade
        
    