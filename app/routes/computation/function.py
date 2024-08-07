from app.algohub.algorithms.function import (
    quadratic_roots,
    horner_evaluation
)
from app.routes.schemas import (
    quadratic_equation_coefficiets_schema,
    horner_schema
)

from flask_json_schema import JsonSchema

from flask import Blueprint, jsonify, Response, request
import logging

logging.basicConfig(level=logging.INFO)
function_algorithms_blueprint = Blueprint(
    'function_algorithms',
    __name__,
    url_prefix='/api/algorithms/computation/function'
)

schema_3 = JsonSchema()


@function_algorithms_blueprint.route('/quadratic-roots', methods=['POST'])
@schema_3.validate(quadratic_equation_coefficiets_schema)
def handle_quadratic_roots() -> Response:
    json_body = request.json
    a = json_body['a']
    b = json_body.get('b', 0)
    c = json_body.get('c', 0)
    root_result = quadratic_roots(a, b, c)
    return jsonify({'result': root_result}), 200


@function_algorithms_blueprint.route('/horner', methods=['POST'])
@schema_3.validate(horner_schema)
def handle_horner_evaluation() -> Response:
    json_body = request.json
    coefficients = json_body['coefficients']
    value = json_body['value']
    result = horner_evaluation(coefficients, value)
    return jsonify({'result': result}), 200
