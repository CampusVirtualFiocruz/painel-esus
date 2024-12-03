from sqlalchemy import text


def status_cadastro(cnes: int = None, equipe: int = None):
    sql = f"""with
            lista as (
                select distinct
                    tfcp.co_seq_fat_cidadao_pec,
                    tc.st_ativo tb_cidadao_ativo,
                    tfci.co_dim_tipo_saida_cadastro,
                    tde.nu_ine,
                    tfci.st_ficha_inativa,
                    tc.st_faleceu ,
                    te.st_ativo tb_equipe_ativo,
                    tte.nu_ms,
                    tfci.co_dim_tempo,
                    extract(year from age(current_date, tfci.co_dim_tempo::text::date)) * 12 + extract(month from age(current_date, tfci.co_dim_tempo::text::date)) diff_atualizacao,
                    tfcp.co_dim_equipe_vinc codigo_equipe,
                    tfcp.co_dim_unidade_saude_vinc codigo_unidade_saude,
                    tfci.dt_obito
                from
                        tb_fat_cidadao_pec tfcp
                        inner join tb_cidadao tc on tfcp.co_cidadao = tc.co_seq_cidadao
                        left join tb_fat_cad_individual tfci on tc.co_unico_ultima_ficha = tfci.nu_uuid_ficha
                        left join tb_dim_equipe tde on tde.co_seq_dim_equipe = tfcp.co_dim_equipe_vinc
                        or tde.co_seq_dim_equipe = tfci.co_dim_equipe
                        left join tb_equipe te on te.nu_ine = tde.nu_ine --equipe cc
                        left join tb_tipo_equipe tte on te.tp_equipe = tte.co_seq_tipo_equipe
                        left join tb_fat_familia_territorio tfft on tfft.co_fat_cidadao_pec = tfcp.co_seq_fat_cidadao_pec
                        left join tb_fat_cad_domiciliar tfcd on tfcd.co_seq_fat_cad_domiciliar = tfft.co_fat_cad_domiciliar
                        left join tb_dim_raca_cor tdrc on tfci.co_dim_raca_cor = tdrc.co_seq_dim_raca_cor
                        join tb_dim_sexo tds on tds.co_seq_dim_sexo = tfcp.co_dim_sexo
            ),
            lista_pessoas_vivas as (
                select * from lista where 
                    st_faleceu = 0 and dt_obito is null and ( co_dim_tipo_saida_cadastro = 3 or co_dim_tipo_saida_cadastro is null)
            ),
            lista_cadastros_validos as (
                with
        lista_cidadao_pec_from_fichas as ( 
                select distinct co_fat_cidadao_pec  from tb_fat_atendimento_individual tfai  
                union all 
                select distinct co_fat_cidadao_pec  from tb_fat_atendimento_odonto tfao
                union all  
                select distinct co_fat_cidadao_pec  from tb_fat_cad_individual tfci 
                union all 
                select distinct co_fat_cidadao_pec  from tb_fat_proced_atend tfpa  
                union all 
                select distinct co_fat_cidadao_pec   from tb_fat_familia_territorio tfft join tb_fat_cad_domiciliar tfcd  on tfft.co_fat_cad_domiciliar = tfcd.co_seq_fat_cad_domiciliar
),
        pessoas_id as ( 
            select distinct
                                    tfcp.co_seq_fat_cidadao_pec,
                                    tfcp.co_cidadao,
                                    tdrc.ds_raca_cor,
                                    tds.ds_sexo sexo,
                                    tfcp.co_dim_tempo_nascimento::text::date as dt_nascimento,
                                    tfcp.no_cidadao
                            from
                                    tb_fat_cidadao_pec tfcp
                                    inner join tb_cidadao tc on tfcp.co_cidadao = tc.co_seq_cidadao
                                    left join tb_fat_cad_individual tfci on tc.co_unico_ultima_ficha = tfci.nu_uuid_ficha
                                    left join tb_dim_equipe tde on tde.co_seq_dim_equipe = tfcp.co_dim_equipe_vinc
                                    or tde.co_seq_dim_equipe = tfci.co_dim_equipe
                                    left join tb_equipe te on te.nu_ine = tde.nu_ine --equipe cc
                                    left join tb_tipo_equipe tte on te.tp_equipe = tte.co_seq_tipo_equipe
                                    left join tb_fat_familia_territorio tfft on tfft.co_fat_cidadao_pec = tfcp.co_seq_fat_cidadao_pec
                                    left join tb_fat_cad_domiciliar tfcd on tfcd.co_seq_fat_cad_domiciliar = tfft.co_fat_cad_domiciliar
                                    left join tb_dim_raca_cor tdrc on tfci.co_dim_raca_cor = tdrc.co_seq_dim_raca_cor
                                    join tb_dim_sexo tds on tds.co_seq_dim_sexo = tfcp.co_dim_sexo
                            where
                                    exists (select 1 from lista_cidadao_pec_from_fichas ll  where tfcp.co_seq_fat_cidadao_pec = ll.co_fat_cidadao_pec) and
                                    (
                                            (
                                                    tc.st_ativo = 1
                                                    and tfci.co_dim_tipo_saida_cadastro = 3
                                                    and tde.nu_ine is not null
                                                    and tfci.st_ficha_inativa = 0
                                            )
                                            or (
                                                    tfci.co_dim_tipo_saida_cadastro is null
                                                    and tc.st_ativo = 1
                                                    and tc.st_faleceu = 0
                                                    and te.st_ativo = 1
                                                    and tte.nu_ms in ('70', '76')
                                            )
                                    )
                            order by
                                    1 asc 
            ),
                    pessoas as ( 
            select distinct on (p.co_seq_fat_cidadao_pec) p.co_seq_fat_cidadao_pec cidadao_pec,
                    tde.co_seq_dim_equipe codigo_equipe,
                    tdus.co_seq_dim_unidade_saude codigo_unidade_saude    
            from
                pessoas_id p
                left join tb_acomp_cidadaos_vinculados tacv on p.co_cidadao = tacv.co_cidadao
                left join tb_dim_equipe tde on tde.nu_ine = tacv.nu_ine_vinc_equipe
                left join tb_dim_unidade_saude tdus on tdus.nu_cnes = tacv.nu_cnes_vinc_equipe
                left join tb_fat_cad_individual tfci  on tfci.co_fat_cidadao_pec = p.co_seq_fat_cidadao_pec
                )
            select
                    *
            from
                    pessoas order by cidadao_pec asc
            ),
            lista_cadastros_invalidos as (
                select * from lista where
                co_dim_tipo_saida_cadastro != 3 or st_faleceu=1 or dt_obito is not null
            ),
            lista_cadastros_atualizados as (
                select * from lista where
                diff_atualizacao <= 24
            ),
            lista_cadastros_desatualizados as (
                select * from lista where
                diff_atualizacao > 24
            ),
            lista_agregada as (
            select 'cadastros_ativos' as "tipo", codigo_equipe, codigo_unidade_saude, count(*) quantidade from lista_cadastros_validos group by codigo_equipe, codigo_unidade_saude
            union all 
            select 'cadastros_atualizados' as "tipo", codigo_equipe, codigo_unidade_saude, count(*) quantidade from lista_cadastros_atualizados group by codigo_equipe, codigo_unidade_saude
            union all 
            select 'cadastros_desatualizados' as "tipo", codigo_equipe, codigo_unidade_saude, count(*) quantidade from lista_cadastros_desatualizados group by codigo_equipe, codigo_unidade_saude
            union all 
            select 'cadastros_invalidos' as "tipo", codigo_equipe, codigo_unidade_saude, count(*) quantidade from lista_cadastros_invalidos group by codigo_equipe, codigo_unidade_saude
            ),
            lista_porcentagem as ( select * from lista_agregada )
            select * from lista_porcentagem
        """
    return text(sql)
