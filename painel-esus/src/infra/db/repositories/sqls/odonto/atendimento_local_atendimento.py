def get_oral_health_cares_by_place(cnes: int = None):

    if cnes:
        return """
            with 
                local_atendimento as (select distinct ds_local_atendimento, co_seq_fat_atd_odnt  from atendimento_odontologico ao where co_dim_unidade_saude_1 = :cnes)
            select ds_local_atendimento, count(*) as total from local_atendimento group by ds_local_atendimento ;
        """
    return """
        with 
            local_atendimento as (select distinct ds_local_atendimento, co_seq_fat_atd_odnt  from atendimento_odontologico ao )
        select ds_local_atendimento, count(*) as total from local_atendimento group by ds_local_atendimento ;
        """


CARES_BY_PLACE = get_oral_health_cares_by_place
