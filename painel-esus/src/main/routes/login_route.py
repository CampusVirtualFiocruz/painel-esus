import threading
import time

from flask import Blueprint
from flask import jsonify
from flask import request
from src.errors.error_handler import handle_errors
from src.main.adapters.request_login_adapter import request_login_adapter
from src.main.composers.login_composer import login_composer
from src.main.composers.login_composer import set_profile_composer

login_bp = Blueprint("login", __name__)

JANELA_SEGUNDOS = 900
LIMITE_POR_USUARIO = 8
LIMITE_POR_IP = 30
_falhas = {}
_trava = threading.Lock()


def _excedeu(chave, limite):
    agora = time.time()
    with _trava:
        recentes = [t for t in _falhas.get(chave, []) if agora - t < JANELA_SEGUNDOS]
        _falhas[chave] = recentes
        return len(recentes) >= limite


def _registra_falha(*chaves):
    with _trava:
        for chave in chaves:
            _falhas.setdefault(chave, []).append(time.time())


@login_bp.route("", methods=["POST"])
def do_login():
    http_response = None
    response = None
    corpo = request.get_json(silent=True) or {}
    usuario = "u:" + str(corpo.get("username", ""))[:64]
    origem = "ip:" + request.headers.get("X-Real-IP", request.remote_addr or "")
    if _excedeu(usuario, LIMITE_POR_USUARIO) or _excedeu(origem, LIMITE_POR_IP):
        return jsonify({"data": "Too many attempts. Try again later."}), 429
    try:
        http_request = request_login_adapter(request)
        http_response = login_composer(http_request)
        response = jsonify(http_response.body)
        if http_response.status_code == 401:
            _registra_falha(usuario, origem)
        elif http_response.status_code == 200:
            with _trava:
                _falhas.pop(usuario, None)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)

    return response, http_response.status_code


@login_bp.route("/profile", methods=["POST"])
def set_profile():
    http_response = None
    response = None
    try:
        http_request = request_login_adapter(request)
        http_response = set_profile_composer(http_request)
        response = jsonify(http_response.body)
    except Exception as exception:
        http_response = handle_errors(exception)
        response = jsonify(http_response.body)
    return response, http_response.status_code
