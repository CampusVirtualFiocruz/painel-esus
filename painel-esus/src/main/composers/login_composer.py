import logging

from src.data.use_cases.login import LoginUseCase
from src.domain.entities.user_payload import UserPayload
from src.infra.bridge_provider.login_bridge import LoginBridgeRepository
from src.infra.db.repositories.login_adm_repository import LoginAdmRepository
from src.infra.db.repositories.login_repository import (
    LoginRepository as LoginUserRepository,
)
from src.main.server.decorators.token_required import generate_token
from src.presentations.http_types import HttpRequest
from src.presentations.http_types import HttpResponse

logging.basicConfig(level=logging.DEBUG)


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
                )
                return HttpResponse(status_code=200, body={"data": token})
        except Exception as exc:
            logging.exception(exc)
    return HttpResponse(status_code=401, body={"data": "Username or Password invalid."})
