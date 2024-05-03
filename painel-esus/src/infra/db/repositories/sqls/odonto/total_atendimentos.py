
def get_total_oral_cares(cnes: int = None):
    if cnes:
        return f"""with total_atd as
            (select distinct co_seq_fat_atd_odnt from atendimento_odontologico ao where co_dim_unidade_saude_1 = {cnes})
            select count(*) as total from total_atd;"""
    return """
            with total_atd as 
                (select distinct co_seq_fat_atd_odnt from atendimento_odontologico ao)
            select count(*) as total  from total_atd;"""


TOTAL_ATENDIMENTOS = get_total_oral_cares
