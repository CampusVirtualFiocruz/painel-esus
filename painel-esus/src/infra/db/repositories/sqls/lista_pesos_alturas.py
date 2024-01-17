def get_sql_for_imc(table: str, cnes: int = None):
    if cnes is not None:
        return f"""
             with atendimentos as (
                    select
                        co_fat_cidadao_pec,
                        nu_peso,
                        nu_altura
                    from
                        {table} h
                    where
                        co_fat_cidadao_pec NOTNULL and co_dim_unidade_saude = {cnes}
                    group by
                        1,	2
                ), atendimentos_unicos as (
                    select
                        a.co_fat_cidadao_pec,
                        peso.nu_peso,
                        altura.nu_altura
                    from
                        (select co_fat_cidadao_pec, max(nu_peso) as nu_peso from atendimentos group by 1) as peso,
                        (select co_fat_cidadao_pec, max(nu_altura) as nu_altura from atendimentos group by 1) as altura,
                        atendimentos as a
                    where 
                        a.co_fat_cidadao_pec = peso.co_fat_cidadao_pec and a.co_fat_cidadao_pec = altura.co_fat_cidadao_pec
                ) select distinct * from atendimentos_unicos;
            """

    return f"""
             with atendimentos as (
                    select
                        co_fat_cidadao_pec,
                        nu_peso,
                        nu_altura
                    from
                        {table} h
                    where
                        co_fat_cidadao_pec NOTNULL 
                    group by
                        1,	2
                ), atendimentos_unicos as (
                    select
                        a.co_fat_cidadao_pec,
                        peso.nu_peso,
                        altura.nu_altura
                    from
                        (select co_fat_cidadao_pec, max(nu_peso) as nu_peso from atendimentos group by 1) as peso,
                        (select co_fat_cidadao_pec, max(nu_altura) as nu_altura from atendimentos group by 1) as altura,
                        atendimentos as a
                    where 
                        a.co_fat_cidadao_pec = peso.co_fat_cidadao_pec and a.co_fat_cidadao_pec = altura.co_fat_cidadao_pec
                ) select distinct * from atendimentos_unicos;
            """


LISTA_PESOS_ALTURAS = get_sql_for_imc
