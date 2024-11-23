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
                select * from lista where (
                        tb_cidadao_ativo = 1
                        and co_dim_tipo_saida_cadastro = 3
                        and nu_ine is not null
                        and st_ficha_inativa = 0
                )
                or (
                        co_dim_tipo_saida_cadastro is null
                        and tb_cidadao_ativo = 1
                        and st_faleceu = 0
                        and tb_equipe_ativo = 1
                        and nu_ms in ('70', '76')
                )
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
