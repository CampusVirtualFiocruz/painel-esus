# pylint: disable=C0301, W0611
import os

# from src.main.server.decorators.check_access import check_access
import sys

import blueprint_decr
from flask import Flask, send_from_directory
from flask_cors import CORS
from src.env import env as config
from src.main.routes.admin_settings import (
    AdminSettingsPath,
    admin_settings_bp,
    admin_settings_path,
)
from src.main.routes.city_informations_route import CityInfoPath, city_informations_bp
from src.main.routes.demographic_route import DemographicPath, demographics_bp
from src.main.routes.diabetes_routes import DiabetesPath, diabetes_bp
from src.main.routes.elderly_routes import ElderlyPath, elderly_bp
from src.main.routes.hypertension_routes import HypertensionPath, hypertension_bp
from src.main.routes.infantil_routes import ChildrenPath, children_bp
from src.main.routes.login_route import login_bp
from src.main.routes.oral_health import OralHealthPath, oral_health_bp
from src.main.routes.records_routes import RecordsPath, records_bp
from src.main.routes.settings import SettingsPath, settings_bp, settings_path
from src.main.routes.units_route import TeamsPath, UnitsPath, teams_bp, units_bp
from src.main.server.cache import cache
from src.main.server.decorators.token_required import token_required

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

import logging as logger

from src.presentations import rich_banner

log = logger.getLogger("werkzeug")
log.disabled = True
cli = sys.modules["flask.cli"]
# cli.show_server_banner = lambda *x: logging.info(banner_message())
cli.show_server_banner = lambda *x: rich_banner()
# tell Flask to use the above defined config

if config["ENV"] == "instalador":
    static_folder = os.path.join(os.getcwd(), "static-files")
elif config["ENV"] == "windows":
    static_folder = os.path.join(os.getcwd(), "..", "paineis-v2-front", "static-files")
    static_folder = os.path.relpath(static_folder)
else:
    static_folder = os.path.join(os.getcwd(), "..", "paineis-v2-front", "static-files")
    static_folder = os.path.abspath(static_folder)

app = Flask(__name__, static_folder=f"{static_folder}")
CORS(app)

cache.init_app(app)
app.json.sort_keys = False


def register_blueprint(_app, blueprint, decorators_list):
    if len(decorators_list) > 0:
        for idx, decorator in enumerate(decorators_list):
            decorated = blueprint_decr.attach(blueprint[0], decorator)
            _app.register_blueprint(
                decorated, url_prefix=blueprint[1], name=f"{blueprint[1]}-{idx}"
            )
    else:
        _app.register_blueprint(
            blueprint[0], url_prefix=blueprint[1], name=f"{blueprint[1]}"
        )


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(app.static_folder + "/" + path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")


# Register Blueprints


app.register_blueprint(login_bp, url_prefix="/v1/auth")

city_info = CityInfoPath()
register_blueprint(
    app,
    (city_informations_bp, city_info.root_path),
    [cache.cached(timeout=24 * 60 * 60)],
)


units = UnitsPath()
app.register_blueprint(units_bp, url_prefix=units.root_path)

teams = TeamsPath()
app.register_blueprint(teams_bp, url_prefix=teams.root_path)


demographics_info = DemographicPath()
register_blueprint(
    app,
    (demographics_bp, demographics_info.root_path),
    [token_required, cache.cached(timeout=24 * 60 * 60, query_string=True)],
)

diabetes = DiabetesPath()
register_blueprint(
    app,
    (diabetes_bp, diabetes.root_path),
    [token_required, cache.cached(timeout=24 * 60 * 60, query_string=True)],
)

hypertension = HypertensionPath()
register_blueprint(
    app,
    (hypertension_bp, hypertension.root_path),
    [token_required, cache.cached(timeout=24 * 60 * 60, query_string=True)],
)


oral_path = OralHealthPath()
register_blueprint(app, (oral_health_bp, oral_path.root_path), [token_required])

# smoking = SmokingPath()
# register_blueprint(
#     app,
#     (smoking_bp, smoking.root_path),
#     [token_required, cache.cached(timeout=24 * 60 * 60, query_string=True)],
# )

children = ChildrenPath()
register_blueprint(
    app,
    (children_bp, children.root_path),
    [token_required, cache.cached(timeout=24 * 60 * 60, query_string=True)],
)

elderly = ElderlyPath()
register_blueprint(
    app,
    (elderly_bp, elderly.root_path),
    [token_required, cache.cached(timeout=24 * 60 * 60, query_string=True)],
)

settings = SettingsPath()
register_blueprint(
    app,
    (settings_bp, settings.root_path),
    [],
)
admin_settings = AdminSettingsPath()
register_blueprint(
    app,
    (admin_settings_bp, admin_settings.root_path),
    [],
)


records = RecordsPath()
register_blueprint(
    app,
    (records_bp, records.root_path),
    [token_required, cache.cached(timeout=24 * 60 * 60, query_string=True)],
)
