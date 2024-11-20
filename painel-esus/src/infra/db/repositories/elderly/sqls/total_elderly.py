from sqlalchemy import text


def get_elderly_total_on_ubs_and_team(cnes: int = None, equipe:int = None):

    cnes_where_clause, team_where_clause = "", ""
    if cnes is not None and cnes:
        cnes_where_clause += (
            f"(select count(*) from idosos WHERE codigo_unidade_saude={cnes} ) total_pessoas_idosas_na_ubs, "
        )
        if equipe is not None and equipe:
            team_where_clause += (
                f"(select count(*) from idosos WHERE codigo_unidade_saude={cnes} and codigo_equipe = {equipe}) total_pessoas_idosas_na_equipe,"
            )

    sql = f"""with 
	    idosos as (
            SELECT
                DISTINCT idoso.cidadao_pec AS cidadao_pec,
                equipes.codigo_unidade_saude,
                equipes.codigo_equipe 
            FROM
                idoso
            JOIN pessoas ON
                pessoas.cidadao_pec = idoso.cidadao_pec
            JOIN equipes ON
                equipes.cidadao_pec = idoso.cidadao_pec
        )
        select 
            {cnes_where_clause}
            {team_where_clause}
            ( select count(*) from idosos) total_pessoas_atendidas"""
    return text(sql)
