class HttpForbiddenError(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'Forbidden'
        self.status_code = 403
