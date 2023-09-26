import os

import blueprint_decr
from flask import Flask, send_from_directory, jsonify

from src.main.routes.demographics_info_route import demographics_info_bp
from src.main.routes.diabetes_routes import diabetes_bp
from src.main.routes.hypertension_routes import hypertension_bp
from src.main.routes.login_route import login_bp
from src.main.server.decorators.token_required import token_required
from flask_cors import CORS

app = Flask(
    __name__,
    static_folder=f'{os.getcwd()}/../paineis-v2-front/build'
)
CORS(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')


# Register Blueprints

@app.route('/v1/city-informations', methods=['GET'])
def city():
    return jsonify('ok'), 200


app.register_blueprint(login_bp, url_prefix='/v1/auth')
demographics_info_decorated = blueprint_decr.attach(
    demographics_info_bp, token_required)
app.register_blueprint(demographics_info_decorated,
                       url_prefix='/v1/get-demographic-info')
# diabetes_bp_decorated = blueprint_decr.attach(diabetes_bp, token_required)
app.register_blueprint(diabetes_bp, url_prefix='/v1/diabetes')
app.register_blueprint(hypertension_bp, url_prefix='/v1/arterial-hypertension')
