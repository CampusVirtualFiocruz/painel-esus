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
join tb_ator_papel tap on tap.co_seq_ator_papel  = tam.co_ator_papel 	
join tb_uf tu on
	tu.co_uf = tl.co_uf
where tap.st_ativo =1
limit 1 """
