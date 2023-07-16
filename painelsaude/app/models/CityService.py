from sqlalchemy.sql import text
import collections
import os 

def getCityInformation (con):

    sql = '''select
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
	tu.co_uf = tl.co_uf LIMIT 1'''

    item = con.consultar(sql)
    if len(item) == 0 :
        return None
    result = collections.OrderedDict()
    result['municipio'] = os.getenv('CIDADE', item[0][0])
    result['cep'] = item[0][1]
    result['codIgbe'] = item[0][2]
    result['uf'] = os.getenv('UF',item[0][3])
    result['estado'] = os.getenv('ESTADO',item[0][4])

    return result
