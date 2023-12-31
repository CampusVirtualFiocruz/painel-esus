import pandas as pd

def load_cadastro_mestre():
    print('ok')
    return pd.read_excel(
          'files/CADASTRO_MESTRE_JOIN_AT_IND_GEST_HIP_DIAB_JOIN_UNIDADES_CLEAN_PAINEL.xlsx', engine='openpyxl')

def load_gestantes_base():
    return pd.read_excel(
          'files/BASE_GESTACOES_FINAL_PAINEL.xlsx', engine='openpyxl')

def load_hipertensao_base():
    return pd.read_excel(
          'files/BASE_ATENDIMENTOS_X_HIPERTENSAO.xlsx', engine='openpyxl')

def load_diabetes_base():
    return pd.read_excel(
        'files/BASE_ATENDIMENTOS_X_DIABETICOS.xlsx', engine='openpyxl')