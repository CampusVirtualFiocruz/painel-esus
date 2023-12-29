
def get_total_oral_cares_by_location(cnes: int = None):
    if cnes:
        return f"""
        with 
            atd as (select distinct co_seq_fat_atd_odnt, ds_tipo_localizacao  from atendimento_odontologico ao where co_dim_unidade_saude_1 = {cnes} )
        select ds_tipo_localizacao , count(*) as total from atd group by ds_tipo_localizacao ;
        """
    return """
        with 
            atd as (select distinct co_seq_fat_atd_odnt, ds_tipo_localizacao  from atendimento_odontologico ao )
        select ds_tipo_localizacao , count(*) as total from atd group by ds_tipo_localizacao
        """


ALL_CARES_BY_PLACE = get_total_oral_cares_by_location
