from src.errors.logger.custom_levels.new_levels import base_log
from src.errors.logging import logging
from src.infra.requests.api_log import ApiLog
from src.main.server.decorators.token_required import check_token, extract_token


def send_download_request(message, id, request):
    message, extra_info = base_log(
        message,
        extra={
            "query_params": {k: v for k, v in request.args.items() if k not in ("q", "cpf", "nome")},
            "usuario": check_token(request).get("cns"),
            "ip": request.headers.get("X-Real-IP", request.remote_addr),
            "path_params": request.view_args,
            "id": id,
        },
    )
    extra_info = extra_info["extra"]
    token = extract_token(request.headers.get("Authorization"))
    logging.download(
        message,extra=extra_info
    )
    extra_info["description"] = message
    ApiLog().send_download_log(token, extra_info)

def send_login_log(request, body):
    if "username" in body:
        logging.login(
            "Efetuando login",
            extra={"username": str(body["username"])[:3] + "***", "ip": request.headers.get("X-Real-IP", request.remote_addr)}
        )
        ApiLog().send_authentication_logs(body)
