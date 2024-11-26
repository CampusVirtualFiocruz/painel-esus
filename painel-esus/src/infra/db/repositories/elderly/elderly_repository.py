import pandas as pd
from sqlalchemy import or_
from src.infra.db.entities.equipes import Equipes
from src.infra.db.entities.idoso import Idoso
from src.infra.db.entities.pessoas import Pessoas
from src.infra.db.repositories.elderly.sqls import (
    get_elderly_total_influenza,
    get_elderly_total_odonto,
    get_elderly_total_on_ubs_and_team,
    group_by_age_gender,
    group_by_age_location,
    group_by_imc,
    group_by_race,
    total_hipertension_diabetes,
)
from src.infra.db.settings.connection_local import DBConnectionHandler

columns = [
    Idoso.cidadao_pec,
    Idoso.atendimentos_medicos,
    Idoso.data_ultimo_atendimento_medicos,
    Idoso.indicador_atendimentos_medicos,
    Idoso.medicoes_peso_altura,
    Idoso.data_ultima_medicao_peso_altura,
    Idoso.indicador_medicoes_peso_altura,
    Idoso.imc,
    Idoso.categoria_imc,
    Idoso.registros_creatinina,
    Idoso.data_ultimo_registro_creatinina,
    Idoso.indicador_registros_creatinina,
    Idoso.vacinas_influenza,
    Idoso.data_ultima_vacina_influenza,
    Idoso.indicador_vacinas_influenza,
    Idoso.atendimentos_odontologicos,
    Idoso.data_ultimo_atendimento_odontologico,
    Idoso.indicador_atendimento_odontologico,
    Idoso.visitas_domiciliares_acs,
    Idoso.data_ultima_visita_domiciliar_acs,
    Idoso.indicador_visitas_domiciliares_acs,
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

class ElderlyRepository:

    def find_total(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = get_elderly_total_on_ubs_and_team(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_group_by_age_location(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = group_by_age_location(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_group_by_race(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = group_by_race(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_group_by_age_gender(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = group_by_age_gender(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_group_by_influenza_rate(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = get_elderly_total_influenza(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_group_by_odonto_rate(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = get_elderly_total_odonto(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_total_hipertension_diabetes(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = total_hipertension_diabetes(cnes, equipe)
            result = con.execute(sql)
            return list(result)

    def find_group_by_imc(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler().get_engine().connect() as con:
            sql = group_by_imc(cnes, equipe)
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
        query: str = None,
    ):
        page = int(page) if page is not None else 0
        pagesize = int(pagesize) if pagesize is not None else 0
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session.query(*columns)
                .distinct(Idoso.cidadao_pec)
                .join(
                    Pessoas,
                    Pessoas.cidadao_pec == Idoso.cidadao_pec,
                )
                .join(
                    Equipes,
                    Equipes.cidadao_pec == Idoso.cidadao_pec,
                )
            )

            conditions, or_conditions = [],[]
            if cnes is not None and cnes:
                conditions+=[Equipes.codigo_unidade_saude == cnes]

            if nome is not None and nome:
                conditions+=[Pessoas.nome.ilike(f"%{nome}%")]

            if cpf is not None and cpf:
                conditions=+[Pessoas.cpf.ilike(f"%{cpf}%")]

            if equipe is not None and equipe:
                conditions+=[Equipes.codigo_equipe == equipe]

            if query is not None and query:
                or_conditions += [
                    Pessoas.cpf.ilike(f"%{query}%"),
                    Pessoas.cns.ilike(f"%{query}%"),
                    Pessoas.nome.ilike(f"%{query}%"),
                ]
            if len(conditions) > 0:
                users = users.filter(*conditions)

            if len(or_conditions) > 0:
                users = users.filter(or_(*or_conditions))
                
            users = users.group_by(Idoso.cidadao_pec)
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

    def find_all_download(self, cnes: int = None, equipe: int = None):
        with DBConnectionHandler() as db_con:
            where_clause = ""
            if cnes is not None and cnes:
                where_clause +=  f' where e.codigo_unidade_saude = {cnes} '
                if equipe is not None and equipe:
                    where_clause +=  f' and e.codigo_equipe = {equipe} '
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
                    STRFTIME( '%d-%m-%Y',p.data_nascimento) data_nascimento,
                    p.idade ,
                    p.tipo_endereco ,
                    p.endereco || ' ' || p.numero logradouro,
                    p.complemento,
                    p.bairro ,
                    p.cep,
                    p.tipo_localidade ,
                    i.atendimentos_medicos,
                    STRFTIME( '%d-%m-%Y',i.data_ultimo_atendimento_medicos) data_ultimo_atendimento_medicos,
                    i.medicoes_peso_altura , 
                    STRFTIME( '%d-%m-%Y',i.data_ultima_medicao_peso_altura) data_ultima_medicao_peso_altura, 
                    case 
                        when i.indicador_medicoes_peso_altura  = 1 then 'SIM'
                        when i.indicador_medicoes_peso_altura != 1 then 'NÃO'	
                    end indicador_medicoes_peso_altura ,
                    i.imc , 
                    i.categoria_imc , 
                    i.registros_creatinina , 
                    STRFTIME( '%d-%m-%Y',i.data_ultimo_registro_creatinina) data_ultimo_registro_creatinina, 
                    case 
                        when i.indicador_registros_creatinina   = 1 then 'SIM'
                        when i.indicador_registros_creatinina  != 1 then 'NÃO'	
                    end indicador_registros_creatinina  ,
                    case 
                        when i.indicador_visitas_domiciliares_acs   = 1 then 'SIM'
                        when i.indicador_visitas_domiciliares_acs  != 1 then 'NÃO'	
                    end indicador_visitas_domiciliares_acs  ,
                    i.visitas_domiciliares_acs , 
                    STRFTIME( '%d-%m-%Y',i.data_ultima_visita_domiciliar_acs) data_ultima_visita_domiciliar_acs, 
                    i.vacinas_influenza , 
                    STRFTIME( '%d-%m-%Y',i.data_ultima_vacina_influenza) data_ultima_vacina_influenza, 
                    case 
                        when i.indicador_vacinas_influenza   = 1 then 'SIM'
                        when i.indicador_vacinas_influenza  != 1 then 'NÃO'	
                    end indicador_vacinas_influenza  ,
                    i.atendimentos_odontologicos , 
                    STRFTIME( '%d-%m-%Y',i.data_ultimo_atendimento_odontologico) data_ultimo_atendimento_odontologico, 
                    case 
                        when i.indicador_atendimento_odontologico 	   = 1 then 'SIM'
                        when i.indicador_atendimento_odontologico 	  != 1 then 'NÃO'	
                    end indicador_atendimento_odontologico 	  
                from
                    idoso i   join pessoas p on p.cidadao_pec = i.cidadao_pec 
                    left join equipes e on e.cidadao_pec  = p.cidadao_pec 
                {where_clause}
group by p.cidadao_pec	
order by p.nome
                """,
            )
            return response
