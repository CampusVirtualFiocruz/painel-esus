import pandas as pd
import numpy as np

def mergeMestre( gestantes, mestre):
    gestantes['co_fat_cidadao_pec'] = gestantes['co_fat_cidadao_pec'].astype(str).astype(float).astype(int)
    mestre['co_fat_cidadao_pec'] = mestre['co_fat_cidadao_pec'].astype(str).astype(float).astype(int)
    # gestantes['co_fat_cidadao_pec'] = gestantes['co_fat_cidadao_pec'].str[:-2]
    mestre = mestre[['co_fat_cidadao_pec','ds_tipo_localizacao']]
    gestante = gestantes.merge(mestre, on='co_fat_cidadao_pec', how='left', indicator=True)
    gestante['_merge'].value_counts()
    gestante = gestante.drop(columns=['_merge'])
    if 'ds_tipo_localizacao' not in gestante:
        gestante['ds_tipo_localizacao'] = gestante['ds_tipo_localizacao_x']
    return gestante

def criarBaseFinalGestante( path ):
    gestante = pd.read_excel( path + '/BASE_GESTACOES_3_INDICADORES.xlsx')
    gestante['co_fat_cidadao_pec_x'] = gestante['co_fat_cidadao_pec_x'].astype(str).str[:-2]

    unidades = pd.read_csv( path +  '/tb_dim_unidade_saude.csv',sep=';',engine='python', decimal = ',',keep_default_na=False)

    """### Overview of the Dataset, first 5 rows"""


    """### Count number of Columns and rows"""


    """### Processamento (limpeza das bases)

    ##### Deixando somente colunas de interesse para o painel
    """

    gestante_SELECTED = gestante[['co_fat_cidadao_pec_y','Chave','dt_nascimento','NEW_DUM_y','NEW_Gestacao_N_y','co_unidade_saude','co_dim_equipe_1','co_dim_tempo','ds_filtro_cids','ds_filtro_ciaps','ds_filtro_proced_avaliados',
                                'ds_filtro_proced_solicitados','st_vacinacao_em_dia','st_gravidez_planejada','nu_idade_gestacional_semanas','nu_gestas_previas','consultas_6_prenatal','exames_para_sifilis_HIV','STRICTED','RAZOAVEL','AMPLO']]

  


    """**Calcular faixa etaria gestante**"""

    #Calcular Idade
    now = pd.Timestamp('now')
    gestante_SELECTED['dt_nascimento'] = pd.to_datetime(gestante_SELECTED['dt_nascimento'], format ='%Y-%m-%d', errors='coerce')
    gestante_SELECTED['dt_nascimento'] = gestante_SELECTED['dt_nascimento'].where(gestante_SELECTED['dt_nascimento'] < now, gestante_SELECTED['dt_nascimento'] - np.timedelta64(100, 'Y')) 
    gestante_SELECTED['AGE'] = (now - gestante_SELECTED['dt_nascimento']).astype('<m8[Y]') 

    def age_group(row):
        if row['AGE'] >= 0 and row['AGE'] <=16:
            return "Faixa 1"
        elif row['AGE'] >= 17 and row['AGE'] <=20:
            return "Faixa 2"
        elif row['AGE'] >= 21 and row['AGE'] <=25:
            return "Faixa 3"
        elif row['AGE'] >= 26 and row['AGE'] <=30:
            return "Faixa 4"
        elif row['AGE'] >= 31 and row['AGE'] <=34:
            return "Faixa 5"
        elif row['AGE'] >= 35:
            return "Faixa 6"
        else:
            return "NaN"

    gestante_SELECTED['FAIXA_ETARIA'] = gestante_SELECTED.apply (lambda row: age_group(row), axis=1)

    """**Calcular Idade gestacional**"""

    gestante_SELECTED['NEW_DUM_y'] = pd.to_datetime(gestante_SELECTED['NEW_DUM_y'], format ='%Y-%m-%d', errors='coerce')
    gestante_SELECTED['co_dim_tempo'] = pd.to_datetime(gestante_SELECTED['co_dim_tempo'], format ='%Y-%m-%d', errors='coerce')
    gestante_SELECTED['Difference'] = (gestante_SELECTED['co_dim_tempo'] - gestante_SELECTED['NEW_DUM_y']).dt.days
    gestante_SELECTED['semanas_diff'] = gestante_SELECTED['Difference'] / 7

    def ig(row):  
        if row['nu_idade_gestacional_semanas'] >= 0:
            return row['nu_idade_gestacional_semanas']
        else:
            return row['semanas_diff']
    
    gestante_SELECTED['IG'] = gestante_SELECTED.apply(lambda row: ig(row), axis=1)

    def idade_gestacional(row):
        if row['IG'] >= 0 and row['IG'] <=12:
            return "1º Trimestre"
        elif row['IG'] >= 13 and row['IG'] <=24:
            return "2º Trimestre"
        elif row['IG'] >= 25 and row['IG'] <=41:
            return "3º Trimestre"
        else:
            return "NaN"

    gestante_SELECTED['nu_idade_gestacional'] = gestante_SELECTED.apply (lambda row: idade_gestacional(row), axis=1)

    """### Delete unecessary Column and Rename"""

    gestante_SELECTED_FINAL = gestante_SELECTED.drop(columns=['co_dim_equipe_1','nu_idade_gestacional_semanas','nu_gestas_previas','Difference','semanas_diff'])
    gestante_SELECTED_FINAL = gestante_SELECTED_FINAL.rename(columns={'co_fat_cidadao_pec_y': 'co_fat_cidadao_pec',
                                                        'NEW_DUM_y': 'co_dim_tempo_dum',
                                                        'NEW_Gestacao_N_y': 'N_gestacoes',
                                                        'co_unidade_saude': 'co_dim_unidade_saude',
                                                        'exames_para_sifilis_HIV': 'exames_para_sifilis_hiv',
                                                        'STRICTED': 'com_atendimento_odontologico_stricted',
                                                        'RAZOAVEL': 'com_atendimento_odontologico_razoavel',
                                                        'AMPLO': 'com_atendimento_odontologico_amplo',
                                                        'FAIXA_ETARIA': 'ds_faixa_etaria_gestante',
                                                        'AGE': 'idade',
                                                        'IG': 'nu_idade_gestacional',
                                                        'nu_idade_gestacional': 'nu_idade_gestacional_trimestre'})


    """### Linkages Unidade de Saúde"""

    unidades['co_seq_dim_unidade_saude'] = unidades['co_seq_dim_unidade_saude'].astype(int)
    unidades.rename(columns={'co_seq_dim_unidade_saude': 'co_dim_unidade_saude'}, inplace=True)

    gestante_SELECTED_FINAL['co_dim_unidade_saude'] = gestante_SELECTED_FINAL['co_dim_unidade_saude'].replace(np.nan, 0)
    gestante_SELECTED_FINAL['co_dim_unidade_saude'] = gestante_SELECTED_FINAL['co_dim_unidade_saude'].astype(int)

    gestante_SELECTED_FINAL = gestante_SELECTED_FINAL.merge(unidades, on='co_dim_unidade_saude', how='left', indicator=True)


    """### Add Diabete and Hipertensão"""

    match = ['T89','T90','W85','E10','E100','E101','E102','E103','E104','E105','E106','E107','E108','E109','E11','E110','E111','E112','E113','E114','E115','E116','E117','E118','E119','E12','E120',
            'E121','E122','E123','E124','E125','E126','E127','E128','E129','E13','E130','E131','E132','E133','E134','E135','E136','E137','E138','E139','E14','E140','E141','E142','E143','E144','E145',
            'E146','E147','E148','E149','O24','O240','O241','O242','O243','O244','O249','P702','ABP006']

    def string_finder(row, words):
        if any(word in field for field in row for word in words):
            return True
        return False

    gestante_SELECTED_FINAL['isContained_DIABETE'] = gestante_SELECTED_FINAL.astype(str).apply(string_finder, words=match, axis=1)

    match = ['K86','K87','W81','I10','I11','I110','I119','I12','I120','I129','I13','I130','I131','I132','I139','I15','I150','I151','I152','I158','I159','I270','I272','O10','O100','O101','O102','O103',
            'O104','O109','ABP005']

    def string_finder(row, words):
        if any(word in field for field in row for word in words):
            return True
        return False

    gestante_SELECTED_FINAL['isContained_HIPERTENSAO'] = gestante_SELECTED_FINAL.astype(str).apply(string_finder, words=match, axis=1)

    """### Exportando para excel FINAL DATABASE GESTAÇÔES"""

    gestante_SELECTED_FINAL = gestante_SELECTED_FINAL.drop(columns=['_merge'])
    
    cadastro_mestre = pd.read_excel( path + '/CADASTRO_MESTRE_JOIN_AT_IND_GEST_HIP_DIAB_JOIN_UNIDADES_CLEAN_PAINEL.xlsx')
    cadastro_mestre_ = cadastro_mestre[['ds_tipo_localizacao', 'co_fat_cidadao_pec']]
    gestante_SELECTED_FINAL = mergeMestre(gestante_SELECTED_FINAL, cadastro_mestre_)
    gestante_SELECTED_FINAL.to_excel( path +  '/BASE_GESTACOES_FINAL_PAINEL.xlsx')

