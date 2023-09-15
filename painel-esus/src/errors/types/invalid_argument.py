
class InvalidArgument(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(self, message)
        self.message = message
        self.name = 'InvalidArgument'
        self.status_code = 400
