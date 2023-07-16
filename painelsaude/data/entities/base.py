from ..tests.factories.pessoa import pessoa_factory_com_dt_nascimento, PessoaEnums, birthday_factory, Pessoa
from ..entities.atendimento_mestre import AtendimentoMestre, AtendimentoMestreCollection, UnidadeSaude
from ..tests.factories.atendimento_mestre_factory import atendimento_hipertensao_factory, atendimento_diabetes_factory
from ..tests.factories.unidade import unidade_factory

from typing import List
from enum import Enum

import random
import math 

class BaseEnums(Enum):
    
    FAIXA_ETARIA_1 = 1 # 0 -4
    FAIXA_ETARIA_2 = 2 # 5- 9
    FAIXA_ETARIA_3 = 3 # 10 -14
    FAIXA_ETARIA_4 = 4 # 15 -19
    FAIXA_ETARIA_5 = 5 # 20 -24
    FAIXA_ETARIA_6 = 6 # 25 - 29
    FAIXA_ETARIA_7 = 7 # 30 -34
    FAIXA_ETARIA_8 = 8 # 35 - 39
    FAIXA_ETARIA_9 = 9 # 40 - 44
    FAIXA_ETARIA_10 = 10 # 45 - 49
    FAIXA_ETARIA_11 = 11 # 50 - 54
    FAIXA_ETARIA_12 = 12 # 55 - 59
    FAIXA_ETARIA_13 = 13 # 60 - 64
    FAIXA_ETARIA_14 = 14 # 65 - 69
    FAIXA_ETARIA_15 = 15 # 70 - 74
    FAIXA_ETARIA_16 = 16 # 75 - 79
    FAIXA_ETARIA_17 = 17 # 80 - 84
    FAIXA_ETARIA_18 = 18 # 85 - 89
    FAIXA_ETARIA_19 = 19 # 90 - 94
    FAIXA_ETARIA_20 = 20 # 95 - 100 

