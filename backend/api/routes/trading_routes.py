from flask import Blueprint, jsonify, request
from trading_logic.strategy import execute_strategy
from trading_logic.signal_processing import process_signals

trading_blueprint = Blueprint('trading_routes', __name__)

@trading_blueprint.route('/execute', methods=['POST'])
def execute_trade():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400

    strategy_result = execute_strategy(data)
    return jsonify({'result': strategy_result})

@trading_blueprint.route('/process_signals', methods=['POST'])
def process_signals_route():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400

    signal_result = process_signals(data)
    return jsonify({'signals': signal_result})
