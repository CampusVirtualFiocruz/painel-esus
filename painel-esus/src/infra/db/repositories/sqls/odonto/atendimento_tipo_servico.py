def cares_by_type_of_services(cnes: int = None):
    if cnes:
        return """
            with 
                tipo_consulta as (
                    select distinct ds_tipo_consulta_odonto, co_seq_fat_atd_odnt  from atendimento_odontologico where co_dim_unidade_saude_1 = :cnes
                )
            select count(*) total, ds_tipo_consulta_odonto from tipo_consulta group by ds_tipo_consulta_odonto;
                """
    return """
with 
	tipo_consulta as (
		select distinct ds_tipo_consulta_odonto, co_seq_fat_atd_odnt  from atendimento_odontologico
	)
select count(*) total, ds_tipo_consulta_odonto from tipo_consulta group by ds_tipo_consulta_odonto;
	"""


CARES_BY_TYPE_OF_SERVICE = cares_by_type_of_services
