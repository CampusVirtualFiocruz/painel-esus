# pylint: disable=W0613,line-too-long

from flask import Blueprint
from src.main.composers.settings_composer import (
    check_instalation_composer,
    get_term_acceptance_settings_composer,
    instalation_status_composer,
    save_instalation_settings_composer,
    save_term_acceptance_settings_composer,
    start_instalation_composer,
    stop_instalation_settings_composer,
    test_connection_composer,
)
from src.presentations.controllers.settings.settings_controller import (
    SettingsController,
)

from .utils import handle_request

settings_bp = Blueprint("settings", __name__)


class SettingsPath:
    root_path = "/v1/settings"
    urls = {
        "instalation-status": "/instalation-status",
        "check-instalation": "/check-instalation",
        "instalation-settings": "/instalation-settings",
        "test-connection": "/test-connection",
        "test-connection": "/test-connection",
        "term-acceptance": "/term-acceptance",
        "stop-instalation": "/stop-instalation",
        "start-instalation": "/start-instalation",
    }


settings_path = SettingsPath()
urls = settings_path.urls

controller = SettingsController()


@settings_bp.route(
    urls["instalation-status"],
    methods=["GET"],
    endpoint="instalation-status",
)
def instalation_status():
    return handle_request(instalation_status_composer)


@settings_bp.route(
    urls["check-instalation"],
    methods=["GET"],
    endpoint="check-instalation",
)
def check_instalation():
    return handle_request(check_instalation_composer)


@settings_bp.route(
    urls["test-connection"],
    methods=["POST"],
    endpoint="test-connection",
)
def test_connection():
    return handle_request(test_connection_composer)


@settings_bp.route(
    urls["instalation-settings"],
    methods=["POST"],
    endpoint="instalation-settings",
)
def save_instalation_settings():
    return handle_request(save_instalation_settings_composer)


@settings_bp.route(
    urls["term-acceptance"],
    methods=["GET"],
    endpoint="term-acceptancee",
)
def get_term_acceptance():
    return handle_request(get_term_acceptance_settings_composer)


@settings_bp.route(
    urls["term-acceptance"],
    methods=["POST"],
    endpoint="term-acceptance-save",
)
def save_term_acceptance():
    return handle_request(save_term_acceptance_settings_composer)


@settings_bp.route(
    urls["stop-instalation"],
    methods=["GET"],
    endpoint="stop-instalation",
)
def stop_instalation():
    return handle_request(stop_instalation_settings_composer)


@settings_bp.route(
    urls["start-instalation"],
    methods=["GET"],
    endpoint="start-instalation",
)
def start_instalation():
    return handle_request(start_instalation_composer)
