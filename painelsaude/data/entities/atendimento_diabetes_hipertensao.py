from typing import List
from ..entities.unidade_saude import UnidadeSaude
from ..tests.utils import join, surround
from .atendimento_mestre import AtendimentoCollection

class AtendimentoModel:
    
    def __init__(
        self,
        co_dim_tempo: str,
        co_dim_equipe_1: int,
        nu_peso: int,
        nu_altura: float,
        co_seq_dim_cbo: int,
        ds_filtro_cids: List[str],
        ds_filtro_ciaps: List[str],
        ds_filtro_proced_avaliados: List[str],
        ds_filtro_proced_solicitados: List[str],
        nu_cbo: int,
        FAIXA_ETARIA,
        ds_agravo_FINAL_NOM,
        ds_agravo_FINAL_COD,
        CBO_PROFISSIONAL,
        nu_peso_last,
        nu_altura_last_M,
        IMC,
        IMC_FINAL        
    ) -> None:
        self.co_dim_tempo=co_dim_tempo
        self.co_dim_equipe_1=co_dim_equipe_1
        self.nu_peso=nu_peso
        self.nu_altura=nu_altura
        self.co_seq_dim_cbo=co_seq_dim_cbo
        self.ds_filtro_cids=ds_filtro_cids
        self.ds_filtro_ciaps=ds_filtro_ciaps
        self.ds_filtro_proced_avaliados=ds_filtro_proced_avaliados
        self.ds_filtro_proced_solicitados=ds_filtro_proced_solicitados
        self.nu_cbo=nu_cbo
        self.FAIXA_ETARIA = FAIXA_ETARIA
        self.ds_agravo_FINAL_NOM=ds_agravo_FINAL_NOM
        self.ds_agravo_FINAL_COD=ds_agravo_FINAL_COD
        self.CBO_PROFISSIONAL=CBO_PROFISSIONAL
        self.nu_peso_last=nu_peso_last
        self.nu_altura_last_M=nu_altura_last_M
        self.IMC=IMC
        self.IMC_FINAL=IMC_FINAL
    
    @staticmethod
    def imc( peso, altura):
        imc_value = round(peso/(altura * altura), 2)
        
        categoria = "OUTROS"
        if imc_value <= 18.5:
            categoria = "Baixo Peso"
        elif imc_value > 18.5 and imc_value <=24.9:
            categoria = "Normal"
        elif imc_value >= 25 and imc_value <=29.9:
            categoria = "Excesso de Peso"
        elif imc_value >= 30:
            categoria = "Obesidade"
        else:
            categoria = "OUTROS"
        
        return ( imc_value, categoria)
        
