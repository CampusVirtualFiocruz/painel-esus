import pandas as pd
import numpy as np
import gc
from datetime import date


def criarCadastroMeste(path):

    cidadao_pec = pd.read_csv(path + '/tb_fat_cidadao_pec.csv',
                              sep=';', engine='python', decimal=',', keep_default_na=False)
    cidadao_pec = cidadao_pec.drop_duplicates()

    cidadao_territorio = pd.read_csv(
        path + '/tb_fat_cidadao_territorio.csv', sep=';', engine='python', decimal=',')
    cidadao_territorio = cidadao_territorio.drop_duplicates()

    familia_territorio = pd.read_csv(
        path + '/tb_fat_familia_territorio.csv', sep=';', engine='python', decimal=',')
    familia_territorio = familia_territorio.drop_duplicates()
    # familia_territorio['co_fat_cidadao_territorio'] = familia_territorio['co_fat_cidadao_territorio'].str[:-2]
    familia_territorio['co_fat_cidadao_territorio'] = familia_territorio['co_fat_cidadao_territorio'].fillna(
        0).astype(str).astype(float).astype(int)

    cad_domiciliar = pd.read_csv(
        path + '/tb_fat_cad_domiciliar.csv', sep=';', engine='python', decimal=',')
    cad_domiciliar = cad_domiciliar.drop_duplicates()

    cad_individual = pd.read_csv(
        path + '/tb_fat_cad_individual.csv', sep=';', engine='python', decimal=',')
    cad_individual = cad_individual.drop_duplicates()

    """Deixando somente colunas de interesse"""

    cad_individual_SELECTED = cad_individual[['co_seq_fat_cad_individual', 'nu_cns', 'dt_nascimento', 'co_dim_unidade_saude', 'co_dim_equipe', 'co_dim_tempo', 'co_dim_sexo',
                                              'co_dim_raca_cor', 'co_dim_nacionalidade', 'nu_cns_responsavel', 'st_responsavel_familiar', 'co_dim_municipio',
                                              'st_frequenta_creche', 'st_plano_saude_privado', 'st_deficiencia', 'st_defi_auditiva', 'st_defi_intelectual_cognitiva', 'st_defi_outra', 'st_defi_visual',
                                              'st_defi_fisica', 'st_gestante', 'st_doenca_respiratoria', 'st_doenca_respira_asma', 'st_doenca_respira_dpoc_enfisem', 'st_doenca_respira_outra',
                                              'st_doenca_respira_n_sabe', 'st_fumante', 'st_alcool', 'st_outra_droga', 'st_hipertensao_arterial', 'st_diabete', 'st_avc', 'st_infarto', 'st_hanseniase',
                                              'st_tuberculose', 'st_cancer', 'st_internacao_12', 'st_tratamento_psiquiatra', 'st_acamado', 'st_domiciliado', 'st_doenca_cardiaca',
                                              'st_doenca_card_insuficiencia', 'st_problema_rins', 'st_problema_rins_insuficiencia', 'st_morador_rua', 'co_dim_tipo_parentesco',
                                              'co_dim_tipo_escolaridade', 'co_dim_situacao_trabalho', 'co_dim_tipo_orientacao_sexual', 'co_dim_tipo_condicao_peso', 'co_dim_tempo_morador_rua',
                                              'co_dim_etnia', 'co_dim_identidade_genero', 'co_dim_faixa_etaria', 'nu_micro_area', 'co_fat_cidadao_pec', 'co_fat_cidadao_pec_responsvl',
                                              'nu_cpf_cidadao', 'nu_cpf_responsavel']]

    """Renomeando possíveis duplicatas nas tabelas"""

    cad_individual_SELECTED = cad_individual_SELECTED.rename(
        columns={'co_dim_unidade_saude': 'co_dim_unidade_saude_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(
        columns={'co_dim_equipe': 'co_dim_equipe_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(
        columns={'dt_nascimento': 'dt_nascimento_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(
        columns={'co_dim_faixa_etaria': 'co_dim_faixa_etaria_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(
        columns={'co_dim_sexo': 'co_dim_sexo_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(
        columns={'nu_cns': 'nu_cns_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(
        columns={'co_dim_identidade_genero': 'co_dim_identidade_genero_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(
        columns={'nu_cpf_cidadao': 'nu_cpf_cidadao_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(
        columns={'co_dim_municipio': 'co_dim_municipio_CI'})

    """Otimização do codigo"""

    cad_individual_SELECTED = cad_individual_SELECTED[['co_fat_cidadao_pec', 'co_dim_sexo_CI', 'co_dim_unidade_saude_CI',
                                                       'co_dim_municipio_CI', 'co_dim_tempo', 'co_dim_identidade_genero_CI', 'dt_nascimento_CI', 'nu_cpf_cidadao_CI']]

    """Deixando somente as colunas de interesse"""

    cidadao_pec_SELECTED = cidadao_pec.drop(
        columns=['co_cidadao', 'no_social_cidadao', 'nu_telefone_celular', 'st_faleceu', 'st_lookup_etl', 'st_deletar'])

    """Renomeando"""

    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(
        columns={'co_seq_fat_cidadao_pec': 'co_fat_cidadao_pec'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(
        columns={'nu_cns': 'nu_cns_CP'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(
        columns={'co_dim_unidade_saude_vinc': 'co_dim_unidade_saude_vinc_CP'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(
        columns={'co_dim_equipe_vinc': 'co_dim_equipe_vinc_CP'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(
        columns={'co_dim_sexo': 'co_dim_sexo_CP'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(
        columns={'co_dim_equipe_vinc': 'co_dim_equipe_vinc_CP'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(
        columns={'co_dim_identidade_genero': 'co_dim_identidade_genero_CP'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(
        columns={'nu_cpf_cidadao': 'nu_cpf_cidadao_CP'})

    """Otimização do codigo"""

    cidadao_pec_SELECTED = cidadao_pec_SELECTED[[
        'co_fat_cidadao_pec', 'co_dim_sexo_CP', 'co_dim_identidade_genero_CP', 'co_dim_tempo_nascimento', 'no_cidadao']]

    """###Cidadão Território"""

    cidadao_territorio_SELECTED = cidadao_territorio.drop(columns=['co_dim_equipe', 'nu_micro_area',
                                                                   'st_responsavel', 'st_responsavel_informado', 'st_mudou_se', 'st_vivo',
                                                                   'st_responsavel_com_fci', 'st_cns_null', 'st_cidadao_consistente',
                                                                   'co_fat_ciddo_terrtrio_resp', 'st_processado_cidadao_respnsvl'])

    cidadao_territorio_SELECTED = cidadao_territorio_SELECTED.rename(
        columns={'co_fat_familia_territorio': 'co_seq_fat_familia_territorio'})

    """Otimização codigo """

    cidadao_territorio_SELECTED = cidadao_territorio_SELECTED[[
        'co_fat_cidadao_pec', 'co_seq_fat_cidadao_territorio', 'co_seq_fat_familia_territorio']]

    """###Família Território"""

    columns = ['co_seq_fat_familia_territorio', 'co_fat_cidadao_pec',
               'co_fat_cad_domiciliar', 'nu_prontuario', 'co_fat_cidadao_territorio']
    familia_territorio_SELECTED = pd.DataFrame(
        familia_territorio, columns=columns)

    """Otimização codigo"""

    familia_territorio_SELECTED = familia_territorio_SELECTED[[
        'co_fat_cidadao_pec', 'co_seq_fat_familia_territorio', 'co_fat_cad_domiciliar']]

    """###Cadastro Domiciliar"""

    columns = ['co_seq_fat_cad_domiciliar', 'co_dim_unidade_saude', 'co_dim_equipe', 'co_dim_tempo', 'qt_morador', 'nu_comodo', 'co_dim_tipo_imovel',
               'co_dim_tipo_logradouro', 'co_dim_tipo_situacao_moradia', 'co_dim_tipo_localizacao', 'co_dim_tipo_domicilio', 'co_dim_tipo_posse_terra',
               'co_dim_tipo_acesso_domicilio', 'co_dim_tipo_material_parede', 'co_dim_tipo_abastecimento_agua', 'co_dim_tipo_tratamento_agua',
               'co_dim_tipo_escoamento_sanitar', 'co_dim_tipo_destino_lixo', 'st_disp_energia', 'st_animal_domiciliar', 'nu_micro_area', 'ds_filtro_tipo_renda_familiar', 'co_dim_municipio']
    cad_domiciliar_SELECTED = pd.DataFrame(cad_domiciliar, columns=columns)

    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(
        columns={'co_dim_unidade_saude': 'co_dim_unidade_saude_CD'})
    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(
        columns={'co_dim_equipe': 'co_dim_equipe_CD'})
    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(
        columns={'co_dim_tempo': 'co_dim_tempo_CD'})
    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(
        columns={'nu_micro_area': 'nu_micro_area_CD'})
    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(
        columns={'co_dim_municipio': 'co_dim_municipio_CD'})

    """Otimização codigo"""

    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED[[
        'co_seq_fat_cad_domiciliar', 'co_dim_tipo_localizacao', 'co_dim_municipio_CD', 'co_dim_tempo_CD']]

    cad_individual_SELECTED['co_dim_tempo_CI'] = pd.to_datetime(
        cad_individual_SELECTED['co_dim_tempo'].astype(str), format='%Y%m%d')

    cad_individual_SELECTED_group = cad_individual_SELECTED.groupby(
        ['co_fat_cidadao_pec'], as_index=False
    ).agg(
        {
            'co_dim_tempo_CI': 'max',  # get the first date per group
        }
    )

    cad_individual_merge = pd.merge(cad_individual_SELECTED, cad_individual_SELECTED_group, how="right", on=[
                                    'co_fat_cidadao_pec', 'co_dim_tempo_CI'])

    # To keep discard the duplicated row with a condition to keep only those with an higher amount of CPF
    cad_individual_merge = cad_individual_merge.sort_values('nu_cpf_cidadao_CI', ascending=True).drop_duplicates(
        subset=['co_fat_cidadao_pec', 'co_dim_tempo_CI'], keep='last')

    """Otimização de codigos"""

    cad_individual_merge = cad_individual_merge.drop(
        ['nu_cpf_cidadao_CI'], axis=1)

    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(
        columns={'co_seq_fat_cidadao_pec': 'co_fat_cidadao_pec'})

    cidadao_territorio_SELECTED_group = cidadao_territorio_SELECTED.groupby(
        ['co_fat_cidadao_pec'], as_index=False
    ).agg(
        {
            'co_seq_fat_cidadao_territorio': 'max',  # get the first date per group
        }
    )

    cidadao_territorio_merge = pd.merge(cidadao_territorio_SELECTED, cidadao_territorio_SELECTED_group, how="right", on=[
                                        'co_fat_cidadao_pec', 'co_seq_fat_cidadao_territorio'])
    del cidadao_territorio_SELECTED
    del cidadao_territorio_SELECTED_group
    familia_territorio_SELECTED = familia_territorio_SELECTED.rename(
        columns={'co_seq_fat_familia_territorio': 'co_fat_familia_territorio'})

    familia_territorio_SELECTED = familia_territorio_SELECTED.rename(
        columns={'co_fat_cidadao_pec': 'co_fat_cidadao_pec_FT'})

    cad_domiciliar_SELECTED['co_dim_tempo_CD'] = pd.to_datetime(
        cad_domiciliar_SELECTED['co_dim_tempo_CD'].astype(str), format='%Y%m%d')
    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(
        columns={'co_seq_fat_cad_domiciliar': 'co_fat_cad_domiciliar'})

    cad_domiciliar_SELECTED_group = cad_domiciliar_SELECTED.groupby(
        ['co_fat_cad_domiciliar'], as_index=False
    ).agg(
        {
            'co_dim_tempo_CD': 'max',  # get the first date per group
        }
    )

    cad_domiciliar_merge = pd.merge(cad_domiciliar_SELECTED, cad_domiciliar_SELECTED_group, how="right", on=[
                                    'co_fat_cad_domiciliar', 'co_dim_tempo_CD'])

    linkage_A = cidadao_pec_SELECTED.merge(
        cad_individual_merge, on='co_fat_cidadao_pec', how='left', indicator=True)
    del cad_individual_merge
    linkage_A = linkage_A.rename(columns={'_merge': '_mergeA'})

    linkage_B = linkage_A.merge(
        cidadao_territorio_merge, on='co_fat_cidadao_pec', how='left', indicator=True)
    del cidadao_territorio_merge
    linkage_B = linkage_B.rename(columns={'_merge': '_mergeB'})

    linkage_B = linkage_B.rename(
        columns={'co_seq_fat_familia_territorio': 'co_fat_familia_territorio'})

    linkage_C = linkage_B.merge(familia_territorio_SELECTED,
                                on='co_fat_familia_territorio', how='left', indicator=True)
    del familia_territorio_SELECTED
    linkage_C = linkage_C.rename(columns={'_merge': '_mergeC'})

    linkage_D = linkage_C.merge(
        cad_domiciliar_merge, on='co_fat_cad_domiciliar', how='left', indicator=True)
    del cad_domiciliar_merge
    Cadastro_Mestre_Pessoas = linkage_D

    Cadastro_Mestre_Pessoas['co_dim_identidade_genero_CI'] = Cadastro_Mestre_Pessoas['co_dim_identidade_genero_CI'].astype(
        str)

    Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas.assign(**{
        'CO_DIM_IDENTIDADE_GENERO': Cadastro_Mestre_Pessoas['co_dim_identidade_genero_CI'].mask(
            lambda x: x == 'nan', Cadastro_Mestre_Pessoas['co_dim_identidade_genero_CP'])})

    Cadastro_Mestre_Pessoas_MERGE['CO_DIM_IDENTIDADE_GENERO'] = pd.to_numeric(
        Cadastro_Mestre_Pessoas_MERGE['CO_DIM_IDENTIDADE_GENERO'])
    Cadastro_Mestre_Pessoas_MERGE['CO_DIM_IDENTIDADE_GENERO'] = Cadastro_Mestre_Pessoas_MERGE['CO_DIM_IDENTIDADE_GENERO'].astype(
        str)

    Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CI'] = Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CI'].astype(
        str)

    Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.assign(**{
        'CO_DIM_SEXO': Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CI'].mask(
            lambda x: x == 'nan', Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CP'])})

    Cadastro_Mestre_Pessoas_MERGE['CO_DIM_SEXO'] = pd.to_numeric(
        Cadastro_Mestre_Pessoas_MERGE['CO_DIM_SEXO'])
    Cadastro_Mestre_Pessoas_MERGE['CO_DIM_SEXO'] = Cadastro_Mestre_Pessoas_MERGE['CO_DIM_SEXO'].astype(
        str)

    Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.drop(
        ['co_dim_sexo_CP'], axis=1)

    Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.drop(
        columns=['co_fat_cidadao_pec_FT'])

    Cadastro_Mestre_Pessoas_MERGE['co_dim_tempo_nascimento'] = pd.to_datetime(
        Cadastro_Mestre_Pessoas_MERGE['co_dim_tempo_nascimento'].astype(str), format='%Y-%m-%d', errors='coerce')

    Cadastro_Mestre_Pessoas_MERGE['dt_nascimento_CI'] = pd.to_datetime(
        Cadastro_Mestre_Pessoas_MERGE['dt_nascimento_CI'].astype(str), format='%Y-%m-%d', errors='coerce')
    Cadastro_Mestre_Pessoas_MERGE['dt_nascimento_CI'].fillna(
        pd.NaT, inplace=True)

    def _age(birth_date):
        today = date.today()
        y = today.year - birth_date.year
        if today.month < birth_date.month or today.month == birth_date.month and today.day < birth_date.day:
            y -= 1
        return y
    # merge same column of two dataframe in only 1
    Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.assign(**{
        'DT_NASCIMENTO': Cadastro_Mestre_Pessoas_MERGE['dt_nascimento_CI'].mask(
            lambda x: x == 'NaT', Cadastro_Mestre_Pessoas_MERGE['co_dim_tempo_nascimento'])})
    Cadastro_Mestre_Pessoas_MERGE['nu_idade'] = Cadastro_Mestre_Pessoas_MERGE['DT_NASCIMENTO'].apply(
        _age)
    Cadastro_Mestre_Pessoas_MERGE.to_csv(
        path + '/CADASTRO_MESTRE_PESSOAS.csv')
    gc.collect()
