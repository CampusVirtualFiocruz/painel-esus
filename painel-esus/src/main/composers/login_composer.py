import logging

from src.data.use_cases.login import LoginUseCase
from src.domain.entities.user_payload import UserPayload
from src.errors.logging import logging
from src.infra.bridge_provider.login_bridge import LoginBridgeRepository
from src.infra.db.repositories.login_adm_repository import LoginAdmRepository
from src.infra.db.repositories.login_repository import (
    LoginRepository as LoginUserRepository,
)
from src.main.server.decorators.token_required import generate_token, validate_token
from src.presentations.http_types import HttpRequest, HttpResponse


def login_composer(request: HttpRequest):
    providers_repositories = [
        LoginAdmRepository(),
        LoginBridgeRepository(),
        LoginUserRepository(),
    ]
    body = None
    if request.body:
        body = request.body

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
            logging.exception(exc)
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

    request_adapter = {
        "tipo": body["tipo"],
        "cbo": {
            "id": body["id"],
            "cbo2002": body["cbo"],
        },
        "unidadeSaude": {
            "id": (
                body["ubs"]["id"] if "ubs" in body and body["ubs"] is not None else None
            ),
        },
        "equipe": {
            "id": (
                body["equipe"]["id"]
                if "equipe" in body and body["equipe"] is not None
                else None
            ),
        },
    }
    user = use_case.check_role(request_adapter)
    token = generate_token(
        token_parsed["username"],
        token_parsed["cns"],
        token_parsed["uf"],
        token_parsed["municipio"],
        user[0],
        user[1],
        user[2]
    )
    body = {"data": token}
    return HttpResponse(status_code=200, body=body)
