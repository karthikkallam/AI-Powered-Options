from flask import Blueprint, jsonify, request
from data_acquisition.fetch_data import fetch_market_data
from data_acquisition.preprocess_data import preprocess_data

data_blueprint = Blueprint('data_routes', __name__)

@data_blueprint.route('/fetch', methods=['GET'])
def fetch_data_route():
    try:
        data = fetch_market_data()
        return jsonify({'data': data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@data_blueprint.route('/preprocess', methods=['POST'])
def preprocess_data_route():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400
    
    try:
        processed_data = preprocess_data(data)
        return jsonify({'processed_data': processed_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
