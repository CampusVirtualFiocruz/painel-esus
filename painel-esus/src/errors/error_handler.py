import logging

from src.presentations.http_types import HttpResponse

from .types import (HttpBadRequestError, HttpCredentialsFailError,
                    HttpNotFoundError, HttpUnprocessableEntityError,
                    InvalidIMC)

logging.basicConfig(level=logging.DEBUG)


def handle_errors(error: Exception) -> HttpResponse:
    logging.exception(error)
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
