from flask import Blueprint, request, jsonify
from src.main.adapters.request_login_adapter import request_login_adapter
from src.main.composers.login_composer import login_composer
from src.errors.error_handler import handle_errors
login_bp = Blueprint("login", __name__)


@login_bp.route('', methods=['POST'])
def do_login():
    http_response = None
    response = None
    try:
        http_request = request_login_adapter(request)
        http_response = login_composer(http_request)
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code
