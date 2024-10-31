# pylint: disable=invalid-name
# pylint: disable=too-many-arguments
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import Integer
from sqlalchemy import String
from src.infra.db.settings.base import Base


class Pessoas(Base):
    __tablename__ = "pessoas"
    cidadao_pec = Column(Integer,  primary_key=True, autoincrement=True)
    co_cidadao = Column(Integer)
    raca_cor = Column(String)
    cpf = Column(String)
    cns = Column(String)
    nome = Column(String)
    nome_social = Column(String)
    data_nascimento = Column(Date)
    idade = Column(Integer)
    sexo = Column(String)
    identidade_genero = Column(String)
    telefone = Column(String)
    ultima_atualizacao_cidadao = Column(Date)
    ultima_atualizacao_fcd = Column(Date)
    tipo_endereco = Column(String)
    endereco = Column(String)
    complemento = Column(String)
    numero = Column(String)
    bairro = Column(String)
    cep = Column(String)
    tipo_localidade = Column(String)
    
    def __repr__(self):
        return f"""
        Nome: {self.nome}
        cidadao_pec: {self.cidadao_pec}
        cpf: {self.cpf}
        """
