from .lista_cidadao_pec_from_fichas import lista_cidadao_pec_from_fichas
from .pessoas_id import pessoas_id
from .pessoas_list import pessoas_list

pessoas = f"""
with
	lista_cidadao_pec_from_fichas as ( {lista_cidadao_pec_from_fichas}),
	pessoas_id as ( {pessoas_id} ),
	pessoas as ( {pessoas_list} )
select
	*
from
	pessoas order by cidadao_pec asc
"""


pessoas_tb_acompanhamento = """
select distinct on( tfci.co_fat_cidadao_pec) 
	tacv.co_cidadao,
	tfci.co_fat_cidadao_pec cidadao_pec,
	tdrc.ds_raca_cor raca_cor,
	tacv.nu_cpf_cidadao cpf,
	tacv.nu_cns_cidadao cns,
	coalesce(tacv.no_cidadao, 'Nome não informado') nome,
	tacv.no_social_cidadao nome_social,
	tacv.dt_nascimento_cidadao data_nascimento,
	extract(year from age(now(), coalesce(tacv.dt_nascimento_cidadao ) )) idade,
	tacv.no_sexo_cidadao sexo,
	tacv.tp_identidade_genero_cidadao identidade_genero,
	tacv.nu_telefone_celular telefone,
	tacv.dt_ultima_atualizacao_cidadao ultima_atualizacao_cidadao,
	tacv.dt_atualizacao_fcd ultima_atualizacao_fcd,
	coalesce(tacv.no_tipo_logradouro_tb_cidadao, '') tipo_endereco,
	coalesce(tacv.ds_logradouro_tb_cidadao, '') endereco,
	coalesce(tacv.ds_complemento_tb_cidadao, '') complemento,
	coalesce(tacv.nu_numero_tb_cidadao, '') numero,
	coalesce(tacv.no_bairro_tb_cidadao, '') bairro,
	tacv.ds_cep_tb_cidadao cep,
	tdtl.ds_tipo_localizacao tipo_localidade,
	tacv.st_possui_fci possui_fci,
	tacv.st_possui_fcdt possui_fcdt,
	tacv.dt_ultima_atualizacao_cidadao,
	extract(year from age(current_date, tacv.dt_ultima_atualizacao_cidadao)) * 12 + extract(month from age(current_date, tacv.dt_ultima_atualizacao_cidadao)) diferenca_ultima_atualizacao_cidadao,
	tacv.dt_atualizacao_fcd,
	extract(year from age(current_date, tacv.dt_atualizacao_fcd)) * 12 + extract(month from age(current_date, tacv.dt_atualizacao_fcd)) diferenca_ultima_atualizacao_fcd,
	tde.co_seq_dim_equipe codigo_equipe_vinculada,
	tdus.co_seq_dim_unidade_saude codigo_unidade_saude,
	tacv.st_usar_cadastro_individual,
	tfci.st_recusa_cadastro
from
	tb_acomp_cidadaos_vinculados tacv 
left join tb_fat_cad_individual tfci on tfci.nu_uuid_ficha = tacv.co_unico_ultima_ficha 
left join (
	select 
		ft.co_fat_cidadao_pec, ft.co_fat_cad_domiciliar, ft.co_fat_cidadao_territorio, ft.co_seq_fat_familia_territorio, ft.co_dim_tempo_fcd  
	from tb_fat_familia_territorio ft 
	join (
		select co_fat_cidadao_pec, max(co_dim_tempo_fcd) co_dim_tempo_fcd  from tb_fat_familia_territorio group by 1
	) tfft on tfft.co_fat_cidadao_pec=ft.co_fat_cidadao_pec and tfft.co_dim_tempo_fcd =ft.co_dim_tempo_fcd 
	order by tfft.co_fat_cidadao_pec asc
) tfft on tfft.co_fat_cidadao_pec = tfci.co_fat_cidadao_pec
left join tb_fat_cad_domiciliar tfcd on tfcd.co_seq_fat_cad_domiciliar  = tfft.co_fat_cad_domiciliar
left join tb_dim_tipo_localizacao tdtl on tdtl.co_seq_dim_tipo_localizacao = tfcd.co_dim_tipo_localizacao
left join tb_dim_equipe tde on tde.nu_ine = tacv.nu_ine_vinc_equipe
left join tb_dim_unidade_saude tdus on tdus.nu_cnes = tacv.nu_cnes_vinc_equipe
left join tb_dim_raca_cor tdrc on tfci.co_dim_raca_cor = tdrc.co_seq_dim_raca_cor
order by tfci.co_fat_cidadao_pec asc
"""
