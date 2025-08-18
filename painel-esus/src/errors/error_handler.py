from src.errors.logging import logging
from src.infra.requests.api_log import ApiLog
from src.presentations.http_types import HttpResponse

from .types import (
    HttpBadRequestError,
    HttpCredentialsFailError,
    HttpNotFoundError,
    HttpUnprocessableEntityError,
    InvalidIMC,
)


def handle_errors(error: Exception, token=None) -> HttpResponse:

    logging.exception(error)
    
    ApiLog().send_exception_logs(str(error), token)
    if isinstance(error, (HttpNotFoundError, HttpBadRequestError, HttpUnprocessableEntityError,
                          InvalidIMC, HttpCredentialsFailError)):
        # mandar mensagem para logger falando que teve esse erro!
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
