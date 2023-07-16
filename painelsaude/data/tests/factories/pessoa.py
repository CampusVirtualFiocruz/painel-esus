from ...entities.pessoa import PessoaEnums, Pessoa, age_group, age_range_by_age_group
from ..factories.unidade import unidade_factory

from typing import Union

from ..config.faker import faker
from dateutil.relativedelta import relativedelta
import datetime




def pessoa_factory(
    sexo = PessoaEnums.FEMININO, 
    local = PessoaEnums.URBANA,
    faixa_etaria = PessoaEnums.FAIXA_ETARIA_4
):
    if sexo.value == PessoaEnums.FEMININO.value:
         name = faker.name_female()
    else:
         name = faker.name_male()
        
    co_fat_cidadao_pec = faker.ssn()
    ds_tipo_localizacao = local
    st_vacinacao_em_dia = True
    st_hipertensao = True
    st_diabetes = True
    st_gestante = True
    ds_sexo = sexo.value
    
    age_range = age_range_by_age_group(PessoaEnums.get_label(faixa_etaria.value))
    
    dt_nascimento = faker.date_between(start_date = f'-{age_range[1]}y', end_date = f'-{age_range[0]}y')
    nu_idade = relativedelta(
        datetime.datetime.now(),
        datetime.datetime.fromisoformat(dt_nascimento.isoformat())
    ).years
    ds_faixa_etaria = age_group(int(nu_idade))
    
    unidade = unidade_factory()
    pessoa = Pessoa(
        co_fat_cidadao_pec=co_fat_cidadao_pec,
        ds_tipo_localizacao=ds_tipo_localizacao,
        st_vacinacao_em_dia=st_vacinacao_em_dia,
        st_hipertensao=st_hipertensao,
        st_diabetes=st_diabetes,
        st_gestante=st_gestante,
        ds_sexo=ds_sexo,
        dt_nascimento=dt_nascimento,
        nu_idade=nu_idade,
        ds_faixa_etaria=ds_faixa_etaria,
        unidade_saude=unidade,
        atendimentos= None,
        nome=name
    )
    
    return pessoa

def birthday_factory( min_age: int, max_age: int):
    return faker.date_of_birth(
            minimum_age = min_age,
            maximum_age = max_age
        )
def pessoa_factory_com_dt_nascimento(
    sexo = PessoaEnums.FEMININO, 
    local = PessoaEnums.URBANA,
    dt_nascimento: datetime  = None
):
    if sexo.value == PessoaEnums.FEMININO.value:
         name = faker.name_female()
    else:
         name = faker.name_male()
        
    co_fat_cidadao_pec = faker.ssn()
    ds_tipo_localizacao = local
    st_vacinacao_em_dia = True
    st_hipertensao = True
    st_diabetes = True
    st_gestante = False
    ds_sexo = sexo.value
    
    nu_idade = relativedelta(
        datetime.datetime.now(),
        datetime.datetime.fromisoformat(dt_nascimento.isoformat())
    ).years
    ds_faixa_etaria = age_group(int(nu_idade))
    
    unidade = unidade_factory()
    pessoa = Pessoa(
        co_fat_cidadao_pec=co_fat_cidadao_pec,
        ds_tipo_localizacao=ds_tipo_localizacao,
        st_vacinacao_em_dia=st_vacinacao_em_dia,
        st_hipertensao=st_hipertensao,
        st_diabetes=st_diabetes,
        st_gestante=st_gestante,
        ds_sexo=ds_sexo,
        dt_nascimento=dt_nascimento,
        nu_idade=nu_idade,
        ds_faixa_etaria=ds_faixa_etaria,
        unidade_saude=unidade,
        atendimentos= None,
        nome=name
    )
    
    return pessoa