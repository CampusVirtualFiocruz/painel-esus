# pylint: disable=invalid-name
# pylint: disable=too-many-arguments
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String
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
    data_nascimento = Column(DateTime)
    idade = Column(Integer)
    sexo = Column(String)
    identidade_genero = Column(String)
    telefone = Column(String)
    ultima_atualizacao_cidadao = Column(DateTime)
    ultima_atualizacao_fcd = Column(DateTime)
    tipo_endereco = Column(String)
    endereco = Column(String)
    complemento = Column(String)
    numero = Column(String)
    bairro = Column(String)
    cep = Column(String)
    tipo_localidade = Column(String)
    diferenca_ultima_atualizacao_cidadao = Column(Integer)
    diferenca_ultima_atualizacao_fcd = Column(Integer)
    codigo_equipe_vinculada = Column(Integer)
    codigo_unidade_saude = Column(Integer)
    # st_usar_cadastro_individual = Column(Boolean)
    st_recusa_cadastro = Column(Boolean)

    acompanhamento = Column(String)
    status_cadastro = Column(String)
    nu_micro_area_domicilio = Column(String)
    nome_equipe = Column(String)
    nome_unidade_saude = Column(String)
    fci_att_2anos = Column(Integer)
    fcdt_att_2anos = Column(Integer)
    alerta_status_cadastro = Column(Integer)
    alerta = Column(Integer)
    tipo_ident_cpf_cns = Column(Integer)
    faixa_etaria = Column(String)
    st_recusa_cadastro= Column(Boolean)

    def __repr__(self):
        return f"""
        Nome: {self.nome}
        cidadao_pec: {self.cidadao_pec}
        cpf: {self.cpf}
        """
