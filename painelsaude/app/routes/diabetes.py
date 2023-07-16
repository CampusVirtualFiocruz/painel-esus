from app import app
from app.models.Exams import DiabetesExamsList
from app.models.AgeGroup import AgeGroupModelDiabetes
from flask import jsonify, request
import json
from ..helpers.helper import token_required, connection
from app.models.DiabetesAndHypertensionBase import DiabetesBase
from app.models.AttackModel import DiabeticDiseaseModel, DiabeticDiseaseSummaryModel
from app.models.IMC import ImcModel
from app.models.Professionals import ProfessionalsList
import traceback    

@app.route('/v1/diabetes/total', methods=['GET'])
@token_required
def diabetesTotal():
    diabetes = DiabetesBase()
    base = diabetes.findByCnes()
    try:
        
        return jsonify({ 'message': 'successfully fetched', 'data': base.shape[0]  })
    except:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting arterial diabetes total information' }), 500

@app.route('/v1/diabetes/total/<nu_cnes>', methods=['GET'])
@token_required
def diabetesTotal_nu_cnes(nu_cnes):
    diabetes = DiabetesBase(nu_cnes)
    base = diabetes.findByCnes(nu_cnes)
    try:
        
        return jsonify({ 'message': 'successfully fetched', 'data': base.shape[0]  })
    except:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting arterial diabetes total information' }), 500


@app.route('/v1/diabetes/age-group-location', methods=['GET'])
@token_required
def diabetesAgeGroupLocation():
    diabetes = DiabetesBase()
    base = diabetes.findByCnes()
    groupModel = AgeGroupModelDiabetes()
    try:
        base.apply( lambda row: groupModel.pipelineFn(row), axis=1)
        return jsonify({ 'message': 'successfully fetched', 'data': groupModel.getLocations()  })
    except Exception as e: 
        print(traceback.format_exc())
        return jsonify({ 'message': 'Error',  'data': 'Error on getting arterial diabetes location information' }), 500

@app.route('/v1/diabetes/age-group-location/<nu_cnes>', methods=['GET'])
@token_required
def diabetesAgeGroupLocationByCnes(nu_cnes):
    diabetes = DiabetesBase()
    base = diabetes.findByCnes(nu_cnes)
    groupModel = AgeGroupModelDiabetes()
    try:
        base.apply( lambda row: groupModel.pipelineFn(row), axis=1)
        return jsonify({ 'message': 'successfully fetched', 'data': groupModel.getLocations()  })
    except:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting arterial diabetes location information' }), 500



@app.route('/v1/diabetes/age-group-gender', methods=['GET'])
@token_required
def diabetesAgeGroupGender():
    diabetes = DiabetesBase()
    base = diabetes.findByCnes()
    groupModel = AgeGroupModelDiabetes()
    try:
        base.apply( lambda row: groupModel.pipelineFn(row), axis=1)
        return jsonify({ 'message': 'successfully fetched', 'data': groupModel.getLocationsByGender()  })
    except:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting arterial diabetes location information' }), 5

@app.route('/v1/diabetes/age-group-gender/<nu_cnes>', methods=['GET'])
@token_required
def diabetesAgeGroupGenderByCnes(nu_cnes):
    diabetes = DiabetesBase()
    base = diabetes.findByCnes(nu_cnes)
    groupModel = AgeGroupModelDiabetes()
    try:
        base.apply( lambda row: groupModel.pipelineFn(row), axis=1)
        return jsonify({ 'message': 'successfully fetched', 'data': groupModel.getLocationsByGender()  })
    except:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting arterial diabetes location information' }), 5


@app.route('/v1/diabetes/complications', methods=['GET'])
@token_required
def diabetesComplications():
    diabetes = DiabetesBase()
    base = diabetes.findByCnes()
    try:
        diabetesDisease = DiabeticDiseaseModel(base.shape[0])
        base.apply( lambda row: diabetesDisease.pipelineFn(row), axis=1)
        return jsonify({ 'message': 'successfully fetched', 'data': diabetesDisease.getResponse()  })
    except:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting arterial diabetes complications information' }), 500 

