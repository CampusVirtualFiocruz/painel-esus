# pylint: disable=C0301
def get_extraction_procedures_proportion(cnes: int = None):
    if cnes:
        return """
            with
                dente_deciduo as (select distinct co_seq_fat_atd_odnt  from atendimento_odontologico where codigo in ('ABPO011','0414020120') and co_dim_unidade_saude_1 = :cnes),
                dente_permanente as (select distinct co_seq_fat_atd_odnt  from atendimento_odontologico where codigo in ('ABPO012',  '0414020138') and co_dim_unidade_saude_1 = :cnes),
                outros as (select distinct  co_seq_fat_atd_odnt  from atendimento_odontologico where codigo not in ('ABPO012',  '0414020138', 'ABPO011','0414020120') and co_dim_unidade_saude_1 = :cnes),
                total_dente_deciduo as ( select count(*) as total from dente_deciduo ),
                total_dente_permanente as ( select count(*) as total from dente_permanente ),
                total_outros as (select count(*) as total from outros)
            select 
                (select * from total_dente_deciduo) as total_dente_deciduo,
                (select * from total_dente_permanente) as total_dente_permanente,
                (select * from total_outros) as total_outros
            """
    return """
            with
                dente_deciduo as (select distinct co_seq_fat_atd_odnt  from atendimento_odontologico where codigo in ('ABPO011','0414020120')),
                dente_permanente as (select distinct co_seq_fat_atd_odnt  from atendimento_odontologico where codigo in ('ABPO012',  '0414020138')),
                outros as (select distinct  co_seq_fat_atd_odnt  from atendimento_odontologico where codigo not in ('ABPO012',  '0414020138', 'ABPO011','0414020120')),
                total_dente_deciduo as ( select count(*) as total from dente_deciduo ),
                total_dente_permanente as ( select count(*) as total from dente_permanente ),
                total_outros as (select count(*) as total from outros)
            select 
                (select * from total_dente_deciduo) as total_dente_deciduo,
                (select * from total_dente_permanente) as total_dente_permanente,
                (select * from total_outros) as total_outros
            """


EXTRACTION_PROCEDURES_PROPORTION = get_extraction_procedures_proportion
