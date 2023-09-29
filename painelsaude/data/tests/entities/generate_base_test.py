from ...entities.base import Base, BaseEnums
from ...entities.pessoa import parse_pessoa_cadatro_mestre, parse_pessoa_atendimento_model
from ...entities.cbo import CboCollection
from ...entities.procedimentos import (
    set_all_arterial_hipertension_procedures,
    set_all_diabetes_procedures,
    set_data_arterial_hipertension_procedures,
    set_data_diabetes_procedures
)

from ..factories.pessoa import birthday_factory
from ..factories.atendimento_hipertensao_diabetes import atendimento_hipertensao_factory_gen, atendimento_diabetes_factory_gen
from ..factories.unidade import unidade_factory

from dateutil.relativedelta import relativedelta
import datetime
import random
from pprint import pprint
import pandas as pd
import math


def test_segmentacao_base():

    base = Base(
        population=17683
    )
    assert base.masculino[BaseEnums.FAIXA_ETARIA_1.value] == 584

    assert len(base.masculino) == len(base.feminino)
    assert len(base.masculino) == len(base.range_faixa_etaria)
    assert len(base.masculino_percent) == len(base.range_faixa_etaria)
    print(len(base.range_faixa_etaria))

    for i in range(len(base.feminino)):
        faixa = base.range_faixa_etaria[i]

        for j in range(10):
            dt_nascimento = birthday_factory(
                min_age=faixa[0], max_age=faixa[1])
            idade = relativedelta(
                datetime.datetime.now(),
                datetime.datetime.fromisoformat(dt_nascimento.isoformat())
            ).years

            assert idade <= faixa[1]
            assert idade >= faixa[0]


def test_geracao():
    base = Base(
        population=17683
    )
    pessoas = base.generate_base()
    base.apply_hypertension(pessoas)
    base.apply_diabetes(pessoas)

    assert base.population == len(pessoas)+1
    pessoas_dict = []
    for pessoa in pessoas:

        p = pessoa.to_dict()
        p = parse_pessoa_cadatro_mestre(
            pessoa_dict=p, atendimentos=pessoa.atendimentos)
        pessoas_dict.append(p)

    df = pd.json_normalize(pessoas_dict)

    df.to_excel(
        '../../../files/CADASTRO_MESTRE_JOIN_AT_IND_GEST_HIP_DIAB_JOIN_UNIDADES_CLEAN_PAINEL.xlsx', index=False)

    assert len(pessoas[0].atendimentos.atendimento_list) > 0
    [pessoa.update() for pessoa in pessoas]
    assert pessoas[0].st_hipertensao == False

    pessoas_hipertensao = list(filter(lambda x: x.st_hipertensao, pessoas))
    pessoas_hipertensao_dict = []
    total_exec = 0
    cbo_collection = CboCollection()

    number_cases = [0, 0, 0, 0, 0, 0, 0, 0]
    for pessoa in pessoas_hipertensao:
        pessoa = atendimento_hipertensao_factory_gen(
            random.choices(
                cbo_collection.cbo_list,
                k=random.randint(1, 10)
            ),
            pessoa
        )
        # set_all_arterial_hipertension_procedures(pessoa=pessoa)
        set_data_arterial_hipertension_procedures(
            pessoa=pessoa, number_cases=number_cases)

        pessoa_dict = pessoa.to_dict()
        pessoa_dict = parse_pessoa_atendimento_model(
            pessoa_dict=pessoa_dict, atendimentos=pessoa.atendimentos)
        pessoas_hipertensao_dict.append(pessoa_dict)

    df = pd.json_normalize(pessoas_hipertensao_dict)
    df.to_excel(
        '../../../files/BASE_ATENDIMENTOS_X_HIPERTENSAO.xlsx', index=False)

    pessoas_diabetes = list(filter(lambda x: x.st_diabetes, pessoas))
    pessoas_diabetes_dict = []
    for pessoa in pessoas_diabetes:
        pessoa = atendimento_diabetes_factory_gen(
            random.choices(
                cbo_collection.cbo_list,
                k=random.randint(1, 10)
            ),
            pessoa
        )
        # set_all_diabetes_procedures(pessoa=pessoa)
        set_data_diabetes_procedures(pessoa=pessoa)
        pessoa_dict = pessoa.to_dict()
        pessoa_dict = parse_pessoa_atendimento_model(
            pessoa_dict=pessoa_dict, atendimentos=pessoa.atendimentos, type="diabetes")
        pessoas_diabetes_dict.append(pessoa_dict)

    df = pd.json_normalize(pessoas_diabetes_dict)
    # df.to_excel('../../../files/BASE_ATENDIMENTOS_X_DIABETICOS.xlsx', index=False)
