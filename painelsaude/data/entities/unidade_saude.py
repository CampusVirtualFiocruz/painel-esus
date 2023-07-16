from .cidade import Cidade 

class UnidadeSaude:
    def __init__(self,
                 co_unidade_saude: int,
                 ds_unidade_saude: str,
                 cnes: int,
                 cidade: Cidade) -> None:
        self.co_unidade_saude = co_unidade_saude
        self.ds_unidade_saude = ds_unidade_saude
        self.cnes = cnes
        self.cidade = cidade
        
    def to_dict(self):
        unidade = {
            "co_unidade_saude": self.co_unidade_saude,
            "ds_unidade_saude": self.ds_unidade_saude,
            "nu_cnes": self.cnes
        }
        unidade.update(self.cidade.to_dict())
        return unidade