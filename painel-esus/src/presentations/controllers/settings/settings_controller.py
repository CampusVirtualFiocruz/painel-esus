import os
import threading
import webbrowser

from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy import text
from src.env.conf import is_installed_ok, update_env, getenv
from src.errors import HttpForbiddenError
from src.infra.db.repositories.settings.acceptance_term_repository import (
    AcceptanceTermRepository,
)
from src.infra.db.settings.connection import DBConnectionHandler
from src.main.composers.schedule_compose import generate_base_scheduled
from src.presentations.controllers.create_bases.generate_base_thread import GenerateBase
from src.presentations.controllers.create_bases.instalation_status import (
    InstalationStatus,
)
from src.presentations.http_types import HttpRequest, HttpResponse
from src.presentations.validators.dashboard_validator import acceptance_term_validation
from typing_extensions import Literal


class SettingsController:

    def __init__(self): ...

    def _check_instalation(self):
        status, response = is_installed_ok()
        if status:
            raise HttpForbiddenError("Settings already done.")

    def instalation_status(self, request: HttpRequest) -> HttpResponse:
        s = InstalationStatus()
        return HttpResponse(
            status_code=200,
            body=s.to_dict(),
        )

    def check_instalation(self, request: HttpRequest) -> HttpResponse:
        status, response = is_installed_ok()
        print(f"{status=}")
        if not status:
            return HttpResponse(
                status_code=200,
                body={
                    "showSetupWizardOnLaunch": True,
                    "env": response,
                },
            )
        else:
            return HttpResponse(
                status_code=200,
                body={
                    "showSetupWizardOnLaunch": False,
                },
            )

    def test_connection(self, request: HttpRequest) -> HttpResponse:
        self._check_instalation()
        body = request.body
        DB_HOST = body.get("DB_HOST", "")
        DB_DATABASE = body.get("DB_DATABASE", "")
        DB_USER = body.get("DB_USER", "")
        DB_PASSWORD = body.get("DB_PASSWORD", "")
        DB_PORT = body.get("DB_PORT", "0")
        with DBConnectionHandler(
            DB_USER,
            DB_PASSWORD,
            DB_HOST,
            DB_PORT,
            DB_DATABASE,
        ) as db_con:
            db_con.session.connection().execute(
                text("select * from information_schema.tables")
            )
            return HttpResponse(
                status_code=200,
                body={},
            )

    def save_instalation_settings(self, request: HttpRequest) -> HttpResponse:
        self._check_instalation()
        body = request.body
        update_env(body)
        return HttpResponse(
            status_code=200,
            body={},
        )

    def get_term_acceptance_settings(self, request: HttpRequest) -> HttpResponse:
        body = request.query_params
        acceptance_term_validation(body)
        repo = AcceptanceTermRepository()
        result = repo.find_username_ibge_version(
            body["username"],
            getenv("CIDADE_IBGE", "", False),
            body["version"],
        )
        return HttpResponse(
            status_code=200,
            body=result,
        )

    def save_term_acceptance_settings(self, request: HttpRequest) -> HttpResponse:
        body = request.body
        acceptance_term_validation(body)
        repo = AcceptanceTermRepository()
        repo.save(
            {
                "cod_ibge": getenv("CIDADE_IBGE", "", False),
                "username": body["username"],
                "version": body["version"],
            }
        )
        return HttpResponse(
            status_code=200,
            body={},
        )

    def stop_instalation_settings(self, request: HttpRequest) -> HttpResponse:

        thread = GenerateBase()
        thread.stop()
        s = InstalationStatus()
        s.cancel()
        return HttpResponse(
            status_code=200,
            body={},
        )

    def start_instalation(self, request: HttpRequest) -> HttpResponse:
        scheduler = BackgroundScheduler()
        status, env = is_installed_ok()
        if status:
            s = InstalationStatus()
            s.reset()
            generate_base_scheduled(scheduler)
            return HttpResponse(
                status_code=200,
                body={},
            )
        else:
            null_list = list(filter(lambda x: x[1] is None, env.items()))
            keys = [k[0] for k in null_list]
            keys = ", ".join(keys)
            return HttpResponse(
                status_code=400,
                body={ "message": f"The keys are not configured: {keys}"},
            )
    def instalation_ready(self, request: HttpRequest = None) -> HttpResponse:
        working_directory = os.getcwd()
        files = [
            "crianca.parquet",
            "cadastro_db.parquet",
            "diabetes.parquet",
            "hipertensao.parquet",
            "idoso.parquet",
            "saude_bucal.parquet",
        ]
        completed = True
        total_files = 0
        for file in files:
            file_path = os.path.join(working_directory, "dados", "output", file)
            if not os.path.exists(file_path):
                completed = False
            else:
                total_files += 1

        percentual = round((total_files / len(files)), 2)
        return HttpResponse(
            status_code=200,
            body={
                "completed": completed,
                "percentual": percentual,
            },
        )
    def redirect(self, protocol: Literal['http','https'], port):
        result = self.instalation_ready()
        completed = result.body['completed']
        url = f'localhost:{port}'
        if protocol == 'https':
            url = f'https://{url}'
        else:
            url = f"http://{url}"

        status, _ = is_installed_ok()
        if not status:
            url = f"{url}/configuracao"
        elif not completed:
            url = f"{url}/instalacao"

        thread = threading.Thread(
            target=lambda: webbrowser.open(url)
        )
        thread.start()
