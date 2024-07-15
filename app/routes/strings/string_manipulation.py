from app.algohub.algorithms.strings.string_manipulation import (
    reverse,
    compress,
    custom_join,
    lower,
    upper
)

from flask import Blueprint, request, jsonify
import logging

logging.basicConfig(level=logging.INFO)

strings_manipulation_blueprint = Blueprint('strings_manipulation', __name__, url_prefix='/strings_manipulation')


# todo wszystko zrobione ze string manipulation

@strings_manipulation_blueprint.route('/reverse', methods=['POST'])
def reverse_():
    text = request.args.get('text', type=str)

    if not text:
        return jsonify({'message': 'No text provided'}), 400
    reversed_text = reverse(text)
    return jsonify({'Text reversed successfuly': reversed_text}), 201


# jak nie podam queyr params w ogole to ABACDA,a jak podam pusty to wejdzie w warunek


@strings_manipulation_blueprint.route('/compress', methods=['POST'])
def compress_():
    # http://localhost/strings_manipulation/compress? to bedzie ABACDA
    # text = request.args.get('text', type=str, default='ABACDA').strip()
    # http://localhost/strings_manipulation/compress?text a jak cos takiego to bedzie empty string.
    text = request.args.get('text', type=str)
    if not text:
        return jsonify({'message': 'No text provided'}), 400
    compressed_text = compress(text)
    return jsonify({'Text compressed successfuly': compressed_text}), 201


@strings_manipulation_blueprint.route('/join', methods=['POST'])
def custom_join_():
    text = request.args.get('text', type=str)
    if not text:
        return jsonify({'message': 'No text provided'}), 400

    sep = request.args.get('sep', type=str)
    if not sep:
        return jsonify({'message': 'No seperator provided'}), 400
    text_items = list(text)
    new_text = custom_join(text_items, sep)
    return jsonify({'Text joined successfuly': new_text}), 201


# moge zrobic ze cos tam= lower albo cos tam = upper jako query params
# case
@strings_manipulation_blueprint.route('/<string:text>', methods=['POST'])
def transform(text: str):
    if not text:
        return jsonify({'message': 'No text provided'}), 400
    case = request.args.get('case', type=str)

    if case not in ['lower', 'upper']:
        return jsonify({'message': 'Case is invalid'}), 400

    if case == 'lower':
        return jsonify({'Text lowercased successfuly': lower(text)}), 201
    if case == 'upper':
        return jsonify({'Text uppercased successfuly': upper(text)}), 201
