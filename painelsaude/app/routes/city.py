from app import app
from app.models import LoginService, UnidadesService,  IreceBase
from ..models.CityService import getCityInformation
from flask import jsonify, request
import json
from ..helpers.helper import token_required, connection

@app.route('/v1/city-informations', methods=['GET'])
def cityInformations():
    con = connection()
    try:
        data = getCityInformation(con)
        return jsonify({ 'message': 'successfully fetched', 'data': data  })
    except:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting city information' }), 500

