# pylint: disable=W0613,line-too-long
import os

from flask import Blueprint, jsonify, request
from sqlalchemy import text
from src.env.conf import is_installed_ok, update_env
from src.errors.error_handler import handle_errors
from src.infra.db.settings.connection import DBConnectionHandler
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
        "instalation-settings": "/instalation-settings",
        "test-connection": "/test-connection",
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


@settings_bp.route(
    urls["test-connection"],
    methods=["POST"],
    endpoint="test-connection",
)
def test_connection():
    http_response = None
    response = None
    try:
        body = request.json
        DB_HOST = body.get("DB_HOST", "")
        DB_DATABASE= body.get('DB_DATABASE','')
        DB_USER= body.get('DB_USER','')
        DB_PASSWORD = body.get('DB_PASSWORD','')
        DB_PORT= body.get('DB_PORT','0')
        try:
            with DBConnectionHandler(
                DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE
            ) as db_con:
                db_con.session.connection().execute(text("select * from information_schema.tables"))
                return jsonify({}), 200
        except Exception as e:
            return jsonify({ "message": f"Erro: {str(e)}"}), 400

    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), 400


@settings_bp.route(
    urls["instalation-settings"],
    methods=["POST"],
    endpoint="instalation-settings",
)
def save_instalation_settings():
    http_response = None
    response = None
    try:
        body = request.json
        update_env(body)
        print(os.getenv('DB_USER'))
        return jsonify({}), 200

    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), 400
