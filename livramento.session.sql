with
cids as (
	select unnest (array[
      'T89','T90','W85','E10','E100','E101','E102','E103','E104','E105','E106','E107','E108','E109','E11','E110','E111','E112','E113','E114','E115','E116','E117','E118','E119','E12','E120','E121','E122','E123','E124','E125','E126','E127','E128','E129','E13','E130','E131','E132','E133','E134','E135','E136','E137','E138','E139','E14','E140','E141','E142','E143','E144','E145','E146','E147','E148','E149','O24','O240','O241','O242','O243','O244','O249','P702','ABP006']) as codigo
),
ultimo_atendimento as ( 
	select max(co_dim_tempo::text::date) as ultimo_atendimento from tb_fat_atendimento_individual tfai
),
condicao_saude as (
	select 
		distinct tfai.co_fat_cidadao_pec,
		regexp_replace(concat(string_agg(tfai.ds_filtro_ciaps,''),string_agg(tfai.ds_filtro_cids,'')), '[||]+','|', 'g') as cids
	from tb_fat_atendimento_individual tfai 
	where (
            EXISTS (
                SELECT 1 
                FROM cids cr
                WHERE tfai.ds_filtro_cids LIKE '%' || cr.codigo || '%'
            ) 
            OR 
            EXISTS (
                SELECT 1 
                FROM cids cr
                WHERE tfai.ds_filtro_ciaps LIKE '%' || cr.codigo || '%'
            )
        )
        and substring(co_dim_tempo::text, 0, 5)<= substring(now()::text, 0, 5)
        and co_dim_tempo::text::date between 
		   (SELECT ultimo_atendimento - INTERVAL '12 month' FROM ultimo_atendimento) AND 
		   (SELECT ultimo_atendimento FROM ultimo_atendimento)  
	   group by tfai.co_fat_cidadao_pec
),
primeiro_atendimento as (
	select 
		co_fat_cidadao_pec, min(co_dim_tempo)::text::date primeiro_atendimento
	from tb_fat_atendimento_individual tfai 
	where exists ( select 1 from condicao_saude cs where tfai.co_fat_cidadao_pec = cs.co_fat_cidadao_pec)
	group by 1
),
lista_nominal_base as (
    select 
        cs.*, 
        coalesce ( tacv.no_cidadao, tfcp.no_cidadao) no_cidadao,
        coalesce (tacv.nu_cns_cidadao, tfcp.nu_cns, tc.nu_cns) nu_cns,
        coalesce (tacv.nu_cpf_cidadao, tc.nu_cpf ) nu_cpf,
        coalesce (tacv.no_sexo_cidadao, case 
            when tfcp.co_dim_sexo = 1 then 'MASCULINO'
            when tfcp.co_dim_sexo = 2 then 'FEMINIMO'
            when tfcp.co_dim_sexo = 4 then 'Não informado' 	
        end
        ) no_sexo,
        trc.no_raca_cor no_raca_cor ,
        coalesce ( tacv.dt_nascimento_cidadao, tfcp.co_dim_tempo_nascimento::text::date ) dt_nascimento,
        extract (year from age(now(), coalesce ( tacv.dt_nascimento_cidadao, tfcp.co_dim_tempo_nascimento::text::date ) ))  idade,
        coalesce ( 
            INITCAP(tacv.no_tipo_logradouro_tb_cidadao || ' ' || tacv.ds_logradouro_tb_cidadao), 
            '-') ds_logradouro,
        coalesce ( INITCAP(tacv.no_bairro_tb_cidadao ), INITCAP(tc.no_bairro),'-') no_bairro,
        coalesce ( tacv.nu_numero_tb_cidadao, 'S/N') nu_numero,
        coalesce ( tacv.ds_cep_tb_cidadao, '-') ds_cep,
        coalesce ( tacv.no_municipio_tb_cidadao, '-') no_localidade , 
        coalesce ( tacv.sg_uf_tb_cidadao, '-') no_uf,
        coalesce ( tacv.nu_cnes_vinc_equipe, '-') nu_cnes_vinc_equipe,
        tde.co_seq_dim_equipe co_dim_equipe,
        tacv.no_equipe_vinc_equipe no_equipe,
        tacv.nu_ine_vinc_equipe,
        tus.co_seq_unidade_saude,
        tus.no_unidade_saude,
        coalesce (tacv.nu_micro_area_tb_cidadao, tacv.nu_micro_area_domicilio) nu_micro_area,
        cs.cids,
        pa.primeiro_atendimento,
        (case
            when tacv.no_bairro_tb_cidadao = 'Zona Rural' then 'Rural'
            when tacv.no_bairro_tb_cidadao is null then 'Não Informado'
            when tacv.no_bairro_tb_cidadao is not null and tacv.no_bairro_tb_cidadao != 'Zona Rural'  then 'Urbana'
        end
        ) ds_tipo_localizacao
    from 
        condicao_saude cs
        left join primeiro_atendimento pa on pa.co_fat_cidadao_pec = cs.co_fat_cidadao_pec 
        left join tb_fat_cidadao_pec tfcp on tfcp.co_seq_fat_cidadao_pec = cs.co_fat_cidadao_pec
        left join tb_acomp_cidadaos_vinculados tacv on tacv.co_cidadao = tfcp.co_seq_fat_cidadao_pec
        left join tb_dim_equipe tde on tde.nu_ine = tacv.nu_ine_vinc_equipe
        left join      tb_unidade_saude tus on tus.nu_cnes::text = tacv.nu_cnes_vinc_equipe
        left join tb_cidadao tc on tc.co_seq_cidadao = tfcp.co_cidadao  
        left join tb_raca_cor trc on trc.co_raca_cor = tc.co_raca_cor 
)
select * from lista_nominal_base
limit 10 offset 4	
;

