# pylint: disable=R0913,W0611
from sqlalchemy import extract
from src.infra.db.entities.crianca import Crianca
from src.infra.db.entities.equipes import Equipes
from src.infra.db.entities.pessoas import Pessoas
from src.infra.db.repositories.children.sqls import (
    children_by_age_and_gender,
    children_by_age_and_location,
    children_location_rate,
    children_total,
    children_total_cares,
    group_by_race,
)
from src.infra.db.settings.connection_local import DBConnectionHandler

columns = [
    Crianca.cidadao_pec,
    Crianca.indicador_atendimentos_medicos_enfermeiros,
    Crianca.data_ultimo_atendimento_medico_enfermeiro,
    Crianca.atendimentos_medicos_enfermeiros_8d_vida,
    Crianca.atendimentos_medicos_enfermeiros_puericult,
    Crianca.data_ultimo_atendimento_medicos_enfermeiros_puericultura,
    Crianca.indicador_atendimentos_medicos_enfermeiros_puericultura,
    Crianca.medicoes_peso_altura_ate2anos,
    Crianca.data_ultima_medicao_peso_altura_ate2anos,
    Crianca.indicador_medicoes_peso_altura_ate2anos,
    Crianca.data_ultima_visita_domiciliar_acs,
    Crianca.indicador_visitas_domiciliares_acs,
    Crianca.visitas_domiciliares_acs,
    Crianca.teste_pezinho,
    Crianca.indicador_teste_pezinho,
    Crianca.data_ultimo_teste_pezinho,
    Crianca.atendimentos_odontologicos,
    Crianca.data_ultimo_atendimento_odontologico,
    Crianca.indicador_atendimentos_odontologicos,
    Crianca.n_penta,
    Crianca.n_polio,
    Crianca.n__triplici,
    Crianca.data_ultima_vacina_penta,
    Crianca.data_ultima_vacina_polio,
    Crianca.data_ultima_vacina_triplici,
    Crianca.indicador_vacinas_penta_polio_triplici,
    Crianca.n_medicos,
    Crianca.n_enfer,
    Crianca.n_fono,
    Crianca.n_psicol,
    Crianca.n_educ_fisica,
    Crianca.n_assist_social,
    Crianca.n_tera_ocup,
    Crianca.n_farmac,
    Crianca.n_fisio,
    Crianca.n_nutric,
    Crianca.n_ciru_dent,
    Crianca.n_outros,
    Crianca.total,
    Pessoas.co_cidadao,
    Pessoas.raca_cor,
    Pessoas.cpf,
    Pessoas.cns,
    Pessoas.nome,
    Pessoas.nome_social,
    Pessoas.data_nascimento,
    Pessoas.idade,
    Pessoas.sexo,
    Pessoas.identidade_genero,
    Pessoas.telefone,
    Pessoas.ultima_atualizacao_cidadao,
    Pessoas.ultima_atualizacao_fcd,
    Pessoas.tipo_endereco,
    Pessoas.endereco,
    Pessoas.complemento,
    Pessoas.numero,
    Pessoas.bairro,
    Pessoas.cep,
    Pessoas.tipo_localidade,
    Equipes.nome_unidade_saude,
    Equipes.nome_equipe,
    Equipes.micro_area,
]

class ChildrenRepository:

    def find_total_children_cares(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = children_total_cares(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_grouping_by_ages_location(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = children_by_age_and_location(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_filter_nominal(
        self,
        cnes: int,
        page: int = 0,
        pagesize: int = 10,
        nome: str = None,
        cpf: str = None,
        equipe: int = None,
    ):
        page = int(page) if page is not None else 0
        pagesize = int(pagesize) if pagesize is not None else 0
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session.query(*columns)
                .distinct(Crianca.cidadao_pec)
                .join(
                    Pessoas,
                    Pessoas.cidadao_pec == Crianca.cidadao_pec,
                )
                .join(
                    Equipes,
                    Equipes.cidadao_pec == Crianca.cidadao_pec,
                )
            )

            users = users.filter(Equipes.codigo_unidade_saude == cnes)
            if nome is not None and nome:
                users = users.filter(Pessoas.nome.ilike(f"%{nome}%"))
            if cpf is not None and cpf:
                users = users.filter(Pessoas.cpf.ilike(f"%{cpf}%"))
            if equipe is not None and equipe:
                users = users.filter(Equipes.codigo_equipe == equipe)
            
            users = users.group_by(Crianca.cidadao_pec)
            total = users.count()
            users = (
                users.order_by(Pessoas.nome)
                .offset(max(0, page - 1) * pagesize)
                .limit(pagesize)
            )
            return {
                "itemsCount": total,
                "itemsPerPage": pagesize,
                "page": page,
                "pagesCount": round(total / pagesize),
                "items": list(users),
            }

    def find_grouping_by_ages_gender(self, cnes:int=None, equipe:int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = children_by_age_and_gender(cnes, equipe)
            result = con.execute(sql)
            return result

    def find_children_location_rate(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = children_location_rate(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_grouping_by_race(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = group_by_race(cnes, equipe)
            result = con.execute(sql)
            return list(result)
