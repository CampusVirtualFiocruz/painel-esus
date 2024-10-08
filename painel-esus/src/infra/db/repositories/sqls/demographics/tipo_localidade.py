def filter_by_localidade(cnes: int = None):
    where_clause = ""
    if cnes is not None:
        where_clause = f""" where
	tus.co_seq_dim_unidade_saude = {cnes} 
        """

    return f"""WITH cidadaos as (
select
	tacv.*,
	case 
		when no_bairro_domicilio_filtro is null then 'nao_definido'
		when no_bairro_domicilio_filtro = 'zona rural' then 'rural'
		when no_bairro_domicilio_filtro is not null  and no_bairro_domicilio_filtro != 'zona rural' then 'urbano'
	end tipo	
from
	tb_acomp_cidadaos_vinculados tacv
join tb_dim_unidade_saude tus on
	tus.nu_cnes = tacv.nu_cnes_vinc_equipe
{where_clause}
)
select tipo, count(*) total  from cidadaos group by 1;"""