@app.route('/v1/diabetes/complications/<nu_cnes>', methods=['GET'])
@token_required
def diabetesComplicationsByCnes(nu_cnes):
    diabetes = DiabetesBase()
    base = diabetes.findByCnes(nu_cnes)
    try:
        diabetesDisease = DiabeticDiseaseModel(base.shape[0])
        base.apply( lambda row: diabetesDisease.pipelineFn(row), axis=1)
        return jsonify({ 'message': 'successfully fetched', 'data': diabetesDisease.getResponse()  })
    except:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting arterial diabetes complications information' }), 500 



@app.route('/v1/diabetes/imc', methods=['GET'])
@token_required
def diabetesIMC():  
    diabetes = DiabetesBase()
    base = diabetes.findByCnes()
    try:
        imcModel = ImcModel(base.shape[0])
        base.apply( lambda row: imcModel.pipelineFn(row), axis=1)
        return jsonify({ 'message': 'successfully fetched', 'data': imcModel.getResponse()  })
    except:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting arterial diabetes imc information' }), 500

@app.route('/v1/diabetes/imc/<nu_cnes>', methods=['GET'])
@token_required
def diabetesIMCByCnes(nu_cnes):  
    diabetes = DiabetesBase()
    base = diabetes.findByCnes(nu_cnes)
    try:
        imcModel = ImcModel(base.shape[0])
        base.apply( lambda row: imcModel.pipelineFn(row), axis=1)
        return jsonify({ 'message': 'successfully fetched', 'data': imcModel.getResponse()  })
    except:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting city information' }), 500


@app.route('/v1/diabetes/proffessionals', methods=['GET'])
@token_required
def diabetesProffessionals():
    diabetes = DiabetesBase()
    base = diabetes.findByCnes()
    try:
        diabetesProfessionalsList = ProfessionalsList()
        base.apply( lambda row: diabetesProfessionalsList.pipelineFn(row), axis=1)
        return jsonify({ 'message': 'successfully fetched', 'data': diabetesProfessionalsList.sortResponse()  })
    except:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting arterial diabetes professionals information' }), 500

@app.route('/v1/diabetes/proffessionals/<nu_cnes>', methods=['GET'])
@token_required
def diabetesProffessionalsByCnes(nu_cnes):
    diabetes = DiabetesBase()
    base = diabetes.findByCnes(nu_cnes)
    try:
        diabetesProfessionalsList = ProfessionalsList()
        base.apply( lambda row: diabetesProfessionalsList.pipelineFn(row), axis=1)
        return jsonify({ 'message': 'successfully fetched', 'data': diabetesProfessionalsList.sortResponse()  })
    except:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting arterial diabetes professionals information' }), 500

@app.route('/v1/diabetes/exams', methods=['GET'])
@token_required
def diabetesExams():
    diabetes = DiabetesBase()
    base = diabetes.findByCnes()
    try:
        examesList = DiabetesExamsList()
        base.apply( lambda row: examesList.pipelineFn(row), axis=1)
        return jsonify({ 'message': 'successfully fetched', 'data': examesList.getResponse()  })
    except:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting arterial diabetes professionals information' }), 500

@app.route('/v1/diabetes/exams/<nu_cnes>', methods=['GET'])
@token_required
def diabetesExamsByCnes(nu_cnes):
    diabetes = DiabetesBase()
    base = diabetes.findByCnes(nu_cnes)
    try:
        examesList = DiabetesExamsList()
        base.apply( lambda row: examesList.pipelineFn(row), axis=1)
        return jsonify({ 'message': 'successfully fetched', 'data': examesList.getResponse()  })
    except:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting arterial diabetes professionals information' }), 500

@app.route('/v1/get-diabetes-list', methods=['GET'])
@token_required
def get_diabetes_list():
    diabetes = DiabetesBase()
    base = diabetes.getBase()
    try:
        diabetesModel = DiabeticDiseaseSummaryModel(base.shape[0], base)
        base.apply( lambda row: diabetesModel.pipelineFn(row), axis=1)
        return jsonify({ 'message': 'successfully fetched', 'data': diabetesModel.result  })
    except:
        return jsonify({ 'message': 'Error',  'data': 'Error on getting Diabetes list' })