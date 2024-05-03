MAX_DT_ATENDIMENTO_ATENDIMENTO_INDIVIDUAL = """
select
	max(dt_registro)
from
	tb_fat_atendimento_individual tfai
join tb_dim_tempo t on
	t.co_seq_dim_tempo = tfai.co_dim_tempo ;
"""