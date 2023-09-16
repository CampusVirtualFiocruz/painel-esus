from flask import Flask
from src.main.routes.demographics_info_route import demographics_info_bp
from src.main.routes.diabetes_routes import diabetes_bp
from src.main.routes.login_route import login_bp
app = Flask(__name__)

# Register Blueprints
app.register_blueprint(demographics_info_bp, url_prefix='/v1/get-demographic-info')
app.register_blueprint(diabetes_bp, url_prefix='/v1/diabetes')
app.register_blueprint(login_bp, url_prefix='/v1/auth')
