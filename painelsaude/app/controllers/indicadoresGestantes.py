
import pandas as pd
import numpy as np
def criarIndicadoresGestantes( path ):

    cadastro_mestre = pd.read_excel( path + '/CADASTRO_MESTRE_JOIN_AT_IND_GEST_HIP_DIAB_JOIN_UNIDADES_CLEAN_PAINEL.xlsx')

    tb_fat_at_ind_2018_2019_2020  = pd.read_csv(path + '/tb_fat_atendimento_individual.csv',sep=';',engine='python', decimal = ',',keep_default_na=False)

    """### Concat Atendimento Individual and merge with Cadastro Mestre do get Unidade de Saúde"""


    tb_fat_at_ind_2018_2019_2020_SELECTED = tb_fat_at_ind_2018_2019_2020[['co_fat_cidadao_pec','co_dim_unidade_saude_1','co_dim_equipe_1','co_dim_tempo','dt_nascimento','nu_peso','nu_altura','st_vacinacao_em_dia','co_dim_tempo_dum', 
                                                                        'st_gravidez_planejada','nu_idade_gestacional_semanas','nu_gestas_previas','nu_partos','ds_filtro_cids','ds_filtro_ciaps','ds_filtro_proced_avaliados', 
                                                                        'ds_filtro_proced_solicitados']]

    cadastro_mestre = cadastro_mestre[['co_fat_cidadao_pec','co_unidade_saude']]

    """### Linkage between cadastro & Atendimento"""

    cadastro_mestre['co_fat_cidadao_pec'] = cadastro_mestre['co_fat_cidadao_pec'].astype(str).str[:-2]
    
    tb_fat_at_ind_2018_2019_2020_SELECTED['co_fat_cidadao_pec'] = tb_fat_at_ind_2018_2019_2020_SELECTED['co_fat_cidadao_pec'].astype(str).str[:-2]

 
    
    tb_fat_at_ind_2018_2019_2020_SELECTED = tb_fat_at_ind_2018_2019_2020_SELECTED.merge(cadastro_mestre, on='co_fat_cidadao_pec', how='left', indicator=True)




    """### Filter CID / CIAP and clean DUM

    **Identificando atendimentos relacionados ao pré-natal pelo CID/CIAP**
    """

    match_CID = ['|O009|','|O11|','|O12|','|O120|','|O121|','|O122|','|O13|','|O14|','|O140|','|O141|','|O149|','|O15|','|O150|','|O151|','|O159|','|O16|','|O20|',
            '|O200|','|O208|','|O209|','|O21|','|O210|','|O211|','|O212|','|O218|','|O219|','|O22|','|O220|','|O221|','|O222|','|O223|','|O224|','|O225|','|O228|',
            '|O229|','|O23|','|O230|','|O231|','|O232|','|O233|','|O234|','|O235|','|O239|','|O24|','|O240|','|O241|','|O242|','|O243|','|O244|','|O249|','|O25|',
            '|O26|','|O260|','|O261|','|O263|','|O264|','|O265|','|O268|','|O269|','|O28|','|O280|','|O281|','|O282|','|O283|','|O284|','|O285|','|O288|','|O289|',
            '|O29|','|O290|','|O291|','|O292|','|O293|','|O294|','|O295|','|O296|','|O298|','|O299|','|O30|','|O300|','|O301|','|O302|','|O308|','|O309|','|O31|',
            '|O311|','|O312|','|O318|','|O32|','|O320|','|O321|','|O322|','|O323|','|O324|','|O325|','|O326|','|O328|','|O329|','|O33|','|O330|','|O331|','|O332|',
            '|O333|','|O334|','|O335|','|O336|','|O337|','|O338|','|O339|','|O34|','|O340|','|O341|','|O342|','|O343|','|O344|','|O345|','|O346|','|O347|','|O348|',
            '|O349|','|O35|','|O350|','|O351|','|O352|','|O353|','|O354|','|O355|','|O356|','|O357|','|O358|','|O359|','|O36|','|O360|','|O361|','|O362|','|O363|',
            '|O365|','|O366|','|O367|','|O368|','|O369|','|O40|','|O41|','|O410|','|O411|','|O418|','|O419|','|O43|','|O430|','|O431|','|O438|','|O439|','|O44|',
            '|O440|','|O441|','|O46|','|O460|','|O468|','|O469|','|O47|','|O470|','|O471|','|O479|','|O48|','|Z321|','|Z33|','|Z34|','|Z340|','|Z348|','|Z349|',
            '|Z35|','|Z350|','|Z351|','|Z352|','|Z353|','|Z354|','|Z357|','|Z358|','|Z359|','|Z640|']
    match_CIAP = ['|W03|','|W05|','|W71|','|W78|','|W79|','|W80|','|W81|','|W84|','|W85|','|ABP001|']


    def string_finder(row, words):
        if any(word in field for field in row for word in words):
            return True
        return False

    tb_fat_at_ind_2018_2019_2020_SELECTED['isContained_CID'] = tb_fat_at_ind_2018_2019_2020_SELECTED.astype(str).apply(string_finder, words=match_CID, axis=1)
    tb_fat_at_ind_2018_2019_2020_SELECTED['isContained_CIAP'] = tb_fat_at_ind_2018_2019_2020_SELECTED.astype(str).apply(string_finder, words=match_CIAP, axis=1)


    # Atendimentos identificamos pelo CID ou CIAP PN
    Atendimentos_2018_2019_2020_gestante = tb_fat_at_ind_2018_2019_2020_SELECTED[(tb_fat_at_ind_2018_2019_2020_SELECTED['isContained_CID'] == True) | (tb_fat_at_ind_2018_2019_2020_SELECTED['isContained_CIAP'] == True)]

    # Atendimentos não identificados pelos códigos CID/CIAP, recuperados pela DUM válida e IG
    df = tb_fat_at_ind_2018_2019_2020_SELECTED[(tb_fat_at_ind_2018_2019_2020_SELECTED['isContained_CID'] == False) & (tb_fat_at_ind_2018_2019_2020_SELECTED['isContained_CIAP'] == False)]

    Atendimentos_2018_2019_2020_SELECTED_FILTERED = df[(df['co_dim_tempo_dum'] != 30001231) | (df['nu_idade_gestacional_semanas'] != '')]

    # Total de atendimentos de gestantes/puérperas identificados 
    Gestantes_2018_2019_2020 =  pd.concat([Atendimentos_2018_2019_2020_gestante, Atendimentos_2018_2019_2020_SELECTED_FILTERED])

    # Total de atendimentos de gestantes/puérperas identificados com co_fat_cidadao_pec preenchido
    Gestantes_2018_2019_2020_long = Gestantes_2018_2019_2020[(Gestantes_2018_2019_2020['co_fat_cidadao_pec'] != '')]


    Gestante_2018_2019_2020_long = Gestantes_2018_2019_2020_long.sort_values(by='co_dim_tempo')

    # counting unique values
    n = len(pd.unique(Gestantes_2018_2019_2020_long['co_fat_cidadao_pec']))
    


    """**Identificando os casos inválidos**"""

    #Group gestantes com a media da DUM
    Gestantes_2018_2019_2020_long_GROUPED_MEAN = Gestantes_2018_2019_2020_long.groupby('co_fat_cidadao_pec', as_index=False)['co_dim_tempo_dum'].mean()

    df_1 = Gestantes_2018_2019_2020_long[Gestantes_2018_2019_2020_long['co_fat_cidadao_pec']=='102241']

    Gestantes_2018_2019_2020_long_GROUPED_MEAN["co_dim_tempo_dum"] = Gestantes_2018_2019_2020_long_GROUPED_MEAN["co_dim_tempo_dum"].fillna(0.0).astype(int)

    # Gestantes que tem a DUM INVALIDA
    Gestantes_2018_2019_2020_long_GROUPED_MEAN_FILTERED_3000 = Gestantes_2018_2019_2020_long_GROUPED_MEAN.loc[Gestantes_2018_2019_2020_long_GROUPED_MEAN['co_dim_tempo_dum'] == 30001231]

    Gestantes_2018_2019_2020_long_GROUPED_MEAN_FILTERED_3000['FILTER'] = 'INVALIDA'

    Gestantes_2018_2019_2020_long = Gestantes_2018_2019_2020_long.drop(columns=['_merge'])
    Gestantes_2018_2019_2020_long_INVALIDA = Gestantes_2018_2019_2020_long.merge(Gestantes_2018_2019_2020_long_GROUPED_MEAN_FILTERED_3000, on='co_fat_cidadao_pec', how='left', indicator=True )

    Gestantes_2018_2019_2020_long_INVALIDA_SELECTED_PUERP_PN = Gestantes_2018_2019_2020_long_INVALIDA[(Gestantes_2018_2019_2020_long_INVALIDA['FILTER'] == 'INVALIDA')]


    """**Fechamos a base de gestantes com 13.124 atendimentos à gestantes, na base wide ficamos com 2.838 gestantes, sendo que destas 388 só possuem DUM inválida.**

    ### Create NEW_DUM and function to find GESTAÇÔES
    """

    df_test_1660 = Gestantes_2018_2019_2020_long_INVALIDA[Gestantes_2018_2019_2020_long_INVALIDA['co_fat_cidadao_pec']=='1660']


    #Gestantes_2018_2019_2020_long_INVALIDA = Gestantes_2018_2019_2020_long_INVALIDA.drop(columns=['_merge','co_dim_tempo_dum_y'])
    Gestantes_2018_2019_2020_long_INVALIDA = Gestantes_2018_2019_2020_long_INVALIDA.rename(columns={'co_dim_tempo_dum_x': 'co_dim_tempo_dum'})
    Gestantes_2018_2019_2020_long_INVALIDA['co_dim_tempo_dum'] = pd.to_datetime(Gestantes_2018_2019_2020_long_INVALIDA['co_dim_tempo_dum'], format ='%Y%m%d',errors = 'coerce')

    """**Identificando a DUM mínima - PDUM**"""

    df_grouped = Gestantes_2018_2019_2020_long_INVALIDA.groupby(['co_fat_cidadao_pec'])['co_dim_tempo_dum'].min().reset_index()

    df_grouped_TEST_MIN = df_grouped[df_grouped['co_fat_cidadao_pec']=='1660']

    """**Identificando a DUM máxima - MDUM**"""

    df_grouped_max = Gestantes_2018_2019_2020_long_INVALIDA.groupby(['co_fat_cidadao_pec'])['co_dim_tempo_dum'].max().reset_index()

    df_grouped_TEST_MAX = df_grouped_max[df_grouped_max['co_fat_cidadao_pec']=='1660']

    df_grouped.rename(columns={'co_dim_tempo_dum': 'PDUM'}, inplace=True)
    df_grouped_max.rename(columns={'co_dim_tempo_dum': 'MDUM'}, inplace=True)

    df = df_grouped[df_grouped['co_fat_cidadao_pec'] == '1660']



    Gestantes_2018_2019_2020_long_INVALIDA = Gestantes_2018_2019_2020_long_INVALIDA.drop(columns=['_merge'])
    Gestantes_2018_2019_2020_long_PDUM = Gestantes_2018_2019_2020_long_INVALIDA.merge(df_grouped, on='co_fat_cidadao_pec', how='left', indicator=True )

    Gestantes_2018_2019_2020_long_PDUM = Gestantes_2018_2019_2020_long_PDUM.drop(columns=['_merge'])
    Gestantes_2018_2019_2020_long_PDUM_MDUM = Gestantes_2018_2019_2020_long_PDUM.merge(df_grouped_max, on='co_fat_cidadao_pec', how='left', indicator=True )


    Gestantes_2018_2019_2020_long_PDUM_MDUM = Gestantes_2018_2019_2020_long_PDUM_MDUM.sort_values(by='co_dim_tempo')

    """**Identificando o fim da gestação e o primeiro trimestre**"""

    Gestantes_2018_2019_2020_long_PDUM_MDUM['PDUM_294'] = Gestantes_2018_2019_2020_long_PDUM_MDUM.PDUM + pd.Timedelta(days=294)
    Gestantes_2018_2019_2020_long_PDUM_MDUM['PDUM_91'] = Gestantes_2018_2019_2020_long_PDUM_MDUM.PDUM + pd.Timedelta(days=91)
    Gestantes_2018_2019_2020_long_PDUM_MDUM['Gestacao_N'] = np.where((Gestantes_2018_2019_2020_long_PDUM_MDUM.FILTER == 'INVALIDA'),0,1)

    Gestantes_2018_2019_2020_long_PDUM_MDUM['co_dim_tempo'] = pd.to_datetime(Gestantes_2018_2019_2020_long_PDUM_MDUM['co_dim_tempo'], format ='%Y%m%d',errors = 'coerce')

    Gestantes_2018_2019_2020_long_PDUM_MDUM["co_dim_tempo_dum"] = Gestantes_2018_2019_2020_long_PDUM_MDUM.co_dim_tempo_dum.astype(object).where(Gestantes_2018_2019_2020_long_PDUM_MDUM.co_dim_tempo_dum.notnull(), None)
    Gestantes_2018_2019_2020_long_PDUM_MDUM["co_dim_tempo"] = Gestantes_2018_2019_2020_long_PDUM_MDUM.co_dim_tempo.astype(object).where(Gestantes_2018_2019_2020_long_PDUM_MDUM.co_dim_tempo.notnull(), None)


    df_test_1660 = Gestantes_2018_2019_2020_long_PDUM_MDUM[Gestantes_2018_2019_2020_long_PDUM_MDUM['co_fat_cidadao_pec']=='1660']

    Gestantes_2018_2019_2020_long_PDUM_MDUM['co_dim_tempo'] = pd.to_datetime(Gestantes_2018_2019_2020_long_PDUM_MDUM['co_dim_tempo'], format ='%Y-%m-%d', errors='coerce')
    Gestantes_2018_2019_2020_long_PDUM_MDUM['co_dim_tempo_dum'] = pd.to_datetime(Gestantes_2018_2019_2020_long_PDUM_MDUM['co_dim_tempo_dum'], format ='%Y-%m-%d', errors='coerce')

    #NEW_DUM
    def categorise(row):
        if row['co_dim_tempo_dum'] is pd.NaT and row['co_dim_tempo'] <= row['MDUM']:
            return row['PDUM']
        elif row['co_dim_tempo_dum'] is pd.NaT and row['MDUM'] < row['PDUM_91']:
            return row['PDUM']
        elif row['co_dim_tempo_dum'] is pd.NaT and row['co_dim_tempo'] > row['PDUM_294']:
            return row['MDUM']
        elif row['co_dim_tempo_dum'] is pd.NaT and row['co_dim_tempo'] <= row['PDUM_294']:
            return row['PDUM']
        elif row['co_dim_tempo_dum'] is pd.NaT and row['PDUM'] == row['MDUM']:
            return row['PDUM']
        elif row['co_dim_tempo_dum'] <= row['PDUM_91']:
            return row['PDUM']
        elif row['co_dim_tempo_dum'] > row['PDUM_91']:
            return row['co_dim_tempo_dum'] 
    
    Gestantes_2018_2019_2020_long_PDUM_MDUM['NEW_DUM'] = Gestantes_2018_2019_2020_long_PDUM_MDUM.apply(lambda row: categorise(row), axis=1)
    Gestantes_2018_2019_2020_long_PDUM_MDUM['NEW_DUM'] = pd.to_datetime(Gestantes_2018_2019_2020_long_PDUM_MDUM['NEW_DUM'], format ='%Y-%m-%d', errors='coerce')
    Gestantes_2018_2019_2020_long_PDUM_MDUM['NEW_DUM_294'] = Gestantes_2018_2019_2020_long_PDUM_MDUM.NEW_DUM + pd.Timedelta(days=294)

    """**Conforme decidido em reunião, os casos INVÁLIDOS serão desconsiderados da base**"""

    def gestacoes(row):  
        if  row['Gestacao_N'] == 0:
            return 0
        elif row['NEW_DUM'] == row['PDUM']:
            return 1
        elif row['NEW_DUM'] != row['PDUM']:
            return 2
            
            
    Gestantes_2018_2019_2020_long_PDUM_MDUM['NEW_Gestacao_N'] = Gestantes_2018_2019_2020_long_PDUM_MDUM.apply(lambda row: gestacoes(row), axis=1)



    df_test_1660 = Gestantes_2018_2019_2020_long_PDUM_MDUM[Gestantes_2018_2019_2020_long_PDUM_MDUM['co_fat_cidadao_pec']=='1660']

    null_df = Gestantes_2018_2019_2020_long_PDUM_MDUM[Gestantes_2018_2019_2020_long_PDUM_MDUM['NEW_DUM'].isnull()]
    null_df_OK = null_df.loc[null_df['FILTER'] != 'INVALIDA']



    """**Retirando os casos inválidos da base**"""

    Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA = Gestantes_2018_2019_2020_long_PDUM_MDUM[Gestantes_2018_2019_2020_long_PDUM_MDUM['Gestacao_N'] != 0]

    # counting unique values - gestantes
    n = len(pd.unique(Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['co_fat_cidadao_pec']))
    

    Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['NEW_Gestacao_N'] = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['NEW_Gestacao_N'].astype(str)
    Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['Chave'] = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA[['co_fat_cidadao_pec','NEW_Gestacao_N']].apply('_'.join, axis=1)

    df_teste_wsa = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA[Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['co_fat_cidadao_pec']=='1660']

    # counting unique values - Chave
    n = len(pd.unique(Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['Chave']))
    

    df_test = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA[Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['co_fat_cidadao_pec'] == '40482']

    """### Calculo dos Indices banco novo com as gestações

    #### INDICADOR 01 (Proporção de gestantes com pelo menos 6 consultas pré-nata(PN))
    """


    Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA[Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA.groupby(['co_fat_cidadao_pec','NEW_Gestacao_N'])['co_fat_cidadao_pec'].transform('size') >= 6]

    # Total de atendimentos com 6 ou mais consultas realizadas


    Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['co_fat_cidadao_pec'] = Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['co_fat_cidadao_pec'].astype(str).astype(float).astype(int)
    Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['nu_idade_gestacional_semanas'] = pd.to_numeric(Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['nu_idade_gestacional_semanas'])
    Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED[Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['co_fat_cidadao_pec'] == 7029]

    """**Completando a idade gestacional a partir da NEW_DUM**"""

    Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['NEW_DUM'] = pd.to_datetime(Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['NEW_DUM'], format ='%Y-%m-%d', errors='coerce')
    Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['co_dim_tempo'] = pd.to_datetime(Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['co_dim_tempo'], format ='%Y-%m-%d', errors='coerce')
    Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['Difference'] = (Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['co_dim_tempo'] - Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['NEW_DUM']).dt.days
    Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['semanas_diff'] = Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['Difference'] / 7

    def ig(row):  
        if row['nu_idade_gestacional_semanas'] >= 0:
            return row['nu_idade_gestacional_semanas']
        else:
            return row['semanas_diff']
    
    Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['IG'] = Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED.apply(lambda row: ig(row), axis=1)



    df = Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED[Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['Chave'] == '10244_1']

    """Total de gestações com 6 ou mais consultas - 886 ok"""

    # counting unique values - Chave
    n = len(pd.unique(Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['Chave']))
    

    test_final = Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED.groupby('Chave').agg(IG = ('IG', 'min')).reset_index()



    df = test_final[test_final['Chave'] == '10244_1']

    final_result = test_final.loc[test_final['IG'] <= 20.0]

    final_result['consultas_6_prenatal'] = True

    final_result_Prenatal = final_result[['Chave','consultas_6_prenatal']]




    final_result_Prenatal_merge = final_result_Prenatal.merge(Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA, how='right', on='Chave', indicator='exists' )


    df = final_result_Prenatal_merge[final_result_Prenatal_merge['Chave'] == '10244_1']


    """#### INDICADOR 02 (Proporção de gestantes com realização de exames para sífilis e HIV) 1421"""



    # create regex pattern out of the list of words
    positive = '|'.join(['0202031110','ABEX019','0202030300','ABEX018','0202031179','0214010074','ABPG026','0214010082','0214010058','ABPG024','0214010040'])

    Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['POSITIVE_proced_avaliados'] = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['ds_filtro_proced_avaliados'].str.contains(positive)

    Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA.loc[Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['POSITIVE_proced_avaliados'] == True]


    Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL = Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL.astype(str)


    df = Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL[Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL['co_fat_cidadao_pec'] == '40368']

    Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL_PIVOTED = Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL.groupby(['Chave']).agg({'co_dim_unidade_saude_1':','.join, 
                                                                                    'co_dim_equipe_1':','.join, 
                                                                                    'co_dim_tempo':','.join, 
                                                                                    'dt_nascimento':','.join, 
                                                                                    'nu_peso':','.join, 
                                                                                    'nu_altura':','.join, 
                                                                                    'st_vacinacao_em_dia':','.join, 
                                                                                    'co_dim_tempo_dum':','.join, 
                                                                                    'st_gravidez_planejada':','.join, 
                                                                                    'nu_idade_gestacional_semanas':','.join, 
                                                                                    'nu_gestas_previas':','.join, 
                                                                                    'nu_partos':','.join, 
                                                                                    'ds_filtro_cids':','.join, 
                                                                                    'ds_filtro_ciaps':','.join, 
                                                                                    'ds_filtro_proced_avaliados':','.join, 
                                                                                    'ds_filtro_proced_solicitados': ','.join,
                                                                                    'NEW_DUM': ','.join,
                                                                                    'NEW_DUM_294': ','.join,
                                                                                    'POSITIVE_proced_avaliados': ','.join,}).reset_index()



    Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL_PIVOTED['exames_para_sifilis_HIV'] = Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL_PIVOTED['POSITIVE_proced_avaliados'].str.split(',').str[0]

    final_result_sifilis_hiv = Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL_PIVOTED[['Chave','exames_para_sifilis_HIV']]


    final_result_Prenatal_sifilis_hiv_merge = final_result_sifilis_hiv.merge(final_result_Prenatal_merge, how='right', on='Chave', indicator='exists_2' )



    """#### INDICADOR 03 (Proporção de gestantes com atendimento odontológico realizado)"""


    df = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA[Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['co_fat_cidadao_pec'] == '49089']

    Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA.astype(str)

    Gestantes_2018_2019_2020_long_PDUM_MDUM_FINAL_PIVOTED = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA.groupby(['co_fat_cidadao_pec','NEW_Gestacao_N']).agg({'co_dim_unidade_saude_1':','.join, 
                                                                                    'co_dim_equipe_1':','.join, 
                                                                                    'co_dim_tempo':','.join, 
                                                                                    'dt_nascimento':','.join, 
                                                                                    'nu_peso':','.join, 
                                                                                    'nu_altura':','.join, 
                                                                                    'st_vacinacao_em_dia':','.join, 
                                                                                    'co_dim_tempo_dum':','.join, 
                                                                                    'st_gravidez_planejada':','.join, 
                                                                                    'nu_idade_gestacional_semanas':','.join, 
                                                                                    'nu_gestas_previas':','.join, 
                                                                                    'nu_partos':','.join, 
                                                                                    'ds_filtro_cids':','.join, 
                                                                                    'ds_filtro_ciaps':','.join, 
                                                                                    'ds_filtro_proced_avaliados':','.join, 
                                                                                    'ds_filtro_proced_solicitados': ','.join,
                                                                                    'NEW_DUM': ','.join,
                                                                                    'NEW_DUM_294': ','.join,
                                                                                    'Chave': ','.join}).reset_index()



    df = Gestantes_2018_2019_2020_long_PDUM_MDUM_FINAL_PIVOTED[Gestantes_2018_2019_2020_long_PDUM_MDUM_FINAL_PIVOTED['co_fat_cidadao_pec'] == '10715']

    Odonto_2018_2019_2020 = pd.read_csv( path + '/tb_fat_atendimento_odonto.csv',sep=';',engine='python', decimal = ',')


    Odonto_2018_2019_2020['co_dim_tempo'] = pd.to_datetime(Odonto_2018_2019_2020['co_dim_tempo'], format ='%Y%m%d')
    Odonto_2018_2019_2020 = Odonto_2018_2019_2020.astype(str)
    Odonto_2018_2019_2020_PIVOTED = Odonto_2018_2019_2020.groupby('co_fat_cidadao_pec').agg({'co_dim_tempo':','.join}).reset_index()

    Odonto_2018_2019_2020_PIVOTED['co_fat_cidadao_pec'] = Odonto_2018_2019_2020_PIVOTED['co_fat_cidadao_pec'].astype(str).str[:-2]

    #NOVO METODO DE GESTACAO 2N
    Linkage_2018_2019_2020_Gestante_Odoto = Gestantes_2018_2019_2020_long_PDUM_MDUM_FINAL_PIVOTED.merge(Odonto_2018_2019_2020_PIVOTED, on='co_fat_cidadao_pec', how='left', indicator=True )

    Linkage_2018_2019_2020_Gestante_Odoto_YES = Linkage_2018_2019_2020_Gestante_Odoto.loc[Linkage_2018_2019_2020_Gestante_Odoto['_merge'] == 'both']

    Linkage_2018_2019_2020_Gestante_Odoto_YES['Chave'] = Linkage_2018_2019_2020_Gestante_Odoto_YES['Chave'].str.split(',').str[0]

    """Merge ok com 491"""

    Linkage_2018_2019_2020_Gestante_Odoto_YES = Linkage_2018_2019_2020_Gestante_Odoto_YES.rename(columns={'co_dim_tempo_x': 'co_dim_tempo_Gestante'})
    Linkage_2018_2019_2020_Gestante_Odoto_YES = Linkage_2018_2019_2020_Gestante_Odoto_YES.rename(columns={'co_dim_tempo_y': 'co_dim_tempo_Odonto'})
    Linkage_2018_2019_2020_Gestante_Odoto_YES = Linkage_2018_2019_2020_Gestante_Odoto_YES[['co_fat_cidadao_pec','NEW_Gestacao_N','co_dim_tempo_Gestante','co_dim_tempo_Odonto','NEW_DUM','Chave']]

    df1 = Linkage_2018_2019_2020_Gestante_Odoto_YES['NEW_DUM'].str.split(',', expand=True).astype(str)
    df1 = df1.apply(pd.to_datetime,errors='coerce')
    df = Linkage_2018_2019_2020_Gestante_Odoto_YES.assign(DUM=df1.max(axis=1,skipna=True))



    df_test = df[df['co_fat_cidadao_pec'] == '40755']


    df['DUM_294'] = df.DUM + pd.Timedelta(days=294)
    df['DUM_MEN_71'] = df.DUM - pd.Timedelta(days=71)
    df['DUM__MEN_365'] = df.DUM - pd.Timedelta(days=365)

    df.DUM.apply( lambda x: x+ pd.Timedelta(days=294))

    df2 = df['co_dim_tempo_Odonto'].str.split(',', expand=True).astype(str)
    df2 = df2.apply(pd.to_datetime,errors='coerce')
    df_FINAL = df.assign(minyear_Odonto=df2.min(axis=1,skipna=True),maxyear_Odonto=df2.max(axis=1,skipna=True))

    df_test = df_FINAL[df_FINAL['co_fat_cidadao_pec'] == '40755']


    df_string = df_FINAL.astype(str)


    df_string['minyear_Odonto'] = pd.to_datetime(df_string['minyear_Odonto'], format ='%Y-%m-%d')
    df_string['DUM'] = pd.to_datetime(df_string['DUM'], format ='%Y-%m-%d')
    df_string['maxyear_Odonto'] = pd.to_datetime(df_string['maxyear_Odonto'], format ='%Y-%m-%d')
    df_string['DUM_294'] = pd.to_datetime(df_string['DUM_294'], format ='%Y-%m-%d')
    df_string['DUM_MEN_71'] = pd.to_datetime(df_string['DUM_MEN_71'], format ='%Y-%m-%d')
    df_string['DUM__MEN_365'] = pd.to_datetime(df_string['DUM__MEN_365'], format ='%Y-%m-%d')


    df_string['STRICTED'] = np.where((df_string.minyear_Odonto >= df_string.DUM)&(df_string.maxyear_Odonto <= df_string.DUM_294),1,0)
    df_string['RAZOAVEL'] = np.where((df_string.minyear_Odonto >= df_string.DUM_MEN_71)&(df_string.maxyear_Odonto <= df_string.DUM_294),1,0)
    df_string['AMPLO'] = np.where((df_string.minyear_Odonto >= df_string.DUM__MEN_365)&(df_string.maxyear_Odonto <= df_string.DUM_294),1,0)

    df_test = df_string[df_string['co_fat_cidadao_pec'] == '40755']


    total = df_string['STRICTED'].sum()
    total_R = df_string['RAZOAVEL'].sum()
    total_A = df_string['AMPLO'].sum()

    FINAL_RESULTS = df_string.merge(final_result_Prenatal_sifilis_hiv_merge, how='right', on='Chave', indicator='exists_3' )



    """### Exportando para excel FINAL DATABASE GESTAÇÔES"""

    FINAL_RESULTS.to_excel( path + '/BASE_GESTACOES_3_INDICADORES.xlsx')


