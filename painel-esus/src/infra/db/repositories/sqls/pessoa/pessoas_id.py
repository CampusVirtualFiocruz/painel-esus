# pylint: disable=R0913,C0103
# pessoas_id = """
# select distinct
# 			tfcp.co_seq_fat_cidadao_pec,
# 			tfcp.co_cidadao,
# 			tdrc.ds_raca_cor
# 		from
# 			tb_fat_cidadao_pec tfcp
# 			inner join tb_cidadao tc on tfcp.co_cidadao = tc.co_seq_cidadao
# 			left join tb_fat_cad_individual tfci on tc.co_unico_ultima_ficha = tfci.nu_uuid_ficha
# 			left join tb_dim_equipe tde on tde.co_seq_dim_equipe = tfcp.co_dim_equipe_vinc
# 			or tde.co_seq_dim_equipe = tfci.co_dim_equipe
# 			left join tb_equipe te on te.nu_ine = tde.nu_ine --equipe cc
# 			left join tb_tipo_equipe tte on te.tp_equipe = tte.co_seq_tipo_equipe
# 			left join tb_fat_familia_territorio tfft on tfft.co_fat_cidadao_pec = tfcp.co_seq_fat_cidadao_pec
# 			left join tb_fat_cad_domiciliar tfcd on tfcd.co_seq_fat_cad_domiciliar = tfft.co_fat_cad_domiciliar
# 			left join tb_dim_raca_cor tdrc on tfci.co_dim_raca_cor = tdrc.co_seq_dim_raca_cor
# 		where
# 			(
# 				(
# 					tc.st_ativo = 1
# 					and tfci.co_dim_tipo_saida_cadastro = 3
# 					and tde.nu_ine is not null
# 					and tfci.st_ficha_inativa = 0
# 				)
# 				or (
# 					tfci.co_dim_tipo_saida_cadastro is null
# 					and tc.st_ativo = 1
# 					and tc.st_faleceu = 0
# 					and te.st_ativo = 1
# 					and tte.nu_ms in ('70', '76')
# 				)
# 			)
# 		order by
# 			1 asc
# """

pessoas_id = """
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
"""
