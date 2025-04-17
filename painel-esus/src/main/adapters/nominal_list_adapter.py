# pylint: disable=R0902, W4901, W0611, C0103
import pandas as pd
import math
import numpy as np
from src.domain.entities.diabetes import Diabetes
from src.domain.entities.hypertension import Hypertension
from src.infra.db.entities.crianca import Crianca
from src.infra.db.entities.diabetes_nominal import DiabetesNominal
from src.infra.db.entities.hipertensao_nominal import HipertensaoNominal
from src.infra.db.entities.pessoas import Pessoas
import re
from src.env.conf import getenv

def mock_word(phrase, gap=2, skip_first=False):
        mock = getenv("MOCK", False, False) == 'True'
        if not mock or phrase=="" or phrase is None:
            return phrase
        words = phrase.split()
        if skip_first:
            return " ".join([words[0],*[word[:gap]+"".join(["*" for n in word[gap:]]) for word in words[1:]]])
        else:
            return " ".join([word[:gap]+"".join(["*" for n in word[gap:]]) for word in words])

def is_sequence(obj):
    return isinstance(obj, (np.ndarray, np.generic))

class AlertRecord:
    def __init__(
        self,
        descricao: str,
        data,
        exibir_alerta,
        tipo_alerta: str,
        classificacao: str = None
    ):
        self.descricao = descricao
        self.data = data
        self.exibir_alerta = exibir_alerta
        self.tipo_alerta = tipo_alerta
        self.classificacao = classificacao

    def to_dict(self):
        response = {
                "descricao": self.descricao,
                "data": self.data,
                "exibirAlerta": self.exibir_alerta,
                "tipoAlerta": self.tipo_alerta,
            }
        if self.classificacao is not None:
            response["classificacao"] = self.classificacao
        return dict(
            response
        )


class BaseNominalAdapter:
    def __init__(self, user):
        if 'alerta_afericao_pa' not in user:
            print('---------->')
            print(user)
            return 
        endereco = self.get(user, 'endereco')
        endereco += " " + self.get(user, 'numero')
        endereco += " " + self.get(user, 'bairro')

        self.nome = user["nome"]
        self.nome_social = "-"
        self.tipo_localidade = self.get(user,"tipo_localidade")
        self.cpf = user["cpf"]
        self.cns = user["cns"]
        self.data_nascimento = self.get(user,"data_nascimento")
        self.idade = user["idade"]
        self.sexo = user["sexo"]
        self.equipe = self.get(user,"nome_equipe")
        self.microarea = self.get(user,"micro_area")
        self.endereco = endereco
        self.tipo_logradouro = self.get(user,"tipo_endereco")
        self.complemento = self.get(user,"complemento")
        self.cep = user["cep"]
        self.telefone = user["telefone"]
        self.registros = []
        self.primeiro_registro = self.get(user,"dt_primeiro_reg_condicao")

    def get(self, item, field):
        return item[field] if field in item and item[field] is not None else ""
    