class AtendimentoHipertensao(AtendimentoModel):
    
    def __init__(
        self,
        co_dim_tempo: str,
        co_dim_equipe_1: int,
        nu_peso: int,
        nu_altura: float,
        co_seq_dim_cbo: int,
        ds_filtro_cids: List[str],
        ds_filtro_ciaps: List[str],
        ds_filtro_proced_avaliados: List[str],
        ds_filtro_proced_solicitados: List[str],
        nu_cbo: int,
        FAIXA_ETARIA,
        ds_agravo_FINAL_NOM,
        ds_agravo_FINAL_COD,
        CBO_PROFISSIONAL,
        nu_peso_last,
        nu_altura_last_M,
        IMC,
        IMC_FINAL
    ) -> None:
        super().__init__(
            co_dim_tempo,
            co_dim_equipe_1,
            nu_peso,
            nu_altura,
            co_seq_dim_cbo,
            ds_filtro_cids,
            ds_filtro_ciaps,
            ds_filtro_proced_avaliados,
            ds_filtro_proced_solicitados,
            nu_cbo,
            FAIXA_ETARIA,
            ds_agravo_FINAL_NOM,
            ds_agravo_FINAL_COD,
            CBO_PROFISSIONAL,
            nu_peso_last,
            nu_altura_last_M,
            IMC,
            IMC_FINAL
        )
        
    def __str__(self) -> str:
        return f'\
            \n\t"co_dim_tempo": {self.co_dim_tempo}, \
            \n\t"co_dim_equipe_1": {self.co_dim_equipe_1}, \
            \n\t"nu_peso": {self.nu_peso}, \
            \n\t"nu_altura": {self.nu_altura}, \
            \n\t"co_seq_dim_cbo": {self.co_seq_dim_cbo}, \
            \n\t"ds_filtro_cids": {self.ds_filtro_cids}, \
            \n\t"ds_filtro_ciaps": {self.ds_filtro_ciaps}, \
            \n\t"ds_filtro_proced_avaliados": {self.ds_filtro_proced_avaliados}, \
            \n\t"ds_filtro_proced_solicitados": {self.ds_filtro_proced_solicitados}, \
            \n\t"nu_cbo": {self.nu_cbo}, \
            \n\t"ds_agravo_FINAL_NOM": {self.ds_agravo_FINAL_NOM}, \
            \n\t"ds_agravo_FINAL_COD": {self.ds_agravo_FINAL_COD}, \
            \n\t"CBO_PROFISSIONAL": {self.CBO_PROFISSIONAL}, \
            \n\t"nu_peso_last": {self.nu_peso_last}, \
            \n\t"nu_altura_last_M": {self.nu_altura_last_M}, \
            \n\t"IMC": {self.IMC}, \
            \n\t"IMC_FINAL": {self.IMC_FINAL}, \
            \n\t"FAIXA_ETARIA_HIPERTENSAO": {self.FAIXA_ETARIA}'
    
    def to_dict(self):
        return {
            "co_dim_tempo": {self.co_dim_tempo},
            "co_dim_equipe_1": {self.co_dim_equipe_1},
            "nu_peso": {self.nu_peso},
            "nu_altura": {self.nu_altura},
            "co_seq_dim_cbo": {self.co_seq_dim_cbo},
            "ds_filtro_cids": {self.ds_filtro_cids},
            "ds_filtro_ciaps": {self.ds_filtro_ciaps},
            "ds_filtro_proced_avaliados": {self.ds_filtro_proced_avaliados},
            "ds_filtro_proced_solicitados": {self.ds_filtro_proced_solicitados},
            "nu_cbo": {self.nu_cbo},
            "ds_agravo_FINAL_NOM": {self.ds_agravo_FINAL_NOM},
            "ds_agravo_FINAL_COD": {self.ds_agravo_FINAL_COD},
            "CBO_PROFISSIONAL": {self.CBO_PROFISSIONAL},
            "nu_peso_last": {self.nu_peso_last},
            "nu_altura_last_M": {self.nu_altura_last_M},
            "IMC": {self.IMC},
            "IMC_FINAL": {self.IMC_FINAL},
            "FAIXA_ETARIA_HIPERTENSAO": {self.FAIXA_ETARIA}
        }
        
class AtendimentoDiabetes(AtendimentoModel):
    
    def __init__(
        self,
        co_dim_tempo: str,
        co_dim_equipe_1: int,
        nu_peso: int,
        nu_altura: float,
        co_seq_dim_cbo: int,
        ds_filtro_cids: List[str],
        ds_filtro_ciaps: List[str],
        ds_filtro_proced_avaliados: List[str],
        ds_filtro_proced_solicitados: List[str],
        nu_cbo: int,
        FAIXA_ETARIA,
        ds_agravo_FINAL_NOM,
        ds_agravo_FINAL_COD,
        CBO_PROFISSIONAL,
        nu_peso_last,
        nu_altura_last_M,
        IMC,
        IMC_FINAL
    ) -> None:
        super().__init__(
            co_dim_tempo,
            co_dim_equipe_1,
            nu_peso,
            nu_altura,
            co_seq_dim_cbo,
            ds_filtro_cids,
            ds_filtro_ciaps,
            ds_filtro_proced_avaliados,
            ds_filtro_proced_solicitados,
            nu_cbo,
            FAIXA_ETARIA,
            ds_agravo_FINAL_NOM,
            ds_agravo_FINAL_COD,
            CBO_PROFISSIONAL,
            nu_peso_last,
            nu_altura_last_M,
            IMC,
            IMC_FINAL
        )
        
