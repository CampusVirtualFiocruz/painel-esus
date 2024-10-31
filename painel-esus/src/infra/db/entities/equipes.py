# pylint: disable=invalid-name
# pylint: disable=too-many-arguments
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from src.infra.db.entities.pessoas import Pessoas
from src.infra.db.settings.base import Base


class Equipes(Base):
    __tablename__ = "equipes"
    index = Column(Integer,  primary_key=True, autoincrement=True)
    cidadao_pec=Column(Integer, ForeignKey("pessoas.cidadao_pec"))
    codigo_unidade_saude=Column(Integer) 
    nome_unidade_saude=Column(String) 
    codigo_equipe=Column(Integer) 
    nome_equipe=Column(String) 
    ine=Column(String) 
    micro_area=Column(String)
    pessoa: Mapped[Pessoas] = relationship("Pessoas", uselist=False, lazy="subquery")
