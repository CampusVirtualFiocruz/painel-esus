# pylint: disable=R0913
from typing import Dict

import pandas as pd
from src.domain.entities.hypertension import Hypertension
from src.infra.db.entities.equipes import Equipes
from src.infra.db.entities.hipertensao_nominal import HipertensaoNominal
from src.infra.db.entities.pessoas import Pessoas
from src.infra.db.settings.connection_local import DBConnectionHandler

columns = [
    HipertensaoNominal.co_fat_cidadao_pec,
    HipertensaoNominal.diagnostico,
    HipertensaoNominal.cids,
    HipertensaoNominal.min_date,
    HipertensaoNominal.data_ultima_visita_acs,
    HipertensaoNominal.alerta_visita_acs,
    HipertensaoNominal.total_consulta_individual_medico,
    HipertensaoNominal.alerta_total_de_consultas_medico,
    HipertensaoNominal.ultimo_atendimento_medico,
    HipertensaoNominal.alerta_ultima_consulta_medico,
    HipertensaoNominal.ultimo_atendimento_odonto,
    HipertensaoNominal.alerta_ultima_consulta_odontologica,
    HipertensaoNominal.ultima_data_afericao_pa,
    HipertensaoNominal.alerta_afericao_pa,
    HipertensaoNominal.ultima_data_creatinina,
    HipertensaoNominal.alerta_creatinina,
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
    Equipes.nome_unidade_saude, Equipes.nome_equipe, Equipes.micro_area
]
class HypertensionNominalListRepository:

    def find_all(self, cnes: int = None) -> Dict:
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session.query(HipertensaoNominal,)
                .join(Pessoas, Pessoas.cidadao_pec == HipertensaoNominal.co_fat_cidadao_pec,)\
                .join(Equipes, Equipes.cidadao_pec == HipertensaoNominal.co_fat_cidadao_pec,)
                .filter(Equipes.codigo_unidade_saude == cnes).all()
            )
            return users

    def find_by_id(self, cidadao_pec):
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session.query(HipertensaoNominal)
                .join(
                    Pessoas,
                    Pessoas.cidadao_pec == HipertensaoNominal.co_fat_cidadao_pec,
                )
                .filter(HipertensaoNominal.co_fat_cidadao_pec == cidadao_pec)
                .first()
            )
            return users

    def find_all_download(self, cnes: int = None) -> Dict:
        with DBConnectionHandler() as db_con:
            response = pd.read_sql_query(
                con=db_con.get_engine(),
                sql=f"""
                select
	p.cidadao_pec as codigo_cidadao,
	p.nome  as nome,
	p.cns as cns,
	p.cpf as cpf,
	p.sexo as sexo,
	p.raca_cor  as "raca/cor",
	group_concat(e.micro_area) micro_area,
	group_concat(e.nome_equipe) nome_equipe,
	e.nome_unidade_saude,
	p.data_nascimento ,
	p.idade ,
	p.tipo_endereco ,
	p.endereco || ' ' || p.numero logradouro,
	p.complemento,
	p.bairro ,
	p.cep,
	p.tipo_localidade ,
	hn.min_date primeiro_atendimento,
	hn.cids ,
	hn.ciaps ,
	hn.diagnostico ,
	hn.data_ultima_visita_acs,
	case 
		when hn.alerta_visita_acs = 1 then 'SIM'
		when hn.alerta_visita_acs = 0 then 'NAO'
	end alerta_visita_acs ,
	hn.total_consulta_individual_medico ,
	hn.total_consulta_individual_enfermeiro,
	hn.total_consulta_individual_medico_enfermeiro total_de_consultas_medicas_enfermagem,
    case 
		when hn.alerta_total_de_consultas_medico = 1 then 'SIM'
		when hn.alerta_total_de_consultas_medico = 0 then 'NAO'
	end alerta_total_de_consultas_medicas_enfermagem,
	hn.ultimo_atendimento_medico_enfermeiro data_ultima_consulta_medica_enfermagem,
	hn.ultimo_atendimento_odonto,
    case 
		when hn.alerta_ultima_consulta_odontologica = 1 then 'SIM'
		when hn.alerta_ultima_consulta_odontologica = 0 then 'NAO'
	end alerta_ultima_consulta_odontologica	,
	hn.ultima_data_afericao_pa ,
	case 
		when hn.alerta_afericao_pa = 1 then 'SIM'
		when hn.alerta_afericao_pa = 0 then 'NAO'
	end alerta_afericao_pa ,
	hn.ultima_data_creatinina  ,
	case 
		when hn.alerta_creatinina  = 1 then 'SIM'
		when hn.alerta_creatinina  = 0 then 'NAO'
	end alerta_creatinina   
from
	hipertensao_nominal hn  join pessoas p on p.cidadao_pec = hn.co_fat_cidadao_pec 
	left join equipes e on e.cidadao_pec  = p.cidadao_pec 
where e.codigo_unidade_saude = {cnes}
group by p.cidadao_pec	
order by p.nome
                """,
            )
            hypertension = Hypertension()
            response['cids'] = response['cids'].apply( lambda x: ", ".join(list(set(x.split("|")) & set(hypertension.target))))
            response['ciaps'] = response['ciaps'].apply( lambda x: ", ".join(list(set(x.split("|")) & set(hypertension.target))))

            return response

    def find_by_nome(self, nome: str):
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session.query(HipertensaoNominal)
                .join(Pessoas, Pessoas.cidadao_pec == HipertensaoNominal.co_fat_cidadao_pec, )
                .filter(Pessoas.nome.ilike(f"%{nome}%"))
                .all()
            )
            return users

    def find_filter(
        self,
        cnes: int,
        page: int = 0,
        pagesize: int = 10,
        nome: str = None,
        cpf: str = None,
    ):
        page = int(page) if page is not None else 0
        pagesize = int(pagesize) if pagesize is not None else 0
        with DBConnectionHandler() as db_con:
            users = (
                db_con.session.query(*columns)
                .distinct(HipertensaoNominal.co_fat_cidadao_pec)
                .join(
                    Pessoas,
                    Pessoas.cidadao_pec == HipertensaoNominal.co_fat_cidadao_pec,
                )
                .join(
                    Equipes,
                    Equipes.cidadao_pec == HipertensaoNominal.co_fat_cidadao_pec,
                )
            )

            users = users.filter(
                Equipes.codigo_unidade_saude == cnes
            )
            if nome is not None:
                users = users.filter(Pessoas.nome.ilike(f"%{nome}%"))
            if cpf is not None:
                users = users.filter(Pessoas.cpf.ilike(f"%{cpf}%"))

            users = users.group_by(HipertensaoNominal.co_fat_cidadao_pec)
            total = users.count()
            users = (
                users.order_by(Pessoas.nome)
                .offset(max(0, ((page - 1) * pagesize)))
                .limit(pagesize)
            )
            return {
                "itemsCount": total,
                "itemsPerPage": pagesize,
                "page": page,
                "pagesCount": round(total / pagesize),
                "items": list(users),
            }
