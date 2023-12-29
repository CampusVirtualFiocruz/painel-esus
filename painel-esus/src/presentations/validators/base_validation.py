# pylint: disable=E0401
from cerberus import Validator

from src.errors.types import HttpUnprocessableEntityError


def _validation(entry, schema):
    query_validator = Validator(schema)
    response = query_validator.validate(entry)

    if response is False:
        raise HttpUnprocessableEntityError(query_validator.errors)
    return response
