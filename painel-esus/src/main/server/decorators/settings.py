from functools import wraps

from flask import jsonify
from src.env.conf import is_installed_ok
from src.errors.types import HttpForbiddenError
from src.presentations.controllers.settings.settings_controller import (
    SettingsController,
)


def is_not_installed():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            controller = SettingsController()
            status = controller.instalation_ready()
            if status.body["completed"]:
                return jsonify({"message":"Endpoint not open for configuration."}), 403
            return f(*args, **kwargs)
        return decorated_function

    return decorator
