class HttpResponse:

    def __init__(self, status_code, body) -> None:
        self.status_code = status_code
        self.body = body

    def __repr__(self) -> str:
        return f'HttpResponse:\tstatus_code: {self.status_code}\tbody: {self.body}'
