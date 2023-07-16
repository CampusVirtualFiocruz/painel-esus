from ...entities.atendimento_mestre import AtendimentoMestre
from ...entities.diseases import Hipertensao, Diabetes, Disease
from ..config.faker import faker

import random
from typing import Union, Literal

which_filter_literal = Literal["cid", "ciap", None]

def atendimento_factory(
    is_hipertenso = False,
    which_filter: which_filter_literal = None, 
    range_date_str= ['-1y', 'today'],
    disease: Disease = None
):
    """_summary_

    Args:
        which_filter (Union[ &#39;cid&#39;,&#39;ciap&#39;, None], optional): _description_. Defaults to None.
        is_hipertenso (bool, optional): _description_. Defaults to False.
        range_date_str (list, optional): _description_. Defaults to ['-1y', 'today'].
        disease: Disease

    Returns:
        _type_: _description_
    """
    if disease is None:
        raise Exception('No disease')
    
    cad_filtro_cids = ['']
    cad_filtro_ciap = ['']
    if is_hipertenso and which_filter is None:
        random_cids_choice = 1 if random.randint(1, 100) > 50 else 0
    
        if random_cids_choice:
            cad_filtro_cids= [ random.choice(disease.cids) ]
            cad_filtro_ciap = [ '' ]
        else:
            cad_filtro_cids = [ '']
            cad_filtro_ciap= [ random.choice(disease.ciaps) ]
            
    cad_proced_avaliados = [''] 
    cad_proced_solicitados = [''] 
    
    if is_hipertenso:
        if which_filter == 'cid':
            cad_filtro_cids= [ random.choice(disease.cids), random.choice(disease.cids) ]
            cad_filtro_ciap = [ '']
        else:
            cad_filtro_cids = [ '']
            cad_filtro_ciap= [ random.choice(disease.ciaps) ]
    
    
    dt_nascimento = faker.date_between(start_date = range_date_str[0], end_date=range_date_str[1])
    
    
        
    atendimento = AtendimentoMestre(
        dt_atendimento= dt_nascimento.strftime("%Y%m%d"),
        cad_filtro_cids = cad_filtro_cids,
        cad_filtro_ciap = cad_filtro_ciap,
        cad_proced_avaliados=cad_proced_avaliados,
        cad_proced_solicitados=cad_proced_solicitados,
        nu_idade_gestacional = 0,
        nu_gestas_previas = 0
    )
    return atendimento
    
def atendimento_hipertensao_factory( 
                                    is_hipertenso = False,
                                    which_filter: which_filter_literal = None, 
                                    range_date_str= ['-1y', 'today']):
    """_summary_

    Args:
        which_filter (Union[ &#39;cid&#39;,&#39;ciap&#39;, None], optional): _description_. Defaults to None.
        is_hipertenso (bool, optional): _description_. Defaults to False.
        range_date_str (list, optional): _description_. Defaults to ['-1y', 'today'].

    Returns:
        _type_: _description_
    """
    
    hipertensao = Hipertensao()
    return atendimento_factory(is_hipertenso, which_filter, range_date_str, hipertensao)
    

def atendimento_diabetes_factory( 
                                    is_diabetes = False,
                                    which_filter: which_filter_literal = None, 
                                    range_date_str= ['-1y', 'today']):
    """_summary_

    Args:
        which_filter (Union[ &#39;cid&#39;,&#39;ciap&#39;, None], optional): _description_. Defaults to None.
        is_diabetes (bool, optional): _description_. Defaults to False.
        range_date_str (list, optional): _description_. Defaults to ['-1y', 'today'].

    Returns:
        _type_: _description_
    """
    
    diabetes = Diabetes()
    return atendimento_factory(is_diabetes, which_filter, range_date_str, diabetes)