LISTA_NOMINAL_DIABETES = """
with 
codigos_relevantes as (
		select unnest (array['K86','K87','W81','I10','I11','I110','I119','I12',
			'I120','I129','I13','I130','I131','I132','I139','I15',
			'I150','I151','I152','I158','I159','I270','I272','O10',
			'O100','O101','O102','O103','O104','O109','ABP005']) as codigo
	),
 atendimento_individual as (
	select 
		tfai.co_seq_fat_atd_ind, tfai.co_fat_cidadao_pec, tfai.co_dim_equipe_1, tfai.co_dim_unidade_saude_1 , tfai.co_dim_cbo_1, cbo.no_cbo, cbo.nu_cbo,
		tfai.co_dim_tempo, tfai.ds_filtro_cids, tfai.ds_filtro_ciaps, tfai.ds_filtro_proced_avaliados,tfai.ds_filtro_proced_solicitados
	from tb_fat_atendimento_individual tfai 
	left join tb_dim_cbo cbo on cbo.co_seq_dim_cbo = tfai.co_dim_cbo_1
	where 
	(
            EXISTS (
                SELECT 1 
                FROM codigos_relevantes cr
                WHERE tfai.ds_filtro_cids LIKE '%' || cr.codigo || '%'
            ) 
            OR 
            EXISTS (
                SELECT 1 
                FROM codigos_relevantes cr
                WHERE tfai.ds_filtro_ciaps LIKE '%' || cr.codigo || '%'
            )
        )
	and substring(co_dim_tempo::text, 0, 5)<= substring(now()::text, 0, 5)
	and
	co_dim_tempo::text::date between (
		select
			max(tfai.co_dim_tempo::text::date)
		from
			tb_fat_atendimento_individual tfai)::DATE - interval '12 month' and (
		select
			max(tfai.co_dim_tempo::text::date) from tb_fat_atendimento_individual tfai)
),
date_range as (
		select ai.co_fat_cidadao_pec, min(ai.co_dim_tempo)::text::date min_date, max(ai.co_dim_tempo)::text::date max_date from atendimento_individual ai group by 1 order by 1 asc
	),
todos_cids as (
	SELECT 
	    tfai.co_fat_cidadao_pec, 
		string_agg(distinct tfai.co_dim_unidade_saude_1::text,',') as co_dim_unidade_saude,
	    regexp_replace(concat(string_agg(tfai.ds_filtro_ciaps,''),string_agg(tfai.ds_filtro_cids,'')), '[||]+','|', 'g') as cids
    FROM 
	    tb_fat_atendimento_individual tfai 
	GROUP BY tfai.co_fat_cidadao_pec
),
cad_individual as (
	select co_fat_cidadao_pec , max(co_dim_tempo) as co_dim_tempo from tb_fat_cad_individual tfci 
	where co_fat_cidadao_pec in ( select co_fat_cidadao_pec from atendimento_individual)
	group by 1
	order by co_fat_cidadao_pec asc
),
cadastro_individual as (
	select 
	distinct tfci.co_fat_cidadao_pec,
	tc.no_cidadao,
	tc.nu_cns,
	tc.nu_cpf,
	tc.no_sexo,
	trc.no_raca_cor,
	tfci.nu_micro_area ,
	tc.nu_area ,
	tc.dt_nascimento,
	tc.ds_logradouro,	
	tc.no_bairro,
	tc.nu_numero,	
	tc.ds_cep,
	tl.no_localidade ,
	tu.no_uf, tu.sg_uf,
	ttl.no_tipo_logradouro,
	tfci.co_dim_equipe,
	tfci.co_dim_unidade_saude,
	tfci.co_dim_tempo,
	upper(tdtl.ds_tipo_localizacao) as ds_tipo_localizacao,
	tde.no_equipe as equipe
from tb_fat_cad_individual tfci 
	left join tb_fat_cidadao_pec tfcp on tfcp.co_seq_fat_cidadao_pec = tfci.co_fat_cidadao_pec 
	left join tb_cidadao tc on tc.co_seq_cidadao = tfcp.co_cidadao  
	left join tb_tipo_logradouro ttl on ttl.co_tipo_logradouro = tc.tp_logradouro
	left join tb_uf tu on tu.co_uf = tc.co_uf 
	left join tb_localidade tl on tl.co_localidade = tc.co_localidade_endereco
	left join tb_raca_cor trc on trc.co_raca_cor = tc.co_raca_cor
 	left join tb_fat_cad_dom_familia tfcdf on tfcdf.co_fat_cidadao_pec = tfcp.co_seq_fat_cidadao_pec and tfcdf.st_mudou = 0
	left join tb_fat_cad_domiciliar tfcd on tfcdf.co_fat_cad_domiciliar = tfcd.co_seq_fat_cad_domiciliar
	left join tb_dim_tipo_localizacao tdtl on tdtl.co_seq_dim_tipo_localizacao = tfcd.co_dim_tipo_localizacao
	left join tb_dim_equipe tde on tde.co_seq_dim_equipe = tfci.co_dim_equipe 
where tfci.co_fat_cidadao_pec in ( select co_fat_cidadao_pec from atendimento_individual)
),
lista_cad_individual as ( select tfci.* from cadastro_individual tfci join cad_individual ci on ci.co_fat_cidadao_pec = tfci.co_fat_cidadao_pec and ci.co_dim_tempo = tfci.co_dim_tempo where tfci.co_fat_cidadao_pec in ( select co_fat_cidadao_pec from atendimento_individual) ),
acs as (
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
),
visita_acs as (
select 
	a1.co_fat_cidadao_pec,
	a1.dt_registro as data_ultima_visita,
	a1.meses_desde_ultima_visita
from
	acs a1 
left join acs a2 on a1.co_fat_cidadao_pec = a2.co_fat_cidadao_pec and a2.dt_registro > a1.dt_registro
where 
	a2.co_fat_cidadao_pec is null
 ),
consulta_medico as (
	select co_fat_cidadao_pec, count(*) as total_consulta_individual_medico from atendimento_individual where nu_cbo like any (array['2235%', '2251%', '2252%','2253%','2231%']) group by 1
),
ultima_consulta_medica as (
	select co_fat_cidadao_pec, max(co_dim_tempo) ultimo_atendimento_medico,
	(
		extract(year from age(now(), max(co_dim_tempo::text::date) ))*12 + extract(month from age(now(), max(co_dim_tempo::text::date) )) 
	) meses_desde_ultima_visita_medica
	from atendimento_individual where nu_cbo like any (array['2235%', '2251%', '2252%','2253%','2231%']) group by 1
),
odonto as (
	select tfao.co_fat_cidadao_pec, max(co_dim_tempo::text::date) ultimo_atendimento_odonto, (
		extract(year from age(now(), max(co_dim_tempo::text::date) ))*12 + extract(month from age(now(), max(co_dim_tempo::text::date) )) 
	) meses_desde_ultima_visita_odontologica from tb_fat_atendimento_odonto tfao where tfao.co_fat_cidadao_pec in ( select co_fat_cidadao_pec from atendimento_individual) group by 1
),
afericao_pa as (
	select co_fat_cidadao_pec , max(co_dim_tempo::text::date) as ultima_data_afericao_pa,
	extract(year from age(now(), max(co_dim_tempo::text::date) ))*12 + extract(month from age(now(), max(co_dim_tempo::text::date) )) as meses_ultima_data_afericao_pa
	from 
	tb_fat_proced_atend where ds_filtro_procedimento like '%|0301100039|%' and co_fat_cidadao_pec in ( select co_fat_cidadao_pec from atendimento_individual) group by 1
),
glicemia_capilar as (
	select co_fat_cidadao_pec , max(co_dim_tempo::text::date) as ultima_data_glicemia_capilar,
	extract(year from age(now(), max(co_dim_tempo::text::date) ))*12 + extract(month from age(now(), max(co_dim_tempo::text::date) )) as meses_ultima_data_glicemia_capilar
	from 
	tb_fat_proced_atend where ds_filtro_procedimento like '%|0214010015|%' and co_fat_cidadao_pec in ( select co_fat_cidadao_pec from atendimento_individual) group by 1
),
hemoglobina_glicada as (
	select co_fat_cidadao_pec , max(co_dim_tempo::text::date) as ultima_data_hemoglobina_glicada,
	extract(year from age(now(), max(co_dim_tempo::text::date) ))*12 + extract(month from age(now(), max(co_dim_tempo::text::date) )) as meses_ultima_data_hemoglobina_glicada
	from 
	tb_fat_proced_atend where ds_filtro_procedimento like '%|0202010503|%' and co_fat_cidadao_pec in ( select co_fat_cidadao_pec from atendimento_individual) group by 1
)
	select 
	distinct on (lci.co_fat_cidadao_pec)
	coalesce(lci.co_fat_cidadao_pec, 0) co_fat_cidadao_pec,
	coalesce(lci.no_cidadao,'-') no_cidadao,
	coalesce(lci.nu_cns,'-') nu_cns,
	coalesce(lci.nu_cpf,'-') nu_cpf,
	coalesce(lci.no_sexo,'-') no_sexo,
	coalesce(lci.no_raca_cor,'-') no_raca_cor,
	coalesce(lci.nu_micro_area ,'-') nu_micro_area,
	coalesce(lci.nu_area ,'-') nu_area,
	lci.dt_nascimento,
	extract(year from age(now(),lci.dt_nascimento )) idade,
	coalesce(lci.ds_logradouro,	'-') ds_logradouro,
	coalesce(lci.no_bairro,'-') no_bairro,
	coalesce(lci.nu_numero,	'-') nu_numero,
	coalesce(lci.ds_cep,'-') ds_cep,
	coalesce(lci.no_localidade ,'-') no_localidade,
	coalesce(lci.no_uf, '-') no_uf,
	coalesce(lci.sg_uf,'-') sg_uf,
	coalesce(lci.no_tipo_logradouro,'-') no_tipo_logradouro,
	coalesce(lci.co_dim_equipe,0) co_dim_equipe,
	tc.co_dim_unidade_saude,
	lci.co_dim_tempo::text::date,
	tc.cids,
	dr.min_date,
	coalesce(lci.ds_tipo_localizacao, 'Não Informado') ds_tipo_localizacao,
	lci.equipe,
	vacs.data_ultima_visita::date as data_ultima_visita_acs,
	coalesce((meses_desde_ultima_visita > 6), false) as alerta_visita_acs,
	---
	cm.total_consulta_individual_medico as total_consulta_individual_medico,
	coalesce((total_consulta_individual_medico < 2), false) as alerta_total_de_consultas_medico, 
	---
	um.ultimo_atendimento_medico::text::date,
	coalesce((meses_desde_ultima_visita_medica > 6), false) as alerta_ultima_consulta_medico,
	---
	o.ultimo_atendimento_odonto,
	coalesce((meses_desde_ultima_visita_odontologica > 6), false) as alerta_ultima_consulta_odontologica,
	---
	pa.ultima_data_afericao_pa,
	coalesce((meses_ultima_data_afericao_pa > 6), false) as alerta_afericao_pa,
	---
	gc.ultima_data_glicemia_capilar,
	coalesce((meses_ultima_data_glicemia_capilar > 6), false) as alerta_ultima_glicemia_capilar,
	---
	hg.ultima_data_hemoglobina_glicada,
	coalesce((meses_ultima_data_hemoglobina_glicada > 6), false) as alerta_ultima_hemoglobina_glicada
	from 
		lista_cad_individual lci
	left join 
		visita_acs vacs on vacs.co_fat_cidadao_pec = lci.co_fat_cidadao_pec
	left join 
		consulta_medico cm on cm.co_fat_cidadao_pec = lci.co_fat_cidadao_pec	
	left join ultima_consulta_medica um on um.co_fat_cidadao_pec = lci.co_fat_cidadao_pec
	left join odonto o on o.co_fat_cidadao_pec = lci.co_fat_cidadao_pec
	left join afericao_pa pa on pa.co_fat_cidadao_pec = lci.co_fat_cidadao_pec
	left join glicemia_capilar gc on gc.co_fat_cidadao_pec = lci.co_fat_cidadao_pec
	left join hemoglobina_glicada hg on hg.co_fat_cidadao_pec = lci.co_fat_cidadao_pec
	left join todos_cids tc on tc.co_fat_cidadao_pec = lci.co_fat_cidadao_pec
	left join date_range dr on dr.co_fat_cidadao_pec = lci.co_fat_cidadao_pec
"""
