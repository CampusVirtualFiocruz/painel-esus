import collections
import os
from ..helpers.str import treatNames
def loginADM():
    result = collections.OrderedDict()
    result['unidadeSaude'] = ''
    result['codigoIbge'] = ''
    result['municipio'] = os.getenv('CIDADE', 'Ouro Preto')
    result['uf'] =  os.getenv('ESTADO', 'MG')
    result['cns'] = ''
    result['cpf'] = ''
    result['conselhoClasse'] = ''
    result['email'] = ''
    result['nome'] = 'admin'
    result['codigoMunicipio'] = ''

    return result

def login (con, cpf, cns):
    if cpf == os.getenv('ADMIN_USR', 'admin') and cns == os.getenv('ADMIN_PASS', '811be8520361ddcc4f8fd385ce3426eb06197eeae6ef0bc7823f3a7686785'):
        return loginADM()
    sql = f'''
        select
        distinct on (tfai.co_dim_unidade_saude_1) co_dim_unidade_saude_1 as  unidadeSaude,
        tbm.co_ibge as  codigoIbge,
        tbm.no_municipio as municipio,
        tduf.sg_uf as uf,  
        tp.nu_cns as cns,
        tp.nu_cpf as cpf,
        tp.nu_conselho_classe  as conselhoClasse,
        tp.ds_email as email,
        tdp.no_profissional as nome,
        tfai.co_dim_municipio as codigoMunicipio
    from
        tb_prof tp
    join tb_dim_profissional tdp on
        tp.nu_cns = tdp.nu_cns
    join tb_fat_atendimento_individual tfai on tfai.co_dim_profissional_1  = tdp.co_seq_dim_profissional 
    join tb_dim_municipio tbm on tbm.co_seq_dim_municipio = tfai.co_dim_municipio 
    join tb_dim_uf tduf on tduf.co_seq_dim_uf = tbm.co_dim_uf	
    where
        tdp.st_registro_valido = 1
        and tp.nu_cpf = '{cpf}'
        and concat( tp.nu_cns , 'painel') = '{cns}' ;
    '''
    item = con.consultar(sql)
    if len(item) == 0 :
        return None
    result = collections.OrderedDict()
    result['unidadeSaude'] = item[0][0]
    result['codigoIbge'] = item[0][1]
    result['municipio'] = item[0][2]
    result['uf'] = item[0][3]
    result['cns'] = treatNames(item[0][4])
    result['cpf'] = treatNames(item[0][5])
    result['conselhoClasse'] = item[0][6]
    result['email'] = treatNames(item[0][7])
    result['nome'] = treatNames(item[0][8])
    result['codigoMunicipio'] = item[0][9]

    return result
