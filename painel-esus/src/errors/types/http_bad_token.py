class HttpBadTokenError(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'BadToken'
        self.status_code = 498
