class HypertensionDiabetesRepositoryInterface:
    def get_total(self, cnes: int = None, equipe: int = None, debug=False):
        pass

    def get_exams_count(self, cnes: int = None, equipe: int = None, debug=False):
        pass

    def get_imc(self, cnes: int = None, equipe: int = None, debug=False):
        pass

    def get_complications(self, cnes: int = None, equipe: int = None, debug=False):
        pass

    def get_by_location(self, cnes: int = None, equipe: int = None, debug=False):
        pass

    def get_by_race(self, cnes: int = None, equipe: int = None, debug=False):
        pass

    def get_by_gender(self, cnes: int = None, equipe: int = None, debug=False):
        pass

    def get_nominal_list_download(self, cnes: int = None, equipe: int = None):
        pass

    def get_nominal_list(
        self, cnes: int, page: int = 1, page_size:int = 10, nome:str = None, cpf: str = None, equipe:int= None, q:str =None, sort = []
    ):
        pass
