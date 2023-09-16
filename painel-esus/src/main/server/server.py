import blueprint_decr
from flask import Flask
from src.main.routes.demographics_info_route import demographics_info_bp
from src.main.routes.diabetes_routes import diabetes_bp
from src.main.routes.login_route import login_bp
from src.main.server.decorators.token_required import token_required

app = Flask(__name__)

# Register Blueprints

app.register_blueprint(login_bp, url_prefix='/v1/auth')
demographics_info_decorated = blueprint_decr.attach(demographics_info_bp, token_required)
app.register_blueprint(demographics_info_decorated, url_prefix='/v1/get-demographic-info')
diabetes_bp_decorated = blueprint_decr.attach(diabetes_bp, token_required)
app.register_blueprint(diabetes_bp_decorated, url_prefix='/v1/diabetes')
