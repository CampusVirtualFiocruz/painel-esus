from app import app
from app.models import LoginService, UnidadesService, IreceBase
from flask import jsonify, request, render_template, send_from_directory
import json
from ..helpers.helper import token_required, auth, connection
import logging

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def loginform():
    return render_template('index.html')

@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)


@app.route('/v1/auth', methods=['POST'])
def _auth():
  try:
    return auth()
  except Exception as e:
    return jsonify({'message': 'Error during login. ' + str(e) }), 400      



  
@app.route('/v1/get-demographic-info', methods=['GET'])
@token_required
def getData():
  try:
    data = IreceBase.IreceBase()
    print(data.getDemographicInfo())
    return jsonify({'message': 'successfully fetched', 'data': data.getDemographicInfo() })    
  except Exception as e:
    logging.critical(e, exc_info=True)
    return jsonify({'message': 'Error during Get Demographic Info' }), 400      

@app.route('/v1/get-units', methods=['GET'])
@token_required
def getDataUnits():
  try:
    con = connection()
    return jsonify({'message': 'successfully fetched', 'data': UnidadesService.getUnits(con).to_dict('records') })    
  except:
    return jsonify({'message': 'Error during Get Units' }), 400 

@app.route('/v1/get-demographic-info/<nu_cnes>', methods=['GET'])
@token_required
def getDataByNuCnes(nu_cnes):
  logging.info( f'nu_cnes: {nu_cnes}')
  try:
    data = IreceBase.IreceBase()
    return jsonify({'message': 'successfully fetched', 'data': data.getDemographicInfo(nu_cnes) })    
  except Exception as e:
    logging.critical(e, exc_info=True) 
    return jsonify({'message': 'Error during Get Data By CNES.'}), 400 