# def criarIndicadoresGestantes( path ):

#     tb_fat_at_ind_2018_2019_2020 = pd.read_csv( path + '/tb_fat_atendimento_individual.csv',sep=';',engine='python', decimal = ',',keep_default_na=False)


#     tb_fat_at_ind_2018_2019_2020_SELECTED = tb_fat_at_ind_2018_2019_2020[['co_fat_cidadao_pec','co_dim_unidade_saude_1','co_dim_equipe_1','co_dim_tempo','dt_nascimento','nu_peso','nu_altura','st_vacinacao_em_dia','co_dim_tempo_dum', 
#                                                                         'st_gravidez_planejada','nu_idade_gestacional_semanas','nu_gestas_previas','nu_partos','ds_filtro_cids','ds_filtro_ciaps','ds_filtro_proced_avaliados', 
#                                                                         'ds_filtro_proced_solicitados']]

#     """**Identificando atendimentos relacionados ao pré-natal pelo CID/CIAP**"""

#     match_CID = ['|O009|','|O11|','|O12|','|O120|','|O121|','|O122|','|O13|','|O14|','|O140|','|O141|','|O149|','|O15|','|O150|','|O151|','|O159|','|O16|','|O20|',
#             '|O200|','|O208|','|O209|','|O21|','|O210|','|O211|','|O212|','|O218|','|O219|','|O22|','|O220|','|O221|','|O222|','|O223|','|O224|','|O225|','|O228|',
#             '|O229|','|O23|','|O230|','|O231|','|O232|','|O233|','|O234|','|O235|','|O239|','|O24|','|O240|','|O241|','|O242|','|O243|','|O244|','|O249|','|O25|',
#             '|O26|','|O260|','|O261|','|O263|','|O264|','|O265|','|O268|','|O269|','|O28|','|O280|','|O281|','|O282|','|O283|','|O284|','|O285|','|O288|','|O289|',
#             '|O29|','|O290|','|O291|','|O292|','|O293|','|O294|','|O295|','|O296|','|O298|','|O299|','|O30|','|O300|','|O301|','|O302|','|O308|','|O309|','|O31|',
#             '|O311|','|O312|','|O318|','|O32|','|O320|','|O321|','|O322|','|O323|','|O324|','|O325|','|O326|','|O328|','|O329|','|O33|','|O330|','|O331|','|O332|',
#             '|O333|','|O334|','|O335|','|O336|','|O337|','|O338|','|O339|','|O34|','|O340|','|O341|','|O342|','|O343|','|O344|','|O345|','|O346|','|O347|','|O348|',
#             '|O349|','|O35|','|O350|','|O351|','|O352|','|O353|','|O354|','|O355|','|O356|','|O357|','|O358|','|O359|','|O36|','|O360|','|O361|','|O362|','|O363|',
#             '|O365|','|O366|','|O367|','|O368|','|O369|','|O40|','|O41|','|O410|','|O411|','|O418|','|O419|','|O43|','|O430|','|O431|','|O438|','|O439|','|O44|',
#             '|O440|','|O441|','|O46|','|O460|','|O468|','|O469|','|O47|','|O470|','|O471|','|O479|','|O48|','|Z321|','|Z33|','|Z34|','|Z340|','|Z348|','|Z349|',
#             '|Z35|','|Z350|','|Z351|','|Z352|','|Z353|','|Z354|','|Z357|','|Z358|','|Z359|','|Z640|']
#     match_CIAP = ['|W03|','|W05|','|W71|','|W78|','|W79|','|W80|','|W81|','|W84|','|W85|','|ABP001|']


