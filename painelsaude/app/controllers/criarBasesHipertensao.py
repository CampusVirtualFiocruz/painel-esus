import pandas as pd
import numpy as np

def criarBasesHipertensao( path ):

    cadastro_mestre = pd.read_excel(path + '/CADASTRO_MESTRE_JOIN_AT_IND_GEST_HIP_DIAB_JOIN_UNIDADES_CLEAN_PAINEL.xlsx')

    tb_fat_at_ind_2018_2019_2020 = pd.read_csv(path + '/tb_fat_atendimento_individual.csv',sep=';',engine='python', decimal = ',',keep_default_na=False)

    Cbo = pd.read_csv(path + '/tb_dim_cbo.csv',sep=';',engine='python', decimal = ',',keep_default_na=False)
 
    tb_fat_at_ind_2018_2019_2020['co_fat_cidadao_pec'] = tb_fat_at_ind_2018_2019_2020['co_fat_cidadao_pec'].astype(str).str[:-2]
    """### Overview of the Dataset, first 5 rows"""

    tb_fat_at_ind_2018_2019_2020_SELECTED = tb_fat_at_ind_2018_2019_2020[['co_fat_cidadao_pec','co_dim_unidade_saude_1','co_dim_equipe_1','co_dim_cbo_1','co_dim_tempo','dt_nascimento','nu_peso','nu_altura','ds_filtro_cids','ds_filtro_ciaps','ds_filtro_proced_avaliados', 
                                                                        'ds_filtro_proced_solicitados']]


    cadastro_mestre = cadastro_mestre[['co_fat_cidadao_pec','co_unidade_saude','ds_tipo_localizacao','ds_sexo','nu_idade','ds_faixa_etaria','nu_cnes']]
    cadastro_mestre['nu_cnes'] = cadastro_mestre['nu_cnes'].astype(str).str[:-2]
    

    """### Linkage between cadastro & Atendimento"""

    cadastro_mestre['co_fat_cidadao_pec'] = cadastro_mestre['co_fat_cidadao_pec'].astype(str)
    tb_fat_at_ind_2018_2019_2020_SELECTED = tb_fat_at_ind_2018_2019_2020_SELECTED.merge(cadastro_mestre, on='co_fat_cidadao_pec', how='left', indicator=True)

    """### Linkage between cadastro & Atendimento & CBO"""

    Cbo = Cbo[['co_seq_dim_cbo','nu_cbo']]
    tb_fat_at_ind_2018_2019_2020_SELECTED = tb_fat_at_ind_2018_2019_2020_SELECTED.drop(columns=['_merge'])
    tb_fat_at_ind_2018_2019_2020_SELECTED = tb_fat_at_ind_2018_2019_2020_SELECTED.rename(columns={'co_dim_cbo_1': 'co_seq_dim_cbo'})
    tb_fat_at_ind_2018_2019_2020_SELECTED = tb_fat_at_ind_2018_2019_2020_SELECTED.merge(Cbo, on='co_seq_dim_cbo', how='left', indicator=True)

    """### Filter CID / CIAP HIPERTENSÂO

    **Identificando atendimentos relacionados a hipertensão pelo CID/CIAP**
    """

    #DIABETICOS
    '''
    match = ['T89','T90','W85','E10','E100','E101','E102','E103','E104','E105','E106','E107','E108','E109','E11','E110','E111','E112','E113','E114','E115','E116','E117','E118','E119','E12','E120',
            'E121','E122','E123','E124','E125','E126','E127','E128','E129','E13','E130','E131','E132','E133','E134','E135','E136','E137','E138','E139','E14','E140','E141','E142','E143','E144','E145',
            'E146','E147','E148','E149','O24','O240','O241','O242','O243','O244','O249','P702','ABP006']

    def string_finder(row, words):
        if any(word in field for field in row for word in words):
            return True
        return False

    gestante_SELECTED_FINAL['isContained_DIABETE'] = gestante_SELECTED_FINAL.astype(str).apply(string_finder, words=match, axis=1)
    '''

    match = ['K86','K87','W81','I10','I11','I110','I119','I12','I120','I129','I13','I130','I131','I132','I139','I15','I150','I151','I152','I158','I159','I270','I272','O10','O100','O101','O102','O103',
            'O104','O109','ABP005']

    #match = ['F83','H360','I64','I12','I129','I13','I130','I131','I132','I139','N083','N179','N18','N180','N188','N189','N19','U14','U99','U88','U90','I24','I248','I249','I25','I251','I258','I259','I518', 
    #         'I519','I110','I119','I130','I132','I50','I500','I509','G46','G468','I67','I678','I679','I68','I688','I69','I699']

    def string_finder(row, words):
        if any(word in field for field in row for word in words):
            return True
        return False

    tb_fat_at_ind_2018_2019_2020_SELECTED['isContained_HIPERTENSAO'] = tb_fat_at_ind_2018_2019_2020_SELECTED.astype(str).apply(string_finder, words=match, axis=1)

    # Atendimentos identificamos pelo CID ou CIAP PN
    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO = tb_fat_at_ind_2018_2019_2020_SELECTED[(tb_fat_at_ind_2018_2019_2020_SELECTED['isContained_HIPERTENSAO'] == True)]


    """### DS AGRAVO"""

    match = ['I21', 'I210', 'I211','I212', 'I213', 'I214', 'I219']

    def string_finder(row, words):
        if any(word in field for field in row for word in words):
            return True
        return False

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['ds_agravo_1'] = tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO.astype(str).apply(string_finder, words=match, axis=1)

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_nom_1"] = np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_1"] == True, 'Infarto Agudo do Miocárdio', '')
    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_cod_1"] = np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_1"] == True, 'I21, I210, I211,I212, I213, I214, I219', '')


    match = ['I64']

    def string_finder(row, words):
        if any(word in field for field in row for word in words):
            return True
        return False

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['ds_agravo_2'] = tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO.astype(str).apply(string_finder, words=match, axis=1)

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_nom_2"] = np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_2"] == True, 'Acidente Vascular Encefálico', '')
    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_cod_2"] = np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_2"] == True, 'I64', '')

    match = ['I12','I129','I13','I130','I131','I132','I139','N083','N179','N18','N180','N188','N189','N19','​​U14','U99','U88','U90']

    def string_finder(row, words):
        if any(word in field for field in row for word in words):
            return True
        return False

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['ds_agravo_3'] = tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO.astype(str).apply(string_finder, words=match, axis=1)

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_nom_3"] = np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_3"] == True, 'Doença renal', '')
    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_cod_3"] = np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_3"] == True, 'I12,I129,I13,I130,I131,I132,I139,N083,N179,N18,N180,N188,N189,N19,​​U14,U99,U88,U90', '')

    match = ['I24','I248','I249','I25','I251','I258','I259','I518','I519','I110','I119','I130','I132','I50','I500','I509']

    def string_finder(row, words):
        if any(word in field for field in row for word in words):
            return True
        return False

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['ds_agravo_4'] = tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO.astype(str).apply(string_finder, words=match, axis=1)

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_nom_4"] = np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_4"] == True, 'Doença Coronariana', '')
    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_cod_4"] = np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_4"] == True, 'I24,I248,I249,I25,I251,I258,I259,I518,I519,I110,I119,I130,I132,I50,I500,I509', '')

    match = ['G46','G468','I67','I678','I679','I68','I688','I69','I699']

    def string_finder(row, words):
        if any(word in field for field in row for word in words):
            return True
        return False

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['ds_agravo_5'] = tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO.astype(str).apply(string_finder, words=match, axis=1)

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_nom_5"] = np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_5"] == True, 'Doença Cerebrovascular', '')
    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_cod_5"] = np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO["ds_agravo_5"] == True, 'G46,G468,I67,I678,I679,I68,I688,I69,I699', '')

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['ds_agravo_FINAL_NOM'] = tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['ds_agravo_nom_1'] + ',' +\
                                                                            tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['ds_agravo_nom_2'] + ',' +\
                                                                            tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['ds_agravo_nom_3'] + ',' +\
                                                                            tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['ds_agravo_nom_4'] + ',' +\
                                                                            tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['ds_agravo_nom_5']

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['ds_agravo_FINAL_COD'] = tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['ds_agravo_cod_1'] + ',' +\
                                                                            tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['ds_agravo_cod_2'] + ',' +\
                                                                            tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['ds_agravo_cod_3'] + ',' +\
                                                                            tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['ds_agravo_cod_4'] + ',' +\
                                                                            tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['ds_agravo_cod_5']



    """### IDADE 01"""

    def age_group(row):
        if row['nu_idade'] >= 0 and row['nu_idade'] <=17:
            return "Faixa 1"
        elif row['nu_idade'] >= 18 and row['nu_idade'] <=29:
            return "Faixa 2"
        elif row['nu_idade'] >= 30 and row['nu_idade'] <=44:
            return "Faixa 3"
        elif row['nu_idade'] >= 45 and row['nu_idade'] <=59:
            return "Faixa 4"
        elif row['nu_idade'] >= 60:
            return "Faixa 5"
        else:
            return "NaN"

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['FAIXA_ETARIA_HIPERTENSO'] = tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO.apply (lambda row: age_group(row), axis=1)


    """### CBO PROFISSIONAL"""

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['CBO_PROFISSIONAL'] = np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_cbo'].str.startswith("225", na=False), 'MÉDICOS', 
                                                                            (np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_cbo'].str.startswith("2232", na=False), 'CIRURGIÕES-DENTISTAS',
                                                                            (np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_cbo'].str.startswith("2234", na=False), 'FARMACÊUTICOS',
                                                                            (np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_cbo'].str.startswith("2236", na=False), 'FISIOTERAPEUTAS',
                                                                            (np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_cbo'].str.startswith("2237", na=False), 'NUTRICIONISTAS',
                                                                            (np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_cbo'].str.startswith("2238", na=False), 'FONOAUDIÓLOGOS',
                                                                            (np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_cbo'].str.startswith("2239", na=False), 'TERAPEUTAS OCUPACIONAIS',
                                                                            (np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_cbo'].str.startswith("2241", na=False), 'EDUCAÇÃO FÍSICA',
                                                                            (np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_cbo'].str.startswith("2263", na=False), 'INTEGRATIVA E COMPLEMENTAR',
                                                                            (np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_cbo'].str.startswith("2515", na=False), 'PSCICÓLOGO',
                                                                            (np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_cbo'].str.startswith("2516", na=False), 'ASSITENTE SOCIAL',
                                                                            (np.where(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_cbo'].str.startswith("2235", na=False), 'ENFERMEIROS', 'OUTRO')))))))))))))))))))))))


    """### GROP BY CO_FAT_PEC 1 LINHA 1 PACIENTE"""

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO.dtypes


    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO = tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO.drop(columns=['_merge','isContained_HIPERTENSAO','ds_faixa_etaria','ds_agravo_1','ds_agravo_2','ds_agravo_3','ds_agravo_4','ds_agravo_5'])
    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO = tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO.astype(str)
    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO = tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO.groupby(['co_fat_cidadao_pec']).agg({'co_dim_unidade_saude_1':','.join, 
                                                                                    'co_dim_equipe_1':','.join, 
                                                                                    'co_dim_tempo':','.join, 
                                                                                    'dt_nascimento':','.join, 
                                                                                    'nu_peso':','.join, 
                                                                                    'nu_altura':','.join, 
                                                                                    'co_seq_dim_cbo':','.join, 
                                                                                    'ds_filtro_cids':','.join, 
                                                                                    'ds_filtro_ciaps':','.join, 
                                                                                    'ds_filtro_proced_avaliados':','.join, 
                                                                                    'ds_filtro_proced_solicitados': ','.join,
                                                                                    'co_unidade_saude': ','.join,
                                                                                    'ds_tipo_localizacao': ','.join,
                                                                                    'ds_sexo': ','.join,
                                                                                    'nu_idade': ','.join,
                                                                                    'nu_cbo': ','.join,
                                                                                    'nu_cnes': ','.join,
                                                                                    'FAIXA_ETARIA_HIPERTENSO': ','.join,
                                                                                    'ds_agravo_FINAL_NOM': ','.join,
                                                                                    'ds_agravo_FINAL_COD': ','.join,
                                                                                    'CBO_PROFISSIONAL': ','.join,}).reset_index()

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO.dtypes

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO = tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO.replace(r'^s*$', float('NaN'), regex = True) 
    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO.dropna(subset = ["co_fat_cidadao_pec"], inplace=True)

    """### Take Last Peso & Altura for Calculating IMC"""

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_peso_last'] = tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_peso'].str.split(',').str[-1]
    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_altura_last'] = tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_altura'].str.split(',').str[-1]

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_peso_last'] = pd.to_numeric(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_peso_last'],errors='coerce')
    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_altura_last'] = pd.to_numeric(tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_altura_last'],errors='coerce')

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_altura_last_M'] = tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_altura_last'] /100

    """### IMC = peso (kg)/ (altura (m))²"""

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['IMC'] = tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_peso_last'] / (tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_altura_last_M']*tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['nu_altura_last_M'])


    def IMC(row):
        if row['IMC'] <= 18.5:
            return "Baixo Peso"
        elif row['IMC'] > 18.5 and row['IMC'] <=24.9:
            return "Normal"
        elif row['IMC'] >= 25 and row['IMC'] <=29.9:
            return "Excesso de Peso"
        elif row['IMC'] >= 30:
            return "Obesidade"
        else:
            return "OUTROS"

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO['IMC_FINAL'] = tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO.apply (lambda row: IMC(row), axis=1)


    """### Exportando para excel FINAL DATABASE HIPERTENSÂO"""

    tb_fat_at_ind_2018_2019_2020_SELECTED_HIPERTENSAO.to_excel( path + '/BASE_ATENDIMENTOS_X_HIPERTENSAO.xlsx')