class HypertensionNominalListAdapter(BaseNominalAdapter):

    def __init__(self, user):
        super().__init__(user)
        self.diagnostico = 'cid/ciaps' if user['autoreferido'] is None or user['autoreferido'] == 0 else 'autoreferido'

        alertas = [
            "alerta_afericao_pa",
            "alerta_creatinina",
            "alerta_ultima_consulta_medico",
            "alerta_ultima_consulta_odontologica",
            "alerta_visita_acs",
        ]
        for i in alertas:
            user[i] = user[i] if isinstance(user[i], int) else 0

        self.possui_alertas =  (
            not user["alerta_afericao_pa"]
            or not user["alerta_creatinina"]
            or not user["alerta_total_de_consultas_medico"]
            or not user["alerta_ultima_consulta_medico"]
            or not user["alerta_ultima_consulta_odontologica"]
            or not user["alerta_visita_acs"]
        )
        self.cids = user["codigos_1atend"].tolist() if is_sequence(user["codigos_1atend"]) else []
        self.registros.append(
            AlertRecord(
                data= user["ultima_data_afericao_pa"],
                exibir_alerta=not user["alerta_afericao_pa"],
                descricao="Data da última aferição de PA",
                tipo_alerta="alerta-afericao-pa-maior-6-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["ultima_data_creatinina"],
                exibir_alerta=(
                    not user["alerta_creatinina"]
                ),
                descricao="Data da última avaliação da Dosagem de Creatinina",
                tipo_alerta="alerta-creatinina-maior-6-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["total_consulta_med_enferm"],
                exibir_alerta=False,
                descricao="Total de consultas Médicas ou de Enfermagem",
                tipo_alerta="alerta-total-de-consultas-medico-menor-2",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["ultimo_atendimento_medico"],
                exibir_alerta=not user["alerta_ultima_consulta_medico"],
                descricao="Data da última consulta médica ou de Enfermagem",
                tipo_alerta="alerta-ultimo-atendimento-medico-maior-6-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=(
                    user["ultimo_atendimento_odonto"]
                ),
                exibir_alerta=not user["alerta_ultima_consulta_odontologica"],
                descricao="Data da última consulta odontológica",
                tipo_alerta="alerta-ultimo-atendimento-odonto-maior-6-meses",
            )
        )

        self.registros.append(
            AlertRecord(
                data=(
                    user["dt_ultima_visita_acs"]
                ),
                exibir_alerta=not user["alerta_visita_acs"],
                descricao="Data da última visita ACS",
                tipo_alerta="alerta-data-ultima-visita-acs-maior-6-meses",
            )
        )

    def to_dict(self):
        return dict(
            {
                "nome":  mock_word(self.nome, 3, True),
                "nomeSocialSelecionado": mock_word(self.nome_social, 3, True),
                "zonaUrbana": self.tipo_localidade == "Urbana",
                "zonaRural": self.tipo_localidade == "Rural",
                "possuiAlertas": self.possui_alertas,
                "cpf": mock_word(self.cpf,4),
                "cns": mock_word(self.cns,4),
                "dataNascimento": self.data_nascimento,
                "idade": self.idade,
                "diagnostico": self.diagnostico,
                "sexo": self.sexo,
                "equipe": mock_word(self.equipe, 3),
                "microarea": self.microarea,
                "endereco": mock_word(self.endereco, 5),
                "complemento": mock_word(self.complemento, 5),
                "tipoLogradouro": self.tipo_logradouro,
                "cep": self.cep,
                "telefone": self.telefone,
                "detalhesCondicaoSaude": [
                    {
                        "cidCondicaoSaude": self.cids,
                        "primeiroDiagnostico": self.primeiro_registro,
                        "registros": [
                            registro.to_dict() for registro in self.registros
                        ],
                    }
                ],
            }
        )


