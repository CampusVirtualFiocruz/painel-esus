# pylint: disable=invalid-name
# pylint: disable=too-many-arguments
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship
from src.infra.db.entities.pessoas import Pessoas
from src.infra.db.settings.base import Base


class Idoso(Base):
    __tablename__ = "idoso"
    index = Column(Integer, primary_key=True, autoincrement=True)
    cidadao_pec = Column(Integer, ForeignKey("pessoas.cidadao_pec"))
    pessoa: Mapped[Pessoas] = relationship("Pessoas", uselist=False, lazy="subquery")

    atendimentos_medicos = Column(Integer) 
    data_ultimo_atendimento_medicos = Column(DateTime) 
    indicador_atendimentos_medicos = Column(Integer)
    medicoes_peso_altura = Column(Integer)
    data_ultima_medicao_peso_altura = Column(DateTime) 
    indicador_medicoes_peso_altura = Column(Integer)
    imc =  Column(Float)
    categoria_imc = Column(String)
    registros_creatinina = Column(Integer) 
    data_ultimo_registro_creatinina = Column(DateTime) 
    indicador_registros_creatinina = Column(Integer)
    vacinas_influenza = Column(Integer) 
    data_ultima_vacina_influenza = Column(DateTime)  
    indicador_vacinas_influenza = Column(Integer)
    atendimentos_odontologicos = Column(Integer) 
    data_ultimo_atendimento_odontologico = Column(DateTime) 
    indicador_atendimento_odontologico = Column(Integer)
    visitas_domiciliares_acs = Column(Integer) 
    data_ultima_visita_domiciliar_acs = Column(DateTime)  
    indicador_visitas_domiciliares_acs = Column(Integer)
    data_ultima_vacina_influenza = Column(DateTime)  
    indicador_vacinas_influenza = Column(Integer)
    atendimentos_odontologicos = Column(Integer) 
    data_ultimo_atendimento_odontologico = Column(DateTime) 
    indicador_atendimento_odontologico = Column(Integer)
    visitas_domiciliares_acs = Column(Integer) 
    data_ultima_visita_domiciliar_acs = Column(DateTime)  
    indicador_visitas_domiciliares_acs = Column(Integer)