# def criarBaseFinalGestante( path ):


#     gestante = pd.read_parquet( path + '/BASE_GESTACOES_3_INDICADORES.parquet')
    

#     unidades = pd.read_csv( path + '/tb_dim_unidade_saude.csv',sep=';',engine='python', decimal = ',',keep_default_na=False)

#     """### Overview of the Dataset, first 5 rows"""


#     """### Count number of Columns and rows"""


#     """### Processamento (limpeza das bases)

#     ##### Deixando somente colunas de interesse para o painel
#     """

#     gestante_SELECTED = gestante[['co_fat_cidadao_pec_y','Chave','dt_nascimento','NEW_DUM_y','NEW_Gestacao_N_y','co_dim_unidade_saude_1','co_dim_equipe_1','co_dim_tempo','ds_filtro_cids','ds_filtro_ciaps','ds_filtro_proced_avaliados',
#                                 'ds_filtro_proced_solicitados','st_vacinacao_em_dia','st_gravidez_planejada','nu_idade_gestacional_semanas','nu_gestas_previas','consultas_6_prenatal','exames_para_sifilis_HIV','STRICTED','RAZOAVEL','AMPLO']]








#     """**Calcular faixa etaria gestante**"""

#     #Calcular Idade
#     now = pd.Timestamp('now')
#     gestante_SELECTED['dt_nascimento'] = pd.to_datetime(gestante_SELECTED['dt_nascimento'], format ='%Y-%m-%d', errors='coerce')
#     gestante_SELECTED['dt_nascimento'] = gestante_SELECTED['dt_nascimento'].where(gestante_SELECTED['dt_nascimento'] < now, gestante_SELECTED['dt_nascimento'] - np.timedelta64(100, 'Y')) 
#     gestante_SELECTED['AGE'] = (now - gestante_SELECTED['dt_nascimento']).astype('<m8[Y]') 