class DiabetesNominalListAdapter(BaseNominalAdapter):

    def __init__(self, user: DiabetesNominal):
        super().__init__(user)

        alertas = [
            "alerta_ultima_consulta_medico",
            "alerta_ultima_consulta_odontologica",
            "alerta_visita_acs",
            "alerta_ultima_hemoglobina_glicada",
        ]
        for i in alertas:
            user[i] = user[i] if isinstance(user[i], int) else 0

        self.possui_alertas = (
            not user["alerta_afericao_pa"]
            or not user["alerta_total_de_consultas_medico"]
            or not user["alerta_ultima_consulta_medico"]
            or not user["alerta_creatinina"]
            or not user["alerta_ultima_consulta_odontologica"]
            or not user["alerta_visita_acs"]
            or not user["alerta_ultima_hemoglobina_glicada"]
        )
        self.diagnostico = (
            "cid/ciaps"
            if user["autoreferido"] is None or user["autoreferido"] == 0
            else "autoreferido"
        )

        self.cids = (
            user["codigos_1atend"].tolist()
            if is_sequence(user["codigos_1atend"])
            else []
        )
        self.registros.append(
            AlertRecord(
                data=user["ultima_data_afericao_pa"],
                exibir_alerta=not user["alerta_afericao_pa"],
                descricao="Data da última aferição de PA",
                tipo_alerta="alerta-afericao-pa-maior-6-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["ultima_data_creatinina"],
                exibir_alerta=(not user["alerta_creatinina"]),
                descricao="Data da última avaliação da Dosagem de Creatinina",
                tipo_alerta="alerta-creatinina-maior-6-meses",
            )
        )

        self.registros.append(
            AlertRecord(
                data=user["total_consulta_med_enferm"],
                exibir_alerta=False,
                descricao="Total de consultas Médicas ou de Enfermagem",
                tipo_alerta="alerta-total-de-consultas-medico-menor-2",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["ultimo_atendimento_medico"],
                exibir_alerta=(
                    not user["alerta_ultima_consulta_medico"]
                ),
                descricao="Data da última consulta Médica ou de Enfermagem",
                tipo_alerta="alerta-ultimo-atendimento-medico-maior-6-meses",
            )
        )

        self.registros.append(
            AlertRecord(
                data=user["ultimo_atendimento_odonto"],
                exibir_alerta=(
                    not user["alerta_ultima_consulta_odontologica"]
                ),
                descricao="Data da última consulta Odontológica",
                tipo_alerta="alerta-ultimo-atendimento-odonto-maior-6-meses",
            )
        )

        self.registros.append(
            AlertRecord(
                data=user["dt_ultima_visita_acs"],
                exibir_alerta=(
                    not user["alerta_visita_acs"]
                ),
                descricao="Data da última visita ACS",
                tipo_alerta="alerta-data-ultima-visita-acs-maior-6-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["ultima_data_hemoglobina_glicada"] or "-",
                exibir_alerta=(
                    not user["alerta_ultima_hemoglobina_glicada"]
                ),
                descricao="Data da última avaliação da Dosagem de Hemoglobina Glicada",
                tipo_alerta="alerta-ultima-data-hemoglobina-glicada-maior-6-meses",
            )
        )

    def to_dict(self):
        return dict(
            {
                "nome": mock_word(self.nome, 3, True),
                "nomeSocialSelecionado": mock_word(self.nome_social),
                "zonaUrbana": self.tipo_localidade == "Urbana",
                "zonaRural": self.tipo_localidade == "Rural",
                "possuiAlertas": self.possui_alertas,
                "cpf": mock_word(self.cpf,4),
                "cns": mock_word(self.cns,4),
                "dataNascimento": self.data_nascimento,
                "idade": self.idade,
                "diagnostico": self.diagnostico,
                "sexo": self.sexo,
                "equipe": mock_word(self.equipe,3),
                "microarea": self.microarea,
                "endereco": mock_word(self.endereco, 5),
                "complemento": mock_word(self.complemento, 5),
                "tipoLogradouro": self.tipo_logradouro,
                "cep": mock_word(self.cep),
                "telefone": mock_word(self.telefone),
                "detalhesCondicaoSaude": [
                    {
                        "cidCondicaoSaude": self.cids,
                        "primeiroDiagnostico": self.primeiro_registro,
                        "registros": [
                            registro.to_dict() for registro in self.registros
                        ],
                    }
                ],
            }
        )


