from functools import wraps

from flask import jsonify
from src.env.conf import is_installed_ok
from src.errors.types import HttpForbiddenError


def is_not_installed():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            status, _ = is_installed_ok()
            if status:
                 return jsonify({"message":"Endpoint not open for configuration."}), 403

        return decorated_function

    return decorator
