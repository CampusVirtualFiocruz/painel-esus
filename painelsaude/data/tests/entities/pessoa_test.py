from ...entities.pessoa import Pessoa, PessoaEnums, age_group, parse_pessoa_cadatro_mestre
from ...entities.atendimento_mestre import AtendimentoMestreCollection

from ..factories.unidade import unidade_factory
from ..factories.pessoa import pessoa_factory
from ..factories.atendimento_mestre_factory import atendimento_hipertensao_factory, atendimento_diabetes_factory

from pprint import pprint
import random
import pandas as pd

def test_pessoa_enuns():
    assert PessoaEnums.URBANA.value == 1
    assert PessoaEnums.get_label(PessoaEnums.URBANA.value) == 'Urbano'
    
    assert PessoaEnums.RURAL.value == 2
    assert PessoaEnums.get_label(PessoaEnums.RURAL.value) == 'Rural'
    
    assert PessoaEnums.MASCULINO.value == 3
    assert PessoaEnums.get_label(PessoaEnums.MASCULINO.value) == 'Masculino'
    
    assert PessoaEnums.FEMININO.value == 4
    assert PessoaEnums.get_label(PessoaEnums.FEMININO.value) == 'Feminino'
    
    
    
def test_pessoa():  
    pessoa = pessoa_factory(
        sexo=PessoaEnums.FEMININO,
    )
    assert pessoa.ds_sexo == PessoaEnums.FEMININO.value
    assert pessoa.ds_faixa_etaria == PessoaEnums.get_label(PessoaEnums.FAIXA_ETARIA_4.value)
    assert pessoa.ds_tipo_localizacao is PessoaEnums.URBANA 
    
    pessoa = pessoa_factory(
        sexo=PessoaEnums.MASCULINO,
        local=PessoaEnums.RURAL
    )
    assert pessoa.ds_sexo == PessoaEnums.MASCULINO.value
    assert pessoa.ds_faixa_etaria == PessoaEnums.get_label(PessoaEnums.FAIXA_ETARIA_4.value)
    assert pessoa.ds_tipo_localizacao is PessoaEnums.RURAL 
    
    pessoa = pessoa_factory(
        sexo=PessoaEnums.MASCULINO,
        local=PessoaEnums.RURAL,
        faixa_etaria=PessoaEnums.FAIXA_ETARIA_1
    )
    assert pessoa.ds_sexo == PessoaEnums.MASCULINO.value
    assert pessoa.ds_faixa_etaria == PessoaEnums.get_label(PessoaEnums.FAIXA_ETARIA_1.value)
    assert pessoa.ds_tipo_localizacao is PessoaEnums.RURAL
    
    
def test_pessoa_com_atendimento():
    atendimentos = []
    for i in range(5):
        is_hipertenso = True if random.randint(0,10) > 5 else False
        if is_hipertenso:
            which_filter = 'cid' if random.randint(0,10) > 5 else 'ciap'
        else:
            which_filter=None
            
        atendimentos.append(atendimento_hipertensao_factory(
            is_hipertenso= is_hipertenso,
            which_filter= which_filter
        ))
        
    unidade = unidade_factory()
    atendimento_list = AtendimentoMestreCollection(atendimento_list=atendimentos, unidade=unidade)
    pessoa = pessoa_factory(
        sexo=PessoaEnums.FEMININO,
    )
    pessoa.atendimentos = atendimento_list
    pessoa_dict = pessoa.to_dict()

def test_pessoa_com_atendimento_hipertensao():
    
    atendimentos = []            
    atendimentos.append(atendimento_hipertensao_factory(
        is_hipertenso= False,
    ))
        
    unidade = unidade_factory()
    atendimento_list = AtendimentoMestreCollection(atendimento_list=atendimentos, unidade=unidade)
    pessoa = pessoa_factory(
        sexo=PessoaEnums.FEMININO,
    )
    pessoa.atendimentos = atendimento_list
    pessoa_dict = pessoa.to_dict()
    pessoa_dict=parse_pessoa_cadatro_mestre(pessoa_dict=pessoa_dict, atendimentos=pessoa.atendimentos)
    
    assert pessoa_dict["st_hipertensao"] == False
    
    
    atendimentos=[]
    atendimentos.append(atendimento_hipertensao_factory(
        is_hipertenso= True,
        which_filter='cid'
    ))
    atendimento_list = AtendimentoMestreCollection(atendimento_list=atendimentos, unidade=unidade)
    pessoa = pessoa_factory(
        sexo=PessoaEnums.FEMININO,
    )
    pessoa.atendimentos = atendimento_list
    pessoa_dict = pessoa.to_dict()
    pessoa_dict=parse_pessoa_cadatro_mestre(pessoa_dict=pessoa_dict, atendimentos=pessoa.atendimentos)
    
    assert pessoa_dict["st_hipertensao"] == True
    # df = pd.json_normalize(pessoa_dict)
    # df.to_csv('output.csv', index=False)
    
def test_pessoa_com_atendimento_diabetes():
    
    atendimentos = []            
    atendimentos.append(atendimento_diabetes_factory(
        is_diabetes= False,
    ))
        
    unidade = unidade_factory()
    atendimento_list = AtendimentoMestreCollection(atendimento_list=atendimentos, unidade=unidade)
    pessoa = pessoa_factory(
        sexo=PessoaEnums.FEMININO,
    )
    pessoa.atendimentos = atendimento_list
    pessoa_dict = pessoa.to_dict()
    pessoa_dict=parse_pessoa_cadatro_mestre(pessoa_dict=pessoa_dict, atendimentos=pessoa.atendimentos)
    
    assert pessoa_dict["st_diabetes"] == False
    
    
    atendimentos=[]
    atendimentos.append(atendimento_diabetes_factory(
        is_diabetes= True,
        which_filter='cid'
    ))
    atendimento_list = AtendimentoMestreCollection(atendimento_list=atendimentos, unidade=unidade)
    pessoa = pessoa_factory(
        sexo=PessoaEnums.FEMININO,
    )
    pessoa.atendimentos = atendimento_list
    pessoa_dict = pessoa.to_dict()
    pessoa_dict=parse_pessoa_cadatro_mestre(pessoa_dict=pessoa_dict, atendimentos=pessoa.atendimentos)
    assert pessoa_dict["st_diabetes"] == True