#     def string_finder(row, words):
#         if any(word in field for field in row for word in words):
#             return True
#         return False

#     tb_fat_at_ind_2018_2019_2020_SELECTED['isContained_CID'] = tb_fat_at_ind_2018_2019_2020_SELECTED.astype(str).apply(string_finder, words=match_CID, axis=1)
#     tb_fat_at_ind_2018_2019_2020_SELECTED['isContained_CIAP'] = tb_fat_at_ind_2018_2019_2020_SELECTED.astype(str).apply(string_finder, words=match_CIAP, axis=1)


#     # Atendimentos identificamos pelo CID ou CIAP PN
#     Atendimentos_2018_2019_2020_gestante = tb_fat_at_ind_2018_2019_2020_SELECTED[(tb_fat_at_ind_2018_2019_2020_SELECTED['isContained_CID'] == True) | (tb_fat_at_ind_2018_2019_2020_SELECTED['isContained_CIAP'] == True)]

#     # Atendimentos não identificados pelos códigos CID/CIAP, recuperados pela DUM válida e IG
#     df = tb_fat_at_ind_2018_2019_2020_SELECTED[(tb_fat_at_ind_2018_2019_2020_SELECTED['isContained_CID'] == False) & (tb_fat_at_ind_2018_2019_2020_SELECTED['isContained_CIAP'] == False)]

