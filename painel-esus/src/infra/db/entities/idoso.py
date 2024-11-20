# pylint: disable=invalid-name
# pylint: disable=too-many-arguments
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from src.infra.db.entities.pessoas import Pessoas
from src.infra.db.settings.base import Base


class Idoso(Base):
    __tablename__ = "idoso"
    index = Column(Integer, primary_key=True, autoincrement=True)
    cidadao_pec = Column(Integer, ForeignKey("pessoas.cidadao_pec"))
    pessoa: Mapped[Pessoas] = relationship("Pessoas", uselist=False, lazy="subquery")

    indicador_atendimentos_medicos_enfermeiros = Column(Integer)
    data_ultimo_atendimento_medico_enfermeiro = Column(Date)
    atendimentos_medicos_enfermeiros_8d_vida = Column(Integer)
    atendimentos_medicos_enfermeiros_puericult = Column(Integer)
    data_ultimo_atendimento_medicos_enfermeiros_puericult = Column(Date)
    indicador_atendimentos_medicos_enfermeiros_puericult = Column(Integer)
    medicoes_peso_altura_ate2anos = Column(Integer)
    data_ultima_medicao_peso_altura_ate2anos = Column(Date)
    indicador_medicoes_peso_altura_ate2anos = Column(Integer)
    teste_pezinho = Column(Integer)
    indicador_teste_pezinho = Column(Integer)
    data_ultimo_teste_pezinho = Column(Date)
    atendimentos_odontologicos = Column(Integer)
    data_ultimo_atendimento_odontologico = Column(Date)
    indicador_atendimentos_odontologicos = Column(Integer)
    visitas_domiciliares_acs = Column(Integer)
    data_ultima_visita_domiciliar_acs = Column(Date)
    indicador_visitas_domiciliares_acs = Column(Integer)
