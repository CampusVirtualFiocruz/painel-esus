"""Demografia: Distribuição por sexo.

Consulta agregada por sexo (feminino/masculino) e retorna um dicionário
com a contagem normalizada.
"""

import duckdb
from src.data.interfaces.demographic_repository import GenderInterface
from src.infra.db.repositories.sqls.demographics import filter_by_sexo
from src.infra.db.settings.connection_duckdb import DuckDbHandler


class GenderRepository(GenderInterface):

    def __init__(self, db_connection=DuckDbHandler()):
        """Inicializa a conexão."""
        self.db = db_connection

    def get_gender(self, cnes: int = None, equipe: int = None):
        """Retorna contagens por sexo em formato de dicionário, opcionalmente filtradas por CNES e equipe.
        """
        gender = {"feminino": 0, "masculino": 0}
        gender_sql = filter_by_sexo(cnes, equipe)
        result_gender = self.db.fetchall(gender_sql)

        for resp in result_gender:
            gender[str(resp[0]).lower()] = int(resp[1])
        return gender