#     Atendimentos_2018_2019_2020_SELECTED_FILTERED = df[(df['co_dim_tempo_dum'] != 30001231) | (df['nu_idade_gestacional_semanas'] != '')]

#     # Total de atendimentos de gestantes/puérperas identificados 
#     Gestantes_2018_2019_2020 =  pd.concat([Atendimentos_2018_2019_2020_gestante, Atendimentos_2018_2019_2020_SELECTED_FILTERED])

#     # Total de atendimentos de gestantes/puérperas identificados com co_fat_cidadao_pec preenchido
#     Gestantes_2018_2019_2020_long = Gestantes_2018_2019_2020[(Gestantes_2018_2019_2020['co_fat_cidadao_pec'] != '')]


#     Gestante_2018_2019_2020_long = Gestantes_2018_2019_2020_long.sort_values(by='co_dim_tempo')

#     # counting unique values
#     n = len(pd.unique(Gestantes_2018_2019_2020_long['co_fat_cidadao_pec']))
    


#     """**Identificando os casos inválidos**"""

#     #Group gestantes com a media da DUM
#     Gestantes_2018_2019_2020_long_GROUPED_MEAN = Gestantes_2018_2019_2020_long.groupby('co_fat_cidadao_pec', as_index=False)['co_dim_tempo_dum'].mean()

