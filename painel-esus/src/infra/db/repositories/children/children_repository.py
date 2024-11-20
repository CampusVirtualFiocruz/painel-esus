# pylint: disable=R0913,W0611
from sqlalchemy import extract
from src.infra.db.entities.crianca import Crianca
from src.infra.db.entities.equipes import Equipes
from src.infra.db.entities.pessoas import Pessoas
from src.infra.db.repositories.children.sqls import children_by_age_and_gender
from src.infra.db.repositories.children.sqls import children_by_age_and_location
from src.infra.db.repositories.children.sqls import children_location_rate
from src.infra.db.repositories.children.sqls import children_total
from src.infra.db.repositories.children.sqls import children_total_cares
from src.infra.db.repositories.children.sqls import group_by_race
from src.infra.db.settings.connection_local import DBConnectionHandler

columns = [
    Crianca.atendimentos_medicos,
    Crianca.data_ultimo_atendimento_medicos,
    Crianca.indicador_atendimentos_medicos,
    Crianca.medicoes_peso_altura,
    Crianca.data_ultima_medicao_peso_altura,
    Crianca.indicador_medicoes_peso_altura,
    Crianca.registros_creatinina,
    Crianca.data_ultimo_registro_creatinina,
    Crianca.indicador_registros_creatinina,
    Crianca.vacinas_influenza,
    Crianca.data_ultima_vacina_influenza,
    Crianca.indicador_vacinas_influenza,
    Crianca.atendimentos_odontologicos,
    Crianca.data_ultimo_atendimento_odontologico,
    Crianca.indicador_atendimento_odontologico,
    Crianca.visitas_domiciliares_acs,
    Crianca.data_ultima_visita_domiciliar_acs,
    Crianca.indicador_visitas_domiciliares_acs,
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
                .distinct(Crianca.co_fat_cidadao_pec)
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
            users = users.group_by(Crianca.co_fat_cidadao_pec)
            total = users.count()
            users = (
                users.order_by(Pessoas.nome)
                .offset(max(0, page - 1) * pagesize)
                .limit(pagesize)
            )
            # print(str(users))
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