class Base:
    
    def __init__(self, population: int):
        
        self.population = population
        self.masculino_percent = [
            0,
            0.033,
            0.034,
            0.035,
            0.037,
            0.039,
            0.04,
            0.04,
            0.04,
            0.038,
            0.033,
            0.029,
            0.027,
            0.023,
            0.017,
            0.012,
            0.008,
            0.004,
            0.002,
            0,
            0,
        ]
        self.feminino_percent = [
            0,
            0.031,
            0.033,
            0.034,
            0.035,
            0.038,
            0.039,
            0.039,
            0.04,
            0.039,
            0.035,
            0.031,
            0.029,
            0.026,
            0.021,
            0.016,
            0.011,
            0.007,
            0.003,
            0.001,
            0
        ]
        
        self.masculino = []
        self.feminino = []
        
        self.range_faixa_etaria = [
            (0,0),
            (0, 4),
            (5, 9),
            (10, 14),
            (15, 19),
            (20, 24),
            (25,  29),
            (30, 34),
            (35,  39),
            (40,  44),
            (45,  49),
            (50,  54),
            (55,  59),
            (60,  64),
            (65,  69),
            (70,  74),
            (75,  79),
            (80,  84),
            (85,  89),
            (90,  94),
            (95,  100 )
        ]
        
        for i, _ in enumerate(self.masculino_percent):
            self.masculino.append( math.ceil( self.masculino_percent[i] * self.population ))
            self.feminino.append( math.ceil(self.feminino_percent[i] * self.population))
            
        
    def generate_base(self) -> List[Pessoa]:
        qtd_faixas = len(self.range_faixa_etaria)
        
        pessoas = []
        unidade = unidade_factory()
        for faixa in range(1, qtd_faixas):
            qtd_masculino = self.masculino[faixa]
            qtd_feminino = self.feminino[faixa]
            faixa_etaria_range = self.range_faixa_etaria[faixa]
            for _ in range(qtd_masculino):
                local_choice = random.randint(0,100)  
                local_unit = random.randint(1,100)              
                homem = pessoa_factory_com_dt_nascimento(
                    sexo=PessoaEnums.MASCULINO,
                    local= PessoaEnums.URBANA if local_choice >30 else PessoaEnums.RURAL,
                    dt_nascimento=birthday_factory(
                        min_age=faixa_etaria_range[0],
                        max_age=faixa_etaria_range[1]
                    )                   
                )
                atendimentos=[]
                atendimentos.append(atendimento_hipertensao_factory(
                    is_hipertenso= False,
                ))
                atendimento_list = AtendimentoMestreCollection(atendimento_list=atendimentos, unidade=unidade)
                homem.atendimentos = atendimento_list
                homem.unidade_saude = unidade_factory(
                    unidade_saude= 1 if local_unit > 30 else 2
                )
                pessoas.append(homem)
                
            for _ in range(qtd_feminino):
                local_choice = random.randint(0,100)
                mulher = pessoa_factory_com_dt_nascimento(
                    sexo=PessoaEnums.FEMININO,
                    local= PessoaEnums.URBANA if local_unit >30 else PessoaEnums.RURAL,
                    dt_nascimento=birthday_factory(
                        min_age=faixa_etaria_range[0],
                        max_age=faixa_etaria_range[1]
                    )                   
                )
                atendimentos=[]
                atendimentos.append(atendimento_hipertensao_factory(
                    is_hipertenso= False,
                ))
                atendimento_list = AtendimentoMestreCollection(atendimento_list=atendimentos, unidade=unidade)
                mulher.atendimentos = atendimento_list
                mulher.unidade_saude = unidade_factory(
                    unidade_saude= 1 if random.randint(1,100) >50 else 2
                )
                pessoas.append(mulher)
                
        
        return pessoas
    
    def generate_atendimento(self, sample, base, unidade, taxas):
        masculino = random.sample( sample['masculino'], math.ceil(taxas[0] * len(sample['masculino']))) if len(sample['masculino']) else []
        feminino = random.sample( sample['feminino'], math.ceil(taxas[1] * len(sample['feminino']))) if len(sample['feminino']) else []
        
        for i in masculino:
            atendimentos=[]
            atendimentos.append(atendimento_hipertensao_factory(
                is_hipertenso= True,
                which_filter='cid'
            ))
            atendimento_list = AtendimentoMestreCollection(atendimento_list=atendimentos, unidade=unidade)
            base[i].atendimentos = atendimento_list
        
        for i in feminino:
            atendimentos=[]
            atendimentos.append(atendimento_hipertensao_factory(
                is_hipertenso= True,
                which_filter='cid'
            ))
            atendimento_list = AtendimentoMestreCollection(atendimento_list=atendimentos, unidade=unidade)
            base[i].atendimentos = atendimento_list
            
    def generate_atendimento_diabetes(self, sample, base, unidade, taxas):
        masculino = random.sample( sample['masculino'], math.ceil(taxas[0] * len(sample['masculino']))) if len(sample['masculino']) else []
        feminino = random.sample( sample['feminino'], math.ceil(taxas[1] * len(sample['feminino']))) if len(sample['feminino']) else []
        
        for i in masculino:
            atendimentos= [] + base[i].atendimentos.atendimento_list
            atendimentos.append(atendimento_diabetes_factory(
                is_diabetes= True,
                which_filter='cid'
            ))
            atendimento_list = AtendimentoMestreCollection(atendimento_list=atendimentos, unidade=unidade)
            base[i].atendimentos = atendimento_list
        
        for i in feminino:
            atendimentos= [] + base[i].atendimentos.atendimento_list
            atendimentos.append(atendimento_diabetes_factory(
                is_diabetes= True,
                which_filter='cid'
            ))
            atendimento_list = AtendimentoMestreCollection(atendimento_list=atendimentos, unidade=unidade)
            base[i].atendimentos = atendimento_list
        
            
    def apply_hypertension(self, base: List[Pessoa]):
        idx = []
        faixa_18_24 = { "masculino": [],
                       "feminino": []}
        faixa_25_34 = { "masculino": [],
                       "feminino": []}
        faixa_35_44 = { "masculino": [],
                       "feminino": []}
        faixa_45_54 = { "masculino": [],
                       "feminino": []}
        faixa_55_64 = { "masculino": [],
                       "feminino": []}
        faixa_65 = { "masculino": [],
                       "feminino": []}
        
        for i, val in enumerate(base):
            if val.nu_idade >= 18 and val.nu_idade <= 24:
                if val.ds_sexo == PessoaEnums.FEMININO:
                    faixa_18_24["feminino"].append(i)
                else:
                    faixa_18_24["masculino"].append(i)
            elif val.nu_idade >= 25 and val.nu_idade <= 34:
                if val.ds_sexo == PessoaEnums.FEMININO:
                    faixa_25_34["feminino"].append(i)
                else:
                    faixa_25_34["masculino"].append(i)
            elif val.nu_idade >= 35 and val.nu_idade <= 44:
                if val.ds_sexo == PessoaEnums.FEMININO:
                    faixa_35_44["feminino"].append(i)
                else:
                    faixa_35_44["masculino"].append(i)
            elif val.nu_idade >= 45 and val.nu_idade <= 54:
                if val.ds_sexo == PessoaEnums.FEMININO:
                    faixa_45_54["feminino"].append(i)
                else:
                    faixa_45_54["masculino"].append(i)
            elif val.nu_idade >= 55 and val.nu_idade <= 64:
                if val.ds_sexo == PessoaEnums.FEMININO:
                    faixa_55_64["feminino"].append(i)
                else:
                    faixa_55_64["masculino"].append(i)
            elif val.nu_idade >= 65:
                if val.ds_sexo == PessoaEnums.FEMININO:
                    faixa_65["feminino"].append(i)
                else:
                    faixa_65["masculino"].append(i)

        unidade = unidade_factory()
        
        self.generate_atendimento(faixa_18_24, base, unidade, (0.031, 0.066))
        self.generate_atendimento(faixa_25_34, base, unidade, (0.139, 0.152))
        self.generate_atendimento(faixa_35_44, base, unidade, (0.199, 0.208))
        self.generate_atendimento(faixa_45_54, base, unidade, (0.328, 0.325))
        self.generate_atendimento(faixa_55_64, base, unidade, (0.465, 0.550))
        self.generate_atendimento(faixa_65, base, unidade, (0.511, 0.658))

    def apply_diabetes(self, base: List[Pessoa]):

        faixa_20_39 = { "masculino": [],
                       "feminino": []}
        faixa_40_64 = { "masculino": [],
                       "feminino": []}
        faixa_65 = { "masculino": [],
                       "feminino": []}
        
        for i, val in enumerate(base):
            if val.nu_idade >= 20 and val.nu_idade <= 39:
                if val.ds_sexo == PessoaEnums.FEMININO:
                    faixa_20_39["feminino"].append(i)
                else:
                    faixa_20_39["masculino"].append(i)
            elif val.nu_idade >= 40 and val.nu_idade <= 64:
                if val.ds_sexo == PessoaEnums.FEMININO:
                    faixa_40_64["feminino"].append(i)
                else:
                    faixa_40_64["masculino"].append(i)
            elif val.nu_idade >= 65:
                if val.ds_sexo == PessoaEnums.FEMININO:
                    faixa_65["feminino"].append(i)
                else:
                    faixa_65["masculino"].append(i)

        unidade = unidade_factory()
        
        self.generate_atendimento_diabetes(faixa_20_39, base, unidade, (0.015, 0.015))
        self.generate_atendimento_diabetes(faixa_40_64, base, unidade, (0.079, 0.079))
        self.generate_atendimento_diabetes(faixa_65, base, unidade, (0.167, 0.167))
        
        
            
        
    
        