#     df_1 = Gestantes_2018_2019_2020_long[Gestantes_2018_2019_2020_long['co_fat_cidadao_pec']=='102241']

#     Gestantes_2018_2019_2020_long_GROUPED_MEAN["co_dim_tempo_dum"] = Gestantes_2018_2019_2020_long_GROUPED_MEAN["co_dim_tempo_dum"].fillna(0.0).astype(int)

#     # Gestantes que tem a DUM INVALIDA
#     Gestantes_2018_2019_2020_long_GROUPED_MEAN_FILTERED_3000 = Gestantes_2018_2019_2020_long_GROUPED_MEAN.loc[Gestantes_2018_2019_2020_long_GROUPED_MEAN['co_dim_tempo_dum'] == 30001231]

#     Gestantes_2018_2019_2020_long_GROUPED_MEAN_FILTERED_3000['FILTER'] = 'INVALIDA'

#     Gestantes_2018_2019_2020_long_INVALIDA = Gestantes_2018_2019_2020_long.merge(Gestantes_2018_2019_2020_long_GROUPED_MEAN_FILTERED_3000, on='co_fat_cidadao_pec', how='left', indicator=True )

#     Gestantes_2018_2019_2020_long_INVALIDA_SELECTED_PUERP_PN = Gestantes_2018_2019_2020_long_INVALIDA[(Gestantes_2018_2019_2020_long_INVALIDA['FILTER'] == 'INVALIDA')]


