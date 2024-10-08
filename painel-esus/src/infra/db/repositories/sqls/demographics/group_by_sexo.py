def filter_by_sexo(cnes: int = None):
    where_clause = ""
    if cnes is not None:
        where_clause = f""" where
	tus.co_seq_dim_unidade_saude = {cnes} """

    return f"""select
	lower(tacv.no_sexo_cidadao),
	count(*) total
from
	tb_acomp_cidadaos_vinculados tacv
join tb_dim_unidade_saude tus on
	tus.nu_cnes = tacv.nu_cnes_vinc_equipe
{where_clause}
group by 1;"""
