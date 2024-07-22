from app.algohub.algorithms.numbers.digits import (
    get_digit,
    sum_digits,
    sum_range,
    validate_luhn,
    move_zeroes
)
from flask import request, jsonify, Blueprint, Response
from flask_restful import reqparse

from flask_json_schema import JsonSchema
from app.routes.schemas import range_schema, numbers_list_schema, text_schema
import logging

logging.basicConfig(level=logging.INFO)

digits_blueprint = Blueprint('digits', __name__, url_prefix='/api/algorithms/numbers/digits')
schema = JsonSchema()


@digits_blueprint.route('/get_digit/number/<int:number>/position/<int:position>', methods=['GET'])
def handle_get_digit(number: int, position: int) -> Response:
    digit = get_digit(number, position)
    return jsonify({'digit': digit}), 200


@digits_blueprint.route('/digits-sum/<int:number>', methods=['GET'])
def handle_sum_digits(number: int) -> Response:
    digits_sum = sum_digits(number)
    return jsonify({'sum': digits_sum}), 201


@digits_blueprint.route('/range-sum', methods=['POST'])
@schema.validate(range_schema)
def handle_sum_range() -> Response:
    json_body = request.get_json()
    a, b = json_body['r_start'], json_body['r_end']
    return jsonify({'Sum': sum_range(a, b)}), 200


#
@digits_blueprint.route('/move-zeroes', methods=['POST'])
@schema.validate(numbers_list_schema)
def handle_move_zeroes():
    json_body = request.get_json()
    numbers = json_body['numbers']
    if 0 not in numbers or numbers[len(numbers) - 1] == 0:
        return jsonify({'message': 'No zeroes to move', 'numbers': numbers}), 200

    move_zeroes(numbers)
    return jsonify({'message': 'Zeroes moved to the end', 'numbers': numbers}), 200


@digits_blueprint.route('/luhn', methods=['GET'])
def handle_validate_luhn() -> Response:
    card_number = request.args.get('card_number').strip()
    if not card_number:
        return jsonify({'message': 'Empty string provided'}), 400

    result = validate_luhn(card_number)
    if result:
        return jsonify({'message': 'card number is valid', 'card_number': card_number}), 200
    return jsonify({'message': 'card number is invalid', 'card_number': card_number}), 200