#     """**Fechamos a base de gestantes com 13.124 atendimentos à gestantes, na base wide ficamos com 2.838 gestantes, sendo que destas 388 só possuem DUM inválida.**

#     ### Create NEW_DUM and function to find GESTAÇÔES
#     """

#     df_test_1660 = Gestantes_2018_2019_2020_long_INVALIDA[Gestantes_2018_2019_2020_long_INVALIDA['co_fat_cidadao_pec']=='1660']


#     #Gestantes_2018_2019_2020_long_INVALIDA = Gestantes_2018_2019_2020_long_INVALIDA.drop(columns=['_merge','co_dim_tempo_dum_y'])
#     Gestantes_2018_2019_2020_long_INVALIDA = Gestantes_2018_2019_2020_long_INVALIDA.rename(columns={'co_dim_tempo_dum_x': 'co_dim_tempo_dum'})
#     Gestantes_2018_2019_2020_long_INVALIDA['co_dim_tempo_dum'] = pd.to_datetime(Gestantes_2018_2019_2020_long_INVALIDA['co_dim_tempo_dum'], format ='%Y%m%d',errors = 'coerce')

#     """**Identificando a DUM mínima - PDUM**"""

#     df_grouped = Gestantes_2018_2019_2020_long_INVALIDA.groupby(['co_fat_cidadao_pec'])['co_dim_tempo_dum'].min().reset_index()

#     df_grouped_TEST_MIN = df_grouped[df_grouped['co_fat_cidadao_pec']=='1660']

#     """**Identificando a DUM máxima - MDUM**"""

#     df_grouped_max = Gestantes_2018_2019_2020_long_INVALIDA.groupby(['co_fat_cidadao_pec'])['co_dim_tempo_dum'].max().reset_index()

#     df_grouped_TEST_MAX = df_grouped_max[df_grouped_max['co_fat_cidadao_pec']=='1660']

#     df_grouped.rename(columns={'co_dim_tempo_dum': 'PDUM'}, inplace=True)
#     df_grouped_max.rename(columns={'co_dim_tempo_dum': 'MDUM'}, inplace=True)

#     df = df_grouped[df_grouped['co_fat_cidadao_pec'] == '1660']



#     Gestantes_2018_2019_2020_long_INVALIDA = Gestantes_2018_2019_2020_long_INVALIDA.drop(columns=['_merge'])
#     Gestantes_2018_2019_2020_long_PDUM = Gestantes_2018_2019_2020_long_INVALIDA.merge(df_grouped, on='co_fat_cidadao_pec', how='left', indicator=True )

#     Gestantes_2018_2019_2020_long_PDUM = Gestantes_2018_2019_2020_long_PDUM.drop(columns=['_merge'])
#     Gestantes_2018_2019_2020_long_PDUM_MDUM = Gestantes_2018_2019_2020_long_PDUM.merge(df_grouped_max, on='co_fat_cidadao_pec', how='left', indicator=True )


#     Gestantes_2018_2019_2020_long_PDUM_MDUM = Gestantes_2018_2019_2020_long_PDUM_MDUM.sort_values(by='co_dim_tempo')

#     """**Identificando o fim da gestação e o primeiro trimestre**"""

#     Gestantes_2018_2019_2020_long_PDUM_MDUM['PDUM_294'] = Gestantes_2018_2019_2020_long_PDUM_MDUM.PDUM + pd.Timedelta(days=294)
#     Gestantes_2018_2019_2020_long_PDUM_MDUM['PDUM_91'] = Gestantes_2018_2019_2020_long_PDUM_MDUM.PDUM + pd.Timedelta(days=91)
#     Gestantes_2018_2019_2020_long_PDUM_MDUM['Gestacao_N'] = np.where((Gestantes_2018_2019_2020_long_PDUM_MDUM.FILTER == 'INVALIDA'),0,1)

#     Gestantes_2018_2019_2020_long_PDUM_MDUM['co_dim_tempo'] = pd.to_datetime(Gestantes_2018_2019_2020_long_PDUM_MDUM['co_dim_tempo'], format ='%Y%m%d',errors = 'coerce')

#     Gestantes_2018_2019_2020_long_PDUM_MDUM["co_dim_tempo_dum"] = Gestantes_2018_2019_2020_long_PDUM_MDUM.co_dim_tempo_dum.astype(object).where(Gestantes_2018_2019_2020_long_PDUM_MDUM.co_dim_tempo_dum.notnull(), None)
#     Gestantes_2018_2019_2020_long_PDUM_MDUM["co_dim_tempo"] = Gestantes_2018_2019_2020_long_PDUM_MDUM.co_dim_tempo.astype(object).where(Gestantes_2018_2019_2020_long_PDUM_MDUM.co_dim_tempo.notnull(), None)


#     df_test_1660 = Gestantes_2018_2019_2020_long_PDUM_MDUM[Gestantes_2018_2019_2020_long_PDUM_MDUM['co_fat_cidadao_pec']=='1660']

#     Gestantes_2018_2019_2020_long_PDUM_MDUM['co_dim_tempo'] = pd.to_datetime(Gestantes_2018_2019_2020_long_PDUM_MDUM['co_dim_tempo'], format ='%Y-%m-%d', errors='coerce')
#     Gestantes_2018_2019_2020_long_PDUM_MDUM['co_dim_tempo_dum'] = pd.to_datetime(Gestantes_2018_2019_2020_long_PDUM_MDUM['co_dim_tempo_dum'], format ='%Y-%m-%d', errors='coerce')

#     #NEW_DUM
#     def categorise(row):
#         if row['co_dim_tempo_dum'] is pd.NaT and row['co_dim_tempo'] <= row['MDUM']:
#             return row['PDUM']
#         elif row['co_dim_tempo_dum'] is pd.NaT and row['MDUM'] < row['PDUM_91']:
#             return row['PDUM']
#         elif row['co_dim_tempo_dum'] is pd.NaT and row['co_dim_tempo'] > row['PDUM_294']:
#             return row['MDUM']
#         elif row['co_dim_tempo_dum'] is pd.NaT and row['co_dim_tempo'] <= row['PDUM_294']:
#             return row['PDUM']
#         elif row['co_dim_tempo_dum'] is pd.NaT and row['PDUM'] == row['MDUM']:
#             return row['PDUM']
#         elif row['co_dim_tempo_dum'] <= row['PDUM_91']:
#             return row['PDUM']
#         elif row['co_dim_tempo_dum'] > row['PDUM_91']:
#             return row['co_dim_tempo_dum'] 
    
