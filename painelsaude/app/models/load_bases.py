import pandas as pd


def load_cadastro_mestre():
    print('ok')
    return pd.read_csv(
        'files/CADASTRO_MESTRE_JOIN_AT_IND_GEST_HIP_DIAB_JOIN_UNIDADES_CLEAN_PAINEL.csv')


def load_gestantes_base():
    return pd.read_csv(
        'files/BASE_GESTACOES_FINAL_PAINEL.csv')


def load_hipertensao_base():
    return pd.read_csv(
        'files/BASE_ATENDIMENTOS_X_HIPERTENSAO.csv')


def load_diabetes_base():
    return pd.read_csv(
        'files/BASE_ATENDIMENTOS_X_DIABETICOS.csv')
