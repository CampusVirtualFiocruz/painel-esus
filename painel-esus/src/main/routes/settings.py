# pylint: disable=W0613,line-too-long
from flask import Blueprint, jsonify, request
from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter
from src.presentations.controllers.create_bases.instalation_status import (
    InstalationStatus,
)

settings_bp = Blueprint("settings", __name__)


class SettingsPath:
    root_path = "/v1"
    urls = {
        "settings": "/settings",
    }


settings_path = SettingsPath()
urls = settings_path.urls


@settings_bp.route(
    urls["settings"],
    methods=["GET"],
    endpoint="settings",
)
def settings():
    http_response = None
    response = None
    try:
        s = InstalationStatus()
        return  jsonify(s.to_dict()), 200
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), 400

