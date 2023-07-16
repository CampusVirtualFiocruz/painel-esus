from ..entities.unidade_saude import UnidadeSaude, Cidade

from typing import List
from pprint import pprint

from ..tests.utils import join, surround

class AtendimentoCollection:
    def __init__(self, atendimento_list) -> None:
        self.atendimento_list = atendimento_list
class AtendimentoMestre:
    
    def __init__(self,
                 dt_atendimento,
                 cad_filtro_cids,
                 cad_filtro_ciap,
                 cad_proced_solicitados,
                 cad_proced_avaliados,
                 nu_idade_gestacional,
                 nu_gestas_previas) -> None:
        """ Constructor of Atendimento mestre

        Args:
            dt_atendimento str: string as yyyymmdd like *20180322*
            cad_filtro_cids List[str]: List of cids ["J111", "Z000"]
            cad_filtro_ciap List[str]: List of ciaps ["ABP023", "P20"]
            cad_proced_solicitados List[str]: List of ciaps ["20140826"]
            cad_proced_avaliados List[str]: List of ciaps ["20140826"]
            nu_idade_gestacional int
            nu_gestas_previas int
        """
        self.dt_atendimento = dt_atendimento
        self.cad_filtro_cids = cad_filtro_cids
        self.cad_filtro_ciap = cad_filtro_ciap
        self.nu_idade_gestacional = nu_idade_gestacional
        self.nu_gestas_previas = nu_gestas_previas
        self.cad_proced_solicitados = cad_proced_solicitados
        self.cad_proced_avaliados = cad_proced_avaliados
        
    def __repr__(self) -> str:
        return self.__str__()
    
    def __str__(self) -> str:
        return f'dt_atendimento: {self.dt_atendimento}, \
    cad_filtro_cids: {self.cad_filtro_cids}, \
    cad_filtro_ciap: {self.cad_filtro_ciap}, \
    nu_idade_gestacional: {self.nu_idade_gestacional}, \
    nu_gestas_previas: {self.nu_gestas_previas}, \
    cad_proced_solicitados: {self.cad_proced_solicitados}, \
    cad_proced_avaliados: {self.cad_proced_avaliados}\
    '
        
    
class AtendimentoMestreCollection(AtendimentoCollection):
    def __init__(self, atendimento_list: List[AtendimentoMestre], unidade: UnidadeSaude) -> None:
        super().__init__(atendimento_list)
        self.unidade = unidade
        self.co_unidade_saude = []
        self.co_municipio = []
        self.co_dim_uf = []
        self.nu_cnes = []
        
        self.dt_atendimento = []
        self.cad_filtro_cids = []
        self.cad_filtro_ciap = []
        self.nu_idade_gestacional = []
        self.nu_gestas_previas = []
        
        self.cad_proced_avaliados = []
        self.cad_proced_solicitados = []
        self.update()

        
    def __str__(self) -> str:
        result = ''
        for i in self.atendimento_list:
            result += str(i) + "\n"
        return result
    
    def update(self):
        for atendimento in self.atendimento_list:
            self.co_unidade_saude.append(str(self.unidade.co_unidade_saude))
            self.co_municipio.append(str(self.unidade.cidade.co_municipio))
            self.co_dim_uf.append(self.unidade.cidade.sg_uf)
            self.nu_cnes.append(self.unidade.cnes)
            self.dt_atendimento .append( str(atendimento.dt_atendimento))
            self.cad_filtro_cids += [ surround(atd) for atd in atendimento.cad_filtro_cids]
            self.cad_filtro_ciap += [ surround(atd) for atd in atendimento.cad_filtro_ciap]
            
            self.cad_proced_solicitados += [ surround(atd) for atd in atendimento.cad_proced_solicitados]
            self.cad_proced_avaliados += [ surround(atd) for atd in atendimento.cad_proced_avaliados]
            
            self.nu_idade_gestacional.append( str(atendimento.nu_idade_gestacional) )
            self.nu_gestas_previas.append(str(atendimento.nu_gestas_previas) )
            
    def to_dict(self):
        self.update()
        return {
            "co_unidade_saude": join(self.co_unidade_saude),
            "co_municipio": join(self.co_municipio),
            "dt_atendimento": join(self.dt_atendimento),
            "cad_filtro_cids": join(self.cad_filtro_cids),
            "cad_filtro_ciap": join(self.cad_filtro_ciap),
            "nu_idade_gestacional": join(self.nu_idade_gestacional),
            "nu_gestas_previas": join(self.nu_gestas_previas),
            "cad_proced_solicitados": join(self.cad_proced_solicitados),
            "cad_proced_avaliados": join(self.cad_proced_avaliados)
        }
        