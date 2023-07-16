import pandas as pd
import numpy as np


def criarCadastroMeste( path ):

    cidadao_pec = pd.read_csv( path + '/tb_fat_cidadao_pec.csv',sep=';',engine='python', decimal = ',',keep_default_na=False)
    cidadao_pec = cidadao_pec.drop_duplicates()

    cidadao_territorio = pd.read_csv( path + '/tb_fat_cidadao_territorio.csv',sep=';',engine='python', decimal = ',')
    cidadao_territorio = cidadao_territorio.drop_duplicates()

    familia_territorio = pd.read_csv( path + '/tb_fat_familia_territorio.csv',sep=';',engine='python', decimal = ',')
    familia_territorio = familia_territorio.drop_duplicates()
    # familia_territorio['co_fat_cidadao_territorio'] = familia_territorio['co_fat_cidadao_territorio'].str[:-2]
    familia_territorio['co_fat_cidadao_territorio'] = familia_territorio['co_fat_cidadao_territorio'].fillna(0).astype(str).astype(float).astype(int)

    cad_domiciliar = pd.read_csv( path + '/tb_fat_cad_domiciliar.csv',sep=';',engine='python', decimal = ',')
    cad_domiciliar = cad_domiciliar.drop_duplicates()

    cad_individual = pd.read_csv( path + '/tb_fat_cad_individual.csv',sep=';',engine='python', decimal = ',')
    cad_individual = cad_individual.drop_duplicates()

    """Deixando somente colunas de interesse"""

    cad_individual_SELECTED = cad_individual[['co_seq_fat_cad_individual','nu_cns','dt_nascimento','co_dim_unidade_saude','co_dim_equipe','co_dim_tempo','co_dim_sexo',
            'co_dim_raca_cor','co_dim_nacionalidade','nu_cns_responsavel','st_responsavel_familiar','co_dim_municipio',
            'st_frequenta_creche','st_plano_saude_privado','st_deficiencia','st_defi_auditiva','st_defi_intelectual_cognitiva','st_defi_outra','st_defi_visual',
            'st_defi_fisica','st_gestante','st_doenca_respiratoria','st_doenca_respira_asma','st_doenca_respira_dpoc_enfisem','st_doenca_respira_outra',
            'st_doenca_respira_n_sabe','st_fumante','st_alcool','st_outra_droga','st_hipertensao_arterial','st_diabete','st_avc','st_infarto','st_hanseniase',
            'st_tuberculose','st_cancer','st_internacao_12','st_tratamento_psiquiatra','st_acamado','st_domiciliado','st_doenca_cardiaca',
            'st_doenca_card_insuficiencia','st_problema_rins','st_problema_rins_insuficiencia','st_morador_rua','co_dim_tipo_parentesco',
            'co_dim_tipo_escolaridade','co_dim_situacao_trabalho','co_dim_tipo_orientacao_sexual','co_dim_tipo_condicao_peso','co_dim_tempo_morador_rua',
            'co_dim_etnia','co_dim_identidade_genero','co_dim_faixa_etaria','nu_micro_area','co_fat_cidadao_pec','co_fat_cidadao_pec_responsvl',
            'nu_cpf_cidadao','nu_cpf_responsavel']]
    

    

    """Renomeando possíveis duplicatas nas tabelas"""

    cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'co_dim_unidade_saude': 'co_dim_unidade_saude_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'co_dim_equipe': 'co_dim_equipe_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'dt_nascimento': 'dt_nascimento_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'co_dim_faixa_etaria': 'co_dim_faixa_etaria_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'co_dim_sexo': 'co_dim_sexo_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'nu_cns': 'nu_cns_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'co_dim_identidade_genero': 'co_dim_identidade_genero_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'nu_cpf_cidadao': 'nu_cpf_cidadao_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'co_dim_municipio': 'co_dim_municipio_CI'})

    """Otimização do codigo"""

    cad_individual_SELECTED = cad_individual_SELECTED[['co_fat_cidadao_pec','co_dim_sexo_CI','co_dim_unidade_saude_CI','co_dim_municipio_CI','co_dim_tempo','co_dim_identidade_genero_CI','dt_nascimento_CI','nu_cpf_cidadao_CI']]


    """Deixando somente as colunas de interesse"""

    cidadao_pec_SELECTED = cidadao_pec.drop(columns=['co_cidadao','no_social_cidadao','nu_telefone_celular','st_faleceu','st_lookup_etl','st_deletar'])

    """Renomeando"""

    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_seq_fat_cidadao_pec':'co_fat_cidadao_pec'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'nu_cns': 'nu_cns_CP'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_dim_unidade_saude_vinc': 'co_dim_unidade_saude_vinc_CP'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_dim_equipe_vinc': 'co_dim_equipe_vinc_CP'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_dim_sexo': 'co_dim_sexo_CP'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_dim_equipe_vinc': 'co_dim_equipe_vinc_CP'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_dim_identidade_genero': 'co_dim_identidade_genero_CP'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'nu_cpf_cidadao': 'nu_cpf_cidadao_CP'})

    """Otimização do codigo"""

    cidadao_pec_SELECTED = cidadao_pec_SELECTED[['co_fat_cidadao_pec','co_dim_sexo_CP','co_dim_identidade_genero_CP','co_dim_tempo_nascimento']]

    """###Cidadão Território"""

    cidadao_territorio_SELECTED = cidadao_territorio.drop(columns=['co_dim_equipe','nu_micro_area',
                                                                                'st_responsavel','st_responsavel_informado','st_mudou_se','st_vivo',
                                                                                'st_responsavel_com_fci','st_cns_null','st_cidadao_consistente',
                                                                                'co_fat_ciddo_terrtrio_resp','st_processado_cidadao_respnsvl'])

    cidadao_territorio_SELECTED = cidadao_territorio_SELECTED.rename(columns={'co_fat_familia_territorio':'co_seq_fat_familia_territorio'})

    """Otimização codigo """

    cidadao_territorio_SELECTED = cidadao_territorio_SELECTED[['co_fat_cidadao_pec','co_seq_fat_cidadao_territorio','co_seq_fat_familia_territorio']]

    """###Família Território"""


    columns = ['co_seq_fat_familia_territorio','co_fat_cidadao_pec','co_fat_cad_domiciliar','nu_prontuario','co_fat_cidadao_territorio']
    familia_territorio_SELECTED = pd.DataFrame(familia_territorio, columns=columns)

    """Otimização codigo"""

    familia_territorio_SELECTED = familia_territorio_SELECTED[['co_fat_cidadao_pec','co_seq_fat_familia_territorio','co_fat_cad_domiciliar']]

    """###Cadastro Domiciliar"""

    columns = ['co_seq_fat_cad_domiciliar','co_dim_unidade_saude','co_dim_equipe','co_dim_tempo','qt_morador','nu_comodo','co_dim_tipo_imovel',
            'co_dim_tipo_logradouro','co_dim_tipo_situacao_moradia','co_dim_tipo_localizacao','co_dim_tipo_domicilio','co_dim_tipo_posse_terra',
            'co_dim_tipo_acesso_domicilio','co_dim_tipo_material_parede','co_dim_tipo_abastecimento_agua','co_dim_tipo_tratamento_agua',
            'co_dim_tipo_escoamento_sanitar','co_dim_tipo_destino_lixo','st_disp_energia','st_animal_domiciliar','nu_micro_area','ds_filtro_tipo_renda_familiar','co_dim_municipio']
    cad_domiciliar_SELECTED = pd.DataFrame(cad_domiciliar, columns=columns)

    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(columns={'co_dim_unidade_saude': 'co_dim_unidade_saude_CD'})
    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(columns={'co_dim_equipe': 'co_dim_equipe_CD'})
    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(columns={'co_dim_tempo': 'co_dim_tempo_CD'})
    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(columns={'nu_micro_area': 'nu_micro_area_CD'})
    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(columns={'co_dim_municipio': 'co_dim_municipio_CD'})

    """Otimização codigo"""

    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED[['co_seq_fat_cad_domiciliar','co_dim_tipo_localizacao','co_dim_municipio_CD','co_dim_tempo_CD']]

    """## Preparação para o linkage

    ###Cadastro Individual

    Saber quantos tem chave única
    """

    len(cad_individual_SELECTED ['co_fat_cidadao_pec'].unique().tolist())

    cad_individual_SELECTED ['co_dim_tempo_CI'] = pd.to_datetime(cad_individual_SELECTED ['co_dim_tempo'].astype(str), format='%Y%m%d')


    cad_individual_SELECTED_group = cad_individual_SELECTED.groupby(
    ['co_fat_cidadao_pec'],as_index=False
    ).agg(
        {
            'co_dim_tempo_CI': 'max',  # get the first date per group
        }
    )

    cad_individual_merge = pd.merge(cad_individual_SELECTED, cad_individual_SELECTED_group, how="right", on=['co_fat_cidadao_pec', 'co_dim_tempo_CI'])
    cad_individual_merge.shape


    # To keep discard the duplicated row with a condition to keep only those with an higher amount of CPF
    cad_individual_merge = cad_individual_merge.sort_values('nu_cpf_cidadao_CI',ascending=True).drop_duplicates(subset=['co_fat_cidadao_pec', 'co_dim_tempo_CI'],keep = 'last')

    """Otimização de codigos"""

    cad_individual_merge = cad_individual_merge.drop(['nu_cpf_cidadao_CI'], axis = 1)

    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_seq_fat_cidadao_pec': 'co_fat_cidadao_pec'})

    cidadao_territorio_SELECTED_group = cidadao_territorio_SELECTED.groupby(
    ['co_fat_cidadao_pec'],as_index=False
    ).agg(
        {
            'co_seq_fat_cidadao_territorio': 'max',  # get the first date per group
        }
    )

    cidadao_territorio_merge = pd.merge(cidadao_territorio_SELECTED, cidadao_territorio_SELECTED_group, how="right", on=['co_fat_cidadao_pec', 'co_seq_fat_cidadao_territorio'])

    familia_territorio_SELECTED = familia_territorio_SELECTED.rename(columns={'co_seq_fat_familia_territorio': 'co_fat_familia_territorio'})

    familia_territorio_SELECTED = familia_territorio_SELECTED.rename(columns={'co_fat_cidadao_pec': 'co_fat_cidadao_pec_FT'})


    cad_domiciliar_SELECTED['co_dim_tempo_CD'] = pd.to_datetime(cad_domiciliar_SELECTED['co_dim_tempo_CD'].astype(str), format='%Y%m%d')
    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(columns={'co_seq_fat_cad_domiciliar': 'co_fat_cad_domiciliar'})

    cad_domiciliar_SELECTED_group = cad_domiciliar_SELECTED.groupby(
    ['co_fat_cad_domiciliar'],as_index=False
    ).agg(
        {
            'co_dim_tempo_CD': 'max',  # get the first date per group
        }
    )

    cad_domiciliar_merge = pd.merge(cad_domiciliar_SELECTED, cad_domiciliar_SELECTED_group, how="right", on=['co_fat_cad_domiciliar', 'co_dim_tempo_CD'])

    linkage_A = cidadao_pec_SELECTED.merge(cad_individual_merge, on='co_fat_cidadao_pec', how='left', indicator=True)


    linkage_A = linkage_A.rename (columns={'_merge': '_mergeA'})


    linkage_B = linkage_A.merge(cidadao_territorio_merge, on='co_fat_cidadao_pec', how='left', indicator=True)

    linkage_B = linkage_B.rename (columns={'_merge': '_mergeB'})

    linkage_B = linkage_B.rename (columns={'co_seq_fat_familia_territorio': 'co_fat_familia_territorio'})


    linkage_C = linkage_B.merge(familia_territorio_SELECTED, on='co_fat_familia_territorio', how='left', indicator=True)

    linkage_C = linkage_C.rename (columns={'_merge': '_mergeC'})


    linkage_D = linkage_C.merge(cad_domiciliar_merge, on='co_fat_cad_domiciliar', how='left', indicator=True)


    Cadastro_Mestre_Pessoas = linkage_D


    Cadastro_Mestre_Pessoas['co_dim_identidade_genero_CI'] = Cadastro_Mestre_Pessoas['co_dim_identidade_genero_CI'].astype(str)

    Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas.assign(**{
        'CO_DIM_IDENTIDADE_GENERO': Cadastro_Mestre_Pessoas['co_dim_identidade_genero_CI'].mask(
            lambda x: x == 'nan', Cadastro_Mestre_Pessoas['co_dim_identidade_genero_CP'])})

    Cadastro_Mestre_Pessoas_MERGE['CO_DIM_IDENTIDADE_GENERO']=pd.to_numeric(Cadastro_Mestre_Pessoas_MERGE['CO_DIM_IDENTIDADE_GENERO'])
    Cadastro_Mestre_Pessoas_MERGE['CO_DIM_IDENTIDADE_GENERO']=Cadastro_Mestre_Pessoas_MERGE['CO_DIM_IDENTIDADE_GENERO'].astype(str)

    Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CI'] = Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CI'].astype(str)

    Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.assign(**{
        'CO_DIM_SEXO': Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CI'].mask(
            lambda x: x == 'nan', Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CP'])})

    Cadastro_Mestre_Pessoas_MERGE['CO_DIM_SEXO']=pd.to_numeric(Cadastro_Mestre_Pessoas_MERGE['CO_DIM_SEXO'])
    Cadastro_Mestre_Pessoas_MERGE['CO_DIM_SEXO']=Cadastro_Mestre_Pessoas_MERGE['CO_DIM_SEXO'].astype(str)

    Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.drop(['co_dim_sexo_CP'], axis = 1)


    Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.drop(columns=['co_fat_cidadao_pec_FT'])


    Cadastro_Mestre_Pessoas_MERGE['co_dim_tempo_nascimento'] = pd.to_datetime(Cadastro_Mestre_Pessoas_MERGE['co_dim_tempo_nascimento'].astype(str), format='%Y-%m-%d',errors='coerce')

    Cadastro_Mestre_Pessoas_MERGE['dt_nascimento_CI'] = pd.to_datetime(Cadastro_Mestre_Pessoas_MERGE['dt_nascimento_CI'].astype(str), format='%Y-%m-%d',errors='coerce')
    Cadastro_Mestre_Pessoas_MERGE['dt_nascimento_CI'].fillna(pd.NaT, inplace=True)


    # merge same column of two dataframe in only 1
    Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.assign(**{
        'DT_NASCIMENTO': Cadastro_Mestre_Pessoas_MERGE['dt_nascimento_CI'].mask(
            lambda x: x == 'NaT', Cadastro_Mestre_Pessoas_MERGE['co_dim_tempo_nascimento'])})


    #Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.drop(columns=['co_dim_identidade_genero_CI','co_dim_identidade_genero_CP','co_dim_sexo_CI','co_dim_sexo_CP','co_fat_cidadao_pec','co_fat_cidadao_pec_FT',
                                                                                #'nu_cns_CP','nu_cns_CI','nu_cpf_cidadao_CP','nu_cpf_cidadao_CI','dt_nascimento_CI','co_dim_tempo_nascimento'])

    """# Exportando para Excel"""

    Cadastro_Mestre_Pessoas_MERGE.to_excel(path + '/CADASTRO_MESTRE_PESSOAS.xlsx')   


# def criarCadastroMeste( path ):
        
#     cidadao_pec = pd.read_csv( path + '/tb_fat_cidadao_pec.csv',sep=';',engine='python', decimal = ',',keep_default_na=False)
#     cidadao_pec = cidadao_pec.drop_duplicates()

#     cidadao_territorio = pd.read_csv( path + '/tb_fat_cidadao_territorio.csv',sep=';',engine='python', decimal = ',')
#     cidadao_territorio = cidadao_territorio.drop_duplicates()

#     familia_territorio = pd.read_csv( path + '/tb_fat_familia_territorio.csv',sep=';',engine='python', decimal = ',')
#     familia_territorio = familia_territorio.drop_duplicates()

#     cad_domiciliar = pd.read_csv( path + '/tb_fat_cad_domiciliar.csv',sep=';',engine='python', decimal = ',')
#     cad_domiciliar = cad_domiciliar.drop_duplicates()

#     cad_individual = pd.read_csv( path + '/tb_fat_cad_individual.csv',sep=';',engine='python', decimal = ',')
#     cad_individual = cad_individual.drop_duplicates()

#     """## Contagem de linhas e colunas"""

#     cidadao_pec.shape

#     cidadao_territorio.shape

#     familia_territorio.shape

#     cad_domiciliar.shape

#     cad_individual.shape

#     """## Processamento (limpeza das bases)

#     ###Cadastro Individual
#     """

#     cad_individual.head(1)

#     cad_individual.shape

#     """Deixando somente colunas de interesse"""

#     cad_individual_SELECTED = cad_individual[['co_seq_fat_cad_individual','nu_cns','dt_nascimento','co_dim_unidade_saude','co_dim_equipe','co_dim_tempo','co_dim_sexo',
#             'co_dim_raca_cor','co_dim_nacionalidade','nu_cns_responsavel','st_responsavel_familiar',
#             'st_frequenta_creche','st_plano_saude_privado','st_deficiencia','st_defi_auditiva','st_defi_intelectual_cognitiva','st_defi_outra','st_defi_visual',
#             'st_defi_fisica','st_gestante','st_doenca_respiratoria','st_doenca_respira_asma','st_doenca_respira_dpoc_enfisem','st_doenca_respira_outra',
#             'st_doenca_respira_n_sabe','st_fumante','st_alcool','st_outra_droga','st_hipertensao_arterial','st_diabete','st_avc','st_infarto','st_hanseniase',
#             'st_tuberculose','st_cancer','st_internacao_12','st_tratamento_psiquiatra','st_acamado','st_domiciliado','st_doenca_cardiaca',
#             'st_doenca_card_insuficiencia','st_problema_rins','st_problema_rins_insuficiencia','st_morador_rua','co_dim_tipo_parentesco',
#             'co_dim_tipo_escolaridade','co_dim_situacao_trabalho','co_dim_tipo_orientacao_sexual','co_dim_tipo_condicao_peso','co_dim_tempo_morador_rua',
#             'co_dim_etnia','co_dim_identidade_genero','co_dim_faixa_etaria','nu_micro_area','co_fat_cidadao_pec','co_fat_cidadao_pec_responsvl',
#             'nu_cpf_cidadao','nu_cpf_responsavel']]
#     cad_individual_SELECTED.shape

#     """Renomeando possíveis duplicatas nas tabelas"""

#     cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'co_dim_unidade_saude': 'co_dim_unidade_saude_CI'})
#     cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'co_dim_equipe': 'co_dim_equipe_CI'})
#     cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'dt_nascimento': 'dt_nascimento_CI'})
#     cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'co_dim_faixa_etaria': 'co_dim_faixa_etaria_CI'})
#     cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'co_dim_sexo': 'co_dim_sexo_CI'})
#     cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'nu_cns': 'nu_cns_CI'})
#     cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'co_dim_identidade_genero': 'co_dim_identidade_genero_CI'})
#     cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'nu_cpf_cidadao': 'nu_cpf_cidadao_CI'})


#     """Deixando somente as colunas de interesse"""


#     cidadao_pec_SELECTED = cidadao_pec.drop(columns=['co_cidadao','no_social_cidadao','nu_telefone_celular','st_faleceu','st_lookup_etl','st_deletar'])
#     cidadao_pec_SELECTED.shape

#     """Renomeando"""

#     cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_seq_fat_cidadao_pec':'co_fat_cidadao_pec'})
#     cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'nu_cns': 'nu_cns_CP'})
#     cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_dim_unidade_saude_vinc': 'co_dim_unidade_saude_vinc_CP'})
#     cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_dim_equipe_vinc': 'co_dim_equipe_vinc_CP'})
#     cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_dim_sexo': 'co_dim_sexo_CP'})
#     cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_dim_equipe_vinc': 'co_dim_equipe_vinc_CP'})
#     cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_dim_identidade_genero': 'co_dim_identidade_genero_CP'})
#     cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'nu_cpf_cidadao': 'nu_cpf_cidadao_CP'})

#     """###Cidadão Território"""

#     cidadao_territorio.head(1)

#     cidadao_territorio.shape

#     cidadao_territorio_SELECTED = cidadao_territorio.drop(columns=['co_dim_equipe','nu_micro_area',
#                                                                                 'st_responsavel','st_responsavel_informado','st_mudou_se','st_vivo',
#                                                                                 'st_responsavel_com_fci','st_cns_null','st_cidadao_consistente',
#                                                                                 'co_fat_ciddo_terrtrio_resp','st_processado_cidadao_respnsvl'])
#     cidadao_territorio_SELECTED.shape

#     cidadao_territorio_SELECTED = cidadao_territorio_SELECTED.rename(columns={'co_fat_familia_territorio':'co_seq_fat_familia_territorio'})

#     """###Família Território"""

#     familia_territorio.head(1)

#     familia_territorio.shape

#     columns = ['co_seq_fat_familia_territorio','co_fat_cidadao_pec','co_fat_cad_domiciliar','nu_prontuario','co_fat_cidadao_territorio']
#     familia_territorio_SELECTED = pd.DataFrame(familia_territorio, columns=columns)
#     familia_territorio_SELECTED.shape

#     """###Cadastro Domiciliar"""

#     cad_domiciliar.head(1)

#     cad_domiciliar.shape

#     columns = ['co_seq_fat_cad_domiciliar','co_dim_unidade_saude','co_dim_equipe','co_dim_tempo','qt_morador','nu_comodo','co_dim_tipo_imovel',
#             'co_dim_tipo_logradouro','co_dim_tipo_situacao_moradia','co_dim_tipo_localizacao','co_dim_tipo_domicilio','co_dim_tipo_posse_terra',
#             'co_dim_tipo_acesso_domicilio','co_dim_tipo_material_parede','co_dim_tipo_abastecimento_agua','co_dim_tipo_tratamento_agua',
#             'co_dim_tipo_escoamento_sanitar','co_dim_tipo_destino_lixo','st_disp_energia','st_animal_domiciliar','nu_micro_area','ds_filtro_tipo_renda_familiar']
#     cad_domiciliar_SELECTED = pd.DataFrame(cad_domiciliar, columns=columns)

#     cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(columns={'co_dim_unidade_saude': 'co_dim_unidade_saude_CD'})
#     cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(columns={'co_dim_equipe': 'co_dim_equipe_CD'})
#     cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(columns={'co_dim_tempo': 'co_dim_tempo_CD'})
#     cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(columns={'nu_micro_area': 'nu_micro_area_CD'})
#     cad_domiciliar_SELECTED.shape

#     """## Preparação para o linkage

#     ###Cadastro Individual

#     Saber quantos tem chave única
#     """

#     len(cad_individual_SELECTED ['co_fat_cidadao_pec'].unique().tolist())

#     cad_individual_SELECTED ['co_fat_cidadao_pec'].dtypes

#     """Criou uma coluna com a data de cadastro formatada"""

#     cad_individual_SELECTED ['co_dim_tempo_CI'] = pd.to_datetime(cad_individual_SELECTED ['co_dim_tempo'].astype(str), format='%Y%m%d')

#     cad_individual_SELECTED.head(1)

#     cad_individual_SELECTED.shape

#     """Agrupando e deixando somente o cadastro mais recente"""

#     cad_individual_SELECTED_group = cad_individual_SELECTED.groupby(
#     ['co_fat_cidadao_pec'],as_index=False
#     ).agg(
#         {
#             'co_dim_tempo_CI': 'max',  # get the first date per group
#         }
#     )

#     cad_individual_merge = pd.merge(cad_individual_SELECTED, cad_individual_SELECTED_group, how="right", on=['co_fat_cidadao_pec', 'co_dim_tempo_CI'])
#     cad_individual_merge.shape

#     cad_individual_merge.head(1)

#     # To keep discard the duplicated row with a condition to keep only those with an higher amount of CPF
#     cad_individual_merge = cad_individual_merge.sort_values('nu_cpf_cidadao_CI',ascending=True).drop_duplicates(subset=['co_fat_cidadao_pec', 'co_dim_tempo_CI'],keep = 'last')
#     cad_individual_merge.shape

#     """###Cidadão PEC"""

#     cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_seq_fat_cidadao_pec': 'co_fat_cidadao_pec'})
#     cidadao_pec_SELECTED.shape

#     len(cidadao_pec_SELECTED['co_fat_cidadao_pec'].unique().tolist())

#     cidadao_pec_SELECTED['co_fat_cidadao_pec'].dtypes

#     """###Cidadão território"""

#     len(cidadao_territorio_SELECTED ['co_fat_cidadao_pec'].unique().tolist())

#     cidadao_territorio_SELECTED ['co_fat_cidadao_pec'].dtypes

#     cidadao_territorio_SELECTED_group = cidadao_territorio_SELECTED.groupby(
#     ['co_fat_cidadao_pec'],as_index=False
#     ).agg(
#         {
#             'co_seq_fat_cidadao_territorio': 'max',  # get the first date per group
#         }
#     )

#     cidadao_territorio_merge = pd.merge(cidadao_territorio_SELECTED, cidadao_territorio_SELECTED_group, how="right", on=['co_fat_cidadao_pec', 'co_seq_fat_cidadao_territorio'])
#     cidadao_territorio_merge.shape

#     cidadao_territorio_merge.head(1)

#     """###Família território"""

#     familia_territorio_SELECTED.shape

#     familia_territorio_SELECTED.head(1)

#     familia_territorio_SELECTED = familia_territorio_SELECTED.rename(columns={'co_seq_fat_familia_territorio': 'co_fat_familia_territorio'})
#     len(familia_territorio_SELECTED['co_fat_familia_territorio'].unique().tolist())

#     familia_territorio_SELECTED = familia_territorio_SELECTED.rename(columns={'co_fat_cidadao_pec': 'co_fat_cidadao_pec_FT'})

#     familia_territorio_SELECTED.head(2)

#     """###Cadastro domiciliar"""

#     cad_domiciliar_SELECTED.head(1)

#     len(cad_domiciliar_SELECTED['co_seq_fat_cad_domiciliar'].unique().tolist())

#     cad_domiciliar_SELECTED['co_dim_tempo_CD'] = pd.to_datetime(cad_domiciliar_SELECTED['co_dim_tempo_CD'].astype(str), format='%Y%m%d')
#     cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(columns={'co_seq_fat_cad_domiciliar': 'co_fat_cad_domiciliar'})

#     cad_domiciliar_SELECTED_group = cad_domiciliar_SELECTED.groupby(
#     ['co_fat_cad_domiciliar'],as_index=False
#     ).agg(
#         {
#             'co_dim_tempo_CD': 'max',  # get the first date per group
#         }
#     )

#     cad_domiciliar_merge = pd.merge(cad_domiciliar_SELECTED, cad_domiciliar_SELECTED_group, how="right", on=['co_fat_cad_domiciliar', 'co_dim_tempo_CD'])
#     cad_domiciliar_merge.shape

#     """## Linkage A = cad_individual VS cidadao_pec"""

#     linkage_A = cidadao_pec_SELECTED.merge(cad_individual_merge, on='co_fat_cidadao_pec', how='left', indicator=True)
#     linkage_A.head(1)

#     linkage_A['_merge'].value_counts()

#     linkage_A = linkage_A.rename (columns={'_merge': '_mergeA'})

#     linkage_A.shape

#     len(linkage_A['co_fat_cidadao_pec'].unique().tolist())

#     """## Linkage B = Linkage A VS cidadao_territorio"""

#     linkage_B = linkage_A.merge(cidadao_territorio_merge, on='co_fat_cidadao_pec', how='left', indicator=True)
#     linkage_B.head(1)

#     linkage_B = linkage_B.rename (columns={'_merge': '_mergeB'})

#     linkage_B = linkage_B.rename (columns={'co_seq_fat_familia_territorio': 'co_fat_familia_territorio'})

#     len(linkage_B['co_fat_familia_territorio'].unique().tolist())

#     len(familia_territorio_SELECTED['co_fat_familia_territorio'].unique().tolist())

#     linkage_B.shape

#     """##Linkage C = Linkage B VS familia_territorio"""

#     linkage_C = linkage_B.merge(familia_territorio_SELECTED, on='co_fat_familia_territorio', how='left', indicator=True)
#     linkage_C.shape

#     linkage_C = linkage_C.rename (columns={'_merge': '_mergeC'})

#     len(linkage_C['co_fat_cad_domiciliar'].unique().tolist())

#     linkage_C.head(5)

#     """##Linkage D = Linkage C VS cad_domiciliar"""

#     linkage_D = linkage_C.merge(cad_domiciliar_merge, on='co_fat_cad_domiciliar', how='left', indicator=True)
#     linkage_D.shape

#     linkage_D.head(2)

#     """###Renomeando Linkage Final"""

#     Cadastro_Mestre_Pessoas = linkage_D

#     Cadastro_Mestre_Pessoas.head(2)

#     Cadastro_Mestre_Pessoas.shape

#     Cadastro_Mestre_Pessoas.dtypes

#     """## Juntar Colunas Duplicadas

#     ###**Identidade de gênero**
#     """

#     Cadastro_Mestre_Pessoas['co_dim_identidade_genero_CI'] = Cadastro_Mestre_Pessoas['co_dim_identidade_genero_CI'].astype(str)
#     Cadastro_Mestre_Pessoas['co_dim_identidade_genero_CI'].value_counts()

#     Cadastro_Mestre_Pessoas['co_dim_identidade_genero_CP'].value_counts()

#     Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas.assign(**{
#         'CO_DIM_IDENTIDADE_GENERO': Cadastro_Mestre_Pessoas['co_dim_identidade_genero_CI'].mask(
#             lambda x: x == 'nan', Cadastro_Mestre_Pessoas['co_dim_identidade_genero_CP'])})

#     Cadastro_Mestre_Pessoas_MERGE['CO_DIM_IDENTIDADE_GENERO']=pd.to_numeric(Cadastro_Mestre_Pessoas_MERGE['CO_DIM_IDENTIDADE_GENERO'])
#     Cadastro_Mestre_Pessoas_MERGE['CO_DIM_IDENTIDADE_GENERO']=Cadastro_Mestre_Pessoas_MERGE['CO_DIM_IDENTIDADE_GENERO'].astype(str)
#     Cadastro_Mestre_Pessoas_MERGE['CO_DIM_IDENTIDADE_GENERO'].value_counts()

#     """###**Sexo**"""

#     Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CI'] = Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CI'].astype(str)
#     Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CI'].value_counts()

#     Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CP'].value_counts()

#     Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.assign(**{
#         'CO_DIM_SEXO': Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CI'].mask(
#             lambda x: x == 'nan', Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CP'])})

#     Cadastro_Mestre_Pessoas_MERGE['CO_DIM_SEXO']=pd.to_numeric(Cadastro_Mestre_Pessoas_MERGE['CO_DIM_SEXO'])
#     Cadastro_Mestre_Pessoas_MERGE['CO_DIM_SEXO']=Cadastro_Mestre_Pessoas_MERGE['CO_DIM_SEXO'].astype(str)
#     Cadastro_Mestre_Pessoas_MERGE['CO_DIM_SEXO'].value_counts()

#     """###**Cidadão PEC**


#     > Apenas fazemos o drop da coluna duplicada que surge a partir do linkage com o Família Território. A variável co_fat_cidadao_pec utilizada como chave no início do linkage será sempre completa.


#     """

#     Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.drop(columns=['co_fat_cidadao_pec_FT'])

#     """###**CNS**


#     > Se por acaso utilizarmos como chave, temos que retirar os zeros.


#     """

#     Cadastro_Mestre_Pessoas_MERGE['nu_cns_CI'] = Cadastro_Mestre_Pessoas_MERGE['nu_cns_CI'].astype('Int64')
#     Cadastro_Mestre_Pessoas_MERGE['nu_cns_CI'].value_counts()

#     Cadastro_Mestre_Pessoas_MERGE['nu_cns_CP'].value_counts()

#     # merge same column of two dataframe in only 1
#     Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.assign(**{
#         'NU_CNS': Cadastro_Mestre_Pessoas_MERGE['nu_cns_CP'].mask(
#             lambda x: x == '', Cadastro_Mestre_Pessoas_MERGE['nu_cns_CI'])})

#     Cadastro_Mestre_Pessoas_MERGE['NU_CNS'].value_counts()

#     """###**CPF**


#     > O mesmo acontece aqui, se for usar como chave, tiramos os zeros.

#     """

#     Cadastro_Mestre_Pessoas_MERGE['nu_cpf_cidadao_CI'] = Cadastro_Mestre_Pessoas_MERGE['nu_cpf_cidadao_CI'].astype('Int64').astype('str')
#     Cadastro_Mestre_Pessoas_MERGE['nu_cpf_cidadao_CI'] = Cadastro_Mestre_Pessoas_MERGE['nu_cpf_cidadao_CI'].apply(lambda x: x.zfill(11))
#     Cadastro_Mestre_Pessoas_MERGE['nu_cpf_cidadao_CI'].value_counts()

#     Cadastro_Mestre_Pessoas_MERGE['nu_cpf_cidadao_CP'].value_counts()

#     # merge same column of two dataframe in only 1
#     Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.assign(**{
#         'NU_CPF': Cadastro_Mestre_Pessoas_MERGE['nu_cpf_cidadao_CP'].mask(
#             lambda x: x == '', Cadastro_Mestre_Pessoas_MERGE['nu_cpf_cidadao_CI'])})

#     Cadastro_Mestre_Pessoas_MERGE['NU_CPF'].value_counts()

#     """###**Data de nascimento**


#     > Aqui ainda temos 17 casos onde temos a data preenchida em "co_dim_tempo_nascimento" mas que na coluna final agrupada continuamos com missing, logo o código [475] não está funcionando corretamente. Acho que tem a ver com o 'NaN' que não temos nas colunas. O total de missing dessa coluna deve ser 13380, mas está com 13397.








#     """

#     Cadastro_Mestre_Pessoas_MERGE['co_dim_tempo_nascimento'] = pd.to_datetime(Cadastro_Mestre_Pessoas_MERGE['co_dim_tempo_nascimento'].astype(str), format='%Y-%m-%d',errors='coerce')
#     Cadastro_Mestre_Pessoas_MERGE['co_dim_tempo_nascimento'].isnull().sum()

#     Cadastro_Mestre_Pessoas_MERGE['co_dim_tempo_nascimento'].value_counts()

#     Cadastro_Mestre_Pessoas_MERGE['dt_nascimento_CI'] = pd.to_datetime(Cadastro_Mestre_Pessoas_MERGE['dt_nascimento_CI'].astype(str), format='%Y-%m-%d',errors='coerce')
#     Cadastro_Mestre_Pessoas_MERGE['dt_nascimento_CI'].fillna(pd.NaT, inplace=True)

#     Cadastro_Mestre_Pessoas_MERGE['dt_nascimento_CI'].value_counts()

#     Cadastro_Mestre_Pessoas_MERGE['dt_nascimento_CI'].isnull().sum()

#     # merge same column of two dataframe in only 1
#     Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.assign(**{
#         'DT_NASCIMENTO': Cadastro_Mestre_Pessoas_MERGE['dt_nascimento_CI'].mask(
#             lambda x: x == 'NaT', Cadastro_Mestre_Pessoas_MERGE['co_dim_tempo_nascimento'])})

#     Cadastro_Mestre_Pessoas_MERGE['DT_NASCIMENTO'].isnull().sum()

#     Cadastro_Mestre_Pessoas_MERGE['DT_NASCIMENTO'].value_counts()

#     #Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.drop(columns=['co_dim_identidade_genero_CI','co_dim_identidade_genero_CP','co_dim_sexo_CI','co_dim_sexo_CP','co_fat_cidadao_pec','co_fat_cidadao_pec_FT',
#                                                                                 #'nu_cns_CP','nu_cns_CI','nu_cpf_cidadao_CP','nu_cpf_cidadao_CI','dt_nascimento_CI','co_dim_tempo_nascimento'])

#     Cadastro_Mestre_Pessoas_MERGE.shape

#     Cadastro_Mestre_Pessoas_MERGE.head(5)

#     """# Exportando para Parquet"""

#     Cadastro_Mestre_Pessoas_MERGE.head(5)

#     del cidadao_pec
#     del cidadao_territorio
#     del cad_domiciliar
#     del cad_individual
#     del familia_territorio

#     Cadastro_Mestre_Pessoas_MERGE['NU_CNS'] = Cadastro_Mestre_Pessoas_MERGE['NU_CNS'].replace(np.nan, 0)
#     Cadastro_Mestre_Pessoas_MERGE['NU_CNS'] = Cadastro_Mestre_Pessoas_MERGE['NU_CNS'].replace('', 0).astype(float)
#     import gc
#     gc.collect()

#     Cadastro_Mestre_Pessoas_MERGE.to_parquet( path + '/CADASTRO_MESTRE.parquet')
