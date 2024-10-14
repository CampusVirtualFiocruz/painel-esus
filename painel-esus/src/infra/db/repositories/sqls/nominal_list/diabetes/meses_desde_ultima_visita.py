
def get_last_visit_alert(co_fat_cidadao_pec: int = None):
    sql = """
        with acs as (
            select 
                tfvd.co_fat_cidadao_pec,
                tcfvd.dt_ficha as dt_registro,
                (
                    extract(year from age(now(), tcfvd.dt_ficha ))*12 + extract(month from age(now(), tcfvd.dt_ficha )) 
                ) meses_desde_ultima_visita
            from tb_cds_ficha_visita_domiciliar tcfvd 
            left join tb_cds_prof tcp  on tcfvd.co_cds_prof = tcp.co_seq_cds_prof 
            left join tb_fat_visita_domiciliar tfvd on tcfvd.co_unico_ficha = tfvd.nu_uuid_ficha 
            left join tb_dim_equipe tde on tde.co_seq_dim_equipe = tfvd.co_dim_equipe 
            left join tb_equipe te  on tde.nu_ine = te.nu_ine
            left join tb_tipo_equipe tte  on te.tp_equipe = tte.co_seq_tipo_equipe
            where 
                tcp.nu_cbo_2002 like any(array['5151%', '3233%']) and  tte.nu_ms in ('70', '76')
            order by tcfvd.dt_ficha asc
        )
        select 
            a1.* 
        from
            acs a1 
        left join acs a2 on a1.co_fat_cidadao_pec = a2.co_fat_cidadao_pec and a2.dt_registro > a1.dt_registro
        where 
            a2.co_fat_cidadao_pec is null 	
"""
    if co_fat_cidadao_pec is not None:
        sql += f" and a1.co_fat_cidadao_pec = {co_fat_cidadao_pec} "
