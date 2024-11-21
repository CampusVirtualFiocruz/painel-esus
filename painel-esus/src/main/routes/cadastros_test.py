from pprint import pprint

from .cadastros import (
    gera_banco,
    localizacao_dos_domicilios_cadastrados,
    porcentagem_de_cadastros_atualizados,
    status_do_cadastro_dos_cidadaos,
    total_de_cadastro,
    total_de_cadastro_por_tipo_identificacao,
    total_domicilio_vs_responsavel,
    total_raca_cor,
    via_de_cadastro_cidadao,
)


def test_gera_banco():
    df1 = gera_banco()
    # df2 = gera_banco(cnes=25, equipe=18)
    # assert df1.shape[0] > df2.shape[0]

def test_total_de_cadastros():
    df = gera_banco(cnes=25, equipe=18)
    result = total_de_cadastro(df)
    pprint(result.head())

def test_localizacao_dos_domicilios_cadastrados():
    df = gera_banco(cnes=25, equipe=18)
    result = localizacao_dos_domicilios_cadastrados(df)
    pprint(result.head())
