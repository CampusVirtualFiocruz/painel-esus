# pylint: disable=W0613,line-too-long
from flask import Blueprint, jsonify, request
from src.env.conf import is_installed_ok
from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.presentations.controllers.create_bases.instalation_status import (
    InstalationStatus,
)

settings_bp = Blueprint("settings", __name__)


class SettingsPath:
    root_path = "/v1/settings"
    urls = {
        "instalation-status": "/instalation-status",
        "check-instalation": "/check-instalation",
    }


settings_path = SettingsPath()
urls = settings_path.urls


@settings_bp.route(
    urls["instalation-status"],
    methods=["GET"],
    endpoint="instalation-status",
)
def instalation_status():
    http_response = None
    response = None
    try:
        s = InstalationStatus()
        return  jsonify(s.to_dict()), 200
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), 400


@settings_bp.route(
    urls["check-instalation"],
    methods=["GET"],
    endpoint="check-instalation",
)
def check_instalation():
    http_response = None
    response = None
    try:
        status, response = is_installed_ok()
        if not status:
            return (
                jsonify(
                    {
                        "showSetupWizardOnLaunch": True,
                        "env": response
                    }
                ),
                200,
            )
        else:
            return jsonify({
                        "showSetupWizardOnLaunch": False
                    }), 200
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), 400
