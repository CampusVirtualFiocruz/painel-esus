from ...entities.atendimento_diabetes_hipertensao import (
    AtendimentoHipertensao, AtendimentoModel, AtendimentoModelCollection, HipertensaoDictAdapter,
    AtendimentoDiabetes, DiabetesDictAdapter
)
from ...entities.cbo import Cbo
from ...entities.diseases import Hipertensao, Disease, Diabetes
from ...entities.pessoa import PessoaEnums, Pessoa, age_group, age_range_by_age_group, parse_pessoa_atendimento_model

from ..config.faker import faker

import random
from typing import List


def atendimento_hipertensao_factory(
    cbo_list: List[Cbo],
    pessoa: Pessoa,
    disease_type: AtendimentoModel,
    disease: Disease
):
    qtd = len(cbo_list)
    months = random.sample(range(1,12), qtd)
    months.sort()
    
    nu_peso = random.randint(50 , 110)
    nu_altura = random.randint(150, 201)/100
    

    disease = disease()
    
    atendimentos =[]
    for i, _ in enumerate(range(qtd)):
        
        date = faker.date_between(
            start_date = f'-{months[i]}M', 
            end_date='today')
        
        imc = disease_type.imc(nu_peso, nu_altura)
        random.shuffle(disease.match)
        random.shuffle(disease.complications)
        atendimento = disease_type(
            co_dim_tempo=date.strftime("%Y%m%d"),
            co_dim_equipe_1=1,
            nu_peso=nu_peso,
            nu_altura=nu_altura,
            co_seq_dim_cbo=cbo_list[i].co_seq_dim_cbo,
            ds_filtro_cids=
                random.choices(disease.match, k=random.randint(1,3)) +
                random.choices(disease.complications, k=random.randint(0,2)) 
            ,
            ds_filtro_ciaps=
                random.choices(disease.match, k=random.randint(1,3))+
                random.choices(disease.complications, k=random.randint(0,2))
            ,
            ds_filtro_proced_avaliados=[''],
            ds_filtro_proced_solicitados=[''],
            nu_cbo=cbo_list[i].nu_cbo,
            FAIXA_ETARIA=pessoa.ds_faixa_etaria,
            ds_agravo_FINAL_NOM = [''],
            ds_agravo_FINAL_COD= [''],
            CBO_PROFISSIONAL=cbo_list[i].label,
            nu_peso_last=nu_peso,
            nu_altura_last_M=nu_altura,
            IMC=imc[0],
            IMC_FINAL=imc[1]
        )
        atendimentos.append(atendimento)
    return atendimentos

def atendimento_hipertensao_factory_gen(
    cbo_list: List[Cbo],
    pessoa: Pessoa
):
    atendimentos = atendimento_hipertensao_factory(cbo_list, pessoa, disease_type=AtendimentoHipertensao, disease=Hipertensao )
    atendimentoCollection = AtendimentoModelCollection(atendimento_list=atendimentos, unidade=pessoa.unidade_saude)
    atendimentos_adapter = HipertensaoDictAdapter(atendimentos=atendimentoCollection)
    pessoa.atendimentos = atendimentoCollection
    pessoa.st_hipertensao = True
    return pessoa

def atendimento_diabetes_factory_gen(
    cbo_list: List[Cbo],
    pessoa: Pessoa
):
    atendimentos = atendimento_hipertensao_factory(cbo_list, pessoa, disease_type=AtendimentoDiabetes, disease=Diabetes )
    atendimentoCollection = AtendimentoModelCollection(atendimento_list=atendimentos, unidade=pessoa.unidade_saude)
    pessoa.atendimentos = atendimentoCollection
    return pessoa