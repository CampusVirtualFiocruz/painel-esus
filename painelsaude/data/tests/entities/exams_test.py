
from ...entities.procedimentos import ArterialHypertensionExamsList, set_all_arterial_hipertension_procedures
from ..factories.pessoa import pessoa_factory_com_dt_nascimento, birthday_factory
from ..factories.atendimento_hipertensao_diabetes import atendimento_diabetes_factory_gen
from ...entities.cbo import CboCollection
from ...entities.procedimentos import ExamStatus

import random


def test_one():
    exams_list = ArterialHypertensionExamsList()
    assert len(exams_list.list) > 0
    
    print( list(exams_list.list[0].exams)[0] )
    
def test_add_procedure_to_person():
    cbo_collection = CboCollection()
    pessoa = pessoa_factory_com_dt_nascimento(dt_nascimento=birthday_factory(max_age=35, min_age=18))
    pessoa = atendimento_diabetes_factory_gen(
            random.choices(
                cbo_collection.cbo_list,
                k=random.randint(1, 10)
            ),
            pessoa
        )
    
    avaliados = pessoa.atendimentos.atendimento_list[0].ds_filtro_proced_avaliados
    solicitados = pessoa.atendimentos.atendimento_list[0].ds_filtro_proced_solicitados
    assert len(avaliados) == 1
    assert avaliados[0] == ''
    assert len(solicitados) == 1
    assert solicitados[0] == ''
    
    set_all_arterial_hipertension_procedures(pessoa=pessoa)  
    
    avaliados = pessoa.atendimentos.atendimento_list[0].ds_filtro_proced_avaliados
    solicitados = pessoa.atendimentos.atendimento_list[0].ds_filtro_proced_solicitados
    assert len(avaliados) > 1
    assert len(solicitados) > 1
    
    len_before = len(solicitados)
    item = random.choice(pessoa.atendimentos.atendimento_list[0].ds_filtro_proced_solicitados)
    pessoa.atendimentos.atendimento_list[0].ds_filtro_proced_solicitados.remove(item)
    solicitados = pessoa.atendimentos.atendimento_list[0].ds_filtro_proced_solicitados
    print(solicitados)
    assert len_before > len(solicitados)
    
def test_exam_computation():
    row = {
        'ds_filtro_proced_avaliados': '|0202010473|,|ABEX003|,|0202010017|,|0202010600|,|0202010295|,|0301100039|',
        'ds_filtro_proced_solicitados': '|0202010473|,|ABEX003|,|0202010017|,|0202010600|,|0202010295|,|0301100039|',        
    }
    exams = ArterialHypertensionExamsList()
    exams.list[0].checkPresence(row)
    
    assert exams.list[0].requested == 0
    assert exams.list[0].evaluated == 0
    
    row = {
        'ds_filtro_proced_avaliados': '|0202010473|,|ABEX003|,|0202010017|,|0202010600|,|0202010295|',
        'ds_filtro_proced_solicitados': '|0202010473|,|ABEX003|,|0202010017|,|0202010600|,|0202010295|',        
    }
    exams = ArterialHypertensionExamsList()
    exams.list[0].checkPresence(row)
    
    assert exams.list[0].requested == 1
    assert exams.list[0].evaluated == 0
    
    row = {
        'ds_filtro_proced_solicitados': '|0202010473|,|ABEX003|,|0202010017|,|0202010600|,|0202010295|,|0301100039|',
        'ds_filtro_proced_avaliados': '|0202010473|,|ABEX003|,|0202010017|,|0202010600|,|0202010295|',        
    }
    exams = ArterialHypertensionExamsList()
    exams.list[0].checkPresence(row)
    
    assert exams.list[0].requested == 0
    assert exams.list[0].evaluated == 1
    