class AtendimentoModelCollection(AtendimentoCollection):
    
    def __init__(
        self,
        atendimento_list: List[AtendimentoModel],
        unidade: UnidadeSaude
    ):
        super().__init__(atendimento_list)
        self.co_dim_tempo=[]
        self.co_dim_equipe_1=[]
        self.nu_peso=[]
        self.nu_altura=[]
        self.co_seq_dim_cbo=[]
        self.ds_filtro_cids=[]
        self.ds_filtro_ciaps=[]
        self.ds_filtro_proced_avaliados=[]
        self.ds_filtro_proced_solicitados=[]
        self.nu_cbo=[]
        self.ds_agravo_FINAL_NOM=[]
        self.ds_agravo_FINAL_COD=[]
        self.CBO_PROFISSIONAL=[]
        self.nu_peso_last=[]
        self.nu_altura_last_M=[]
        self.IMC=[]
        self.IMC_FINAL=[]
        self.FAIXA_ETARIA=[]
        
        self.update()
    
    def update(self):
        for atendimento in self.atendimento_list:
            self.co_dim_tempo.append(str(atendimento.co_dim_tempo))
            self.co_dim_equipe_1.append(str(atendimento.co_dim_equipe_1))
            self.nu_peso.append(str(atendimento.nu_peso))
            self.nu_altura.append(str(atendimento.nu_altura))
            self.co_seq_dim_cbo.append(str(atendimento.co_seq_dim_cbo))
            self.ds_filtro_cids += [ surround(atd) for atd in atendimento.ds_filtro_cids]
            self.ds_filtro_ciaps += [ surround(atd) for atd in atendimento.ds_filtro_ciaps]
            
            self.ds_filtro_proced_solicitados += [ surround(atd) for atd in atendimento.ds_filtro_proced_solicitados]
            self.ds_filtro_proced_avaliados += [ surround(atd) for atd in atendimento.ds_filtro_proced_avaliados]
            
            self.nu_cbo.append(str(atendimento.nu_cbo))
            self.ds_agravo_FINAL_NOM.append(str(atendimento.ds_agravo_FINAL_NOM))
            self.ds_agravo_FINAL_COD.append(str(atendimento.ds_agravo_FINAL_COD))
            self.CBO_PROFISSIONAL.append(str(atendimento.CBO_PROFISSIONAL))
            self.nu_peso_last.append(str(atendimento.nu_peso_last))
            self.nu_altura_last_M.append(str(atendimento.nu_altura_last_M))
            self.IMC.append(str(atendimento.IMC))
            self.IMC_FINAL.append(str(atendimento.IMC_FINAL))
            self.FAIXA_ETARIA.append(str(atendimento.FAIXA_ETARIA))
            
    def to_dict(self):
        return {
            "co_dim_tempo": join(self.co_dim_tempo),
            "co_dim_equipe_1": join(self.co_dim_equipe_1),
            "nu_peso": join(self.nu_peso),
            "nu_altura": join(self.nu_altura),
            "co_seq_dim_cbo": join(self.co_seq_dim_cbo),
            "ds_filtro_cids": join(self.ds_filtro_cids),
            "ds_filtro_ciaps": join(self.ds_filtro_ciaps),
            "ds_filtro_proced_avaliados": join(self.ds_filtro_proced_avaliados),
            "ds_filtro_proced_solicitados": join(self.ds_filtro_proced_solicitados),
            "nu_cbo": join(self.nu_cbo),
            "ds_agravo_FINAL_NOM": join(self.ds_agravo_FINAL_NOM),
            "ds_agravo_FINAL_COD": join(self.ds_agravo_FINAL_COD),
            "CBO_PROFISSIONAL": join(self.CBO_PROFISSIONAL),
            "nu_peso_last": join(self.nu_peso_last),
            "nu_altura_last_M": join(self.nu_altura_last_M),
            "IMC": self.IMC,
            "IMC_FINAL": self.IMC_FINAL,
            "FAIXA_ETARIA": join(self.FAIXA_ETARIA)
        }
                
