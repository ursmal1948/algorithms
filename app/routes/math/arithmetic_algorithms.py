from flask import Blueprint, jsonify, request, Flask
from flask_restful import reqparse, request

from app.algohub.algorithms.math.arithmetic_algorithms import (
    IterativeFactorial,
    RecursiveFactorial,
    binary_search,
    babylonian_sqrt,
    binary_exponentiation
)
import logging

logging.basicConfig(level=logging.INFO)


def configure_arithmetic_algorithms(app: Flask) -> None:
    @app.route('/factorial/<int:number>', methods=['GET'])
    def handle_factorial(number: int):
        method = request.args.get("method", default='iter')
        if method == 'iter':
            return jsonify({'Iterative factorial': IterativeFactorial().calculate_factorial(number)}), 200
        if method == 'recursive':
            return jsonify({'Recursive factorial': RecursiveFactorial().calculate_factorial(number)}), 200
        else:
            return jsonify({'message': 'Wrong factorial method'}), 400

    @app.route('/binary-search', methods=['GET'])
    def handle_binary_search():
        parser = reqparse.RequestParser()
        parser.add_argument('numbers', type=list, help='List of numbers', location='json')
        parser.add_argument('target', type=int, help='Target number')
        request_data = parser.parse_args()
        numbers = request_data['numbers']
        target = request_data['target']
        if numbers is None or target is None:
            return jsonify({'error': 'Numbers or / and target not provided'}), 400
        looked_number_index = binary_search(numbers, target)
        if looked_number_index is not None:
            return jsonify({f'Number {target} at index': looked_number_index}), 200
        return jsonify({'message': 'number not found in the array'}), 404
