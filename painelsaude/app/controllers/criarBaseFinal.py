# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

import math
import gc


def criarBaseFinal(path):

    cadastro_mestre = pd.read_csv(path + '/CADASTRO_MESTRE_PESSOAS.csv')
    if cadastro_mestre.shape[0] == 0:
        return

    tb_fat_at_ind_2018_2019_2020 = pd.read_csv(
        path + '/tb_fat_atendimento_individual.csv', sep=';', engine='python', decimal=',', keep_default_na=False)

    unidades = pd.read_csv(path + '/tb_dim_unidade_saude.csv',
                           sep=';', engine='python', decimal=',', keep_default_na=False)

    municipio = pd.read_csv(path + '/tb_dim_municipio.csv', sep=';',
                            engine='python', decimal=',', keep_default_na=False)
    municipio['co_dim_uf'] = municipio['co_dim_uf'].astype(str).str[:-2]

    cadastro_mestre_SELECTED = cadastro_mestre[['co_fat_cidadao_pec', 'co_dim_municipio_CI',
                                                'co_dim_unidade_saude_CI', 'co_dim_tipo_localizacao', 'CO_DIM_SEXO', 'DT_NASCIMENTO',  'no_cidadao', 'nu_idade']]

    """###Atendimento Individual"""

    def change_string(x):
        return x.replace('ABP009', 'R96').replace("ABP019", "A77").replace('ABP008', 'T91').replace('ABP006', 'T90').replace('ABP010', 'R95').replace('ABP020', 'A78').replace('ABP018', 'A78').replace('ABP005', 'K86').replace('ABP007', 'T82').replace('ABP001', 'W78').replace('ABP004', 'A98').replace('ABP002', 'W18').replace('ABP024', 'K22').replace('ABP015', '57').replace('ABP011', 'P17').replace('ABP017', 'A70').replace('ABP012', 'P16').replace('ABP013', 'P19')
    tb_fat_at_ind_2018_2019_2020["ds_filtro_ciaps"] = tb_fat_at_ind_2018_2019_2020["ds_filtro_ciaps"].map(
        lambda x: change_string(x))

    tb_fat_at_ind_2018_2019_2020['st_ficou_em_observacao'] = np.where(
        tb_fat_at_ind_2018_2019_2020.st_ficou_em_observacao == '1', '-30', '')
    tb_fat_at_ind_2018_2019_2020['st_encaminhamento_intern_hospi'] = np.where(
        tb_fat_at_ind_2018_2019_2020.st_encaminhamento_intern_hospi == 1, '-67', '')
    tb_fat_at_ind_2018_2019_2020['st_encaminhamento_urgencia'] = np.where(
        tb_fat_at_ind_2018_2019_2020.st_encaminhamento_urgencia == 1, '-67', '')
    tb_fat_at_ind_2018_2019_2020['st_gravidez_planejada'] = np.where(
        tb_fat_at_ind_2018_2019_2020.st_gravidez_planejada == '1', 'W99', '')
    tb_fat_at_ind_2018_2019_2020['st_nasf_avaliacao_diagnostico'] = np.where(
        tb_fat_at_ind_2018_2019_2020.st_nasf_avaliacao_diagnostico == 1, '-66', '')
    tb_fat_at_ind_2018_2019_2020['st_encaminhamento_interno_dia'] = np.where(
        tb_fat_at_ind_2018_2019_2020.st_encaminhamento_interno_dia == 1, '-46', '')
    tb_fat_at_ind_2018_2019_2020['st_encaminhamento_intersetoria'] = np.where(
        tb_fat_at_ind_2018_2019_2020.st_encaminhamento_intersetoria == 1, '-62', '')

    tb_fat_at_ind_2018_2019_2020['CIAP'] = tb_fat_at_ind_2018_2019_2020[['st_ficou_em_observacao', 'st_encaminhamento_intern_hospi', 'st_encaminhamento_urgencia', 'st_gravidez_planejada', 'st_nasf_avaliacao_diagnostico',
                                                                        'st_encaminhamento_interno_dia', 'st_encaminhamento_intersetoria']].agg('|'.join, axis=1)

    tb_fat_at_ind_2018_2019_2020_CIAP = tb_fat_at_ind_2018_2019_2020.drop(columns=['st_ficou_em_observacao', 'st_encaminhamento_intern_hospi', 'st_encaminhamento_urgencia', 'st_gravidez_planejada',
                                                                                   'st_nasf_avaliacao_diagnostico', 'st_encaminhamento_interno_dia', 'st_encaminhamento_intersetoria'])

    tb_fat_at_ind_2018_2019_2020_CIAP = tb_fat_at_ind_2018_2019_2020_CIAP.rename(
        columns={'co_dim_municipio': 'co_dim_municipio_AI'})
    tb_fat_at_ind_2018_2019_2020_CIAP = tb_fat_at_ind_2018_2019_2020_CIAP.rename(
        columns={'co_dim_tipo_ficha': 'co_dim_tipo_ficha_AI'})
    tb_fat_at_ind_2018_2019_2020_CIAP = tb_fat_at_ind_2018_2019_2020_CIAP.rename(
        columns={'co_dim_tempo': 'co_dim_tempo_AI'})
    tb_fat_at_ind_2018_2019_2020_CIAP = tb_fat_at_ind_2018_2019_2020_CIAP.rename(
        columns={'nu_uuid_ficha': 'nu_uuid_ficha_AI'})
    tb_fat_at_ind_2018_2019_2020_CIAP = tb_fat_at_ind_2018_2019_2020_CIAP.rename(
        columns={'dt_nascimento': 'dt_nascimento_AI'})
    tb_fat_at_ind_2018_2019_2020_CIAP = tb_fat_at_ind_2018_2019_2020_CIAP.rename(
        columns={'co_dim_faixa_etaria': 'co_dim_faixa_etaria_AI'})
    tb_fat_at_ind_2018_2019_2020_CIAP = tb_fat_at_ind_2018_2019_2020_CIAP.rename(
        columns={'co_dim_sexo': 'co_dim_sexo_AI'})
    tb_fat_at_ind_2018_2019_2020_CIAP = tb_fat_at_ind_2018_2019_2020_CIAP.rename(
        columns={'nu_peso': 'nu_peso_AI'})
    tb_fat_at_ind_2018_2019_2020_CIAP = tb_fat_at_ind_2018_2019_2020_CIAP.rename(
        columns={'nu_altura': 'nu_altura_AI'})
    tb_fat_at_ind_2018_2019_2020_CIAP = tb_fat_at_ind_2018_2019_2020_CIAP.rename(
        columns={'nu_prontuario': 'nu_prontuario_AI'})
    tb_fat_at_ind_2018_2019_2020_CIAP = tb_fat_at_ind_2018_2019_2020_CIAP.rename(
        columns={'CIAP': 'CIAP_AI'})

    tb_fat_at_ind_2018_2019_2020_CIAP = tb_fat_at_ind_2018_2019_2020_CIAP[['co_fat_cidadao_pec', 'co_dim_municipio_AI', 'co_dim_unidade_saude_1', 'co_dim_unidade_saude_2', 'co_dim_tempo_AI', 'dt_nascimento_AI',
                                                                           'co_dim_tempo_dum', 'nu_idade_gestacional_semanas', 'nu_gestas_previas', 'st_vacinacao_em_dia', 'ds_filtro_proced_avaliados',
                                                                           'ds_filtro_proced_solicitados', 'ds_filtro_cids', 'ds_filtro_ciaps', 'co_dim_sexo_AI', 'CIAP_AI']]

    tb_fat_at_ind_2018_2019_2020_CIAP['co_dim_tempo_AI'] = tb_fat_at_ind_2018_2019_2020_CIAP['co_dim_tempo_AI'].astype(
        str)
    tb_fat_at_ind_2018_2019_2020_CIAP['cad_proced_solicitados'] = tb_fat_at_ind_2018_2019_2020_CIAP[[
        'co_dim_tempo_AI', 'ds_filtro_proced_solicitados']].agg(':'.join, axis=1)
    tb_fat_at_ind_2018_2019_2020_CIAP['cad_proced_avaliados'] = tb_fat_at_ind_2018_2019_2020_CIAP[[
        'co_dim_tempo_AI', 'ds_filtro_proced_avaliados']].agg(':'.join, axis=1)

    tb_fat_at_ind_2018_2019_2020_CIAP = tb_fat_at_ind_2018_2019_2020_CIAP.astype(
        str)
    tb_fat_at_ind_2018_2019_2020_CIAP['CIAP_AI'] = tb_fat_at_ind_2018_2019_2020_CIAP['CIAP_AI'].apply(
        str).str.replace('None', '')
    tb_fat_at_ind_2018_2019_2020_CIAP['CIAP_AI_COMB'] = tb_fat_at_ind_2018_2019_2020_CIAP[[
        'ds_filtro_ciaps', 'CIAP_AI']].agg(','.join, axis=1).astype(str)
    pivot_at_ind_2018_2019_2020_CIAP = tb_fat_at_ind_2018_2019_2020_CIAP.groupby('co_fat_cidadao_pec').agg({'co_dim_municipio_AI': ','.join,
                                                                                                            'co_dim_unidade_saude_1': ','.join,
                                                                                                            'co_dim_unidade_saude_2': ','.join,
                                                                                                            'co_dim_tempo_AI': ','.join,
                                                                                                            'dt_nascimento_AI': ','.join,
                                                                                                            'co_dim_sexo_AI': ','.join,
                                                                                                            'co_dim_tempo_dum': ','.join,
                                                                                                            'nu_idade_gestacional_semanas': ','.join,
                                                                                                            'nu_gestas_previas': ','.join,
                                                                                                            'st_vacinacao_em_dia': ','.join,
                                                                                                            'cad_proced_solicitados': ','.join,
                                                                                                            'cad_proced_avaliados': ','.join,
                                                                                                            'ds_filtro_cids': ','.join,
                                                                                                            'CIAP_AI_COMB': ','.join}).reset_index()

    pivot_at_ind_2018_2019_2020_CIAP['co_fat_cidadao_pec'] = pivot_at_ind_2018_2019_2020_CIAP['co_fat_cidadao_pec'].str[:-2]
    cadastro_mestre_SELECTED['co_fat_cidadao_pec'] = cadastro_mestre_SELECTED['co_fat_cidadao_pec'].astype(
        str)
    MESTRE_JOIN_PIVOT_AT_IND = cadastro_mestre_SELECTED.merge(
        pivot_at_ind_2018_2019_2020_CIAP, on='co_fat_cidadao_pec', how='left', indicator=True)
    # print( cadastro_mestre_SELECTED['co_fat_cidadao_pec'] )
    # print(pivot_at_ind_2018_2019_2020_CIAP['co_fat_cidadao_pec'])
    # exit()
    del cadastro_mestre
    del pivot_at_ind_2018_2019_2020_CIAP

    match = ['K86', 'K87', 'W81', 'I10', 'I11', 'I110', 'I119', 'I12', 'I120', 'I129', 'I13', 'I130', 'I131', 'I132', 'I139', 'I15', 'I150', 'I151', 'I152', 'I158', 'I159', 'I270', 'I272', 'O10', 'O100', 'O101', 'O102', 'O103',
             'O104', 'O109', 'ABP005']

    def string_finder(row, words):
        if any(word in field for field in row for word in words):
            return True
        return False

    MESTRE_JOIN_PIVOT_AT_IND['isContained_HIPERTENSAO'] = MESTRE_JOIN_PIVOT_AT_IND.astype(
        str).apply(string_finder, words=match, axis=1)

    match = ['T89', 'T90', 'W85', 'E10', 'E100', 'E101', 'E102', 'E103', 'E104', 'E105', 'E106', 'E107', 'E108', 'E109', 'E11', 'E110', 'E111', 'E112', 'E113', 'E114', 'E115', 'E116', 'E117', 'E118', 'E119', 'E12', 'E120',
             'E121', 'E122', 'E123', 'E124', 'E125', 'E126', 'E127', 'E128', 'E129', 'E13', 'E130', 'E131', 'E132', 'E133', 'E134', 'E135', 'E136', 'E137', 'E138', 'E139', 'E14', 'E140', 'E141', 'E142', 'E143', 'E144', 'E145',
             'E146', 'E147', 'E148', 'E149', 'O24', 'O240', 'O241', 'O242', 'O243', 'O244', 'O249', 'P702', 'ABP006']

    def string_finder(row, words):
        if any(word in field for field in row for word in words):
            return True
        return False

    MESTRE_JOIN_PIVOT_AT_IND['isContained_DIABETE'] = MESTRE_JOIN_PIVOT_AT_IND.astype(
        str).apply(string_finder, words=match, axis=1)

    match = ['W03', 'W05', 'W71', 'W78', 'W79', 'W80', 'W81', 'W84', 'W85', 'ABP001', 'O11', 'O12', 'O120', 'O121', 'O122', 'O13', 'O14', 'O140', 'O141', 'O149', 'O15', 'O150', 'O151', 'O159', 'O16', 'O20', 'O200', 'O2O8', 'O2O9', 'O21', 'O210',
             'O211', 'O212', 'O218', 'O219', 'O22', 'O220', 'O221', 'O222', 'O223', 'O224', 'O225', 'O228', 'O229', 'O23', 'O230', 'O231', 'O232', 'O233', 'O234', 'O235', 'O239', 'O24', 'O240', 'O241', 'O242', 'O243', 'O244', 'O249', 'O25',
             'O26', 'O260', 'O261', 'O263', 'O264', 'O265', 'O268', 'O269', 'O28', 'O280', 'O281', 'O282', 'O283', 'O284', 'O285', 'O288', 'O289', 'O29', 'O290', 'O291', 'O292', 'O293', 'O294', 'O295', 'O296', 'O298', 'O299', 'O30', 'O300',
             'O3O1', 'O3O2', 'O3O8', 'O3O9', 'O31', 'O311', 'O312', 'O318', 'O32', 'O320', 'O321', 'O322', 'O323', 'O324', 'O325', 'O326', 'O328', 'O329', 'O33', 'O330', 'O331', 'O332', 'O333', 'O334', 'O335', 'O336', 'O337', 'O338', 'O339',
             'O34', 'O340', 'O341', 'O342', 'O343', 'O344', 'O345', 'O346', 'O347', 'O348', 'O349', 'O35', 'O350', 'O351', 'O352', 'O353', 'O354', 'O355', 'O356', 'O357', 'O358', 'O359', 'O36', 'O360', 'O361', 'O362', 'O363', 'O365', 'O366',
             'O367', 'O368', 'O369', 'O40', 'O41', 'O410', 'O411', 'O418', 'O419', 'O43', 'O430', 'O431', 'O438', 'O439', 'O44', 'O440', 'O441', 'O46', 'O460', 'O468', 'O469', 'O47', 'O470', 'O471', 'O479', 'O48', 'Z321', 'Z33', 'Z34', 'Z340',
             'Z348', 'Z349', 'Z35', 'Z350', 'Z351', 'Z352', 'Z353', 'Z354', 'Z357', 'Z358', 'Z359', 'Z640']

    def string_finder(row, words):
        if any(word in field for field in row for word in words):
            return True
        return False

    MESTRE_JOIN_PIVOT_AT_IND['isContained_GESTANTE'] = MESTRE_JOIN_PIVOT_AT_IND.astype(
        str).apply(string_finder, words=match, axis=1)

    """##Linked Cadastro Mestre with At HIPER GEST DIAB with UNIDADES"""

    unidades['co_seq_dim_unidade_saude'] = unidades['co_seq_dim_unidade_saude'].astype(
        int)
    unidades.rename(
        columns={'co_seq_dim_unidade_saude': 'co_dim_unidade_saude'}, inplace=True)

    MESTRE_JOIN_PIVOT_AT_IND['co_dim_unidade_saude_CI'] = MESTRE_JOIN_PIVOT_AT_IND['co_dim_unidade_saude_CI'].replace(
        np.nan, 0)
    MESTRE_JOIN_PIVOT_AT_IND['co_dim_unidade_saude_CI'] = MESTRE_JOIN_PIVOT_AT_IND['co_dim_unidade_saude_CI'].astype(
        int)
    MESTRE_JOIN_PIVOT_AT_IND.rename(
        columns={'co_dim_unidade_saude_CI': 'co_dim_unidade_saude'}, inplace=True)
    MESTRE_JOIN_PIVOT_AT_IND = MESTRE_JOIN_PIVOT_AT_IND.drop(columns=[
                                                             '_merge'])
    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES = MESTRE_JOIN_PIVOT_AT_IND.merge(
        unidades, on='co_dim_unidade_saude', how='left', indicator=True)
    del unidades
    """## Linked Cadastro Mestre with Municipios"""

    municipio.rename(
        columns={'co_seq_dim_municipio': 'co_dim_municipio'}, inplace=True)
    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES.rename(
        columns={'co_dim_municipio_CI': 'co_dim_municipio'}, inplace=True)
    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES = MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES.drop(columns=[
                                                                                         '_merge'])
    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO = MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES.merge(
        municipio, on='co_dim_municipio', how='left', indicator=True)

    del municipio

    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['co_ibge'] = MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['co_ibge'].astype(
        str)
    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO[
        'co_ibge'] = MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['co_ibge'].str[:-2]

    """##Clean Linkage Final and Preprocessing for PAINEL

    ### Juntar Sexo e data nascimento
    """

    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['CO_DIM_SEXO'] = MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['CO_DIM_SEXO'].astype(
        str)

    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['co_dim_sexo_AI'] = MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['co_dim_sexo_AI'].str.split(
        ',').str[0]
    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['co_dim_sexo_AI'] = MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['co_dim_sexo_AI'].astype(
        str)

    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO = MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO.assign(**{
        'SEXO_FINAL': MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['CO_DIM_SEXO'].mask(
            lambda x: x == 'nan', MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['co_dim_sexo_AI'])})

    # MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES['SEXO_FINAL']=pd.to_numeric(MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES['SEXO_FINAL'])
    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['SEXO_FINAL'] = MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['SEXO_FINAL'].astype(
        str)

    def conditions(x):
        if x == '2':
            return "Feminino"
        elif x == '1':
            return "Masculino"
        elif x == '2.0':
            return "Feminino"
        elif x == '1.0':
            return "Masculino"
        else:
            return "NaN"

    func = np.vectorize(conditions)
    energy_class = func(
        MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO["SEXO_FINAL"])

    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO["SEXO_FINAL"] = energy_class

    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO = MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO.drop(
        columns=['CO_DIM_SEXO', 'co_dim_sexo_AI'])

    """### Trasformar 2 Urbano 3 Rural """

    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO.dtypes

    def conditions(x):
        if x == 2:
            return "Urbano"
        elif x == 3:
            return "Rural"
        else:
            return "NaN"

    func = np.vectorize(conditions)
    change_column_directly = func(
        MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO["co_dim_tipo_localizacao"])

    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO["co_dim_tipo_localizacao"] = change_column_directly

    """### Create Group Ages"""

    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['dt_nascimento_AI'] = MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['dt_nascimento_AI'].str.split(
        ',').str[0]
    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['dt_nascimento_AI'] = MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['dt_nascimento_AI'].apply(
        pd.Timestamp)
    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['DT_NASCIMENTO'] = pd.to_datetime(
        MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['DT_NASCIMENTO'], format='%Y-%m-%d', errors='coerce')

    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO = MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO.assign(**{
        'DT_NASCIMENTO_FINAL': MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['dt_nascimento_AI'].mask(
            lambda x: x == 'nan', MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['DT_NASCIMENTO'])})

    # Calcular Idade
    now = pd.Timestamp('now')
    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['DT_NASCIMENTO_FINAL'] = MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['DT_NASCIMENTO_FINAL'].where(
        MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['DT_NASCIMENTO_FINAL'] < now, MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['DT_NASCIMENTO_FINAL'] - np.timedelta64(100, 'Y'))

    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO = MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO.dropna(
        axis=0)
    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['AGE'] = (
        now - MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['DT_NASCIMENTO_FINAL']).dt.days.astype('int')

    # print(MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO.tail(5))
    # print(MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['AGE'].value_counts())

    def age_group(row):
        row['AGE'] = math.floor(row['AGE']/365)
        if row['AGE'] >= 0 and row['AGE'] <= 5:
            return "Faixa 1"
        elif row['AGE'] >= 6 and row['AGE'] <= 12:
            return "Faixa 2"
        elif row['AGE'] >= 13 and row['AGE'] <= 17:
            return "Faixa 3"
        elif row['AGE'] >= 18 and row['AGE'] <= 29:
            return "Faixa 4"
        elif row['AGE'] >= 30 and row['AGE'] <= 44:
            return "Faixa 5"
        elif row['AGE'] >= 45 and row['AGE'] <= 59:
            return "Faixa 6"
        elif row['AGE'] >= 60:
            return "Faixa 7"
        else:
            return "NaN"

    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['FAIXA_ETARIA'] = MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO.apply(
        lambda row: age_group(row), axis=1)
    print(MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['AGE'])
    # print(MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO['FAIXA_ETARIA'].value_counts())
    # exit()
    """### Delete unecessary Column and Rename"""
    print(MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO.columns)
    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO = MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO.drop(
        columns=['DT_NASCIMENTO', 'dt_nascimento_AI', '_merge', 'co_dim_unidade_saude_2', 'nu_idade_gestacional_semanas', 'co_dim_municipio', 'co_dim_unidade_saude_1'])
    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO_RENAME = MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO.rename(columns={'co_dim_municipio_AI': 'co_municipio',
                                                                                                                               'co_dim_unidade_saude': 'co_unidade_saude',
                                                                                                                               'co_dim_tipo_localizacao': 'ds_tipo_localizacao',
                                                                                                                               'SEXO_FINAL': 'ds_sexo',
                                                                                                                               'DT_NASCIMENTO_FINAL': 'dt_nascimento',
                                                                                                                               #    'AGE': 'nu_idade',
                                                                                                                               'FAIXA_ETARIA': 'ds_faixa_etaria',
                                                                                                                               'isContained_DIABETE': 'st_diabetes',
                                                                                                                               'isContained_HIPERTENSAO': 'st_hipertensao',
                                                                                                                               'isContained_GESTANTE': 'st_gestante',
                                                                                                                               'co_dim_tempo_dum': 'nu_idade_gestacional',
                                                                                                                               'no_unidade_saude': 'ds_unidade_saude',
                                                                                                                               'ds_filtro_cids': 'cad_filtro_cids',
                                                                                                                               'CIAP_AI_COMB': 'cad_filtro_ciap',
                                                                                                                               'co_dim_tempo_AI': 'dt_atendimento'})

    """# Exportando para Excel"""

    MESTRE_JOIN_PIVOT_AT_IND_JOIN_UNIDADES_MUNICIPIO_RENAME.dropna(how='any').to_csv(
        path + '/CADASTRO_MESTRE_JOIN_AT_IND_GEST_HIP_DIAB_JOIN_UNIDADES_CLEAN_PAINEL.csv')
    gc.collect()
