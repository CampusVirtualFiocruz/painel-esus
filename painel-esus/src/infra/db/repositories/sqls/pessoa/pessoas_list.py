# pylint: disable=R0913,C0103
pessoas_list = """
select distinct on (p.co_seq_fat_cidadao_pec) p.co_seq_fat_cidadao_pec cidadao_pec,
    p.co_cidadao co_cidadao,
    p.ds_raca_cor raca_cor,
    tacv.nu_cpf_cidadao cpf,
    tacv.nu_cns_cidadao cns,
    coalesce(tacv.no_cidadao, p.no_cidadao,'Nome não informado') nome,
    tacv.no_social_cidadao nome_social,
    coalesce(tacv.dt_nascimento_cidadao, p.dt_nascimento) data_nascimento,
    extract(year from age(now(), coalesce(tacv.dt_nascimento_cidadao, p.dt_nascimento) )) idade,
    coalesce(tacv.no_sexo_cidadao, p.sexo) sexo,
    tacv.tp_identidade_genero_cidadao identidade_genero,
    (
        tacv.nu_telefone_celular || tacv.nu_telefone_contato || tacv.nu_fone_residencial
    ) telefone,
    tacv.dt_ultima_atualizacao_cidadao ultima_atualizacao_cidadao,
    tacv.dt_atualizacao_fcd ultima_atualizacao_fcd,
    coalesce(tacv.no_tipo_logradouro_tb_cidadao, '') tipo_endereco,
    coalesce(tacv.ds_logradouro_tb_cidadao, '') endereco,
    coalesce(tacv.ds_complemento_tb_cidadao, '') complemento,
    coalesce(tacv.nu_numero_tb_cidadao, '') numero,
    coalesce(tacv.no_bairro_tb_cidadao, '') bairro,
    tacv.ds_cep_tb_cidadao cep,
    case
        when tacv.no_bairro_tb_cidadao_filtro is not null
        and tacv.no_bairro_tb_cidadao_filtro like '%zona rural%' then 'Zona Rural'
        when tacv.no_bairro_tb_cidadao_filtro is not null
        and tacv.no_bairro_tb_cidadao_filtro not like '%zona rural%' then 'Zona Urbana'
        when tacv.no_bairro_tb_cidadao_filtro is null then 'N/I'
    end tipo_localidade,
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
    pessoas_id p
    left join tb_acomp_cidadaos_vinculados tacv on p.co_cidadao = tacv.co_cidadao
    left join tb_dim_equipe tde on tde.nu_ine = tacv.nu_ine_vinc_equipe
    left join tb_dim_unidade_saude tdus on tdus.nu_cnes = tacv.nu_cnes_vinc_equipe
    left join tb_fat_cad_individual tfci  on tfci.co_fat_cidadao_pec = p.co_seq_fat_cidadao_pec
    """
