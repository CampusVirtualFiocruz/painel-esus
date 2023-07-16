from ...entities.cbo import CboCollection
from ...entities.atendimento_diabetes_hipertensao import AtendimentoModelCollection, HipertensaoDictAdapter
from ...entities.pessoa import parse_pessoa_atendimento_model
from ...entities.procedimentos import set_all_diabetes_procedures

from ..factories.atendimento_hipertensao_diabetes import atendimento_hipertensao_factory_gen, atendimento_diabetes_factory_gen
from ..factories.pessoa import pessoa_factory
from ..factories.unidade import unidade_factory

import random
from pprint import pprint

def test_atendimento_hipertensao():
    cbo_collection = CboCollection()
    pessoa = pessoa_factory()
    pessoa = atendimento_hipertensao_factory_gen( random.choices(cbo_collection.cbo_list, k=3), pessoa )

    pessoa_dict = pessoa.to_dict()
    pessoa_dict = parse_pessoa_atendimento_model(pessoa_dict=pessoa_dict, atendimentos=pessoa.atendimentos)
    pprint(pessoa_dict)
    
def test_atendimento_diabetes():
    cbo_collection = CboCollection()
    pessoa = pessoa_factory()
    pessoa = atendimento_diabetes_factory_gen( random.choices(cbo_collection.cbo_list, k=3), pessoa )

    pessoa_dict = pessoa.to_dict()
    pessoa_dict = parse_pessoa_atendimento_model(pessoa_dict=pessoa_dict, atendimentos=pessoa.atendimentos)
    pprint(pessoa_dict)    
    
    
def test_atendimento_procedimentos():
    cbo_collection = CboCollection()
    pessoa = pessoa_factory()
    pessoa = atendimento_diabetes_factory_gen( random.choices(cbo_collection.cbo_list, k=3), pessoa )

    set_all_diabetes_procedures(pessoa=pessoa)
    pessoa_dict = pessoa.to_dict()
    pessoa_dict = parse_pessoa_atendimento_model(pessoa_dict=pessoa_dict, atendimentos=pessoa.atendimentos)
    pprint(pessoa_dict) 