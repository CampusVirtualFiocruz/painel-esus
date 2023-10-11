from app.models import LoginService, UnidadesService,  IreceBase
from ..models.CityService import getCityInformation
from flask import jsonify, request, Blueprint
import json
from ..helpers.helper import connection
import logging
city_bp = Blueprint('city_bp', __name__)


@city_bp.route('/v1/city-informations', methods=['GET'])
def cityInformations():
    con = connection()
    try:
        data = getCityInformation(con)
        return jsonify({'message': 'successfully fetched', 'data': data})
    except Exception as e:
        logging.critical(e, exc_info=True)
        return jsonify({'message': 'Error',  'data': 'Error on getting city information'}), 500
