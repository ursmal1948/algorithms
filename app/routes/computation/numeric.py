from flask import Blueprint, jsonify, request, Response
import jsonschema
from app.algohub.algorithms.numeric import (
    bisection_root,
    RectangularIntegration,
    TrapezoidalIntegration
)

from app.algohub.utility_functions import (
    execute_function_from_string,
    create_polynomial_function
)
from app.routes.schemas import (
    bisection_root_schema,
    trapezoidal_integration_schema,
    rectangular_integration_schema
)

numeric_algorithms_blueprint = Blueprint(
    'numeric_algorithms',
    __name__,
    url_prefix='/api/algorithms/computation/numeric'
)


@numeric_algorithms_blueprint.route('/trapezoidal-integration', methods=['POST'])
def handle_trapezoidal_integration() -> Response:
    json_body = request.json
    jsonschema.validate(instance=json_body, schema=trapezoidal_integration_schema)
    function_body = json_body['function_body']
    a, b = json_body['a'], json_body['b']
    n = json_body['n']
    result = TrapezoidalIntegration().calculate(lambda x: execute_function_from_string(function_body, x),
                                                a, b, n
                                                )
    return jsonify({'integration result': result}), 200


@numeric_algorithms_blueprint.route('/rectangular-integration', methods=['POST'])
def handle_rectangular_integration() -> Response:
    json_body = request.json
    jsonschema.validate(instance=json_body, schema=rectangular_integration_schema)
    coefficients = json_body['coefficients']
    a, b = json_body['a'], json_body['b']
    n = json_body['n']
    function_from_coeff = create_polynomial_function(coefficients)
    result = RectangularIntegration().calculate(lambda x: function_from_coeff(x), a, b, n)

    return jsonify({'integration result': result}), 200


@numeric_algorithms_blueprint.route('/bisection-root', methods=['POST'])
def handle_bisection_root():
    json_body = request.json
    jsonschema.validate(instance=json_body, schema=bisection_root_schema)
    coefficients = json_body.get('coefficients', None)

    a = json_body['a']
    b = json_body['b']
    if not coefficients:
        function_body = json_body['function_body']
        root = bisection_root(lambda x: execute_function_from_string(function_body, x), a, b)
        return jsonify({'root': root}), 200

    function_from_coeff = create_polynomial_function(coefficients)

    root = bisection_root(lambda x: function_from_coeff(x), a, b)
    return jsonify({'root': root}), 200