class CriancaNominalListAdapter:

    def __init__(self, user: Crianca):
        self.nome = user["nome"]
        self.nome_social = "-"
        self.tipo_localidade = user["tipo_localidade"]
        self.cpf = user["cpf"]
        self.cns = user["cns"]
        self.data_nascimento = user["data_nascimento"]
        self.idade = user["idade"]
        self.sexo = user["sexo"]
        self.equipe = user["nome_equipe"]
        self.microarea = user["micro_area"]
        self.endereco = f"""{user["endereco"]} {user["numero"]}, {user["bairro"]}"""
        self.tipo_logradouro = user["tipo_endereco"]
        self.complemento = user["complemento"]
        self.cep = user["cep"]
        self.telefone = user["telefone"]
        self.possui_alertas = (
            user["indicador_atendimentos_medicos_enfermeiros"] != 1
            or user["indicador_atendimentos_medicos_enfermeiros_puericultura"] != 1
            or user["indicador_medicoes_peso_altura_ate2anos"] != 1
            or user["indicador_visitas_domiciliares_acs"] != 1
            or user["indicador_teste_pezinho"] != 1
            or user["indicador_atendimentos_odontologicos"] != 1
            or user["indicador_vacinas_penta_polio_triplici"] != 1
        )
        self.registros = []
        self.registros.append(
            AlertRecord(
                data=user["data_ultimo_atendimento_medico_enfermeiro"],
                exibir_alerta=user["indicador_atendimentos_medicos_enfermeiros"] != 1,
                descricao="Data do último atendimento Médico/Enfermeiro",
                tipo_alerta="data_ultimo_atendimento_medico_enfermeiro",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["data_ultimo_atendimento_medicos_enfermeiros_puericultura"],
                exibir_alerta=user["indicador_atendimentos_medicos_enfermeiros_puericultura"]
                != 1,
                descricao="Data do último atendimento Médico/Enfermeiro de Puericultura",
                tipo_alerta="indicador_atendimentos_medicos_enfermeiros_puericultura",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["data_ultima_medicao_peso_altura_ate2anos"],
                exibir_alerta=user["indicador_medicoes_peso_altura_ate2anos"] != 1,
                descricao="Data da última medição de peso/altura até dois anos",
                tipo_alerta="data_ultima_medicao_peso_altura_ate2anos",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["data_ultima_visita_domiciliar_acs"],
                exibir_alerta=user["indicador_visitas_domiciliares_acs"] != 1,
                descricao="Data da última visita do ACS ",
                tipo_alerta="data_ultima_visita_domiciliar_acs",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["data_ultimo_teste_pezinho"],
                exibir_alerta=user["indicador_teste_pezinho"] != 1,
                descricao="Data do último Teste do pezinho ",
                tipo_alerta="data_ultimo_teste_pezinho",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["data_ultimo_atendimento_odontologico"],
                exibir_alerta=user["indicador_atendimentos_odontologicos"] != 1,
                descricao="Data do último atendimento Odontológico ",
                tipo_alerta="data_ultimo_atendimento_odontologico",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["data_ultima_vacina_triplici"],
                exibir_alerta=user["indicador_vacinas_penta_polio_triplici"] != 1,
                descricao="Data do último registro de vacina Penta/Polio/Triplici ",
                tipo_alerta="data_ultima_vacina_triplici",
            )
        )

    def to_dict(self):
        return dict(
            {
                "nome": self.nome,
                "nomeSocialSelecionado": self.nome_social,
                "zonaUrbana": self.tipo_localidade == "Urbana",
                "zonaRural": self.tipo_localidade == "Rural",
                "possuiAlertas": self.possui_alertas,
                "cpf": self.cpf,
                "cns": self.cns,
                "dataNascimento": self.data_nascimento,
                "idade": self.idade,
                "sexo": self.sexo,
                "equipe": self.equipe,
                "microarea": self.microarea,
                "endereco": self.endereco,
                "complemento": self.complemento,
                "tipoLogradouro": self.tipo_logradouro,
                "cep": self.cep,
                "telefone": self.telefone,
                "detalhesCondicaoSaude": [
                    {
                        "registros": [
                            registro.to_dict() for registro in self.registros
                        ],
                    }
                ],
            }
        )


