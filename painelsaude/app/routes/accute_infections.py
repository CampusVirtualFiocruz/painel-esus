from flask import Blueprint, request, jsonify
from ..usecases.accute_infections.chart_data import get_chart_data
from ..infra.config.logging import logging

accute_infections_blueprint = Blueprint('accute_infections_blueprint', __name__)

@accute_infections_blueprint.route('/get-chart-data', methods=['GET'])
def get_chart_data_request():
    try:
        data = request.args
        start_date, end_date = None, None
        if 'start_date' in data:
            start_date = data['start_date']
        
        if 'end_date' in data:
            end_date = data['end_date']
            
        if start_date and end_date:        
            date_range = [start_date, end_date]
        else:
            date_range = []
            
        response = get_chart_data(date_range)
        return jsonify({ 'data': response.to_dict(orient='records') }), 200      

    except Exception as e:
        logging.exception(e)
        return jsonify({'message': 'Error during login. ' + str(e) }), 500      
