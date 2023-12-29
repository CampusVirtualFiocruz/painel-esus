def cares_by_line_of_service(cnes: int = None):
    if cnes:
        return f"""
            with 
                atds as (select distinct co_seq_fat_atd_odnt from atendimento_odontologico ao where co_dim_unidade_saude_1 = {cnes}),
                gestantes as (select distinct co_seq_fat_atd_odnt  from atendimento_odontologico where st_gestante = 1 and co_dim_unidade_saude_1 = {cnes}),
                pessoa_com_deficiencia as (select distinct co_seq_fat_atd_odnt  from atendimento_odontologico where st_paciente_necessidades_espec  = 1 and co_dim_unidade_saude_1 = {cnes}) ,
                total_gestantes as (select count(*) as total from gestantes ),
                total_especiais as (select count(*) as total from pessoa_com_deficiencia ),
                total_atd as ( select count(*) as total from atds )
                select 
                    (select total from total_atd) as total,
                    (select total from total_gestantes) as gestantes,
                    (select total from total_especiais) as especiais
                ;
        """
    return """
    with 
        atds as (select distinct co_seq_fat_atd_odnt from atendimento_odontologico ao),
        gestantes as (select distinct co_seq_fat_atd_odnt  from atendimento_odontologico where st_gestante = 1),
        pessoa_com_deficiencia as (select distinct co_seq_fat_atd_odnt  from atendimento_odontologico where st_paciente_necessidades_espec  = 1) ,
        total_gestantes as (select count(*) as total from gestantes),
        total_especiais as (select count(*) as total from pessoa_com_deficiencia),
        total_atd as ( select count(*) as total from atds )
        select 
            (select total from total_atd) as total,
            (select total from total_gestantes) as gestantes,
            (select total from total_especiais) as especiais
        ;
    """


CARES_BY_LINE_OF_SERVICE = cares_by_line_of_service