class IdosoNominalListAdapter:

    def __init__(self, user: Crianca):
        self.nome = user["nome"]
        self.nome_social = "-"
        self.tipo_localidade = user["tipo_localizacao_domicilio"]
        self.cpf = user["cpf"]
        self.cns = user["cns"]
        self.data_nascimento = user["data_nascimento"]
        self.idade = user["idade"]
        self.sexo = user["sexo"]
        self.equipe = user["nome_equipe"]
        self.microarea = user["micro_area"]
        self.endereco = f"""{user["logradouro"]} {user["numero"]}, {user["bairro"]}"""
        self.tipo_logradouro = user["tipo_logradouro"]
        self.complemento = user["complemento"]
        self.cep = user["cep"]
        self.telefone = user["telefone"]
        self.possui_alertas = (
            user["agg_alerta_medicos_enfermeiros"] == 1
            or user["agg_alerta_creatinina"] == 1
            or user["agg_alerta_cirurgiao_dentista"] == 1
            or user["agg_alerta_ivcf_aplicado"] == 1
            or user["agg_alerta_peso_altura"] == 1
            or user["agg_alerta_vacinas_influenza"] == 1
            or user["agg_alerta_visitas_domiciliares_acs"] == 1
        )
        self.registros = []
        self.registros.append(
            AlertRecord(
                data=self.convert_nan(user["total_consulta_medico_enfermeiro"]),
                exibir_alerta=user["agg_alerta_medicos_enfermeiros"] == 1,
                descricao="Total de consultas médicas e/ou de enfermagem",
                tipo_alerta="total_consulta_medico_enfermeiro",
                classificacao='12-meses'
            )
        )
        self.registros.append(
            AlertRecord(
                data=[
                    self.convert_date(user["data_ultima_consulta_medico_enfermeiro"]),
                    self.convert_date(user["data_penultima_consulta_medico_enfermeiro"]),
                ],
                exibir_alerta=user["agg_alerta_medicos_enfermeiros"] == 1,
                descricao="Data das últimas duas consultas médicas e/ou de enfermagem",
                tipo_alerta="data_ultimo_atendimento_medicos",
                classificacao='12-meses'
            )
        )
        self.registros.append(
            AlertRecord(
                data=(
                    "Sim" if user['agg_alerta_peso_altura'] == 1 else "Não"
                ),
                exibir_alerta=user["agg_alerta_peso_altura"] == 1,
                descricao="Registro de peso e altura na mesma data de duas consultas médicas e/ou de enfermagem",
                tipo_alerta="alerta_peso_altura",
                classificacao='24-meses'
            )
        )
        self.registros.append(
            AlertRecord(
                data=self.convert_date(user["data_ultimo_creatinina"]),
                exibir_alerta=user["agg_alerta_creatinina"] == 1,
                descricao="Data do último registro de Creatinina ",
                tipo_alerta="data_ultimo_registro_creatinina",
                classificacao='24-meses'
            )
        )
        self.registros.append(
            AlertRecord(
                data=(
                    self.convert_nan(user['total_visitas_domiciliares_acs'])
                ),
                exibir_alerta=user["agg_visitas_domiciliares_acs"] != 1,
                descricao="Número de visitas domiciliares por ACS/TACS ",
                tipo_alerta="data_ultimo_registro_creatinina",
                classificacao='24-meses'
            )
        )
        self.registros.append(
            AlertRecord(
                data=self.convert_date(user["data_ultima_vacina"]),
                exibir_alerta=user["agg_alerta_vacinas_influenza"] == 1,
                descricao="Data de registro de vacina influenza",
                tipo_alerta="data_ultima_vacina_influenza",
                classificacao='24-meses'
            )
        )
        
        
        self.registros.append(
            AlertRecord(
                data=self.convert_date(user["data_ultimo_atendendimento_odonto"]),
                exibir_alerta=user["agg_alerta_cirurgiao_dentista"] == 1,
                descricao="Data da consulta odontológica na APS ",
                tipo_alerta="alerta_cirurgiao_dentista",
                classificacao='24-meses'
            )
        )
        self.registros.append(
            AlertRecord(
                data=(
                    "Sim" if user["agg_ivcf_aplicado"] == 1 else "Não"
                ),
                exibir_alerta=user["agg_alerta_ivcf_aplicado"] == 1,
                descricao="Avaliação do IVCF-20:",
                tipo_alerta="alerta_ivcf_aplicado",
                classificacao='24-meses'
            )
        )

    def convert_date(self, dt):
        if issubclass(type(dt), type(pd.NaT)):
            return None
        return dt
    
    def convert_nan(self, dt):
        if math.isnan(dt):
            return 0
        return dt    
    
    def to_dict(self):
        return dict(
            {
                "nome": self.nome,
                "nomeSocialSelecionado": self.nome_social,
                "zonaUrbana": self.tipo_localidade == "Urbana",
                "zonaRural": self.tipo_localidade == "Rural",
                "possuiAlertas": self.possui_alertas,
                "cpf": self.cpf,
                "cns": self.cns,
                "dataNascimento": self.data_nascimento,
                "idade": self.idade,
                "sexo": self.sexo,
                "equipe": self.equipe,
                "microarea": self.microarea,
                "endereco": self.endereco,
                "complemento": self.complemento,
                "tipoLogradouro": self.tipo_logradouro,
                "cep": self.cep,
                "telefone": self.telefone,
                "detalhesCondicaoSaude": [
                    {
                        "registros": [
                            registro.to_dict() for registro in self.registros
                        ],
                    }
                ],
            }
        )


