from .cid_explode import CID_EXPLODE
from .ciap_explode import CIAP_EXPLODE
from .requested_procedures_explode import REQUESTED_EXPLODE
from .evaluated_procedures_explode import EVALUATED_EXPLODE

PREGNANCY_BASE = f"""
with 
    atd_base as ( {CID_EXPLODE} UNION ALL {CIAP_EXPLODE} UNION ALL {REQUESTED_EXPLODE} UNION ALL {EVALUATED_EXPLODE} )
select
	atd.*,
    tfcp.no_cidadao,
	coalesce(tfcd.co_dim_tipo_localizacao, 1) co_dim_tipo_localizacao,
	coalesce(tfcp.co_dim_tempo_nascimento, 0) co_dim_tempo_nascimento,
    coalesce(tc.nu_cbo, '0') as cbo,
    t.dt_registro
from
	atd_base atd
left join tb_dim_tempo t on
	t.co_seq_dim_tempo = atd.co_dim_tempo
left join tb_fat_familia_territorio tfft on
	tfft.co_fat_cidadao_pec = atd.co_fat_cidadao_pec
left join tb_fat_cad_domiciliar tfcd on
	tfcd.co_seq_fat_cad_domiciliar = tfft.co_fat_cad_domiciliar
left join tb_fat_cidadao_pec  tfcp on tfcp.co_seq_fat_cidadao_pec  = atd.co_fat_cidadao_pec 
left join tb_dim_cbo tc on atd.co_dim_cbo_1 = tc.co_seq_dim_cbo 
"""
