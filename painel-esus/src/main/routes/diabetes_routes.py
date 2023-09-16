from flask import Blueprint, jsonify
from ..server.decorators.token_required import token_required
diabetes_bp = Blueprint("diabetes", __name__)

@diabetes_bp.route('/total', methods=['GET'])
@token_required
def get_total():
    return jsonify('Not Implemented'), 200

@diabetes_bp.route('/age-group-gender', methods=['GET'])
def get_age_group_gender():
    return jsonify('Not Implemented'), 200

@diabetes_bp.route('/age-group-location', methods=['GET'])
def get_age_group_location():
    return jsonify('Not Implemented'), 200

@diabetes_bp.route('/imc', methods=['GET'])
def get_imc():
    return jsonify('Not Implemented'), 200

@diabetes_bp.route('/complications', methods=['GET'])
def get_complications():
    return jsonify('Not Implemented'), 200

@diabetes_bp.route('/exams', methods=['GET'])
def get_exams():
    return jsonify('Not Implemented'), 200

@diabetes_bp.route('/professionals', methods=['GET'])
def get_professionals():
    return jsonify('Not Implemented'), 200
