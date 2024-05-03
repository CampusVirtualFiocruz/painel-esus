CITY_INFORMATION = """
select
	tl.no_localidade as municipio,
	tl.nu_cep as cep,
	tl.co_ibge as codIbge,
	tu.sg_uf as uf,
	tu.no_uf as estado
from
	tb_adm_municipal tam
join tb_localidade tl on
	tam.co_localidade = tl.co_localidade
join tb_uf tu on
	tu.co_uf = tl.co_uf LIMIT 1
 """
