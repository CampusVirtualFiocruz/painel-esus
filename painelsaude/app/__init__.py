# from .routes import city, pregnants, arterialHypertension, diabetes
import time
from .routes.accute_infections import accute_infections_blueprint
from .routes.routes import route_bp
from .routes.arterialHypertension import hypertension_bp
from .routes.city import city_bp
from .routes.diabetes import diabetes_bp
from .routes.pregnants import pregnants_bp
import os
from .genbase import generateBases
from flask_cors import CORS
from flask import Flask, jsonify, send_from_directory
import logging
from .models import IreceBase, PregnantsBase
import os

logging.basicConfig(level=logging.DEBUG)


app = Flask(
    __name__,
    static_folder=f'{os.getcwd()}/build'
)
CORS(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


app.register_blueprint(accute_infections_blueprint,
                       url_prefix='/v1/accute_infections')

app.register_blueprint(diabetes_bp)
app.register_blueprint(route_bp)
app.register_blueprint(hypertension_bp)
app.register_blueprint(city_bp)
app.register_blueprint(pregnants_bp)

print('path: ' + os.getcwd())
print("Generating base.....")
start_time = time.time()
generateBases(os.getcwd())
print("--- %s seconds ---" % (time.time() - start_time))
print("------")

file = IreceBase.IreceBase()
file.getBase()
pregnants = PregnantsBase.PregnantsBase()
pregnants.getBase()