#     def age_group(row):
#         if row['AGE'] >= 0 and row['AGE'] <=16:
#             return "Faixa 1"
#         elif row['AGE'] >= 17 and row['AGE'] <=20:
#             return "Faixa 2"
#         elif row['AGE'] >= 21 and row['AGE'] <=25:
#             return "Faixa 3"
#         elif row['AGE'] >= 26 and row['AGE'] <=30:
#             return "Faixa 4"
#         elif row['AGE'] >= 31 and row['AGE'] <=34:
#             return "Faixa 5"
#         elif row['AGE'] >= 35:
#             return "Faixa 6"
#         else:
#             return "NaN"

#     gestante_SELECTED['FAIXA_ETARIA'] = gestante_SELECTED.apply (lambda row: age_group(row), axis=1)

#     """**Calcular Idade gestacional**"""

#     gestante_SELECTED['NEW_DUM_y'] = pd.to_datetime(gestante_SELECTED['NEW_DUM_y'], format ='%Y-%m-%d', errors='coerce')
#     gestante_SELECTED['co_dim_tempo'] = pd.to_datetime(gestante_SELECTED['co_dim_tempo'], format ='%Y-%m-%d', errors='coerce')
#     gestante_SELECTED['Difference'] = (gestante_SELECTED['co_dim_tempo'] - gestante_SELECTED['NEW_DUM_y']).dt.days
#     gestante_SELECTED['semanas_diff'] = gestante_SELECTED['Difference'] / 7
#     gestante_SELECTED['nu_idade_gestacional_semanas'] = gestante_SELECTED['nu_idade_gestacional_semanas'].replace('', 0).astype(float)
#     gestante_SELECTED['nu_idade_gestacional_semanas'] = gestante_SELECTED['nu_idade_gestacional_semanas'].astype(str).astype(float).astype(int)
#     def ig(row):  
#         if row['nu_idade_gestacional_semanas'] >= 0:
#             return row['nu_idade_gestacional_semanas']
#         else:
#             return row['semanas_diff']
    
#     gestante_SELECTED['IG'] = gestante_SELECTED.apply(lambda row: ig(row), axis=1)

#     def idade_gestacional(row):
#         if row['IG'] >= 0 and row['IG'] <=12:
#             return "1º Trimestre"
#         elif row['IG'] >= 13 and row['IG'] <=24:
#             return "2º Trimestre"
#         elif row['IG'] >= 25 and row['IG'] <=41:
#             return "3º Trimestre"
#         else:
#             return "NaN"

#     gestante_SELECTED['nu_idade_gestacional'] = gestante_SELECTED.apply (lambda row: idade_gestacional(row), axis=1)

#     """### Delete unecessary Column and Rename"""

