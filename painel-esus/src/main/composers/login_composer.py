import logging

from src.data.use_cases.login import LoginUseCase
from src.domain.entities.user_payload import UserPayload
from src.errors import HttpNotFoundError
from src.errors.logging import logging
from src.infra.bridge_provider.login_bridge import LoginBridgeRepository
from src.infra.db.repositories.login_adm_repository import LoginAdmRepository
from src.infra.db.repositories.login_demo_repository import LoginDemoRepository
from src.infra.db.repositories.login_repository import (
    LoginRepository as LoginUserRepository,
)
from src.main.server.decorators.token_required import generate_token, validate_token
from src.presentations.http_types import HttpRequest, HttpResponse


def login_composer(request: HttpRequest):
    providers_repositories = [
        LoginAdmRepository(),
        LoginBridgeRepository(),
    ]
    body = None
    if request.body:
        body = request.body

    error = None
    for provider in providers_repositories:
        try:
            use_case = LoginUseCase(provider)
            response = use_case.login(
                username=body["username"], password=body["password"]
            )
            if isinstance(response, UserPayload) and response is not None:
                token = generate_token(
                    response.username,
                    response.cns,
                    response.uf,
                    response.municipio,
                    response.profiles,
                    response.ubs,
                    response.equipe
                )

                body = {"data": token, "profiles": response.profiles}

                return HttpResponse(status_code=200, body=body)
        except Exception as exc:
            error=True
    if error:
        logging.info("Nenhum provider foi capaz de logar o usuário.")

    return HttpResponse(status_code=401, body={"data": "Username or Password invalid."})


def set_profile_composer(request: HttpRequest):
    providers_repository = LoginBridgeRepository()
    body = None
    if request.body:
        body = request.body

    if body is None or not all(item in body for item in ["tipo", "ubs", "id", "cbo"]):
        return HttpResponse(status_code=400, body={"data": "Input data missing"})

    token = request.headers["Authorization"].split("Bearer ")[1]
    token_parsed = validate_token(token)
    use_case = LoginUseCase(providers_repository)

    # So vale uma lotacao que veio do PEC e esta assinada no token; o corpo apenas indica qual delas
    lotacoes = token_parsed.get("lotacoes") or token_parsed.get("profiles")
    if not isinstance(lotacoes, list):
        return HttpResponse(status_code=403, body={"data": "Profile not allowed"})
    lotacao = None
    for item in lotacoes:
        if not isinstance(item, dict):
            continue
        if (
            item.get("tipo") == body["tipo"]
            and str(item.get("id")) == str(body["id"])
            and (item.get("ubs") or {}).get("id") == (body.get("ubs") or {}).get("id")
            and (item.get("equipe") or {}).get("id") == (body.get("equipe") or {}).get("id")
        ):
            lotacao = item
            break
    if lotacao is None:
        return HttpResponse(status_code=403, body={"data": "Profile not allowed"})

    request_adapter = {
        "tipo": lotacao["tipo"],
        "cbo": {
            "id": lotacao["id"],
            "cbo2002": lotacao["cbo"],
        },
        "unidadeSaude": {
            "id": (lotacao.get("ubs") or {}).get("id"),
        },
        "equipe": {
            "id": (lotacao.get("equipe") or {}).get("id"),
        },
    }
    user = use_case.check_role(request_adapter)
    if user is None:
        return HttpResponse(status_code=403, body={"data": "Profile not allowed"})
    token = generate_token(
        token_parsed["username"],
        token_parsed["cns"],
        token_parsed["uf"],
        token_parsed["municipio"],
        user[0],
        user[1],
        user[2],
        lotacoes
    )
    body = {"data": token}
    return HttpResponse(status_code=200, body=body)
