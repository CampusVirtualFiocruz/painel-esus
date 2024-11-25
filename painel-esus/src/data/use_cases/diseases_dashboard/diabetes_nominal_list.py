# pylint: disable=R0913
from src.errors import InvalidArgument
from src.main.adapters.nominal_list_adapter import DiabetesNominalListAdapter


class DiabetesNominalListUseCase:

    def __init__(self, repository):
        self.__repository = repository

    def get_nominal_list(
        self,
        cnes: int = None,
        page: int = 0,
        page_size: int = 10,
        nome: str = None,
        cpf: str = None,
        equipe: int = None,
    ):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        response = self.__repository.find_filter(cnes, page, page_size, nome, cpf, equipe)

        response["items"] = [
            DiabetesNominalListAdapter(r).to_dict() for r in response["items"]
        ]
        return response

    def get_nominal_list_download(self, cnes: int = None, equipe:int = None):
        if cnes and not isinstance(cnes, int):
            raise InvalidArgument("CNES must be int")
        response = self.__repository.find_all_download(cnes, equipe)
        return response
