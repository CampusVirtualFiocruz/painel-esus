import duckdb

from src.infra.db.repositories.elderly import elderly_repository
from src.infra.db.repositories.elderly.elderly_repository import ElderlyRepository


def test_order_clause_uses_safe_defaults():
    repository = ElderlyRepository()

    assert repository._build_order_clause(None) == " ORDER BY nome asc"
    assert repository._build_order_clause(
        ['{"field": "idade", "direction": "invalid"}']
    ) == " ORDER BY idade asc"
    assert repository._build_order_clause(
        ['{"field": "cpf", "direction": "DESC"}']
    ) == " ORDER BY cpf desc"


def test_nominal_list_counts_rows_without_materializing_all_results(monkeypatch):
    actual_connect = duckdb.connect
    base_query = """
        SELECT
            range AS codigo_cidadao,
            'Pessoa ' || range AS nome,
            '' AS cpf,
            '' AS cns,
            70 AS idade,
            1 AS codigo_unidade_saude,
            1 AS codigo_equipe
        FROM range(11)
    """

    monkeypatch.setattr(elderly_repository, "get_elderly_base", lambda: base_query)
    monkeypatch.setattr(elderly_repository.duckdb, "connect", actual_connect)

    result = ElderlyRepository().find_filter_nominal(
        cnes=None,
        page=1,
        pagesize=10,
    )

    assert result["itemsCount"] == 11
    assert result["itemsPerPage"] == 10
    assert result["pagesCount"] == 2
    assert len(result["items"]) == 10
