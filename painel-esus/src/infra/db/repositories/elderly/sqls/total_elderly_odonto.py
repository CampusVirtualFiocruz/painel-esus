from sqlalchemy import text


def get_elderly_total_odonto(cnes: int = None, equipe:int = None):
    where_clause, total_where_clause = "  ", " "
    if cnes is not None and cnes:
        where_clause += f" where pessoas.codigo_unidade_saude  = {cnes} "
        total_where_clause += f" and pessoas.codigo_unidade_saude  = {cnes} "
        if equipe is not None and equipe:
            where_clause += f" and pessoas.codigo_equipe_vinculada  = {equipe} "
            total_where_clause += f" and pessoas.codigo_equipe_vinculada  = {equipe} "

    sql =f"""with
    idosos as (
        SELECT
            DISTINCT idoso.cidadao_pec AS idoso_cidadao_pec,
            idoso.indicador_atendimento_odontologico
        FROM
            idoso
        JOIN pessoas ON
            pessoas.cidadao_pec = idoso.cidadao_pec
        JOIN equipes ON
            equipes.cidadao_pec = idoso.cidadao_pec
        {where_clause}
    ),
total as (SELECT  count(DISTINCT pessoas.cidadao_pec ) as total
		FROM pessoas 
        JOIN equipes ON
            equipes.cidadao_pec = pessoas.cidadao_pec
        WHERE pessoas.idade >= 60 {total_where_clause}
)
 select 
  (select count(*) quantidade from idosos i where i.indicador_atendimento_odontologico = 1) total_idosos_atendimento_odontologico,
  (select count(*) quantidade from idosos i where i.indicador_atendimento_odontologico = 1) total_idosos_atendimento_odontologico"""
    return text(sql)
