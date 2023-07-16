from app import app
from app.models.PregnantsService import PregnantsService
from app.models.PregnantsBase import PregnantsBase
from app.models.IreceBase import IreceBase
from ..models.CityService import getCityInformation
from flask import jsonify, request
import json
from ..helpers.helper import token_required, connection


@app.route('/v1/pregnants/prenatal-indicators', methods=['GET'])
@token_required
def prenatalIndicators():
    pregnantsData = PregnantsBase()
    data = pregnantsData.getBase()
    pregnants = PregnantsService()
    try:
        result = pregnants.prenatalIndicators(data)
        return jsonify({ 'message': 'successfully fetched', 'data': result  })
    except Exception as e:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting Pregnants Indicators. ' + str(e) }), 500

@app.route('/v1/pregnants/prenatal-indicators/<nu_cnes>', methods=['GET'])
@token_required
def prenatalIndicatorsByCns(nu_cnes):
    pregnantsData = PregnantsBase()
    data = pregnantsData.getBase()
    pregnants = PregnantsService()
    try:
        result = pregnants.prenatalIndicators(data, nu_cnes)
        return jsonify({ 'message': 'successfully fetched', 'data': result  })
    except Exception as e:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting Pregnants Indicators. ' + str(e) }), 500

@app.route('/v1/pregnants/obstetrics-factors', methods=['GET'])
@token_required
def obstetricFactors():
    pregnantsData = PregnantsBase()
    data = pregnantsData.getBase()
    pregnants = PregnantsService()
    try:
        result = pregnants.obstetricFactors(data)
        return jsonify({ 'message': 'successfully fetched', 'data': result  })
    except Exception as e:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting Obstetrics Factors. '+str(e)  }), 500

@app.route('/v1/pregnants/obstetrics-factors/<nu_cnes>', methods=['GET'])
@token_required
def obstetricFactorsBynu_cnes(nu_cnes):
    pregnantsData = PregnantsBase()
    data = pregnantsData.getBase()
    pregnants = PregnantsService()
    try:
        result = pregnants.obstetricFactors(data, nu_cnes)
        return jsonify({ 'message': 'successfully fetched', 'data': result  })
    except Exception as e:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting Obstetrics Factors. '+str(e)  }), 500        

@app.route('/v1/pregnants/per-weeks', methods=['GET'])
@token_required
def pregnatsPerages():
    pregnantsData = PregnantsBase()
    data = pregnantsData.getBase()
    pregnants = PregnantsService()
    try:
        result = pregnants.pregnatsPerages(data)
        return jsonify({ 'message': 'successfully fetched', 'data': result  })
    except Exception as e:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting city information'+str(e) }), 500


@app.route('/v1/pregnants/per-weeks/<nu_cnes>', methods=['GET'])
@token_required
def pregnatsPeragesBynu_cnes(nu_cnes):
    pregnantsData = PregnantsBase()
    data = pregnantsData.getBase()
    pregnants = PregnantsService()
    try:
        result = pregnants.pregnatsPerages(data, nu_cnes)
        return jsonify({ 'message': 'successfully fetched', 'data': result  })
    except Exception as e:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting city information'+str(e) }), 500

@app.route('/v1/pregnants/total-per-trimester', methods=['GET'])
@token_required
def totalPregnatsByTrimester():
    pregnantsData = PregnantsBase()
    data = pregnantsData.getBase()
    pregnants = PregnantsService()
    try:
        # result = pregnants.byTrimester(data)
        result = pregnants.byTrimester(data)
        return jsonify({ 'message': 'successfully fetched', 'data': result  })
    except Exception as e:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting city information'+str(e) }), 500   

@app.route('/v1/pregnants/total-per-trimester/<nu_cnes>', methods=['GET'])
@token_required
def totalPregnatsByTrimesterBynu_cnes(nu_cnes):
    pregnantsData = PregnantsBase()
    data = pregnantsData.getBase()
    pregnants = PregnantsService()
    try:
        # result = pregnants.byTrimester(data, nu_cnes)
        result = pregnants.byTrimester(data, nu_cnes)
        print(result)
        return jsonify({ 'message': 'successfully fetched', 'data': result  })
    except Exception as e:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting city information'+str(e) }), 500               

@app.route('/v1/pregnants/per-trimester/<trimester>', methods=['GET'])
@token_required
def pregnatsByTrimester(trimester):
    page = 1 
    if request.args.get('page') is not None:
        page = int(request.args.get('page'))
    con = connection()
    pregnantsData = PregnantsBase()
    data = pregnantsData.getBase()
    pregnants = PregnantsService()
    try:
        result = pregnants.pregnantsByTrimester(data, trimester, page, pregnantsData, con)
        return jsonify({ 'message': 'successfully fetched', 'data': result[0], 'total': result[1]  })
    except Exception as e:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting pregnants information. '+str(e) }), 500 

