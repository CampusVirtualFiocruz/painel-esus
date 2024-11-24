# pylint: disable=R0902, W4901, W0611, C0103
from lib2to3.pytree import Base

from src.domain.entities.diabetes import Diabetes
from src.domain.entities.hypertension import Hypertension
from src.infra.db.entities.crianca import Crianca
from src.infra.db.entities.diabetes_nominal import DiabetesNominal
from src.infra.db.entities.hipertensao_nominal import HipertensaoNominal
from src.infra.db.entities.pessoas import Pessoas


class AlertRecord:
    def __init__(
        self,
        descricao: str,
        data,
        exibir_alerta,
        tipo_alerta: str,
    ):
        self.descricao = descricao
        self.data = data
        self.exibir_alerta = exibir_alerta
        self.tipo_alerta = tipo_alerta

    def to_dict(self):
        return dict(
            {
                "descricao": self.descricao,
                "data": self.data,
                "exibirAlerta": self.exibir_alerta,
                "tipoAlerta": self.tipo_alerta,
            }
        )


class BaseNominalAdapter:
    def __init__(self, user):
        self.nome = user.nome
        self.nome_social = "-"
        self.tipo_localidade = user.tipo_localidade
        self.cpf = user.cpf
        self.cns = user.cns
        self.idade = user.idade
        self.diagnostico = user.diagnostico
        self.sexo = user.sexo
        self.equipe = user.nome_equipe
        self.microarea = user.micro_area
        self.endereco = f"{user.endereco} {user.numero}, {user.bairro}"
        self.tipo_logradouro = user.tipo_endereco
        self.complemento = user.complemento
        self.cep = user.cep
        self.telefone = user.telefone
        self.registros = []
        self.primeiro_registro = user.min_date

