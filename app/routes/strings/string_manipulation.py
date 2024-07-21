from app.algohub.algorithms.strings.string_manipulation import (
    reverse,
    compress,
    custom_join,
    lower,
    upper
)

from flask import Blueprint, request, jsonify, Response, Flask
from flask_json_schema import JsonSchema
from app.routes.schemas import (
    text_schema,
    text_and_separator_schema,
    text_and_case_schema)
import logging

logging.basicConfig(level=logging.INFO)

string_manipulation_blueprint = Blueprint('string_manipulation',
                                          __name__,
                                          url_prefix='/api/algorithms/strings/string-manipulation')
schema = JsonSchema()


@string_manipulation_blueprint.route('/reverse', methods=['POST'])
@schema.validate(text_schema)
def handle_reverse() -> Response:
    json_body = request.json
    text = json_body['text']
    if not text.strip():
        return jsonify({'message': 'empty string'}), 400
    reversed_text = reverse(text)
    return jsonify({'reversed': reversed_text}), 200


@string_manipulation_blueprint.route('/compress', methods=['POST'])
@schema.validate(text_schema)
def handle_compress() -> Response:
    json_body = request.json
    text = json_body['text']
    if not text.strip():
        return jsonify({'message': 'empty string'}), 400
    compressed_text = compress(text)
    return jsonify({'compressed': compressed_text}), 200


@string_manipulation_blueprint.route('/join', methods=['POST'])
@schema.validate(text_and_separator_schema)
def handle_custom_join() -> Response:
    json_body = request.json
    text = json_body['text']
    if not text.strip():
        return jsonify({'message': 'empty string'}), 400
    separator = json_body.get('separator', '-')
    items = list(text)
    joined_text = custom_join(items, separator)
    return jsonify({'joined': joined_text}), 200


@string_manipulation_blueprint.route('/transform', methods=['POST'])
@schema.validate(text_and_case_schema)
def handle_lower_upper_case() -> Response:
    json_body = request.json
    text = json_body['text']
    if not text.strip():
        return jsonify({'message': 'empty string'}), 400
    case = json_body.get('case', 'lower')
    if case not in ['lower', 'upper']:
        return jsonify({'message': 'invalid case'}), 400
    if case == 'lower':
        return jsonify({'lowered': lower(text)}), 200
    if case == 'upper':
        return jsonify({'uppered': upper(text)}), 200
