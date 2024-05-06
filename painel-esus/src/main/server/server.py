# pylint: disable=C0301, W0611
import os

import blueprint_decr
from dotenv import dotenv_values
from flask import Flask
from flask import send_from_directory
from flask_cors import CORS
from src.env import env
from src.errors.logging import logging
from src.main.routes.city_informations_route import city_informations_bp
from src.main.routes.city_informations_route import CityInfoPath
from src.main.routes.demographics_info_route import DemographichInfoPath
from src.main.routes.demographics_info_route import demographics_info_bp
from src.main.routes.diabetes_routes import diabetes_bp
from src.main.routes.diabetes_routes import DiabetesPath
from src.main.routes.hypertension_routes import hypertension_bp
from src.main.routes.hypertension_routes import HypertensionPath
from src.main.routes.login_route import login_bp
from src.main.routes.oral_health import oral_health_bp
from src.main.routes.oral_health import OralHealthPath
from src.main.routes.units_route import units_bp
from src.main.routes.units_route import UnitsPath
from src.main.server.cache import cache
from src.main.server.decorators.token_required import token_required

# from src.main.server.decorators.check_access import check_access

app = Flask(__name__)
# tell Flask to use the above defined config
config = dotenv_values(".env")
print('ENV ', config["ENV"])

if config["ENV"] == "instalador":
    static_folder = os.path.join(os.getcwd(), 'static-files')
elif config["ENV"] == "windows":
    static_folder = os.path.join(
        os.getcwd(), '..', 'paineis-v2-front', 'static-files')
    static_folder = os.path.relpath(static_folder)
else:
    static_folder = os.path.join(
        os.getcwd(), '..', 'paineis-v2-front', 'static-files')
    static_folder = os.path.abspath(static_folder)
print('STATIC FOLDER: ', static_folder)

app = Flask(
    __name__,
    static_folder=f'{static_folder}'
)
CORS(app)

cache.init_app(app)
app.json.sort_keys = False


def register_blueprint(_app, blueprint, decorators_list):
    for idx, decorator in enumerate(decorators_list):
        decorated = blueprint_decr.attach(blueprint[0], decorator)
        _app.register_blueprint(decorated,
                                url_prefix=blueprint[1],
                                name=f'{blueprint[1]}-{idx}'
                                )


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')


# Register Blueprints


app.register_blueprint(login_bp, url_prefix='/v1/auth')

city_info = CityInfoPath()
register_blueprint(
    app,
    (city_informations_bp, city_info.root_path),
    [cache.cached(timeout=24*60*60)]
)


units = UnitsPath()
app.register_blueprint(units_bp,
                       url_prefix=units.root_path)

demographics_info = DemographichInfoPath()
register_blueprint(
    app, (demographics_info_bp, demographics_info.root_path),
    [token_required])

diabetes = DiabetesPath()
register_blueprint(
    app, (diabetes_bp, diabetes.root_path), [token_required])

hypertension = HypertensionPath()
register_blueprint(
    app, (hypertension_bp, hypertension.root_path), [token_required])


oral_path = OralHealthPath()
register_blueprint(
    app, (oral_health_bp, oral_path.root_path), [token_required])
