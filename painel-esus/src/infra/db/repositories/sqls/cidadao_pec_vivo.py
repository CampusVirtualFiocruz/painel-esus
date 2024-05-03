CIDADAO_PEC_VIVO = """
with _tipo_local as (
	select 
        tfcp.co_seq_fat_cidadao_pec,
        tfcd.co_dim_tipo_localizacao
    from
        tb_fat_cidadao_pec tfcp
    left join tb_fat_familia_territorio tfft on
        tfft.co_fat_cidadao_pec = tfcp.co_seq_fat_cidadao_pec
    left join tb_fat_cad_domiciliar tfcd on
        tfcd.co_seq_fat_cad_domiciliar = tfft.co_fat_cad_domiciliar
    order by tfcd.co_dim_tempo desc
), tipo_local as (
	select distinct on (co_seq_fat_cidadao_pec) * from _tipo_local 
)
select
	distinct
	tfcp.*,
	tp.co_dim_tipo_localizacao
from
	tb_fat_cidadao_pec tfcp
left join tipo_local tp on
	tp.co_seq_fat_cidadao_pec = tfcp.co_seq_fat_cidadao_pec
where
	tfcp.st_faleceu = 0;
 """