class HypertensionNominalListAdapter(BaseNominalAdapter):

    def __init__(self, user: HipertensaoNominal):
        super().__init__(user)
        self.possui_alertas = (
            user.alerta_afericao_pa
            or user.alerta_creatinina
            or user.alerta_total_de_consultas_medico
            or user.alerta_ultima_consulta_medico
            or user.alerta_ultima_consulta_odontologica
            or user.alerta_visita_acs
        )
        hipertensao = Hypertension()
        self.cids = list(set(user.cids.split("|")) & set(hipertensao.target))
        if user.alerta_afericao_pa:
            self.registros.append(
                AlertRecord(
                    data=user.ultima_data_afericao_pa,
                    exibir_alerta=True,
                    descricao="data da última aferição de PA",
                    tipo_alerta="alerta-afericao-pa-maior-6-meses",
                )
            )
        if user.alerta_creatinina:
            self.registros.append(
                AlertRecord(
                    data=user.ultima_data_creatinina,
                    exibir_alerta=True,
                    descricao="data do último exame de creatinina",
                    tipo_alerta="alerta-creatinina-maior-6-meses",
                )
            )
        if user.alerta_total_de_consultas_medico:
            self.registros.append(
                AlertRecord(
                    data=user.total_consulta_individual_medico,
                    exibir_alerta=True,
                    descricao="total de consultas médicas ou de enfermagem",
                    tipo_alerta="alerta-total-de-consultas-medico-menor-2",
                )
            )
        if user.alerta_ultima_consulta_medico:
            self.registros.append(
                AlertRecord(
                    data=user.ultimo_atendimento_medico,
                    exibir_alerta=True,
                    descricao="data da última consulta médica ou de enfermagem",
                    tipo_alerta="alerta-ultimo-atendimento-medico-maior-6-meses",
                )
            )
        if user.alerta_ultima_consulta_odontologica:
            self.registros.append(
                AlertRecord(
                    data=user.ultimo_atendimento_odonto,
                    exibir_alerta=True,
                    descricao="data da última consulta odontológica",
                    tipo_alerta="alerta-ultimo-atendimento-odonto-maior-6-meses",
                )
            )

        if user.alerta_visita_acs:
            self.registros.append(
                AlertRecord(
                    data=user.data_ultima_visita_acs,
                    exibir_alerta=True,
                    descricao="data da última visita ACS",
                    tipo_alerta="alerta-data-ultima-visita-acs-maior-6-meses",
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
                "idade": self.idade,
                "diagnostico": self.diagnostico,
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
            user.alerta_afericao_pa
            or user.alerta_total_de_consultas_medico
            or user.alerta_ultima_consulta_medico
            or user.alerta_ultima_consulta_odontologica
            or user.alerta_visita_acs
            or user.alerta_ultima_hemoglobina_glicada
            or user.alerta_ultima_glicemia_capilar
        )
        diabetes = Diabetes()
        self.cids = list(set(user.cids.split("|")) & set(diabetes.target))
        self.registros.append(
            AlertRecord(
                data=user.ultima_data_afericao_pa,
                exibir_alerta=user.alerta_afericao_pa,
                descricao="data da última aferição de PA",
                tipo_alerta="alerta-afericao-pa-maior-6-meses",
            )
        )

        self.registros.append(
            AlertRecord(
                data=user.total_consulta_individual_medico,
                exibir_alerta=user.alerta_total_de_consultas_medico,
                descricao="total de consultas médicas ou de enfermagem",
                tipo_alerta="alerta-total-de-consultas-medico-menor-2",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user.ultimo_atendimento_medico,
                exibir_alerta=user.alerta_ultima_consulta_medico,
                descricao="data da última consulta médica ou de enfermagem",
                tipo_alerta="alerta-ultimo-atendimento-medico-maior-6-meses",
            )
        )

        self.registros.append(
            AlertRecord(
                data=user.ultimo_atendimento_odonto,
                exibir_alerta=user.alerta_ultima_consulta_odontologica,
                descricao="data da última consulta odontológica",
                tipo_alerta="alerta-ultimo-atendimento-odonto-maior-6-meses",
            )
        )

        self.registros.append(
            AlertRecord(
                data=user.data_ultima_visita_acs,
                exibir_alerta=user.alerta_visita_acs,
                descricao="data da última visita ACS",
                tipo_alerta="alerta-data-ultima-visita-acs-maior-6-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user.ultima_data_hemoglobina_glicada or "-",
                exibir_alerta=user.alerta_ultima_hemoglobina_glicada,
                descricao="data-da-ultima-hemoglobina-glicada",
                tipo_alerta="alerta-ultima-data-hemoglobina-glicada-maior-6-meses",
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
                "idade": self.idade,
                "diagnostico": self.diagnostico,
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
        self.nome = user.nome
        self.nome_social = "-"
        self.tipo_localidade = user.tipo_localidade
        self.cpf = user.cpf
        self.cns = user.cns
        self.idade = user.idade
        self.sexo = user.sexo
        self.equipe = user.nome_equipe
        self.microarea = user.micro_area
        self.endereco = f"{user.endereco} {user.numero}, {user.bairro}"
        self.tipo_logradouro = user.tipo_endereco
        self.complemento = user.complemento
        self.cep = user.cep
        self.telefone = user.telefone
        self.possui_alertas = (
            user.indicador_atendimentos_medicos_enfermeiros != 1
            or user.indicador_atendimentos_medicos_enfermeiros_puericultura != 1
            or user.indicador_medicoes_peso_altura_ate2anos != 1
            or user.indicador_visitas_domiciliares_acs != 1
            or user.indicador_teste_pezinho != 1
            or user.indicador_atendimentos_odontologicos != 1
            or user.indicador_vacinas_penta_polio_triplici != 1
        )
        self.registros=[]
        self.registros.append(
            AlertRecord(
                data=user.data_ultimo_atendimento_medico_enfermeiro,
                exibir_alerta=user.indicador_atendimentos_medicos_enfermeiros != 1,
                descricao="data do último atendimento médico/enfermeiro",
                tipo_alerta="data_ultimo_atendimento_medico_enfermeiro",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user.data_ultimo_atendimento_medicos_enfermeiros_puericultura,
                exibir_alerta=user.indicador_atendimentos_medicos_enfermeiros_puericultura
                != 1,
                descricao="data do último atendimento médico/enfermeiro de Puericultura",
                tipo_alerta="indicador_atendimentos_medicos_enfermeiros_puericultura",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user.data_ultima_medicao_peso_altura_ate2anos,
                exibir_alerta=user.indicador_medicoes_peso_altura_ate2anos != 1,
                descricao="data da última medição de peso/altura até dois anos",
                tipo_alerta="data_ultima_medicao_peso_altura_ate2anos",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user.data_ultima_visita_domiciliar_acs,
                exibir_alerta=user.indicador_visitas_domiciliares_acs != 1,
                descricao="data da última visita do ACS ",
                tipo_alerta="data_ultima_visita_domiciliar_acs",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user.data_ultimo_teste_pezinho,
                exibir_alerta=user.indicador_teste_pezinho != 1,
                descricao="data do último teste do pezinho ",
                tipo_alerta="data_ultimo_teste_pezinho",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user.data_ultimo_atendimento_odontologico,
                exibir_alerta=user.indicador_atendimentos_odontologicos != 1,
                descricao="data do último atendimento odontológico ",
                tipo_alerta="data_ultimo_atendimento_odontologico",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user.data_ultima_vacina_triplici,
                exibir_alerta=user.indicador_vacinas_penta_polio_triplici != 1,
                descricao="data do último registro de vacina Penta/Polio/Triplici ",
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
        self.nome = user.nome
        self.nome_social = "-"
        self.tipo_localidade = user.tipo_localidade
        self.cpf = user.cpf
        self.cns = user.cns
        self.idade = user.idade
        self.sexo = user.sexo
        self.equipe = user.nome_equipe
        self.microarea = user.micro_area
        self.endereco = f"{user.endereco} {user.numero}, {user.bairro}"
        self.tipo_logradouro = user.tipo_endereco
        self.complemento = user.complemento
        self.cep = user.cep
        self.telefone = user.telefone
        self.possui_alertas = (
            user.indicador_atendimentos_medicos != 1
            or user.indicador_medicoes_peso_altura != 1
            or user.indicador_registros_creatinina != 1
            or user.indicador_vacinas_influenza != 1
            or user.indicador_atendimento_odontologico != 1
            or user.indicador_visitas_domiciliares_acs != 1
        )
        self.registros = []
        self.registros.append(
            AlertRecord(
                data=user.data_ultimo_atendimento_medicos,
                exibir_alerta=user.indicador_atendimentos_medicos != 1,
                descricao="data do último atendimento médico/enfermeiro",
                tipo_alerta="data_ultimo_atendimento_medicos",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user.data_ultima_medicao_peso_altura,
                exibir_alerta=user.indicador_medicoes_peso_altura != 1,
                descricao="data da última medição de peso e altura",
                tipo_alerta="data_ultima_medicao_peso_altura",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user.data_ultimo_registro_creatinina,
                exibir_alerta=user.indicador_registros_creatinina != 1,
                descricao="data do último registro de creatinina ",
                tipo_alerta="data_ultimo_registro_creatinina",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user.data_ultima_vacina_influenza,
                exibir_alerta=user.indicador_vacinas_influenza != 1,
                descricao="data do último registro de vacina da Influenza ",
                tipo_alerta="data_ultima_vacina_influenza",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user.data_ultimo_atendimento_odontologico,
                exibir_alerta=user.indicador_atendimento_odontologico != 1,
                descricao="data do último registro de atendimento odontológico ",
                tipo_alerta="data_ultimo_atendimento_odontologico",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user.data_ultima_visita_domiciliar_acs,
                exibir_alerta=user.indicador_visitas_domiciliares_acs != 1,
                descricao="data da última visita do ACS ",
                tipo_alerta="data_ultima_visita_domiciliar_acs",
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

    def __init__(self, user: Pessoas):
        self.nome = user.nome
        self.nome_social = "-"
        self.tipo_localidade = user.tipo_localidade
        self.cpf = user.cpf
        self.cns = user.cns
        self.idade = user.idade
        self.sexo = user.sexo
        self.equipe = user.nome_equipe
        self.microarea = user.micro_area
        self.endereco = f"{user.endereco} {user.numero}, {user.bairro}"
        self.tipo_logradouro = user.tipo_endereco
        self.complemento = user.complemento
        self.cep = user.cep
        self.telefone = user.telefone

        ultima_atualizacao_cidadao, ultima_atualizacao_fcd = True, True

        if user.diferenca_ultima_atualizacao_cidadao is not None and user.diferenca_ultima_atualizacao_cidadao < 24:
            ultima_atualizacao_cidadao = False

        if user.diferenca_ultima_atualizacao_fcd is not None and user.diferenca_ultima_atualizacao_fcd < 24:
            ultima_atualizacao_fcd = False

        self.possui_alertas = (
            ultima_atualizacao_cidadao or
            ultima_atualizacao_fcd
        )
        self.registros = []
        self.registros.append(
            AlertRecord(
                data=user.ultima_atualizacao_cidadao,
                exibir_alerta=ultima_atualizacao_cidadao,
                descricao="data da última atualização da ficha de cadastro individual",
                tipo_alerta="ultima_atualizacao_cidadao",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user.ultima_atualizacao_fcd,
                exibir_alerta=ultima_atualizacao_fcd,
                descricao="data da última atualização da ficha de cadastro domiciliar e territorial",
                tipo_alerta="ultima_atualizacao_fcd",
            )
        )

    def to_dict(self):
        return dict(
            {
                "nome": self.nome,
                "nomeSocialSelecionado": self.nome_social,
                "zonaUrbana": "urbana" in self.tipo_localidade.lower() ,
                "zonaRural": "rural" in self.tipo_localidade.lower(),
                "possuiAlertas": self.possui_alertas,
                "cpf": self.cpf,
                "cns": self.cns,
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
