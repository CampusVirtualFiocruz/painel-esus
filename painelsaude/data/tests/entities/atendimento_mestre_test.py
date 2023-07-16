from ...entities.atendimento_mestre import AtendimentoMestre, AtendimentoMestreCollection
from ..factories.atendimento_mestre_factory import atendimento_hipertensao_factory
from ..factories.unidade import unidade_factory
from ...entities.diseases import Diabetes,Hipertensao
from ..config.faker import faker


from pprint import pprint

  
def test_atendimento_mestre():
     atendimento_mestre = AtendimentoMestre(
        dt_atendimento='20200101',
        cad_filtro_ciap=[],
        cad_filtro_cids=["J11", "J12"],
        cad_proced_solicitados=[''],
        cad_proced_avaliados=[''],
        nu_gestas_previas=0,
        nu_idade_gestacional=0
    )
     atendimento_mestre2 = AtendimentoMestre(
        dt_atendimento='20200101',
        cad_filtro_ciap=['ABP001'],
        cad_filtro_cids=["J11", "J12"],
        cad_proced_solicitados=[''],
        cad_proced_avaliados=[''],
        nu_gestas_previas=1,
        nu_idade_gestacional=1
    )
     unidade = unidade_factory()
     colec = AtendimentoMestreCollection( [atendimento_mestre, atendimento_mestre2], unidade)
     
     hipertensao = Hipertensao()
     assert hipertensao.check( colec.cad_filtro_cids ) is False
     
     atendimento_mestre3 = AtendimentoMestre(
        dt_atendimento='20200101',
        cad_filtro_ciap=['ABP001'],
        cad_filtro_cids=["J11", "K86"],
        cad_proced_solicitados=[''],
        cad_proced_avaliados=[''],
        nu_gestas_previas=1,
        nu_idade_gestacional=1
    )
     colec = AtendimentoMestreCollection( [atendimento_mestre, atendimento_mestre2, atendimento_mestre3], unidade = unidade)
     assert hipertensao.check( colec.cad_filtro_cids ) is True
     
 
def test_atendimento_diabetes():
    
    atendimento_mestre = AtendimentoMestre(
        dt_atendimento='20200101',
        cad_filtro_ciap=[],
        cad_filtro_cids=["J11", "J12"],
        cad_proced_solicitados=[''],
        cad_proced_avaliados=[''],
        nu_gestas_previas=0,
        nu_idade_gestacional=0
    )
    atendimento_mestre2 = AtendimentoMestre(
        dt_atendimento='20200101',
        cad_filtro_ciap=['ABP001'],
        cad_filtro_cids=["J11", "E122"],
        cad_proced_solicitados=[''],
        cad_proced_avaliados=[''],
        nu_gestas_previas=1,
        nu_idade_gestacional=1
    )
    colec = AtendimentoMestreCollection( [atendimento_mestre, atendimento_mestre2], unidade=unidade_factory())
     
    hipertensao = Hipertensao()
    diabetes = Diabetes()
    assert hipertensao.check( colec.cad_filtro_cids ) is False
    assert diabetes.check( colec.cad_filtro_cids ) is True
    
def test_atendimento_factory_cid():
    atendimento = atendimento_hipertensao_factory(
        is_hipertenso=True,
        which_filter="cid"
    )
    hipertensao = Hipertensao()
    assert len(atendimento.cad_filtro_ciap) == 1
    assert len(atendimento.cad_filtro_cids) > 0
    assert hipertensao.check( atendimento.cad_filtro_cids ) is True
    
def test_atendimento_factory_ciap():
    atendimento = atendimento_hipertensao_factory(
        is_hipertenso=True,
        which_filter="ciap"
    )
    hipertensao = Hipertensao()
    assert len(atendimento.cad_filtro_ciap) > 0
    assert len(atendimento.cad_filtro_cids) == 1
    assert hipertensao.check( atendimento.cad_filtro_ciap ) is True
    
    
    
    pprint(atendimento)
    