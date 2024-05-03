
class InvalidIMC(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(self, message)
        self.message = message
        self.name = 'InvalidIMC'
        self.status_code = 400
