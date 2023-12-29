# pylint: disable=C0301
import os

import blueprint_decr
from flask import Flask, send_from_directory
from flask_cors import CORS
from src.main.routes.city_informations_route import city_informations_bp
from src.main.routes.demographics_info_route import demographics_info_bp
from src.main.routes.diabetes_routes import diabetes_bp
from src.main.routes.hypertension_routes import hypertension_bp
from src.main.routes.login_route import login_bp
from src.main.routes.oral_health import oral_health_bp
from src.main.routes.units_route import units_bp
from src.main.server.cache import cache
# from src.main.server.decorators.check_access import check_access
from src.main.server.decorators.token_required import token_required

app = Flask(__name__)
# tell Flask to use the above defined config

app = Flask(
    __name__,
    static_folder=f'{os.getcwd()}/../paineis-v2-front/build'
)
CORS(app)

cache.init_app(app)


def register_blueprint(_app, blueprint, decorators_list):
    for idx, decorator in enumerate(decorators_list):
        decorated = blueprint_decr.attach(blueprint[0], decorator)
        _app.register_blueprint(decorated,
                                url_prefix=blueprint[1], name=f'{blueprint[1]}-{idx}')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')


# Register Blueprints


app.register_blueprint(login_bp, url_prefix='/v1/auth')

register_blueprint(
    app, (city_informations_bp, '/v1/city-informations'), [cache.cached(timeout=24*60*60)])

app.register_blueprint(units_bp,
                       url_prefix='/v1/get-units')

register_blueprint(
    app, (demographics_info_bp, '/v1/get-demographic-info'),
    [token_required, cache.cached(timeout=24*60*60)])

register_blueprint(
    app, (diabetes_bp, '/v1/diabetes'), [token_required])

register_blueprint(
    app, (hypertension_bp, '/v1/arterial-hypertension'), [token_required])

register_blueprint(
    app, (oral_health_bp, '/v1/oral-health'), [token_required])
