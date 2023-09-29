import pandas as pd
import pytest 

from ...infra.config.connection import con

from .individual_care import get_invidual_cares_not_in, get_all_cares, get_invidual_cares, generate_list_for_all_cares_by_class, group_by_year_and_class, get_list_for_all_cares_by_class_grouped_by_year
from .stub.infeccoes_agudas import INFECCOES_AGUDAS
from .accute_infections import ClassifyDF, ExanthematousFever, IntestinalInfections, NonspecificFever, RespiratoryInfections

def test_quantidade_atendimentos():
    individual_cares = get_invidual_cares(con, [], INFECCOES_AGUDAS)
    all_cares = get_all_cares(con, [])
    individual_cares_not_in = get_invidual_cares_not_in(con, [], INFECCOES_AGUDAS)
    
    all_cares.to_csv('/tmp/atendimentos.csv')
    individual_cares.to_csv('/tmp/atendimentos_individual.csv')
    individual_cares_not_in.to_csv('/tmp/atendimentos_individual_not_in.csv')

    all_size = all_cares.shape[0]
    in_size = len(individual_cares.co_seq_fat_atd_ind.unique().tolist())
    not_in_size = individual_cares_not_in.shape[0]
    assert (in_size+not_in_size) == all_size
    
def test_total_appointments_05_2021_test():
    total = 216
    infeccao_respiratoria = RespiratoryInfections()
    infeccao_intestinal = IntestinalInfections()
    febre_exantematica = ExanthematousFever()
    febre_inespecifica = NonspecificFever()

    target_list = [infeccao_respiratoria, infeccao_intestinal, febre_exantematica, febre_inespecifica]

    dd = get_list_for_all_cares_by_class_grouped_by_year(con, [], INFECCOES_AGUDAS, target_list, ClassifyDF)
    assert total == dd[(dd['ano'] == 2021) & (dd['mes'] == 5)]['count'].sum()    
    
def test_total_appointments_05_2021_08_2021test():
    total = 216
    infeccao_respiratoria = RespiratoryInfections()
    infeccao_intestinal = IntestinalInfections()
    febre_exantematica = ExanthematousFever()
    febre_inespecifica = NonspecificFever()

    target_list = [infeccao_respiratoria, infeccao_intestinal, febre_exantematica, febre_inespecifica]

    dd = get_list_for_all_cares_by_class_grouped_by_year(con, [], INFECCOES_AGUDAS, target_list, ClassifyDF)
    # assert total == dd[(dd['ano'] == 2021) & (dd['mes'] == 5)]['count'].sum()    
    print(dd[(dd['ano'] == 2021) &  (dd['mes'].isin([5,6])) ].head(10))

    

