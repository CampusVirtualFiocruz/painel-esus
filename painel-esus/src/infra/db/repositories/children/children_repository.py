# pylint: disable=R0913,W0611
import pandas as pd
from sqlalchemy import extract, or_
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
    professional_cares,
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
        query:str = None,
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

            conditions, or_conditions = [],[]
            if cnes is not None and cnes:
                conditions+=[Equipes.codigo_unidade_saude == cnes]

            if cpf is not None and cpf:
                conditions += [Pessoas.cpf.ilike(f"%{query}%")]
                
            if query is not None and query:
                or_conditions+=[
                    Pessoas.cpf.ilike(f"%{query}%"),
                    Pessoas.cns.ilike(f"%{query}%"),
                    Pessoas.nome.ilike(f"%{query}%"),
                    ]
            if equipe is not None and equipe:
                conditions+=[Equipes.codigo_equipe == equipe]
            if len(conditions)>0:
                users = users.filter(*conditions)

            if len(or_conditions)>0:
                users = users.filter(or_(*or_conditions))

            users = users.group_by(Crianca.cidadao_pec)

            users = (
                users.order_by(Pessoas.nome)
                .offset(max(0, page - 1) * pagesize)
                .limit(pagesize)
            )
            total = users.count()
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

    def find_group_professionals_care(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = professional_cares(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_grouping_by_race(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = group_by_race(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_all_download(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler() as db_con:
            where_clause = ""
            if cnes is not None and cnes:
                where_clause += f" where e.codigo_unidade_saude = {cnes} "
                if equipe is not None and equipe:
                    where_clause += f" and e.codigo_equipe = {equipe} "
            response = pd.read_sql_query(
                con=db_con.get_engine(),
                sql=f"""select
                    p.cidadao_pec as codigo_cidadao,
                    p.nome  as nome,
                    p.cns as cns,
                    p.cpf as cpf,
                    p.sexo as sexo,
                    p.raca_cor  as "raca/cor",
                    group_concat(e.micro_area) micro_area,
                    group_concat(e.nome_equipe) nome_equipe,
                    e.nome_unidade_saude,
                    STRFTIME( '%d-%m-%Y',p.data_nascimento) data_nascimento ,
                    p.idade ,
                    p.tipo_endereco ,
                    p.endereco || ' ' || p.numero logradouro,
                    p.complemento,
                    p.bairro ,
                    p.cep,
                    p.tipo_localidade ,
                    case 
                        when c.indicador_atendimentos_medicos_enfermeiros   == 1 then 'SIM'
                        when c.indicador_atendimentos_medicos_enfermeiros != 1 or  c.indicador_atendimentos_medicos_enfermeiros is null then 'NÃO'	
                    end indicador_atendimentos_medicos_enfermeiros,
                    STRFTIME( '%d-%m-%Y',c.data_ultimo_atendimento_medico_enfermeiro) data_ultimo_atendimento_medico_enfermeiro, 
                    case
                        when c.atendimentos_medicos_enfermeiros_8d_vida == 1 then 'SIM'
                        when c.atendimentos_medicos_enfermeiros_8d_vida != 1 or  c.atendimentos_medicos_enfermeiros_8d_vida is null then 'NÃO'
                    end atendimentos_medicos_enfermeiros_8d_vida, 
                    c.atendimentos_medicos_enfermeiros_puericult, 
                    STRFTIME( '%d-%m-%Y',c.data_ultimo_atendimento_medicos_enfermeiros_puericult) data_ultimo_atendimento_medicos_enfermeiros_puericult, 
                    case 
                        when c.indicador_atendimentos_medicos_enfermeiros_puericult   = 1 then 'SIM'
                        when c.indicador_atendimentos_medicos_enfermeiros_puericult != 1 or  c.indicador_atendimentos_medicos_enfermeiros_puericult is null then 'NÃO'	
                    end indicador_atendimentos_medicos_enfermeiros_puericultura,
                    c.medicoes_peso_altura_ate2anos, 
                    STRFTIME( '%d-%m-%Y',c.data_ultima_medicao_peso_altura_ate2anos) data_ultima_medicao_peso_altura_ate2anos, 
                    case 
                        when c.indicador_medicoes_peso_altura_ate2anos   = 1 then 'SIM'
                        when c.indicador_medicoes_peso_altura_ate2anos != 1 or  c.indicador_medicoes_peso_altura_ate2anos is null then 'NÃO'	
                    end indicador_medicoes_peso_altura_ate2anos,
                    STRFTIME( '%d-%m-%Y',c.data_ultima_visita_domiciliar_acs) data_ultima_visita_domiciliar_acs, 
                    case 
                        when c.indicador_visitas_domiciliares_acs   = 1 then 'SIM'
                        when c.indicador_visitas_domiciliares_acs != 1 or  c.indicador_visitas_domiciliares_acs is null then 'NÃO'	
                    end indicador_visitas_domiciliares_acs,
                    c.visitas_domiciliares_acs, 
                    c.teste_pezinho, 
                    case 
                        when c.indicador_teste_pezinho   = 1 then 'SIM'
                        when c.indicador_teste_pezinho != 1 or  c.indicador_teste_pezinho is null then 'NÃO'	
                    end indicador_teste_pezinho,
                     STRFTIME( '%d-%m-%Y',c.data_ultimo_teste_pezinho) data_ultimo_teste_pezinho, 
                    c.n_penta, 
                    c.n_polio, 
                    c.n__triplici, 
                    STRFTIME( '%d-%m-%Y',c.data_ultima_vacina_penta) data_ultima_vacina_penta, 
                    STRFTIME( '%d-%m-%Y',c.data_ultima_vacina_polio) data_ultima_vacina_polio, 
                    STRFTIME( '%d-%m-%Y',c.data_ultima_vacina_triplici) data_ultima_vacina_triplici, 
                    case 
                        when c.indicador_vacinas_penta_polio_triplici   == 1 then 'SIM'
                        when c.indicador_vacinas_penta_polio_triplici != 1 or  c.indicador_vacinas_penta_polio_triplici is null then 'NÃO'	
                    end indicador_vacinas_penta_polio_triplici,
                    c.atendimentos_odontologicos, 
                    STRFTIME( '%d-%m-%Y',c.data_ultimo_atendimento_odontologico) data_ultimo_atendimento_odontologico, 
                    case 
                        when c.indicador_atendimentos_odontologicos   == 1 then 'SIM'
                        when c.indicador_atendimentos_odontologicos != 1 or  c.indicador_atendimentos_odontologicos is null  then 'NÃO'	
                    end indicador_atendimentos_odontologicos
                from
                    crianca c   join pessoas p on p.cidadao_pec = c.cidadao_pec 
                    left join equipes e on e.cidadao_pec  = p.cidadao_pec 
                {where_clause}
group by p.cidadao_pec	
order by p.nome
                """,
            )
            return response