class HipertensaoDictAdapter:
    def __init__(self, atendimentos: AtendimentoModelCollection) -> None:
        self.atendimentos = atendimentos

    def to_dict(self):
        return {
            "co_dim_tempo": join(self.atendimentos.co_dim_tempo),
            "co_dim_equipe_1": join(self.atendimentos.co_dim_equipe_1),
            "nu_peso": join(self.atendimentos.nu_peso),
            "nu_altura": join(self.atendimentos.nu_altura),
            "co_seq_dim_cbo": join(self.atendimentos.co_seq_dim_cbo),
            "ds_filtro_cids": join(self.atendimentos.ds_filtro_cids),
            "ds_filtro_ciaps": join(self.atendimentos.ds_filtro_ciaps),
            "ds_filtro_proced_avaliados": join(self.atendimentos.ds_filtro_proced_avaliados),
            "ds_filtro_proced_solicitados": join(self.atendimentos.ds_filtro_proced_solicitados),
            "nu_cbo": join(self.atendimentos.nu_cbo),
            "ds_agravo_FINAL_NOM": join(self.atendimentos.ds_agravo_FINAL_NOM),
            "ds_agravo_FINAL_COD": join(self.atendimentos.ds_agravo_FINAL_COD),
            "CBO_PROFISSIONAL": join(self.atendimentos.CBO_PROFISSIONAL),
            "nu_peso_last": join(self.atendimentos.nu_peso_last),
            "nu_altura_last_M": join(self.atendimentos.nu_altura_last_M),
            "IMC": self.atendimentos.IMC,
            "IMC_FINAL": self.atendimentos.IMC_FINAL,  
            "FAIXA_ETARIA_HIPERTENSO": join(self.atendimentos.FAIXA_ETARIA)
        }

class DiabetesDictAdapter:
    def __init__(self, atendimentos: AtendimentoModelCollection) -> None:
        self.atendimentos = atendimentos
        self.atendimentos.update()

    def to_dict(self):
        return {
            "co_dim_tempo": join(self.atendimentos.co_dim_tempo),
            "co_dim_equipe_1": join(self.atendimentos.co_dim_equipe_1),
            "nu_peso": join(self.atendimentos.nu_peso),
            "nu_altura": join(self.atendimentos.nu_altura),
            "co_seq_dim_cbo": join(self.atendimentos.co_seq_dim_cbo),
            "ds_filtro_cids": join(self.atendimentos.ds_filtro_cids),
            "ds_filtro_ciaps": join(self.atendimentos.ds_filtro_ciaps),
            "ds_filtro_proced_avaliados": join(self.atendimentos.ds_filtro_proced_avaliados),
            "ds_filtro_proced_solicitados": join(self.atendimentos.ds_filtro_proced_solicitados),
            "nu_cbo": join(self.atendimentos.nu_cbo),
            "ds_agravo_FINAL_NOM": join(self.atendimentos.ds_agravo_FINAL_NOM),
            "ds_agravo_FINAL_COD": join(self.atendimentos.ds_agravo_FINAL_COD),
            "CBO_PROFISSIONAL": join(self.atendimentos.CBO_PROFISSIONAL),
            "nu_peso_last": join(self.atendimentos.nu_peso_last),
            "nu_altura_last_M": join(self.atendimentos.nu_altura_last_M),
            "IMC": self.atendimentos.IMC,
            "IMC_FINAL": self.atendimentos.IMC_FINAL,
            "FAIXA_ETARIA_DIABETICO": join(self.atendimentos.FAIXA_ETARIA)
        }
            