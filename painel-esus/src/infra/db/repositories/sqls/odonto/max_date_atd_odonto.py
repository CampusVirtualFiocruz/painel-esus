MAX_DATE_ATENDIMENTO_ODONTO = \
    """select max(co_dim_tempo)::text::DATE as max_date from tb_fat_atendimento_odonto;"""