class RecordNominalListAdapter:

    def __init__(self, user):

        endereco = user['endereco'] if user['endereco'] is not None else ""
        endereco += " " + user["numero"] if user["numero"] is not None else ""
        endereco += " " + user["bairro"] if user["bairro"] is not None else ""

        self.nome = user['nome']
        self.nome_social = "-"
        self.tipo_localidade = user['tipo_localidade']
        self.cpf = user['cpf']
        self.cns = user['cns']
        self.data_nascimento = user['data_nascimento'].date()
        self.idade = user['idade']
        self.sexo = user['sexo']
        self.equipe = user['nome_equipe']
        self.microarea = user['micro_area']
        self.endereco = endereco
        self.tipo_logradouro = user['tipo_endereco']
        self.complemento = user['complemento']
        self.cep = user['cep']
        self.telefone = user['telefone']
        self.alerta_status_cadastro = user['alerta_status_cadastro']
        self.status_cadastro = user['status_cadastro']
        self.alerta = user['alerta']

        ultima_atualizacao_cidadao, ultima_atualizacao_fcd = True, True

        if user["fci_att_2anos"] is not None and user["fci_att_2anos"] == 1:
            ultima_atualizacao_cidadao = False

        if user["fcdt_att_2anos"] is not None and user["fcdt_att_2anos"] ==1:
            ultima_atualizacao_fcd = False

        self.registros = []
        self.registros.append(
            AlertRecord(
                data=user['ultima_atualizacao_fci'],
                exibir_alerta=ultima_atualizacao_cidadao,
                descricao="Data da última atualização da ficha de Cadastro Individual",
                tipo_alerta="ultima_atualizacao_cidadao",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user['ultima_atualizacao_fcd'],
                exibir_alerta=ultima_atualizacao_fcd,
                descricao="Data da última atualização da ficha de Cadastro Domiciliar e Territorial",
                tipo_alerta="ultima_atualizacao_fcd",
            )
        )
        label_map = {
            "cadastro_completo": "Cadastro Completo",
            "cadastro_incompleto": "Cadastro Incompleto",
            "pessoa_ident_nao_cadastrada": "Pessoa não cadastrada",
            "outro": "Outro",
        }
        self.registros.append(
            AlertRecord(
                data=label_map[user['status_cadastro']],
                exibir_alerta=self.alerta_status_cadastro == 1,
                descricao="Status de cadastro",
                tipo_alerta="status_de_cadastro",
            )
        )

    def to_dict(self):
        return dict(
            {
                "nome": mock_word(self.nome, 3, True),
                "nomeSocialSelecionado": mock_word(self.nome_social),
                "zonaUrbana": False,
                "zonaRural": False,
                "possuiAlertas": self.alerta,
                "cpf": mock_word(self.cpf,4),
                "cns": mock_word(self.cns,4),
                "dataNascimento": self.data_nascimento,
                "idade": self.idade,
                "sexo": self.sexo,
                "equipe": mock_word(self.equipe,3),
                "microarea": self.microarea,
                "endereco": mock_word(self.endereco, 5),
                "complemento": mock_word(self.complemento, 5),
                "tipoLogradouro": self.tipo_logradouro,
                "cep": mock_word(self.cep),
                "telefone": mock_word(self.telefone),
                "detalhesCondicaoSaude": [
                    {
                        "registros": [
                            registro.to_dict() for registro in self.registros
                        ],
                    }
                ],
            }
        )
