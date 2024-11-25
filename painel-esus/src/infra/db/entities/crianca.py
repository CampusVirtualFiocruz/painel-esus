# pylint: disable=invalid-name
# pylint: disable=too-many-arguments
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship
from src.infra.db.entities.pessoas import Pessoas
from src.infra.db.settings.base import Base


class Crianca(Base):
    __tablename__ = "crianca"
    index = Column(Integer, primary_key=True, autoincrement=True)
    cidadao_pec = Column(Integer, ForeignKey("pessoas.cidadao_pec"))
    pessoa: Mapped[Pessoas] = relationship("Pessoas", uselist=False, lazy="subquery")

    indicador_atendimentos_medicos_enfermeiros = Column(Integer)
    data_ultimo_atendimento_medico_enfermeiro = Column(DateTime)
    atendimentos_medicos_enfermeiros_8d_vida = Column(Integer)
    atendimentos_medicos_enfermeiros_puericult = Column(Integer)
    data_ultimo_atendimento_medicos_enfermeiros_puericultura = Column(
        DateTime, name="data_ultimo_atendimento_medicos_enfermeiros_puericult"
    )
    indicador_atendimentos_medicos_enfermeiros_puericultura = Column(
        Integer, name="indicador_atendimentos_medicos_enfermeiros_puericult"
    )
    medicoes_peso_altura_ate2anos = Column(Integer)
    data_ultima_medicao_peso_altura_ate2anos = Column(DateTime)
    indicador_medicoes_peso_altura_ate2anos = Column(Integer)
    data_ultima_visita_domiciliar_acs = Column(DateTime)
    indicador_visitas_domiciliares_acs = Column(Integer)
    visitas_domiciliares_acs = Column(Integer)
    teste_pezinho = Column(Integer)
    indicador_teste_pezinho = Column(Integer)
    data_ultimo_teste_pezinho = Column(DateTime)
    atendimentos_odontologicos = Column(Integer)
    data_ultimo_atendimento_odontologico = Column(DateTime)
    indicador_atendimentos_odontologicos = Column(Integer)
    n_penta = Column(Integer, name="n_penta")
    n_polio = Column(Integer, name="n_polio")
    n__triplici = Column(Integer, name="n__triplici")
    data_ultima_vacina_penta = Column(DateTime, name="data_ultima_vacina_penta")
    data_ultima_vacina_polio = Column(DateTime, name="data_ultima_vacina_polio")
    data_ultima_vacina_triplici = Column(DateTime, name="data_ultima_vacina_triplici")
    indicador_vacinas_penta_polio_triplici = Column(
        Integer, name="indicador_vacinas_penta_polio_triplici"
    )
    n_medicos = Column(Integer, name="n_medicos")
    n_enfer = Column(Integer, name="n_enfer")
    n_fono = Column(Integer, name="n_fono")
    n_psicol = Column(Integer, name="n_psicol")
    n_educ_fisica = Column(Integer, name="n_educ_fisica")
    n_assist_social = Column(Integer, name="n_assist_social")
    n_tera_ocup = Column(Integer, name="n_tera_ocup")
    n_farmac = Column(Integer, name="n_farmac")
    n_fisio = Column(Integer, name="n_fisio")
    n_nutric = Column(Integer, name="n_nutric")
    n_ciru_dent = Column(Integer, name="n_ciru_dent")
    n_outros = Column(Integer, name="n_outros")
    total = Column(Integer, name="total")
