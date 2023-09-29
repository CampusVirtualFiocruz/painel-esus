import re 
import pandas as pd
from .sql.individual_care_for_infections import INDIVIDUAL_CARE_FOR_INFECTIONS
from app.models.conexao import Conexao
from app.infra.config.logging import logging

def get_invidual_cares(con, date_range, cidsciaps):
    """ 
        Retrive a list of individual cares filtering by date_range[ str, str] and list of cids or ciaps [str]
        
        Arguments:
            date_range: [str, str] = start date as string and end date as string
            cidsciaps: [str] = list of all cids or ciaps must be filtred
            
        Returns:
            DataFrame
    """
    logging.info( f'get_invidual_cares:\tdate_range: {date_range}, cidsciaps: {cidsciaps}')
    sql = INDIVIDUAL_CARE_FOR_INFECTIONS
    sql = """
        {}
        select
            co_seq_fat_atd_ind,
            t.dt_registro ,
            t.nu_ano ano ,
		    t.nu_mes mes,
            nu_cns,
            co_dim_faixa_etaria,
            co_dim_sexo,
            co_dim_local_atendimento,
            codigo,
            tipo,
            co_fat_cidadao_pec,
            nu_cpf_cidadao,
            total.total
    from
            atd_individual_filtro_ciaps atd
            join tb_dim_tempo t on t.co_seq_dim_tempo = atd.co_dim_tempo,
            total as total
    where
            codigo in ( {} )
    """.format(
        INDIVIDUAL_CARE_FOR_INFECTIONS,
        ",".join([ f"'{re.escape(str(item))}'" for item in cidsciaps])\
        )
    if len(date_range) == 2:
        sql += " and dt_registro between '{}' and '{}';".format( date_range[0],date_range[1])
     
    logging.info( f'get_invidual_cares:\t{sql}')
    return con.consultar_pd(sql, True)

def get_invidual_cares_not_in(con, date_range, cidsciaps):
    """ 
        Retrive a list of individual cares filtering by date_range[ str, str] and list of cids or ciaps ARE NOT PRESENT IN [str]
        
        Arguments:
            date_range: [str, str] = start date as string and end date as string
            cidsciaps: [str] = list of all cids or ciaps must be filtred
            
        Returns:
            DataFrame
    """
    logging.info( f'get_invidual_cares_not_in:\tdate_range: {date_range}, cidsciaps: {cidsciaps}')
    dt_in = get_invidual_cares(con, date_range=date_range, cidsciaps=cidsciaps)
    ids_list = dt_in.co_seq_fat_atd_ind.unique().tolist()
    
    sql = """ select * from  tb_fat_atendimento_individual tfai """
    
    where = [] 

    if ids_list is not None and len(ids_list)>0:
        where.append(""" tfai.co_seq_fat_atd_ind not in ({}) """.format(",".join([ f"'{re.escape(str(item))}'" for item in ids_list])))
    
    if len(date_range) == 2:
        where.append(""" tfai.co_dim_tempo between '{}' and '{}' """.format(
            int(date_range[0].replace('-','')),
            int(date_range[1].replace('-','')),
        ))
    
    if len(where) > 0 :
        sql += ' where '
        sql += " AND ".join(where)
    sql +=";"
    logging.info( f'get_invidual_cares_not_in:\t{sql}')
    return con.consultar_pd(sql, True)

def get_all_cares(con, date_range):
    """ 
        Retrive all individual cares filtering by date_range[ str, str]
        
        Arguments:
            date_range: [str, str] = start date as string and end date as string
            
        Returns:
            DataFrame
    """
    logging.info( f'get_all_cares:\tdate_range: {date_range}')
    
    sql = 'select * from  tb_fat_atendimento_individual tfai'
    
    if len(date_range) == 2:
        sql +=""" where tfai.co_dim_tempo between '{}' and '{}' """.format(
            int(date_range[0].replace('-','')),
            int(date_range[1].replace('-','')),
        )
    sql +=";"
    logging.info( f'get_all_cares:\sql: {sql}')
    return con.consultar_pd(sql, True)

def generate_list_for_all_cares_by_class(_in, _not_in):
    _not_in['classe'] = 'Outros Atendimentos'
    df = _not_in[['co_seq_fat_atd_ind', 'co_dim_tempo','nu_cns', 'co_dim_faixa_etaria', 'co_dim_sexo', 'co_dim_local_atendimento', 'co_fat_cidadao_pec', 'nu_cpf_cidadao', 'ds_filtro_cids', 'ds_filtro_ciaps', 'classe']]
    df['dt_registro'] = df['co_dim_tempo'].apply(lambda x: f'{str(x)[:4]}-{str(x)[4:6]}-{str(x)[6:8]}')
    df['ano'] = df['co_dim_tempo'].apply( lambda x: int(str(x)[:4]) )
    df['mes'] = df['co_dim_tempo'].apply( lambda x: int(str(x)[4:6]) )
    df['time'] = df['co_dim_tempo'].apply(lambda x: f'{str(x)[:4]}-{str(x)[4:6]}')
    _in['time'] = _in.apply(lambda x: f'{x.ano}-{str(x.mes).rjust(2,"0")}', axis=1)
    
    df1 = df.assign(codigo=df['ds_filtro_ciaps'].str.split('|'), tipo='CIAPS').explode('codigo')
    df2 = df.assign(codigo=df['ds_filtro_cids'].str.split('|'), tipo='CID').explode('codigo')
    df1 = pd.concat([df1, df2])
    df1 = df1.loc[df1.codigo != '']

    df1=df1[['co_seq_fat_atd_ind', 'dt_registro', 'ano', 'mes','time', 'nu_cns', 'co_dim_faixa_etaria', 'co_dim_sexo', 'co_dim_local_atendimento', 'co_fat_cidadao_pec', 'nu_cpf_cidadao', 'codigo', 'tipo', 'classe']]
    return pd.concat([_in, df1])

def group_by_year_and_class( df):
    grouped_by_atd_id = df.groupby(by=['co_seq_fat_atd_ind', 'ano',	'mes', 'time','classe']).size().reset_index(name='count')
    return grouped_by_atd_id.groupby(by=['ano',	'mes', 'time','classe']).size().reset_index(name='count')

def get_list_for_all_cares_by_class_grouped_by_year( con, date_range, INFECCOES_AGUDAS, target_list, ClassifyDF):
    individual_cares = get_invidual_cares(con, date_range, INFECCOES_AGUDAS)
    individual_cares_not_in = get_invidual_cares_not_in(con, date_range, INFECCOES_AGUDAS)

    classify_df = ClassifyDF(individual_cares, target_list)
    classify_df.process()

    list_all_cares_by_class = generate_list_for_all_cares_by_class(classify_df.df, individual_cares_not_in)
    return group_by_year_and_class(list_all_cares_by_class)