#     gestante_SELECTED_FINAL = gestante_SELECTED.drop(columns=['co_dim_equipe_1','nu_idade_gestacional_semanas','nu_gestas_previas','Difference','semanas_diff'])
#     gestante_SELECTED_FINAL = gestante_SELECTED_FINAL.rename(columns={'co_fat_cidadao_pec_y': 'co_fat_cidadao_pec',
#                                                         'NEW_DUM_y': 'co_dim_tempo_dum',
#                                                         'NEW_Gestacao_N_y': 'N_gestacoes',
#                                                         'co_dim_unidade_saude_1': 'co_dim_unidade_saude',
#                                                         'exames_para_sifilis_HIV': 'exames_para_sifilis_hiv',
#                                                         'STRICTED': 'com_atendimento_odontologico_stricted',
#                                                         'RAZOAVEL': 'com_atendimento_odontologico_razoavel',
#                                                         'AMPLO': 'com_atendimento_odontologico_amplo',
#                                                         'FAIXA_ETARIA': 'ds_faixa_etaria_gestante',
#                                                         'AGE': 'idade',
#                                                         'IG': 'nu_idade_gestacional',
#                                                         'nu_idade_gestacional': 'nu_idade_gestacional_trimestre'})


#     """### Linkages Unidade de Saúde"""

#     unidades['co_seq_dim_unidade_saude'] = unidades['co_seq_dim_unidade_saude'].astype(int)
#     unidades.rename(columns={'co_seq_dim_unidade_saude': 'co_dim_unidade_saude'}, inplace=True)

#     gestante_SELECTED_FINAL['co_dim_unidade_saude'] = gestante_SELECTED_FINAL['co_dim_unidade_saude'].replace(np.nan, 0)
#     gestante_SELECTED_FINAL['co_dim_unidade_saude'] = gestante_SELECTED_FINAL['co_dim_unidade_saude'].astype(int)

#     gestante_SELECTED_FINAL = gestante_SELECTED_FINAL.merge(unidades, on='co_dim_unidade_saude', how='left', indicator=True)


#     """### Add Diabete and Hipertensão"""

#     match = ['T89','T90','W85','E10','E100','E101','E102','E103','E104','E105','E106','E107','E108','E109','E11','E110','E111','E112','E113','E114','E115','E116','E117','E118','E119','E12','E120',
#             'E121','E122','E123','E124','E125','E126','E127','E128','E129','E13','E130','E131','E132','E133','E134','E135','E136','E137','E138','E139','E14','E140','E141','E142','E143','E144','E145',
#             'E146','E147','E148','E149','O24','O240','O241','O242','O243','O244','O249','P702','ABP006']

#     def string_finder(row, words):
#         if any(word in field for field in row for word in words):
#             return True
#         return False

#     gestante_SELECTED_FINAL['isContained_DIABETE'] = gestante_SELECTED_FINAL.astype(str).apply(string_finder, words=match, axis=1)

#     match = ['K86','K87','W81','I10','I11','I110','I119','I12','I120','I129','I13','I130','I131','I132','I139','I15','I150','I151','I152','I158','I159','I270','I272','O10','O100','O101','O102','O103',
#             'O104','O109','ABP005']

#     def string_finder(row, words):
#         if any(word in field for field in row for word in words):
#             return True
#         return False

#     gestante_SELECTED_FINAL['isContained_HIPERTENSAO'] = gestante_SELECTED_FINAL.astype(str).apply(string_finder, words=match, axis=1)

#     """### Exportando para excel FINAL DATABASE GESTAÇÔES"""

#     gestante_SELECTED_FINAL = gestante_SELECTED_FINAL.drop(columns=['_merge'])


#     irece_mestre = pd.read_parquet( path + '/BASE_DEMOGRAFICO.parquet')

#     gestante_SELECTED_FINAL['co_fat_cidadao_pec'] = gestante_SELECTED_FINAL['co_fat_cidadao_pec'].astype(str)
#     irece_mestre['co_fat_cidadao_pec'] = irece_mestre['co_fat_cidadao_pec'].astype(str)
#     gestante_SELECTED_FINAL['co_fat_cidadao_pec'] = gestante_SELECTED_FINAL['co_fat_cidadao_pec'].str[:-2]

#     irece_mestre = irece_mestre[['co_fat_cidadao_pec','ds_tipo_localizacao']]
#     gestante_localiza = gestante_SELECTED_FINAL.merge(irece_mestre, on='co_fat_cidadao_pec', how='left', indicator=True)
#     gestante_localiza = gestante_localiza.drop(columns=['_merge'])

#     gestante_localiza['N_gestacoes'] =  gestante_localiza['N_gestacoes'].replace('', 0).astype(float)
#     gestante_localiza['st_gravidez_planejada'] =  gestante_localiza['st_gravidez_planejada'].replace('', 0).astype(float)
#     # gestante_SELECTED_FINAL.to_parquet( path + '/BASE_GESTACOES_FINAL_PAINEL.parquet')
#     gestante_localiza.to_parquet( path + '/BASE_GESTACOES_FINAL_PAINEL.parquet')