@app.route('/v1/pregnants/per-trimester/<trimester>/<nu_cnes>', methods=['GET'])
@token_required
def pregnatsByTrimesterBynu_cnes(trimester, nu_cnes):
    page = 1
    if request.args.get('page')  is not None:
        page = int(request.args.get('page')) 
    con = connection()
    pregnantsData = PregnantsBase()
    data = pregnantsData.getBase()
    pregnants = PregnantsService()
    try:
        result = pregnants.pregnantsByTrimester(data, trimester, page, pregnantsData, con, nu_cnes)
        return jsonify({ 'message': 'successfully fetched', 'data': result[0], 'total': result[1]  })
    except Exception as e:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting pregnants information'+str(e) }), 500         

@app.route('/v1/pregnants/per-weekly-range/<weekly>', methods=['GET'])
@token_required
def pregnatsByWeekly(weekly):
    page = 1 
    if request.args.get('page') is not None:
        page = int(request.args.get('page'))
    con = connection()
    pregnantsData = PregnantsBase()
    data = pregnantsData.getBase()
    pregnants = PregnantsService()
    try:
        result = pregnants.pregnantsWeeklyRange(data, weekly, page, pregnantsData, con)
        return jsonify({ 'message': 'successfully fetched', 'data': result[0], 'total': result[1]  })
    except Exception as e:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting pregnants information. '+str(e) }), 500 

@app.route('/v1/pregnants/per-weekly-range/<weekly>/<nu_cnes>', methods=['GET'])
@token_required
def pregnatsByWeeklyBynu_cnes(weekly, nu_cnes):
    page = 1
    if request.args.get('page')  is not None:
        page = int(request.args.get('page')) 
    con = connection()
    pregnantsData = PregnantsBase()
    data = pregnantsData.getBase()
    pregnants = PregnantsService()
    try:
        result = pregnants.pregnantsWeeklyRange(data, weekly, page, pregnantsData, con, nu_cnes)
        return jsonify({ 'message': 'successfully fetched', 'data': result[0], 'total': result[1]  })
    except Exception as e:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting pregnants information'+str(e) }), 500      

@app.route('/v1/pregnants/exams-table', methods=['GET'])
@token_required
def pregnantsExamstable():
    try:
        pregnants = PregnantsService()
        pregnantsData = PregnantsBase()
        data = pregnantsData.getBase()
        response = pregnants.examsAndResultsTable(data)
        return jsonify({ 'message': 'successfully fetched', 'data': response  })
    except Exception as e:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting pregnants information '+str(e) }), 500


@app.route('/v1/pregnants/exams-table/<nu_cnes>', methods=['GET'])
@token_required
def pregnantsExamstableBynu_cnes(nu_cnes):
    try:
        pregnants = PregnantsService()
        pregnantsData = PregnantsBase()
        data = pregnantsData.getBase()
        response = pregnants.examsAndResultsTable(data, nu_cnes)
        return jsonify({ 'message': 'successfully fetched', 'data': response  })
    except Exception as e:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting pregnants information'+str(e) }), 500        

@app.route('/v1/pregnants/pregnants-table', methods=['GET'])
@token_required
def pregnantstable():
    try:
        page = 1
        if request.args.get('page')  is not None:
            page = int(request.args.get('page'))
        con = connection()
        pregnantsData = PregnantsBase()

        pregnants = PregnantsService()
        pregnantsData = PregnantsBase()
        data = pregnantsData.getBase()
        mestreBase = IreceBase()
        mestre = mestreBase.getBase()
        response = pregnants.pregnantsTable(data, mestre, page, pregnantsData, con)
        return jsonify({ 'message': 'successfully fetched', 'data': response[0], 'total': response[1]   })
    except Exception as e:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting pregnants table information. '+str(e) }), 500


@app.route('/v1/pregnants/pregnants-table/<nu_cnes>', methods=['GET'])
@token_required
def pregnantstableBynu_cnes(nu_cnes):
    try:
        page = 1
        if request.args.get('page')  is not None:
            page = int(request.args.get('page')) 

        con = connection()
        
        pregnants = PregnantsService()
        pregnantsData = PregnantsBase()
        data = pregnantsData.getBase()
        mestreBase = IreceBase()
        mestre = mestreBase.getBase()

        response = pregnants.pregnantsTable(data, mestre, page, pregnantsData, con, nu_cnes)
        return jsonify({ 'message': 'successfully fetched', 'data': response[0], 'total': response[1]  })
    except Exception as e:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting pregnants  table information. '+str(e) }), 500        



@app.route('/v1/pregnants/by-id/<pec>', methods=['GET'])
@token_required
def pregnantstableByPec(pec):
    try:
        con = connection()
        
        pregnantsData = PregnantsBase()
        response = pregnantsData.pregnantsByPec( con, pec)
        return jsonify({ 'message': 'successfully fetched', 'data': response  })
    except Exception as e:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting pregnants  information. '+str(e) }), 500        
