"""Demografia: Total de pessoas."""

import duckdb
from src.data.interfaces.demographic_repository import TotalPeopleInterface
from src.infra.db.repositories.sqls.parquet.tb_acompanhamento_vinculo import get_pessoas
from src.infra.db.settings.connection_duckdb import DuckDbHandler


class TotalPeopleRepository(TotalPeopleInterface):

    def __init__(self, db_connection=DuckDbHandler()):
        """Inicializa a conexão."""
        self.db = db_connection

    def get_total_people(self, cnes: int = None, equipe: int = None):
        """Retorna o total de pessoas, opcionalmente filtradas por CNES e equipe."""
        sql_pessoas = get_pessoas(cnes=cnes, equipe=equipe)

        sql = f"""
                with pessoas as ({sql_pessoas})
                select count(*) total
                from pessoas
            """
        db_response = self.db.fetchone(sql)
        return db_response[0] if len(db_response) > 0 else 0
