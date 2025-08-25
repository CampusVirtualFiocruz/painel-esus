from src.infra.db.repositories.sqls.parquet.tb_acompanhamento_vinculo import get_pessoas

from .total import sql_round


def group_records_by_origin(cnes: int = None, equipe: int = None):
    sql_pessoas = get_pessoas(cnes, equipe)
    sql_total_pessoas = get_pessoas()
    # sql = f"""with
    #             total_pessoas_sql as ({sql_total_pessoas}),
    #             pessoas as ({sql_pessoas}),
    #             total_pessoas as (select count(*) from total_pessoas_sql),
    #             usar_cadastro_individual as (select count(*) from pessoas  where pessoas.st_usar_cadastro_individual  = 1 ),
    #             nao_usar_cadastro_individual as (select count(*) from pessoas  where pessoas.st_usar_cadastro_individual  = 0 ),
    #             somente_pec as (select count(*) from pessoas  where pessoas.st_usar_cadastro_individual  is null )
    #         select
    #             (select * from total_pessoas ) total_pessoas,
    #             (select * from usar_cadastro_individual) usar_cadastro_individual,
    #             (select * from nao_usar_cadastro_individual) nao_usar_cadastro_individual,
    #             (select * from somente_pec) somente_pec,
    #             (
    #                 (select * from nao_usar_cadastro_individual)+(select * from somente_pec)
    #             ) pec_nao_usam_cadastro_individual """
    # return sql
    sql = f"""with 
                total_pessoas_sql as ({sql_total_pessoas}),
                pessoas as ({sql_pessoas}),
                total_pessoas as (select count(*) from total_pessoas_sql),
                usar_cadastro_individual as (select count(*) from pessoas   ),
                nao_usar_cadastro_individual as (select count(*) from pessoas   ),
                somente_pec as (select count(*) from pessoas   )
            select 
                (select * from total_pessoas ) total_pessoas,                
                (select * from usar_cadastro_individual) usar_cadastro_individual,
                (select * from nao_usar_cadastro_individual) nao_usar_cadastro_individual,
                (select * from somente_pec) somente_pec,
                (
                    (select * from nao_usar_cadastro_individual)+(select * from somente_pec)
                ) pec_nao_usam_cadastro_individual """
    return sql
