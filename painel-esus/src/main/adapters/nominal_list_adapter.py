# pylint: disable=R0902, W4901, W0611, C0103
import math
import re

import numpy as np
import pandas as pd
from sqlalchemy import true
from src.domain.entities.diabetes import Diabetes
from src.domain.entities.hypertension import Hypertension
from src.env.conf import getenv
from src.infra.db.entities.crianca import Crianca
from src.infra.db.entities.diabetes_nominal import DiabetesNominal
from src.infra.db.entities.hipertensao_nominal import HipertensaoNominal
from src.infra.db.entities.pessoas import Pessoas
from src.infra.db.repositories.utils.str_utils import (
    anonymize_data,
    anonymize_data_address,
    anonymize_data_cep,
    anonymize_data_doc,
    anonymize_data_equipe,
    anonymize_data_name,
    anonymize_data_nascimento,
)


def is_sequence(obj):
    return isinstance(obj, (np.ndarray, np.generic))


class AlertRecord:
    def __init__(
        self,
        descricao: str,
        data,
        exibir_alerta,
        tipo_alerta: str,
        classificacao: str = None,
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
        return dict(response)


class BaseNominalAdapter:
    def __init__(self, user):
        endereco = self.get(user, "endereco")
        endereco += " " + self.get(user, "numero")
        endereco += " " + self.get(user, "bairro")

        self.nome = user["nome"]
        self.nome_social = "-"
        self.tipo_localidade = self.get(user, "tipo_localidade")
        self.cpf = user["cpf"]
        self.cns = user["cns"]
        self.data_nascimento = self.get(user, "data_nascimento")
        self.idade = user["idade"]
        self.sexo = user["sexo"]
        self.equipe = self.get(user, "nome_equipe")
        self.microarea = self.get(user, "micro_area")
        self.endereco = endereco
        self.tipo_logradouro = self.get(user, "tipo_endereco")
        self.complemento = self.get(user, "complemento")
        self.cep = user["cep"]
        self.telefone = user["telefone"]
        self.registros = []
        self.primeiro_registro = self.get(user, "dt_primeiro_reg_condicao")
        self.raca_cor = self.get(user, "raca_cor")
        

    def get(self, item, field):
        return item[field] if field in item and item[field] is not None else ""


class HypertensionNominalListAdapter(BaseNominalAdapter):

    def __init__(self, user):
        super().__init__(user)


        self.diagnostico = (
            "cid/ciaps"
            if user["autoreferido"] is None or user["autoreferido"] == 0
            else "autoreferido"
        )
        self.registros = []
        self.registros = []
        self.possui_alertas = (
            user["agg_afericao_pa"] == 0
            or user["agg_creatinina"] == 0
            or user["agg_medicos_enfermeiros"] == 0
            or user["agg_cirurgiao_dentista"] == 0
            or user["agg_visitas_domiciliares_acs"] == 0
        )
        self.cids = (
            user["codigos_1atend"].tolist()
            if is_sequence(user["codigos_1atend"])
            else []
        )
        self.registros.append(
            AlertRecord(
                data=user["ultima_data_afericao_pa"],
                exibir_alerta=user["agg_afericao_pa"]==0,
                descricao="Data da última aferição de PA",
                tipo_alerta="alerta-afericao-pa-maior-6-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["ultima_data_creatinina"],
                exibir_alerta=user["agg_creatinina"]==0,
                descricao="Data da última avaliação da Dosagem de Creatinina",
                tipo_alerta="alerta-creatinina-maior-6-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["total_consulta_med_enferm"],
                exibir_alerta=user["agg_medicos_enfermeiros"] == 0,
                exibir_alerta=user["agg_medicos_enfermeiros"] == 0,
                descricao="Total de consultas Médicas ou de Enfermagem",
                tipo_alerta="alerta-total-de-consultas-medico-menor-2",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["ultimo_atendimento_medico"],
                exibir_alerta=user["agg_medicos_enfermeiros"]==0,
                descricao="Data da última consulta médica ou de Enfermagem",
                tipo_alerta="alerta-ultimo-atendimento-medico-maior-6-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=(user["ultimo_atendimento_odonto"]),
                exibir_alerta=user["agg_cirurgiao_dentista"]==0,
                descricao="Data da última consulta odontológica",
                tipo_alerta="alerta-ultimo-atendimento-odonto-maior-6-meses",
            )
        )

        self.registros.append(
            AlertRecord(
                data=(user["dt_ultima_visita_acs"]),
                exibir_alerta=user["agg_visitas_domiciliares_acs"]==0,
                descricao="Data da última visita ACS",
                tipo_alerta="alerta-data-ultima-visita-acs-maior-6-meses",
            )
        )

    def to_dict(self):
        return dict(
            {
                "nome": anonymize_data_name(self.nome),
                "nomeSocialSelecionado": anonymize_data_name(self.nome_social),
                "zonaUrbana": self.tipo_localidade == "Urbana",
                "zonaRural": self.tipo_localidade == "Rural",
                "possuiAlertas": self.possui_alertas,
                "cpf": anonymize_data_doc(self.cpf),
                "cns": anonymize_data_doc(self.cns),
                "dataNascimento": anonymize_data_nascimento(self.data_nascimento),
                "idade": self.idade,
                "diagnostico": self.diagnostico,
                "sexo": self.sexo,
                "equipe": anonymize_data_equipe(self.equipe),
                "microarea": anonymize_data(self.microarea),
                "endereco": anonymize_data_address(self.endereco),
                "complemento": anonymize_data(self.complemento),
                "tipoLogradouro": self.tipo_logradouro,
                "cep": anonymize_data_cep(self.cep),
                "telefone": anonymize_data(self.telefone),
                "racaCor": anonymize_data(self.raca_cor),
                "racaCor": anonymize_data(self.raca_cor),
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

        self.possui_alertas = (
            not user["agg_afericao_pa"]
            or not user["agg_creatinina"]
            or not user["agg_medicos_enfermeiros"]
            or not user["agg_cirurgiao_dentista"]
            or not user["agg_visitas_domiciliares_acs"]
            or not user["agg_hemoglobina"]
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
                exibir_alerta=not user["agg_afericao_pa"],
                exibir_alerta=not user["agg_afericao_pa"],
                descricao="Data da última aferição de PA",
                tipo_alerta="alerta-afericao-pa-maior-6-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["ultima_data_creatinina"],
                exibir_alerta=(not user["agg_creatinina"]),
                exibir_alerta=(not user["agg_creatinina"]),
                descricao="Data da última avaliação da Dosagem de Creatinina",
                tipo_alerta="alerta-creatinina-maior-6-meses",
            )
        )

        self.registros.append(
            AlertRecord(
                data=user["total_consulta_med_enferm"],
                exibir_alerta=not user['agg_medicos_enfermeiros'],
                descricao="Total de consultas Médicas ou de Enfermagem",
                tipo_alerta="alerta-total-de-consultas-medico-menor-2",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["ultimo_atendimento_medico"],
                exibir_alerta=(not user["agg_medicos_enfermeiros"]),
                exibir_alerta=(not user["agg_medicos_enfermeiros"]),
                descricao="Data da última consulta Médica ou de Enfermagem",
                tipo_alerta="alerta-ultimo-atendimento-medico-maior-6-meses",
            )
        )

        self.registros.append(
            AlertRecord(
                data=user["ultimo_atendimento_odonto"],
                exibir_alerta=(not user["agg_cirurgiao_dentista"]),
                exibir_alerta=(not user["agg_cirurgiao_dentista"]),
                descricao="Data da última consulta Odontológica",
                tipo_alerta="alerta-ultimo-atendimento-odonto-maior-6-meses",
            )
        )

        self.registros.append(
            AlertRecord(
                data=user["dt_ultima_visita_acs"],
                exibir_alerta=(not user["agg_visitas_domiciliares_acs"]),
                exibir_alerta=(not user["agg_visitas_domiciliares_acs"]),
                descricao="Data da última visita ACS",
                tipo_alerta="alerta-data-ultima-visita-acs-maior-6-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["ultima_data_hemoglobina_glicada"] or "-",
                exibir_alerta=(not user["agg_hemoglobina"]),
                exibir_alerta=(not user["agg_hemoglobina"]),
                descricao="Data da última avaliação da Dosagem de Hemoglobina Glicada",
                tipo_alerta="alerta-ultima-data-hemoglobina-glicada-maior-6-meses",
            )
        )

    def to_dict(self):
        return dict(
            {
                "nome": anonymize_data_name(self.nome),
                "nomeSocialSelecionado": anonymize_data_name(self.nome_social),
                "zonaUrbana": self.tipo_localidade == "Urbana",
                "zonaRural": self.tipo_localidade == "Rural",
                "possuiAlertas": self.possui_alertas,
                "cpf": anonymize_data_doc(self.cpf),
                "cns": anonymize_data_doc(self.cns),
                "dataNascimento": anonymize_data_nascimento(self.data_nascimento),
                "idade": self.idade,
                "diagnostico": self.diagnostico,
                "sexo": self.sexo,
                "equipe": anonymize_data_equipe(self.equipe),
                "microarea": anonymize_data(self.microarea),
                "endereco": anonymize_data_address(self.endereco),
                "complemento": anonymize_data(self.complemento),
                "tipoLogradouro": self.tipo_logradouro,
                "cep": anonymize_data_cep(self.cep),
                "telefone": anonymize_data(self.telefone),
                "racaCor": anonymize_data(self.raca_cor),
                "racaCor": anonymize_data(self.raca_cor),
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
        self.tipo_localidade = user["tipo_localizacao_domicilio"]
        self.cpf = user["cpf"]
        self.cns = user["cns"]
        self.data_nascimento = user["data_nascimento"]

        def calc_idade(user):
            return user["idade_mes_ano"]

        self.idade = calc_idade(user)
        self.sexo = user["sexo"]
        self.equipe = user["nome_equipe"]
        self.microarea = user["micro_area"]
        self.endereco = f"""{user["logradouro"]} {user["numero"]}, {user["bairro"]}"""
        self.tipo_logradouro = user["tipo_logradouro"]
        self.complemento = user["complemento"]
        self.cep = user["cep"]
        self.telefone = user["telefone"]
        self.raca_cor = user["raca_cor"]
        self.possui_alertas = self.check_card_alert(user)
        self.registros = []
        self.registros.append(
            AlertRecord(
                data=self.get_yes_no_data(user, "agg_card_puericultura_ate_8_dias"),
                exibir_alerta=self.check_alert(
                    user, "agg_card_puericultura_ate_8_dias"
                ),
                descricao="Houve 1ª consulta de puericultura até o 8º dia de vida?",
                tipo_alerta="puericultura_ate_8_dias",
            )
        )
        self.registros.append(
            AlertRecord(
                data=self.get_numeric_data(user, "num_consultas_puericultura"),
                exibir_alerta=self.check_alert(
                    user, "agg_card_puericultura_9_consultas_ate_2_anos"
                ),
                descricao="Número de consultas de puericultura até 2 anos de vida:",
                tipo_alerta="puericultura_9_consultas_ate_2_anos",
            )
        )
        self.registros.append(
            AlertRecord(
                data=self.get_yes_no_data(user, "agg_card_visita_acs_ate_30d"),
                exibir_alerta=self.check_alert(user, "agg_card_visita_acs_ate_30d"),
                descricao="Houve visita domiciliar até os primeiros 30 dias de vida?",
                tipo_alerta="visita_acs_ate_30d",
            )
        )
        self.registros.append(
            AlertRecord(
                data=self.get_yes_no_data(user, "agg_card_visita_acs_ate_6m"),
                exibir_alerta=self.check_alert(user, "agg_card_visita_acs_ate_6m"),
                descricao="Houve visita domiciliar dos 31 dias até os 6 meses de vida?",
                tipo_alerta="visita_acs_ate_6m",
            )
        )
        self.registros.append(
            AlertRecord(
                data=self.get_yes_no_data(user, "agg_card_odonto_ate_12m"),
                exibir_alerta=self.check_alert(user, "agg_card_odonto_ate_12m"),
                descricao="Houve 1ª consulta odontológica até os primeiros 12 meses de vida?",
                tipo_alerta="odonto_ate_12m",
            )
        )
        self.registros.append(
            AlertRecord(
                data=self.convert_nan(user["num_odonto_ate24m"]),
                exibir_alerta=self.check_alert(user, "agg_card_odonto_12a24m"),
                descricao="Número de consultas odontológicas até os primeiros 24 meses de vida:",
                tipo_alerta="odonto_12a24m",
            )
        )
        self.registros.append(
            AlertRecord(
                data=self.get_numeric_data(user, "total_peso_altura"),
                exibir_alerta=self.check_alert(user, "agg_card_9_peso_altura"),
                descricao="Número de registros simultâneos de peso e altura realizados na data das consultas de puericultura:",
                tipo_alerta="peso_altura",
            )
        )
        self.registros.append(
            AlertRecord(
                data=self.get_last_height_weight_measure(user),
                exibir_alerta=False,
                descricao="Último registro de peso e altura na data das consultas de puericultura",
                tipo_alerta="ultimo_peso_altura",
            )
        )
        self.registros.append(
            AlertRecord(
                data=self.get_yes_no_data(user, "agg_card_marco_desenvolvimento"),
                exibir_alerta=self.check_alert(user, "agg_card_marco_desenvolvimento"),
                descricao="Houve avaliação dos marcos do desenvolvimento?",
                tipo_alerta="marco_desenvolvimento",
            )
        )
        self.registros.append(
            AlertRecord(
                data=self.get_yes_no_data(user, "agg_card_consumo_alimentar"),
                exibir_alerta=self.check_alert(user, "agg_card_consumo_alimentar"),
                descricao="Houve avaliação do consumo alimentar na data das consultas de puericultura?",
                tipo_alerta="consumo_alimentar",
            )
        )

    def get_last_height_weight_measure(self, user):
        if (
            self.select_column(user, "nu_peso_recentes") is None
            and self.select_column(user, "nu_altura_recentes") is None
        ):
            return "Não se aplica"
        else:
            descricao = self.select_column(user, "descricao_classificacao")
            return f'{self.select_column(user, "nu_peso_recentes")} kg/{self.select_column(user, "nu_altura_recentes")} cm ({descricao})'

    def convert_nan(self, dt):
        if dt is None or math.isnan(dt):
            return 0
        return dt

    def select_column(self, user, column):
        return user[f"{column}"]

    def get_numeric_data(self, user, column):
        return self.convert_nan(self.select_column(user, column))

    def check_alert(self, user, column):
        return self.get_numeric_data(user, column) == 0

    def get_yes_no_data(self, user, column):
        condition = {
            "0": "Não",
            "1": "Sim",
            "99": "Não se aplica",
        }
        return condition[str(self.get_numeric_data(user, column))]

    def check_card_alert(self, user):
        return (
            user["agg_card_puericultura_ate_8_dias"] == 0
            or user["agg_card_puericultura_9_consultas_ate_2_anos"] == 0
            or user["agg_card_9_peso_altura"] == 0
            or user["agg_card_visita_acs_ate_30d"] == 0
            or user["agg_card_visita_acs_ate_6m"] == 0
            or user["agg_card_odonto_ate_12m"] == 0
            or user["agg_card_odonto_12a24m"] == 0
            or user["agg_card_marco_desenvolvimento"] == 0
            or user["agg_card_consumo_alimentar"] == 0
        )

    def to_dict(self):
        return dict(
            {
                "nome": anonymize_data_name(self.nome),
                "nomeSocialSelecionado": anonymize_data_name(self.nome_social),
                "zonaUrbana": self.tipo_localidade == "Urbana",
                "zonaRural": self.tipo_localidade == "Rural",
                "possuiAlertas": self.possui_alertas,
                "cpf": anonymize_data_doc(self.cpf),
                "cns": anonymize_data_doc(self.cns),
                "dataNascimento": anonymize_data_nascimento(self.data_nascimento),
                "idade": self.idade,
                "sexo": self.sexo,
                "equipe": anonymize_data_equipe(self.equipe),
                "microarea": anonymize_data(self.microarea),
                "endereco": anonymize_data_address(self.endereco),
                "complemento": anonymize_data(self.complemento),
                "tipoLogradouro": anonymize_data(self.tipo_logradouro),
                "cep": anonymize_data_cep(self.cep),
                "telefone": anonymize_data(self.telefone),
                "racaCor": anonymize_data(self.raca_cor),
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
        self.raca_cor = user["raca_cor"]
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
                descricao="Total de consultas médicas e/ou de enfermagem nos últimos 12 meses:",
                tipo_alerta="total_consulta_medico_enfermeiro",
                classificacao="12-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=[
                    self.convert_date(user["data_ultima_consulta_medico_enfermeiro"]),
                    self.convert_date(
                        user["data_penultima_consulta_medico_enfermeiro"]
                    ),
                ],
                exibir_alerta=user["agg_alerta_medicos_enfermeiros"] == 1,
                descricao="Data das consultas médicas e/ou de enfermagem nos últimos 12 meses:",
                tipo_alerta="data_ultimo_atendimento_medicos",
                classificacao="12-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=("Sim" if user["agg_peso_altura"] == 1 else "Não"),
                exibir_alerta=user["agg_alerta_peso_altura"] == 1,
                descricao="Houve registro simultâneo de peso e altura nos últimos 24 meses?",
                tipo_alerta="alerta_peso_altura",
                classificacao="24-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=self.convert_date(user["data_ultimo_creatinina"]),
                exibir_alerta=user["agg_alerta_creatinina"] == 1,
                descricao="Data do registro de exame de creatinina nos últimos 24 meses:",
                tipo_alerta="data_ultimo_registro_creatinina",
                classificacao="24-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=(self.convert_nan(user["total_visitas_domiciliares_acs"])),
                exibir_alerta=user["agg_alerta_visitas_domiciliares_acs"] == 1,
                descricao="Número de visitas domiciliares por ACS/TACS nos últimos 24 meses",
                tipo_alerta="data_ultimo_registro_creatinina",
                classificacao="24-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=self.convert_date(user["data_ultima_vacina"]),
                exibir_alerta=user["agg_alerta_vacinas_influenza"] == 1,
                descricao="Data de registro de vacina contra influenza nos últimos 24 meses",
                tipo_alerta="data_ultima_vacina_influenza",
                classificacao="24-meses",
            )
        )

        self.registros.append(
            AlertRecord(
                data=self.convert_date(user["data_ultimo_atendendimento_odonto"]),
                exibir_alerta=user["agg_alerta_cirurgiao_dentista"] == 1,
                descricao="Data das consultas odontológicas na APS nos últimos 24 meses",
                tipo_alerta="alerta_cirurgiao_dentista",
                classificacao="24-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=("Sim" if user["agg_ivcf_aplicado"] == 1 else "Não"),
                exibir_alerta=user["agg_alerta_ivcf_aplicado"] == 1,
                descricao="Houve avaliação do IVCF-20 nos últimos 24 meses?",
                tipo_alerta="alerta_ivcf_aplicado",
                classificacao="24-meses",
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
                "racaCor": anonymize_data(self.raca_cor),
                "nome": anonymize_data_name(self.nome),
                "nomeSocialSelecionado": anonymize_data_name(self.nome_social),
                "zonaUrbana": self.tipo_localidade == "Urbana",
                "zonaRural": self.tipo_localidade == "Rural",
                "possuiAlertas": self.possui_alertas,
                "cpf": anonymize_data_doc(self.cpf),
                "cns": anonymize_data_doc(self.cns),
                "dataNascimento": anonymize_data_nascimento(self.data_nascimento),
                "idade": self.idade,
                "sexo": self.sexo,
                "equipe": anonymize_data_equipe(self.equipe),
                "microarea": anonymize_data(self.microarea),
                "endereco": anonymize_data_address(self.endereco),
                "complemento": anonymize_data(self.complemento),
                "tipoLogradouro": anonymize_data(self.tipo_logradouro),
                "cep": anonymize_data_cep(self.cep),
                "telefone": anonymize_data(self.telefone),
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

        endereco = user["endereco"] if user["endereco"] is not None else ""
        endereco += " " + user["numero"] if user["numero"] is not None else ""
        endereco += " " + user["bairro"] if user["bairro"] is not None else ""

        self.nome = user["nome"]
        self.nome_social = "-"
        self.tipo_localidade = user["tipo_localidade"]
        self.cpf = user["cpf"]
        self.cns = user["cns"]
        self.data_nascimento = user["data_nascimento"].date()
        self.idade = user["idade"]
        self.sexo = user["sexo"]
        self.equipe = user["nome_equipe"]
        self.microarea = user["micro_area"]
        self.endereco = endereco
        self.tipo_logradouro = user["tipo_endereco"]
        self.complemento = user["complemento"]
        self.cep = user["cep"]
        self.telefone = user["telefone"]
        self.alerta_status_cadastro = user["alerta_status_cadastro"]
        self.status_cadastro = user["status_cadastro"]

        self.alerta = user["alerta"]

        ultima_atualizacao_cidadao, ultima_atualizacao_fcd = True, True

        if user["fci_att_2anos"] is not None and user["fci_att_2anos"] == 1:
            ultima_atualizacao_cidadao = False

        if user["fcdt_att_2anos"] is not None and user["fcdt_att_2anos"] == 1:
            ultima_atualizacao_fcd = False

        self.registros = []
        acompanhamento = {"1": "Em acompanhamento", "0": "Não acompanhado"}
        self.registros.append(
            AlertRecord(
                data=acompanhamento[str(user["acompanhamento"])],
                exibir_alerta=False,
                descricao="Situação de acompanhamento",
                tipo_alerta="acompanhamento",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["ultima_atualizacao_fci"],
                exibir_alerta=ultima_atualizacao_cidadao,
                descricao="Data da última atualização da ficha de Cadastro Individual",
                tipo_alerta="ultima_atualizacao_cidadao",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user["ultima_atualizacao_fcd"],
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
                data=label_map[user["status_cadastro"]],
                exibir_alerta=self.alerta_status_cadastro == 1,
                descricao="Status de cadastro",
                tipo_alerta="status_de_cadastro",
            )
        )

    def to_dict(self):
        return dict(
            {
                "nome": anonymize_data_name(self.nome),
                "nomeSocialSelecionado": anonymize_data_name(self.nome_social),
                "zonaUrbana": False,
                "zonaRural": False,
                "possuiAlertas": self.alerta,
                "cpf": anonymize_data_doc(self.cpf),
                "cns": anonymize_data_doc(self.cns),
                "dataNascimento": anonymize_data_nascimento(self.data_nascimento),
                "idade": self.idade,
                "sexo": self.sexo,
                "equipe": anonymize_data_equipe(self.equipe),
                "microarea": anonymize_data(self.microarea),
                "endereco": anonymize_data_address(self.endereco),
                "complemento": anonymize_data(self.complemento),
                "tipoLogradouro": anonymize_data(self.tipo_logradouro),
                "cep": anonymize_data_cep(self.cep),
                "telefone": anonymize_data(self.telefone),
                "detalhesCondicaoSaude": [
                    {
                        "registros": [
                            registro.to_dict() for registro in self.registros
                        ],
                    }
                ],
            }
        )


class OralHealtNominalListAdapter:

    def __init__(self, user, category: str = "atendidas"):
        self.category = category
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
        self.raca_cor = user["raca_cor"]
        self.telefone = user["telefone"]
        self.identidadeGenero = user["tp_identidade_genero_cidadao"]
        self.necessidadesEspeciais = user["st_paciente_necessidades_espec"]
        self.povosComunidades = user["st_comunidade_tradicional"]
        self.gestante = user["st_gestante"]

        self.possui_alertas = self.check_alert(user)
        self.registros = []
        self.registros.append(
            AlertRecord(
                data=self.convert_date(
                    self.select_column(user, "data_primeira_consulta")
                ),
                exibir_alerta=self.select_column(user, "agg_primeira_consulta") == 0,
                descricao="Data da primeira consulta odontológica programática",
                tipo_alerta="primeira_consulta",
            )
        )
        self.registros.append(
            AlertRecord(
                data=self.convert_date(
                    self.select_column(user, "data_tratamento_concluido")
                ),
                exibir_alerta=False,
                descricao="Data de conclusão do tratamento odontológico",
                tipo_alerta="conclusao_tratamento",
            )
        )
        self.registros.append(
            AlertRecord(
                data=self.convert_nan(self.select_column(user, "total_exodontia")),
                exibir_alerta=False,
                descricao="Quantidade de exodontias realizadas",
                tipo_alerta="xodontia_realizadas",
            )
        )

        prevent_codes = self.extract_procedures(
            user, "codigos_procedimentos_preventivos"
        )
        description_codes = self.extract_procedures(
            user, "descricao_procedimentos_preventivos"
        )
        label_alert = list(zip(prevent_codes, description_codes))
        alert_list = [
            f"{item[0]} - {item[1]}" if len(item[1]) > 1 else "" for item in label_alert
        ]
        self.registros.append(
            AlertRecord(
                data=alert_list,
                exibir_alerta=False,
                descricao="Procedimentos preventivos realizados:",
                tipo_alerta="procedimentos_realizados",
            )
        )
        self.registros.append(
            AlertRecord(
                data=self.convert_date(self.select_column(user, "data_TRA")),
                exibir_alerta=False,
                descricao="Data do último tratamento restaurador atraumático",
                tipo_alerta="data_utltimo_tra",
            )
        )

    def check_alert(self, user):

        if self.category == "cadastradas":
            return (
                # user["agg_TRA_cadastradas"] == 0
                user["agg_primeira_consulta_cadastradas"]
                == 0
                # or user["agg_realizaram_exodontia_cadastradas"] == 0
                # or user['agg_procedimentos_preventivos_cadastradas'] == 0
                # or user['agg_tratamento_odonto_concluido_cadastradas'] == 0
            )
        else:
            return (
                # user["agg_TRA_atendidas"] == 0
                user["agg_primeira_consulta_atendidas"]
                == 0
                # or user["agg_procedimentos_preventivos_atendidas"] == 0
                # or user["agg_realizaram_exodontia_atendidas"] == 0
                # or user['agg_tratamento_odonto_concluido_atendidas'] == 0
            )

    def extract_procedures(self, user, column):
        data = user[f"{column}_{self.category}"]
        return data.split("|") if data is not None else []

    def select_column(self, user, column):
        return user[f"{column}_{self.category}"]

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
                "nome": anonymize_data_name(self.nome),
                "nomeSocialSelecionado": anonymize_data_name(self.nome_social),
                "zonaUrbana": self.tipo_localidade == "Urbana",
                "zonaRural": self.tipo_localidade == "Rural",
                "possuiAlertas": self.possui_alertas,
                "cpf": anonymize_data_doc(self.cpf),
                "cns": anonymize_data_doc(self.cns),
                "dataNascimento": anonymize_data_nascimento(self.data_nascimento),
                "idade": self.idade,
                "sexo": self.sexo,
                "equipe": anonymize_data_equipe(self.equipe),
                "microarea": anonymize_data(self.microarea),
                "endereco": anonymize_data_address(self.endereco),
                "complemento": anonymize_data(self.complemento),
                "tipoLogradouro": anonymize_data(self.tipo_logradouro),
                "cep": anonymize_data_cep(self.cep),
                "telefone": anonymize_data(self.telefone),
                "racaCor": anonymize_data(self.raca_cor),
                "identidadeGenero": self.identidadeGenero,
                "necessidadesEspeciais": self.necessidadesEspeciais,
                "povosComunidades": self.povosComunidades,
                "gestante": self.gestante,
                "detalhesCondicaoSaude": [
                    {
                        "registros": [
                            registro.to_dict() for registro in self.registros
                        ],
                    }
                ],
            }
        )