#     Gestantes_2018_2019_2020_long_PDUM_MDUM['NEW_DUM'] = Gestantes_2018_2019_2020_long_PDUM_MDUM.apply(lambda row: categorise(row), axis=1)
#     Gestantes_2018_2019_2020_long_PDUM_MDUM['NEW_DUM'] = pd.to_datetime(Gestantes_2018_2019_2020_long_PDUM_MDUM['NEW_DUM'], format ='%Y-%m-%d', errors='coerce')
#     Gestantes_2018_2019_2020_long_PDUM_MDUM['NEW_DUM_294'] = Gestantes_2018_2019_2020_long_PDUM_MDUM.NEW_DUM + pd.Timedelta(days=294)

#     """**Conforme decidido em reunião, os casos INVÁLIDOS serão desconsiderados da base**"""

#     def gestacoes(row):  
#         if  row['Gestacao_N'] == 0:
#             return 0
#         elif row['NEW_DUM'] == row['PDUM']:
#             return 1
#         elif row['NEW_DUM'] != row['PDUM']:
#             return 2
            
            
#     Gestantes_2018_2019_2020_long_PDUM_MDUM['NEW_Gestacao_N'] = Gestantes_2018_2019_2020_long_PDUM_MDUM.apply(lambda row: gestacoes(row), axis=1)



#     df_test_1660 = Gestantes_2018_2019_2020_long_PDUM_MDUM[Gestantes_2018_2019_2020_long_PDUM_MDUM['co_fat_cidadao_pec']=='1660']

#     null_df = Gestantes_2018_2019_2020_long_PDUM_MDUM[Gestantes_2018_2019_2020_long_PDUM_MDUM['NEW_DUM'].isnull()]
#     null_df_OK = null_df.loc[null_df['FILTER'] != 'INVALIDA']



#     """**Retirando os casos inválidos da base**"""

#     Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA = Gestantes_2018_2019_2020_long_PDUM_MDUM[Gestantes_2018_2019_2020_long_PDUM_MDUM['Gestacao_N'] != 0]

#     # counting unique values - gestantes
#     n = len(pd.unique(Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['co_fat_cidadao_pec']))
    

#     Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['NEW_Gestacao_N'] = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['NEW_Gestacao_N'].astype(str)
#     Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['Chave'] = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA[['co_fat_cidadao_pec','NEW_Gestacao_N']].apply('_'.join, axis=1)

#     df_teste_wsa = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA[Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['co_fat_cidadao_pec']=='1660']

#     # counting unique values - Chave
#     n = len(pd.unique(Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['Chave']))
    

#     df_test = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA[Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['co_fat_cidadao_pec'] == '40482']

#     """### Calculo dos Indices banco novo com as gestações

#     #### INDICADOR 01 (Proporção de gestantes com pelo menos 6 consultas pré-nata(PN))
#     """


#     Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA[Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA.groupby(['co_fat_cidadao_pec','NEW_Gestacao_N'])['co_fat_cidadao_pec'].transform('size') >= 6]

#     # Total de atendimentos com 6 ou mais consultas realizadas


#     Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['co_fat_cidadao_pec'] = Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['co_fat_cidadao_pec'].astype(str).astype(float).astype(int)
#     Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['nu_idade_gestacional_semanas'] = pd.to_numeric(Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['nu_idade_gestacional_semanas'])
#     Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED[Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['co_fat_cidadao_pec'] == 7029]

#     """**Completando a idade gestacional a partir da NEW_DUM**"""

#     Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['NEW_DUM'] = pd.to_datetime(Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['NEW_DUM'], format ='%Y-%m-%d', errors='coerce')
#     Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['co_dim_tempo'] = pd.to_datetime(Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['co_dim_tempo'], format ='%Y-%m-%d', errors='coerce')
#     Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['Difference'] = (Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['co_dim_tempo'] - Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['NEW_DUM']).dt.days
#     Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['semanas_diff'] = Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['Difference'] / 7

#     def ig(row):  
#         if row['nu_idade_gestacional_semanas'] >= 0:
#             return row['nu_idade_gestacional_semanas']
#         else:
#             return row['semanas_diff']
    
#     Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['IG'] = Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED.apply(lambda row: ig(row), axis=1)



#     df = Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED[Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['Chave'] == '10244_1']

#     """Total de gestações com 6 ou mais consultas - 886 ok"""

#     # counting unique values - Chave
#     n = len(pd.unique(Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED['Chave']))
    

#     test_final = Gestantes_2018_2019_2020_long_PDUM_MDUM_PRENATAL_FILTERED.groupby('Chave').agg(IG = ('IG', 'min')).reset_index()



#     df = test_final[test_final['Chave'] == '10244_1']

#     final_result = test_final.loc[test_final['IG'] <= 20.0]

#     final_result['consultas_6_prenatal'] = True

#     final_result_Prenatal = final_result[['Chave','consultas_6_prenatal']]




#     final_result_Prenatal_merge = final_result_Prenatal.merge(Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA, how='right', on='Chave', indicator='exists' )


#     df = final_result_Prenatal_merge[final_result_Prenatal_merge['Chave'] == '10244_1']


#     """#### INDICADOR 02 (Proporção de gestantes com realização de exames para sífilis e HIV) 1421"""



#     # create regex pattern out of the list of words
#     positive = '|'.join(['0202031110','ABEX019','0202030300','ABEX018','0202031179','0214010074','ABPG026','0214010082','0214010058','ABPG024','0214010040'])

#     Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['POSITIVE_proced_avaliados'] = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['ds_filtro_proced_avaliados'].str.contains(positive)

#     Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA.loc[Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['POSITIVE_proced_avaliados'] == True]


#     Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL = Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL.astype(str)


#     df = Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL[Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL['co_fat_cidadao_pec'] == '40368']

#     Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL_PIVOTED = Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL.groupby(['Chave']).agg({'co_dim_unidade_saude_1':','.join, 
#                                                                                     'co_dim_equipe_1':','.join, 
#                                                                                     'co_dim_tempo':','.join, 
#                                                                                     'dt_nascimento':','.join, 
#                                                                                     'nu_peso':','.join, 
#                                                                                     'nu_altura':','.join, 
#                                                                                     'st_vacinacao_em_dia':','.join, 
#                                                                                     'co_dim_tempo_dum':','.join, 
#                                                                                     'st_gravidez_planejada':','.join, 
#                                                                                     'nu_idade_gestacional_semanas':','.join, 
#                                                                                     'nu_gestas_previas':','.join, 
#                                                                                     'nu_partos':','.join, 
#                                                                                     'ds_filtro_cids':','.join, 
#                                                                                     'ds_filtro_ciaps':','.join, 
#                                                                                     'ds_filtro_proced_avaliados':','.join, 
#                                                                                     'ds_filtro_proced_solicitados': ','.join,
#                                                                                     'NEW_DUM': ','.join,
#                                                                                     'NEW_DUM_294': ','.join,
#                                                                                     'POSITIVE_proced_avaliados': ','.join,}).reset_index()



#     Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL_PIVOTED['exames_para_sifilis_HIV'] = Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL_PIVOTED['POSITIVE_proced_avaliados'].str.split(',').str[0]

#     final_result_sifilis_hiv = Gestantes_2018_2019_2020_long_PDUM_MDUM_WIDE_FINAL_PIVOTED[['Chave','exames_para_sifilis_HIV']]


#     final_result_Prenatal_sifilis_hiv_merge = final_result_sifilis_hiv.merge(final_result_Prenatal_merge, how='right', on='Chave', indicator='exists_2' )



#     """#### INDICADOR 03 (Proporção de gestantes com atendimento odontológico realizado)"""


#     df = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA[Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA['co_fat_cidadao_pec'] == '49089']

