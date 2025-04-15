import duckdb
from src.data.interfaces.demographic_repository import DemographicTotalPeopleInterface
from src.infra.db.repositories.sqls.parquet.tb_acompanhamento_vinculo import get_pessoas


class TotalPeopleRepository(DemographicTotalPeopleInterface):

    def __init__(self, db_connection=duckdb):
        self.db = db_connection

    def get_total_people(self, cnes: int = None, equipe: int = None):
        sql_pessoas = get_pessoas(cnes=cnes, equipe=equipe)

        sql = f"""
                with pessoas as ({sql_pessoas})
                select count(*) total
                from pessoas
            """
        db_response = self.db.sql(sql).fetchone()
        # print(db_response[0])
        return db_response[0] if len(db_response) > 0 else 0
