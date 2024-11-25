from .cpf_cns_rate import get_cpf_cns_rate
from .group_localidade import group_localidade
from .group_raca_cor import group_raca_cor
from .group_records_by_origin import group_records_by_origin
from .total import get_total_cadastros, sql_round


def test_total_sql():
    sql = str(get_total_cadastros(25,18))

    assert "pessoas.codigo_equipe_vinculada" in sql
    assert "pessoas.codigo_unidade_saude" in sql

    sql = str(get_total_cadastros())
    print(sql)
    assert "pessoas.codigo_equipe_vinculada" not in sql
    assert "pessoas.codigo_unidade_saude" not in sql

def test_round():
    sql = sql_round("select * from cadastros_atualizados", "select * from total")
    print(sql)

def test_get_cpf_cns_rate():
    sql = get_cpf_cns_rate()
    print(sql)


def test_group_localidade():
    sql = group_localidade()
    print(sql)

def test_group_raca_cor():
    sql = group_raca_cor(25, 18)
    print(sql)

def test_group_records_by_origin():
    sql = group_records_by_origin(25,18)
    print(sql)
