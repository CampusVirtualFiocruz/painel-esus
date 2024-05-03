ATENDIMENTO_ONDONTO = """
with odonto as (
	select 
	co_seq_fat_atd_odnt,
	'Procedimentos' as tipo,
	unnest(STRING_TO_ARRAY(rtrim(ltrim(ds_filtro_procedimentos, '|'), '|'), '|')) as codigo,
	tfao.co_dim_tipo_ficha,
	tdtf.ds_tipo_ficha ,
	tfao.co_dim_municipio,
	tdm.no_municipio ,
	tdm.co_ibge,
	tfao.co_dim_profissional_1,
	tfao.co_dim_cbo_1,
	tdc.no_cbo,
	tfao.co_dim_unidade_saude_1,
	tdus.no_unidade_saude ,
	tfao.co_dim_equipe_1,
	tdt.dt_registro,
	extract(week from to_date(tfao.co_dim_tempo::text, 'YYYYMMDD') + interval '1 day') as epiweek,
	tfao.nu_atendimento,
	tfao.nu_cns,
	tfao.dt_nascimento,
	tfao.co_dim_faixa_etaria,
	tdfe.ds_faixa_etaria ,
	tfao.co_dim_sexo,
	tds.ds_sexo ,
	tfao.co_dim_turno,
	tfao.co_dim_local_atendimento,
	tdla.ds_local_atendimento,
	tfao.st_paciente_necessidades_espec,
	tfao.st_gestante,
	tfao.co_dim_tipo_atendimento,
	tdta.ds_tipo_atendimento ,
	tfao.co_dim_tipo_consulta,
	tdtco.ds_tipo_consulta_odonto,
	tfao.st_vigil_abscesso_dentoalveola,
	tfao.st_vigil_alterac_tecidos_moles,
	tfao.st_vigil_dor_dente,
	tfao.st_vigil_fendas_fissuras_labio,
	tfao.st_vigil_fluorose_dentaria,
	tfao.st_vigil_traumat_dentoalveolar,
	tfao.st_vigil_nao_identificado,
	tfao.st_fornecimento_escova_dental,
	tfao.st_fornecimento_creme_dental,
	tfao.st_fornecimento_fio_dental,
	tfao.st_conduta_consulta_agendada,
	tfao.st_conduta_outros_profissio_ab,
	tfao.st_conduta_agendamento_nasf,
	tfao.st_conduta_agendamento_grupos,
	tfao.st_conduta_alta_episodio,
	tfao.st_conduta_tratamento_concluid,
	tfao.st_encaminhamento_necess_espec,
	tfao.st_encaminhamento_cirurgia_bmf,
	tfao.st_encaminhamento_endodontia,
	tfao.st_encaminhamento_estomatologi,
	tfao.st_encaminhamento_implantodont,
	tfao.st_encaminhamento_odontopediat,
	tfao.st_encaminhamento_ortod_ortop,
	tfao.st_encaminhamento_periodontia,
	tfao.st_encaminhamento_protese_dent,
	tfao.st_encaminhamento_radiologia,
	tfao.st_encaminhamento_outros,
	tfao.st_encaminhamento_nao_aplica,
	tfao.nu_prontuario,
	tfao.co_dim_cds_tipo_origem,
	tfao.co_fat_cidadao_pec,
	tfao.dt_inicial_atendimento,
	tfao.dt_final_atendimento,
	tfao.nu_cpf_cidadao,
	coalesce(tfcd.co_dim_tipo_localizacao, 1) co_dim_tipo_localizacao,
	coalesce(tdtl.ds_tipo_localizacao, '-') ds_tipo_localizacao
	from 
		tb_fat_atendimento_odonto tfao
		left join tb_dim_tipo_ficha tdtf on tdtf.co_seq_dim_tipo_ficha = tfao.co_dim_tipo_ficha 
		left join tb_dim_municipio tdm on tdm.co_seq_dim_municipio = tfao.co_dim_municipio 
		left join tb_dim_cbo tdc on tdc.co_seq_dim_cbo = tfao.co_dim_cbo_1 
		left join tb_dim_sexo tds on tds.co_seq_dim_sexo = tfao.co_dim_sexo 
		left join tb_dim_faixa_etaria tdfe on tdfe.co_seq_dim_faixa_etaria = tfao.co_dim_faixa_etaria 
		left join tb_dim_tipo_atendimento tdta on tdta.co_seq_dim_tipo_atendimento = tfao.co_dim_tipo_atendimento 
		left join tb_dim_tipo_consulta_odonto tdtco on tdtco.co_seq_dim_tipo_cnsulta_odonto = tfao.co_dim_tipo_consulta  
		left join tb_dim_unidade_saude tdus on tdus.co_seq_dim_unidade_saude = tfao.co_dim_unidade_saude_1 
		left join tb_dim_tempo tdt on tdt.co_seq_dim_tempo = tfao.co_dim_tempo 
		left join tb_dim_local_atendimento tdla on tdla.co_seq_dim_local_atendimento  = tfao.co_dim_local_atendimento 
		left join tb_fat_familia_territorio tfft on tfft.co_fat_cidadao_pec = tfao.co_fat_cidadao_pec
		left join tb_fat_cad_domiciliar	 tfcd on tfcd.co_seq_fat_cad_domiciliar = tfft.co_fat_cad_domiciliar
		left join tb_dim_tipo_localizacao tdtl on tfcd.co_dim_tipo_localizacao = tdtl.co_seq_dim_tipo_localizacao
	where co_seq_fat_atd_odnt is not null
UNION
	select 
	co_seq_fat_atd_odnt,
	'CIDS' as tipo,
	unnest(STRING_TO_ARRAY(rtrim(ltrim(tfao.ds_filtro_cids , '|'), '|'), '|')) as codigo,
	tfao.co_dim_tipo_ficha,
	tdtf.ds_tipo_ficha ,
	tfao.co_dim_municipio,
	tdm.no_municipio ,
	tdm.co_ibge,
	tfao.co_dim_profissional_1,
	tfao.co_dim_cbo_1,
	tdc.no_cbo,
	tfao.co_dim_unidade_saude_1,
	tdus.no_unidade_saude ,
	tfao.co_dim_equipe_1,
	tdt.dt_registro,
	extract(week from to_date(tfao.co_dim_tempo::text, 'YYYYMMDD') + interval '1 day') as epiweek,
	tfao.nu_atendimento,
	tfao.nu_cns,
	tfao.dt_nascimento,
	tfao.co_dim_faixa_etaria,
	tdfe.ds_faixa_etaria ,
	tfao.co_dim_sexo,
	tds.ds_sexo ,
	tfao.co_dim_turno,
	tfao.co_dim_local_atendimento,
	tdla.ds_local_atendimento,
	tfao.st_paciente_necessidades_espec,
	tfao.st_gestante,
	tfao.co_dim_tipo_atendimento,
	tdta.ds_tipo_atendimento ,
	tfao.co_dim_tipo_consulta,
	tdtco.ds_tipo_consulta_odonto,
	tfao.st_vigil_abscesso_dentoalveola,
	tfao.st_vigil_alterac_tecidos_moles,
	tfao.st_vigil_dor_dente,
	tfao.st_vigil_fendas_fissuras_labio,
	tfao.st_vigil_fluorose_dentaria,
	tfao.st_vigil_traumat_dentoalveolar,
	tfao.st_vigil_nao_identificado,
	tfao.st_fornecimento_escova_dental,
	tfao.st_fornecimento_creme_dental,
	tfao.st_fornecimento_fio_dental,
	tfao.st_conduta_consulta_agendada,
	tfao.st_conduta_outros_profissio_ab,
	tfao.st_conduta_agendamento_nasf,
	tfao.st_conduta_agendamento_grupos,
	tfao.st_conduta_alta_episodio,
	tfao.st_conduta_tratamento_concluid,
	tfao.st_encaminhamento_necess_espec,
	tfao.st_encaminhamento_cirurgia_bmf,
	tfao.st_encaminhamento_endodontia,
	tfao.st_encaminhamento_estomatologi,
	tfao.st_encaminhamento_implantodont,
	tfao.st_encaminhamento_odontopediat,
	tfao.st_encaminhamento_ortod_ortop,
	tfao.st_encaminhamento_periodontia,
	tfao.st_encaminhamento_protese_dent,
	tfao.st_encaminhamento_radiologia,
	tfao.st_encaminhamento_outros,
	tfao.st_encaminhamento_nao_aplica,
	tfao.nu_prontuario,
	tfao.co_dim_cds_tipo_origem,
	tfao.co_fat_cidadao_pec,
	tfao.dt_inicial_atendimento,
	tfao.dt_final_atendimento,
	tfao.nu_cpf_cidadao,
	coalesce(tfcd.co_dim_tipo_localizacao, 1) co_dim_tipo_localizacao,
	coalesce(tdtl.ds_tipo_localizacao, '-') ds_tipo_localizacao
	from 
		tb_fat_atendimento_odonto tfao
		left join tb_dim_tipo_ficha tdtf on tdtf.co_seq_dim_tipo_ficha = tfao.co_dim_tipo_ficha 
		left join tb_dim_municipio tdm on tdm.co_seq_dim_municipio = tfao.co_dim_municipio 
		left join tb_dim_cbo tdc on tdc.co_seq_dim_cbo = tfao.co_dim_cbo_1 
		left join tb_dim_sexo tds on tds.co_seq_dim_sexo = tfao.co_dim_sexo 
		left join tb_dim_faixa_etaria tdfe on tdfe.co_seq_dim_faixa_etaria = tfao.co_dim_faixa_etaria 
		left join tb_dim_tipo_atendimento tdta on tdta.co_seq_dim_tipo_atendimento = tfao.co_dim_tipo_atendimento 
		left join tb_dim_tipo_consulta_odonto tdtco on tdtco.co_seq_dim_tipo_cnsulta_odonto = tfao.co_dim_tipo_consulta  
		left join tb_dim_unidade_saude tdus on tdus.co_seq_dim_unidade_saude = tfao.co_dim_unidade_saude_1 
		left join tb_dim_tempo tdt on tdt.co_seq_dim_tempo = tfao.co_dim_tempo 
		left join tb_dim_local_atendimento tdla on tdla.co_seq_dim_local_atendimento  = tfao.co_dim_local_atendimento 
		left join tb_fat_familia_territorio tfft on tfft.co_fat_cidadao_pec = tfao.co_fat_cidadao_pec
		left join tb_fat_cad_domiciliar	 tfcd on tfcd.co_seq_fat_cad_domiciliar = tfft.co_fat_cad_domiciliar
		left join tb_dim_tipo_localizacao tdtl on tfcd.co_dim_tipo_localizacao = tdtl.co_seq_dim_tipo_localizacao
	where co_seq_fat_atd_odnt is not null
UNION
	select 
	co_seq_fat_atd_odnt,
	'CIAPS' as tipo,
	unnest(STRING_TO_ARRAY(rtrim(ltrim(tfao.ds_filtro_ciaps  , '|'), '|'), '|')) as codigo,
	tfao.co_dim_tipo_ficha,
	tdtf.ds_tipo_ficha ,
	tfao.co_dim_municipio,
	tdm.no_municipio ,
	tdm.co_ibge,
	tfao.co_dim_profissional_1,
	tfao.co_dim_cbo_1,
	tdc.no_cbo,
	tfao.co_dim_unidade_saude_1,
	tdus.no_unidade_saude ,
	tfao.co_dim_equipe_1,
	tdt.dt_registro,
	extract(week from to_date(tfao.co_dim_tempo::text, 'YYYYMMDD') + interval '1 day') as epiweek,
	tfao.nu_atendimento,
	tfao.nu_cns,
	tfao.dt_nascimento,
	tfao.co_dim_faixa_etaria,
	tdfe.ds_faixa_etaria ,
	tfao.co_dim_sexo,
	tds.ds_sexo ,
	tfao.co_dim_turno,
	tfao.co_dim_local_atendimento,
	tdla.ds_local_atendimento,
	tfao.st_paciente_necessidades_espec,
	tfao.st_gestante,
	tfao.co_dim_tipo_atendimento,
	tdta.ds_tipo_atendimento ,
	tfao.co_dim_tipo_consulta,
	tdtco.ds_tipo_consulta_odonto,
	tfao.st_vigil_abscesso_dentoalveola,
	tfao.st_vigil_alterac_tecidos_moles,
	tfao.st_vigil_dor_dente,
	tfao.st_vigil_fendas_fissuras_labio,
	tfao.st_vigil_fluorose_dentaria,
	tfao.st_vigil_traumat_dentoalveolar,
	tfao.st_vigil_nao_identificado,
	tfao.st_fornecimento_escova_dental,
	tfao.st_fornecimento_creme_dental,
	tfao.st_fornecimento_fio_dental,
	tfao.st_conduta_consulta_agendada,
	tfao.st_conduta_outros_profissio_ab,
	tfao.st_conduta_agendamento_nasf,
	tfao.st_conduta_agendamento_grupos,
	tfao.st_conduta_alta_episodio,
	tfao.st_conduta_tratamento_concluid,
	tfao.st_encaminhamento_necess_espec,
	tfao.st_encaminhamento_cirurgia_bmf,
	tfao.st_encaminhamento_endodontia,
	tfao.st_encaminhamento_estomatologi,
	tfao.st_encaminhamento_implantodont,
	tfao.st_encaminhamento_odontopediat,
	tfao.st_encaminhamento_ortod_ortop,
	tfao.st_encaminhamento_periodontia,
	tfao.st_encaminhamento_protese_dent,
	tfao.st_encaminhamento_radiologia,
	tfao.st_encaminhamento_outros,
	tfao.st_encaminhamento_nao_aplica,
	tfao.nu_prontuario,
	tfao.co_dim_cds_tipo_origem,
	tfao.co_fat_cidadao_pec,
	tfao.dt_inicial_atendimento,
	tfao.dt_final_atendimento,
	tfao.nu_cpf_cidadao,
	coalesce(tfcd.co_dim_tipo_localizacao, 1) co_dim_tipo_localizacao,
	coalesce(tdtl.ds_tipo_localizacao, '-') ds_tipo_localizacao
	from 
		tb_fat_atendimento_odonto tfao
		left join tb_dim_tipo_ficha tdtf on tdtf.co_seq_dim_tipo_ficha = tfao.co_dim_tipo_ficha 
		left join tb_dim_municipio tdm on tdm.co_seq_dim_municipio = tfao.co_dim_municipio 
		left join tb_dim_cbo tdc on tdc.co_seq_dim_cbo = tfao.co_dim_cbo_1 
		left join tb_dim_sexo tds on tds.co_seq_dim_sexo = tfao.co_dim_sexo 
		left join tb_dim_faixa_etaria tdfe on tdfe.co_seq_dim_faixa_etaria = tfao.co_dim_faixa_etaria 
		left join tb_dim_tipo_atendimento tdta on tdta.co_seq_dim_tipo_atendimento = tfao.co_dim_tipo_atendimento 
		left join tb_dim_tipo_consulta_odonto tdtco on tdtco.co_seq_dim_tipo_cnsulta_odonto = tfao.co_dim_tipo_consulta  
		left join tb_dim_unidade_saude tdus on tdus.co_seq_dim_unidade_saude = tfao.co_dim_unidade_saude_1 
		left join tb_dim_tempo tdt on tdt.co_seq_dim_tempo = tfao.co_dim_tempo 
		left join tb_dim_local_atendimento tdla on tdla.co_seq_dim_local_atendimento  = tfao.co_dim_local_atendimento 
		left join tb_fat_familia_territorio tfft on tfft.co_fat_cidadao_pec = tfao.co_fat_cidadao_pec
		left join tb_fat_cad_domiciliar	 tfcd on tfcd.co_seq_fat_cad_domiciliar = tfft.co_fat_cad_domiciliar
		left join tb_dim_tipo_localizacao tdtl on tfcd.co_dim_tipo_localizacao = tdtl.co_seq_dim_tipo_localizacao
	where co_seq_fat_atd_odnt is not null
)
select distinct * from odonto
"""
