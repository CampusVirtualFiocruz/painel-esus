from app.models.Exams import ArterialHypertensionExamsList
from app.models.AgeGroup import AgeGroupModelHipertensao
from flask import jsonify, request, Blueprint
import json
from ..helpers.helper import token_required, connection
from app.models.DiabetesAndHypertensionBase import ArterialHypertensionBase
from app.models.AttackModel import HeartAttackModel, HeartAttackSummaryModel
from app.models.IMC import ImcModel
from app.models.Professionals import ProfessionalsList
import traceback
import logging

hypertension_bp = Blueprint('hypertension_bp', __name__)


@hypertension_bp.route('/v1/arterial-hypertension/total', methods=['GET'])
@token_required
def arterialHypertensionTotal():
    hypertension = ArterialHypertensionBase()
    base = hypertension.findByCnes()
    try:

        return jsonify({'message': 'successfully fetched', 'data': base.shape[0]})
    except Exception as e:
        logging.critical(e, exc_info=True)
        return jsonify({'message': 'Error',  'data': 'Error on getting arterial hypertension total information'}), 500


@hypertension_bp.route('/v1/arterial-hypertension/total/<nu_cnes>', methods=['GET'])
@token_required
def arterialHypertensionTotal_nu_cnes(nu_cnes):
    hypertension = ArterialHypertensionBase()
    base = hypertension.findByCnes(nu_cnes)
    try:

        return jsonify({'message': 'successfully fetched', 'data': base.shape[0]})
    except Exception as e:
        logging.critical(e, exc_info=True)
        return jsonify({'message': 'Error',  'data': 'Error on getting arterial hypertension total information'}), 500


@hypertension_bp.route('/v1/arterial-hypertension/age-group-location', methods=['GET'])
@token_required
def arterialHypertensionAgeGroupLocation():
    hypertension = ArterialHypertensionBase()
    base = hypertension.findByCnes()
    groupModel = AgeGroupModelHipertensao()
    try:
        base.apply(lambda row: groupModel.pipelineFn(row), axis=1)
        return jsonify({'message': 'successfully fetched', 'data': groupModel.getLocations()})
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'message': 'Error',  'data': 'Error on getting arterial hypertension location information'}), 500


@hypertension_bp.route('/v1/arterial-hypertension/age-group-location/<nu_cnes>', methods=['GET'])
@token_required
def arterialHypertensionAgeGroupLocationByCnes(nu_cnes):
    hypertension = ArterialHypertensionBase()
    base = hypertension.findByCnes(nu_cnes)
    groupModel = AgeGroupModelHipertensao()
    try:
        base.apply(lambda row: groupModel.pipelineFn(row), axis=1)
        return jsonify({'message': 'successfully fetched', 'data': groupModel.getLocations()})
    except Exception as e:
        logging.critical(e, exc_info=True)
        return jsonify({'message': 'Error',  'data': 'Error on getting arterial hypertension location information'}), 500


@hypertension_bp.route('/v1/arterial-hypertension/age-group-gender', methods=['GET'])
@token_required
def arterialHypertensionAgeGroupGender():
    hypertension = ArterialHypertensionBase()
    base = hypertension.findByCnes()
    groupModel = AgeGroupModelHipertensao()
    try:
        base.apply(lambda row: groupModel.pipelineFn(row), axis=1)
        return jsonify({'message': 'successfully fetched', 'data': groupModel.getLocationsByGender()})
    except Exception as e:
        logging.critical(e, exc_info=True)
        return jsonify({'message': 'Error',  'data': 'Error on getting arterial hypertension location information'}), 5


@hypertension_bp.route('/v1/arterial-hypertension/age-group-gender/<nu_cnes>', methods=['GET'])
@token_required
def arterialHypertensionAgeGroupGenderByCnes(nu_cnes):
    hypertension = ArterialHypertensionBase()
    base = hypertension.findByCnes(nu_cnes)
    groupModel = AgeGroupModelHipertensao()
    try:
        base.apply(lambda row: groupModel.pipelineFn(row), axis=1)
        return jsonify({'message': 'successfully fetched', 'data': groupModel.getLocationsByGender()})
    except Exception as e:
        logging.critical(e, exc_info=True)
        return jsonify({'message': 'Error',  'data': 'Error on getting arterial hypertension location information'}), 5


@hypertension_bp.route('/v1/arterial-hypertension/complications', methods=['GET'])
@token_required
def arterialHypertensionComplications():
    hypertension = ArterialHypertensionBase()
    base = hypertension.findByCnes()
    try:
        heartAttackDisease = HeartAttackModel(base.shape[0])
        base.apply(lambda row: heartAttackDisease.pipelineFn(row), axis=1)
        return jsonify({'message': 'successfully fetched', 'data': heartAttackDisease.getResponse()})
    except Exception as e:
        logging.critical(e, exc_info=True)
        return jsonify({'message': 'Error',  'data': 'Error on getting arterial hypertension complications information'}), 500


@hypertension_bp.route('/v1/arterial-hypertension/complications/<nu_cnes>', methods=['GET'])
@token_required
def arterialHypertensionComplicationsByCnes(nu_cnes):
    hypertension = ArterialHypertensionBase()
    base = hypertension.findByCnes(nu_cnes)
    try:
        heartAttackDisease = HeartAttackModel(base.shape[0])
        base.apply(lambda row: heartAttackDisease.pipelineFn(row), axis=1)
        return jsonify({'message': 'successfully fetched', 'data': heartAttackDisease.getResponse()})
    except Exception as e:
        logging.critical(e, exc_info=True)
        return jsonify({'message': 'Error',  'data': 'Error on getting arterial hypertension complications information'}), 500