#     Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA.astype(str)

#     Gestantes_2018_2019_2020_long_PDUM_MDUM_FINAL_PIVOTED = Gestantes_2018_2019_2020_long_PDUM_MDUM_VALIDA.groupby(['co_fat_cidadao_pec','NEW_Gestacao_N']).agg({'co_dim_unidade_saude_1':','.join, 
#                                                                                     'co_dim_equipe_1':','.join, 
#                                                                                     'co_dim_tempo':','.join, 
#                                                                                     'dt_nascimento':','.join, 
#                                                                                     'nu_peso':','.join, 
#                                                                                     'nu_altura':','.join, 
#                                                                                     'st_vacinacao_em_dia':','.join, 
#                                                                                     'co_dim_tempo_dum':','.join, 
#                                                                                     'st_gravidez_planejada':','.join, 
#                                                                                     'nu_idade_gestacional_semanas':','.join, 
#                                                                                     'nu_gestas_previas':','.join, 
#                                                                                     'nu_partos':','.join, 
#                                                                                     'ds_filtro_cids':','.join, 
#                                                                                     'ds_filtro_ciaps':','.join, 
#                                                                                     'ds_filtro_proced_avaliados':','.join, 
#                                                                                     'ds_filtro_proced_solicitados': ','.join,
#                                                                                     'NEW_DUM': ','.join,
#                                                                                     'NEW_DUM_294': ','.join,
#                                                                                     'Chave': ','.join}).reset_index()



#     df = Gestantes_2018_2019_2020_long_PDUM_MDUM_FINAL_PIVOTED[Gestantes_2018_2019_2020_long_PDUM_MDUM_FINAL_PIVOTED['co_fat_cidadao_pec'] == '10715']

#     Odonto_2018_2019_2020 = pd.read_csv( path + '/tb_fat_atendimento_odonto.csv',sep=';',engine='python', decimal = ',')

#     Odonto_2018_2019_2020['co_dim_tempo'] = pd.to_datetime(Odonto_2018_2019_2020['co_dim_tempo'], format ='%Y%m%d')
#     Odonto_2018_2019_2020 = Odonto_2018_2019_2020.astype(str)
#     Odonto_2018_2019_2020_PIVOTED = Odonto_2018_2019_2020.groupby('co_fat_cidadao_pec').agg({'co_dim_tempo':','.join}).reset_index()

#     Odonto_2018_2019_2020_PIVOTED['co_fat_cidadao_pec'] = Odonto_2018_2019_2020_PIVOTED['co_fat_cidadao_pec'].str[:-2]

#     #NOVO METODO DE GESTACAO 2N
#     Linkage_2018_2019_2020_Gestante_Odoto = Gestantes_2018_2019_2020_long_PDUM_MDUM_FINAL_PIVOTED.merge(Odonto_2018_2019_2020_PIVOTED, on='co_fat_cidadao_pec', how='left', indicator=True )

#     Linkage_2018_2019_2020_Gestante_Odoto_YES = Linkage_2018_2019_2020_Gestante_Odoto.loc[Linkage_2018_2019_2020_Gestante_Odoto['_merge'] == 'both']

#     Linkage_2018_2019_2020_Gestante_Odoto_YES['Chave'] = Linkage_2018_2019_2020_Gestante_Odoto_YES['Chave'].str.split(',').str[0]

#     """Merge ok com 491"""

#     Linkage_2018_2019_2020_Gestante_Odoto_YES = Linkage_2018_2019_2020_Gestante_Odoto_YES.rename(columns={'co_dim_tempo_x': 'co_dim_tempo_Gestante'})
#     Linkage_2018_2019_2020_Gestante_Odoto_YES = Linkage_2018_2019_2020_Gestante_Odoto_YES.rename(columns={'co_dim_tempo_y': 'co_dim_tempo_Odonto'})
#     Linkage_2018_2019_2020_Gestante_Odoto_YES = Linkage_2018_2019_2020_Gestante_Odoto_YES[['co_fat_cidadao_pec','NEW_Gestacao_N','co_dim_tempo_Gestante','co_dim_tempo_Odonto','NEW_DUM','Chave']]

#     df1 = Linkage_2018_2019_2020_Gestante_Odoto_YES['NEW_DUM'].str.split(',', expand=True).astype(str)
#     df1 = df1.apply(pd.to_datetime,errors='coerce')
#     df = Linkage_2018_2019_2020_Gestante_Odoto_YES.assign(DUM=df1.max(axis=1,skipna=True))



#     df_test = df[df['co_fat_cidadao_pec'] == '40755']


#     df['DUM_294'] = df.DUM.apply( lambda x: x+ pd.Timedelta(days=294))
#     df['DUM_MEN_71'] = df.DUM.apply( lambda x: x - pd.Timedelta(days=71))
#     df['DUM__MEN_365'] = df.DUM.apply( lambda x: x- pd.Timedelta(days=365))

#     df2 = df['co_dim_tempo_Odonto'].str.split(',', expand=True).astype(str)
#     df2 = df2.apply(pd.to_datetime,errors='coerce')
#     df_FINAL = df.assign(minyear_Odonto=df2.min(axis=1,skipna=True),maxyear_Odonto=df2.max(axis=1,skipna=True))

#     df_test = df_FINAL[df_FINAL['co_fat_cidadao_pec'] == '40755']


#     df_string = df_FINAL.astype(str)


#     df_string['minyear_Odonto'] = pd.to_datetime(df_string['minyear_Odonto'], format ='%Y-%m-%d')
#     df_string['DUM'] = pd.to_datetime(df_string['DUM'], format ='%Y-%m-%d')
#     df_string['maxyear_Odonto'] = pd.to_datetime(df_string['maxyear_Odonto'], format ='%Y-%m-%d')
#     df_string['DUM_294'] = pd.to_datetime(df_string['DUM_294'], format ='%Y-%m-%d')
#     df_string['DUM_MEN_71'] = pd.to_datetime(df_string['DUM_MEN_71'], format ='%Y-%m-%d')
#     df_string['DUM__MEN_365'] = pd.to_datetime(df_string['DUM__MEN_365'], format ='%Y-%m-%d')


#     df_string['STRICTED'] = np.where((df_string.minyear_Odonto >= df_string.DUM)&(df_string.maxyear_Odonto <= df_string.DUM_294),1,0)
#     df_string['RAZOAVEL'] = np.where((df_string.minyear_Odonto >= df_string.DUM_MEN_71)&(df_string.maxyear_Odonto <= df_string.DUM_294),1,0)
#     df_string['AMPLO'] = np.where((df_string.minyear_Odonto >= df_string.DUM__MEN_365)&(df_string.maxyear_Odonto <= df_string.DUM_294),1,0)

#     df_test = df_string[df_string['co_fat_cidadao_pec'] == '40755']


#     total = df_string['STRICTED'].sum()
#     total_R = df_string['RAZOAVEL'].sum()
#     total_A = df_string['AMPLO'].sum()

#     FINAL_RESULTS = df_string.merge(final_result_Prenatal_sifilis_hiv_merge, how='right', on='Chave', indicator='exists_3' )





#     """### Exportando para excel FINAL DATABASE GESTAÇÔES"""

#     FINAL_RESULTS.to_parquet( path + '/BASE_GESTACOES_3_INDICADORES.parquet')