# pylint: disable=R0902
from src.infra.db.entities.diabetes_nominal import DiabetesNominal
from src.infra.db.entities.hipertensao_nominal import HipertensaoNominal


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


class HypertensionNominalListAdapter:

    def __init__(self, user: HipertensaoNominal):
        self.nome = user.no_cidadao
        self.nome_social = "-"
        self.tipo_localidade = user.ds_tipo_localizacao
        self.possui_alertas = (
            user.alerta_afericao_pa
            or user.alerta_creatinina
            or user.alerta_total_de_consultas_medico
            or user.alerta_ultima_consulta_medico
            or user.alerta_ultima_consulta_odontologica
            or user.alerta_visita_acs
        )
        self.cpf = user.nu_cpf
        self.cns = user.nu_cns
        self.idade = user.idade
        self.diagnostico = "Hipertensao"
        self.sexo = user.no_sexo
        self.equipe = user.equipe
        self.microarea = user.nu_micro_area
        self.endereco = f"{user.ds_logradouro} {user.nu_numero}"
        self.cep = user.ds_cep
        self.telefone = "-"
        self.registros = []
        self.primeiro_registro = user.min_date
        self.cids = list(set(user.cids.split("|")))
        if user.alerta_afericao_pa:
            self.registros.append(
                AlertRecord(
                    data=user.ultima_data_afericao_pa,
                    exibir_alerta=True,
                    descricao="ultima-afericao-pa",
                    tipo_alerta="alerta-afericao-pa-maior-6-meses",
                )
            )
        if user.alerta_creatinina:
            self.registros.append(
                AlertRecord(
                    data=user.ultima_data_creatinina,
                    exibir_alerta=True,
                    descricao="ultimo-exame-creatinina",
                    tipo_alerta="alerta-creatinina-maior-6-meses",
                )
            )
        if user.alerta_total_de_consultas_medico:
            self.registros.append(
                AlertRecord(
                    data=user.total_consulta_individual_medico,
                    exibir_alerta=True,
                    descricao="total-de-consultas-medico",
                    tipo_alerta="alerta-total-de-consultas-medico-menor-2",
                )
            )
        if user.alerta_ultima_consulta_medico:
            self.registros.append(
                AlertRecord(
                    data=user.ultimo_atendimento_medico,
                    exibir_alerta=True,
                    descricao="ultimo-atendimento-medico",
                    tipo_alerta="alerta-ultimo-atendimento-medico-maior-6-meses",
                )
            )
        if user.alerta_ultima_consulta_odontologica:
            self.registros.append(
                AlertRecord(
                    data=user.ultimo_atendimento_odonto,
                    exibir_alerta=True,
                    descricao="ultimo-atendimento-odonto",
                    tipo_alerta="alerta-ultimo-atendimento-odonto-maior-6-meses",
                )
            )

        if user.alerta_visita_acs:
            self.registros.append(
                AlertRecord(
                    data=user.data_ultima_visita_acs,
                    exibir_alerta=True,
                    descricao="ultimo-data-ultima-visita-acs",
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


class DiabetesNominalListAdapter:

    def __init__(self, user: DiabetesNominal):
        self.nome = user.no_cidadao
        self.nome_social = "-"
        self.tipo_localidade = user.ds_tipo_localizacao
        self.possui_alertas = (
            user.alerta_afericao_pa
            or user.alerta_total_de_consultas_medico
            or user.alerta_ultima_consulta_medico
            or user.alerta_ultima_consulta_odontologica
            or user.alerta_visita_acs
            or user.alerta_ultima_hemoglobina_glicada
            or user.alerta_ultima_glicemia_capilar
        )
        self.cpf = user.nu_cpf
        self.cns = user.nu_cns
        self.idade = user.idade
        self.diagnostico = "Diabetes"
        self.sexo = user.no_sexo
        self.equipe = user.equipe
        self.microarea = user.nu_micro_area
        self.endereco = f"{user.ds_logradouro} {user.nu_numero}"
        self.cep = user.ds_cep
        self.telefone = "-"
        self.registros = []
        self.primeiro_registro = user.min_date
        self.cids = list(set(user.cids.split("|")))

        self.registros.append(
            AlertRecord(
                data=user.ultima_data_afericao_pa,
                exibir_alerta=user.alerta_afericao_pa,
                descricao="ultima-afericao-pa",
                tipo_alerta="alerta-afericao-pa-maior-6-meses",
            )
        )

        self.registros.append(
            AlertRecord(
                data=user.total_consulta_individual_medico,
                exibir_alerta=user.alerta_total_de_consultas_medico,
                descricao="total-de-consultas-medico",
                tipo_alerta="alerta-total-de-consultas-medico-menor-2",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user.ultimo_atendimento_medico,
                exibir_alerta=user.alerta_ultima_consulta_medico,
                descricao="ultimo-atendimento-medico",
                tipo_alerta="alerta-ultimo-atendimento-medico-maior-6-meses",
            )
        )

        self.registros.append(
            AlertRecord(
                data=user.ultimo_atendimento_odonto,
                exibir_alerta=user.alerta_ultima_consulta_odontologica,
                descricao="ultimo-atendimento-odonto",
                tipo_alerta="alerta-ultimo-atendimento-odonto-maior-6-meses",
            )
        )

        self.registros.append(
            AlertRecord(
                data=user.data_ultima_visita_acs,
                exibir_alerta=user.alerta_visita_acs,
                descricao="ultimo-data-ultima-visita-acs",
                tipo_alerta="alerta-data-ultima-visita-acs-maior-6-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user.ultima_data_hemoglobina_glicada or "-",
                exibir_alerta=user.alerta_ultima_hemoglobina_glicada,
                descricao="ultima-data-hemoglobina-glicada",
                tipo_alerta="alerta-ultima-data-hemoglobina-glicada-maior-6-meses",
            )
        )
        self.registros.append(
            AlertRecord(
                data=user.ultima_data_glicemia_capilar or "-",
                exibir_alerta=user.alerta_ultima_glicemia_capilar,
                descricao="ultima-data-glicemia-capilar",
                tipo_alerta="alerta-ultima-data-glicemia-capilar-maior-6-meses",
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