@hypertension_bp.route('/v1/arterial-hypertension/imc', methods=['GET'])
@token_required
def arterialHypertensionIMC():
    hypertension = ArterialHypertensionBase()
    base = hypertension.findByCnes()
    try:
        imcModel = ImcModel(base.shape[0])
        base.apply(lambda row: imcModel.pipelineFn(row), axis=1)
        return jsonify({'message': 'successfully fetched', 'data': imcModel.getResponse()})
    except Exception as e:
        logging.critical(e, exc_info=True)
        return jsonify({'message': 'Error',  'data': 'Error on getting arterial hypertension imc information'}), 500


@hypertension_bp.route('/v1/arterial-hypertension/imc/<nu_cnes>', methods=['GET'])
@token_required
def arterialHypertensionIMCByCnes(nu_cnes):
    hypertension = ArterialHypertensionBase()
    base = hypertension.findByCnes(nu_cnes)
    try:
        imcModel = ImcModel(base.shape[0])
        base.apply(lambda row: imcModel.pipelineFn(row), axis=1)
        return jsonify({'message': 'successfully fetched', 'data': imcModel.getResponse()})
    except Exception as e:
        logging.critical(e, exc_info=True)
        return jsonify({'message': 'Error',  'data': 'Error on getting city information'}), 500


@hypertension_bp.route('/v1/arterial-hypertension/proffessionals', methods=['GET'])
@token_required
def arterialHypertensionProffessionals():
    hypertension = ArterialHypertensionBase()
    base = hypertension.findByCnes()
    try:
        hearAttackProfessionalsList = ProfessionalsList()
        base.apply(
            lambda row: hearAttackProfessionalsList.pipelineFn(row), axis=1)
        return jsonify({'message': 'successfully fetched', 'data': hearAttackProfessionalsList.sortResponse()})
    except Exception as e:
        logging.critical(e, exc_info=True)
        return jsonify({'message': 'Error',  'data': 'Error on getting arterial hypertension professionals information'}), 500


@hypertension_bp.route('/v1/arterial-hypertension/proffessionals/<nu_cnes>', methods=['GET'])
@token_required
def arterialHypertensionProffessionalsByCnes(nu_cnes):
    hypertension = ArterialHypertensionBase()
    base = hypertension.findByCnes(nu_cnes)
    try:
        hearAttackProfessionalsList = ProfessionalsList()
        base.apply(
            lambda row: hearAttackProfessionalsList.pipelineFn(row), axis=1)
        return jsonify({'message': 'successfully fetched', 'data': hearAttackProfessionalsList.sortResponse()})
    except Exception as e:
        logging.critical(e, exc_info=True)
        return jsonify({'message': 'Error',  'data': 'Error on getting arterial hypertension professionals information'}), 500


@hypertension_bp.route('/v1/arterial-hypertension/exams', methods=['GET'])
@token_required
def arterialHypertensionExams():
    hypertension = ArterialHypertensionBase()
    base = hypertension.findByCnes()
    try:
        examesList = ArterialHypertensionExamsList()
        base.apply(lambda row: examesList.pipelineFn(row), axis=1)
        return jsonify({'message': 'successfully fetched', 'data': examesList.getResponse()})
    except Exception as e:
        logging.critical(e, exc_info=True)
        return jsonify({'message': 'Error',  'data': 'Error on getting arterial hypertension professionals information'}), 500


@hypertension_bp.route('/v1/arterial-hypertension/exams/<nu_cnes>', methods=['GET'])
@token_required
def arterialHypertensionExamsByCnes(nu_cnes):
    hypertension = ArterialHypertensionBase()
    base = hypertension.findByCnes(nu_cnes)
    try:
        examesList = ArterialHypertensionExamsList()
        base.apply(lambda row: examesList.pipelineFn(row), axis=1)
        return jsonify({'message': 'successfully fetched', 'data': examesList.getResponse()})
    except Exception as e:
        logging.critical(e, exc_info=True)
        return jsonify({'message': 'Error',  'data': 'Error on getting arterial hypertension professionals information'}), 500


@hypertension_bp.route('/v1/get-hypertensive-list', methods=['GET'])
# @token_required
def get_hypertensive_list():
    hypertension = ArterialHypertensionBase()
    base = hypertension.findByCnes()
    try:
        examesList = ArterialHypertensionExamsList()
        base.apply(lambda row: examesList.pipelineFnList(row), axis=1)
        return jsonify({'message': 'successfully fetched', 'data': examesList.getResponselist()})
    except Exception as e:
        logging.critical(e, exc_info=True)
        return jsonify({'message': 'Error',  'data': 'Error on getting arterial hypertension professionals information'}), 500


@hypertension_bp.route('/v1/get-hypertensive-list/<nu_cnes>', methods=['GET'])
@token_required
def get_hypertensive_list_nu_cnes(nu_cnes):
    hypertension = ArterialHypertensionBase()
    base = hypertension.findByCnes(nu_cnes)
    try:
        examesList = ArterialHypertensionExamsList()
        base.apply(lambda row: examesList.pipelineFnList(row), axis=1)
        return jsonify({'message': 'successfully fetched', 'data': json.loads(examesList.getResponselist())}), 200
    except Exception as e:
        logging.critical(e, exc_info=True)
        return jsonify({'message': 'Error',  'data': 'Error on getting arterial hypertension professionals information'}), 500
