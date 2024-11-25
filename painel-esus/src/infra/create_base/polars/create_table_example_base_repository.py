from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)


class CreateTableExampleBaseRepository(CreateBasesRepositoryInterface):
    _base = "equipes"

    def __init__(self): ...

    def get_base(self):
        return self._base

    def create_base(self):
        """
        Colocar aqui a regra de criação de tabela
        
        1 - Pode colocar a extração das tabelas em questão e salvar em Parquet
        2 - Gerar as outras tabelas dos indicadores 
        """
        ...
