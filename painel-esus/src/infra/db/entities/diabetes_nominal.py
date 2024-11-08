# pylint: disable=invalid-name
# pylint: disable=too-many-arguments
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from src.infra.db.entities.pessoas import Pessoas
from src.infra.db.settings.base import Base

# class DiabetesNominal(Base):
#     __tablename__ = "diabetes_nominal"
#     co_fat_cidadao_pec = Column(Integer,  primary_key=True, autoincrement=True)
#     no_cidadao = Column(String)
#     nu_cns = Column(String)
#     nu_cpf = Column(String)
#     no_sexo = Column(String)
#     no_raca_cor = Column(String)
#     nu_micro_area = Column(String)
#     nu_area = Column(String)
#     dt_nascimento = Column(Date)
#     idade = Column(Integer)
#     cids = Column(String)
#     min_date = Column(String)
#     ds_logradouro = Column(String)
#     no_bairro = Column(String)
#     nu_numero = Column(String)
#     ds_cep = Column(String)
#     no_localidade = Column(String)
#     no_uf = Column(String)
#     sg_uf = Column(String)
#     no_tipo_logradouro = Column(String)
#     co_dim_equipe = Column(Integer)
#     co_dim_unidade_saude = Column(String)
#     co_dim_tempo = Column(Date)
#     data_ultima_visita_acs = Column(Integer)
#     alerta_visita_acs = Column(Boolean)
#     total_consulta_individual_medico = Column(Integer)
#     alerta_total_de_consultas_medico = Column(Boolean)
#     ultimo_atendimento_medico = Column(Date)
#     alerta_ultima_consulta_medico = Column(Boolean)
#     ultimo_atendimento_odonto = Column(Date)
#     alerta_ultima_consulta_odontologica = Column(Boolean)
#     ultima_data_afericao_pa = Column(Date)
#     alerta_afericao_pa = Column(Boolean)
#     ultima_data_glicemia_capilar = Column(Date)
#     alerta_ultima_glicemia_capilar = Column(Boolean)
#     ultima_data_hemoglobina_glicada = Column(Date)
#     alerta_ultima_hemoglobina_glicada = Column(Boolean)
#     ds_tipo_localizacao = Column(String)
#     equipe = Column(String)

#     def get_pessoa() ->Pessoas:
#         return self.pessoa

class DiabetesNominal(Base):
    __tablename__ = "diabetes_nominal"
    
    index = Column(Integer, primary_key=True)
    co_fat_cidadao_pec = Column(Integer, ForeignKey("pessoas.cidadao_pec"))
    diagnostico = Column(String)
    cids = Column(String)
    min_date = Column(String)
    pessoa: Mapped[Pessoas] = relationship("Pessoas", uselist=False, lazy="subquery")
    
    data_ultima_visita_acs = Column(Integer)
    alerta_visita_acs = Column(Boolean)
    total_consulta_individual_medico = Column(Integer)
    alerta_total_de_consultas_medico = Column(Boolean)
    ultimo_atendimento_medico = Column(Date)
    alerta_ultima_consulta_medico = Column(Boolean)
    ultimo_atendimento_odonto = Column(Date)
    alerta_ultima_consulta_odontologica = Column(Boolean)
    ultima_data_afericao_pa = Column(Date)
    alerta_afericao_pa = Column(Boolean)
    ultima_data_glicemia_capilar = Column(Date)
    alerta_ultima_glicemia_capilar = Column(Boolean)
    ultima_data_hemoglobina_glicada = Column(Date)
    alerta_ultima_hemoglobina_glicada = Column(Boolean)

    def get_pessoa(self) ->Pessoas:
        return self.pessoa
