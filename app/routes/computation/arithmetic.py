from flask import Blueprint, jsonify, request, Response

from app.algohub.algorithms.computation.arithmetic import (
    IterativeFactorial,
    RecursiveFactorial,
    binary_search
)
from flask_json_schema import JsonSchema
import logging
from app.routes.schemas import binary_search_schema

schema2 = JsonSchema()

logging.basicConfig(level=logging.INFO)

arithmetic_algorithms_blueprint = Blueprint(
    'arithmetic_algorithms',
    __name__,
    url_prefix='/api/algorithms/computation/arithmetic'
)


@arithmetic_algorithms_blueprint.route('/factorial/<string:method>/<int:number>', methods=['GET'])
def handle_factorial(method, number: int) -> Response:
    if method == 'iterative':
        return jsonify({'factorial': IterativeFactorial().calculate_factorial(number), 'method': 'iterative'}), 200
    if method == 'recursive':
        return jsonify({'factorial': RecursiveFactorial().calculate_factorial(number), 'method': 'recursive'}), 200
    else:
        return jsonify({'message': 'Wrong factorial method'}), 400


@arithmetic_algorithms_blueprint.route('/binary-search', methods=['POST'])
@schema2.validate(binary_search_schema)
def handle_binary_search() -> Response:
    json_body = request.json
    numbers, target = json_body['numbers'], json_body['target']
    result = binary_search(numbers, target)

    if result is False:
        return jsonify({'message': 'Number not found'}), 400

    return jsonify({'result': result}), 200
