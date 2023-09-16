from flask import Flask
from src.main.routes.demographics_info_route import demographics_info_bp
app = Flask(__name__)

# Register Blueprints
app.register_blueprint(demographics_info_bp, url_prefix='/v1/get-demographic-info')
