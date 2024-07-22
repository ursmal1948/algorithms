from flask import Blueprint, jsonify, request

from app.algohub.algorithms.numbers.divisors import (
    count_divisors,
    count_common_divisors,
    sum_divisors
)

divisors_blueprint = Blueprint('divisors', __name__, url_prefix='/api/algorithms/numbers/divisors')


@divisors_blueprint.route('/<int:number>', methods=['GET'])
def handle_divisors(number):
    action = request.args.get('action')
    if action == 'count':
        result = count_divisors(number)
    elif action == 'sum':
        result = sum_divisors(number)
    else:
        return jsonify({'message': 'Invalid action'}), 400
    return jsonify({'result': result, 'action': action}), 200


@divisors_blueprint.route('/count-common-divisors', methods=['GET'])
def common_divisors():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    count_of_common_divisors = count_common_divisors(a, b)
    return jsonify({'count': count_of_common_divisors}), 200
