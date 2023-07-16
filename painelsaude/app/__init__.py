from flask import Flask, jsonify
import logging
from .models import IreceBase, PregnantsBase
logging.basicConfig(level=logging.DEBUG)
from flask_cors import CORS
from .genbase import generateBases
import os


app = Flask(__name__,
    template_folder='../build',
    static_url_path='/static/',
    static_folder='../build/static/'
)
CORS(app)
print("Generating base.....")
import time
start_time = time.time()
# generateBases()
print("--- %s seconds ---" % (time.time() - start_time))
print("------" )

file = IreceBase.IreceBase()
file.getBase()
pregnants = PregnantsBase.PregnantsBase()
# pregnants.getBase()



from .routes import routes, city, pregnants, arterialHypertension, diabetes