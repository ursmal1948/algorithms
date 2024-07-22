from app.algohub.algorithms.ciphers.caesar import CaesarCipher
from app.algohub.algorithms.ciphers.morse import MorseCode
from app.algohub.algorithms.ciphers.vigenere import VigenereCipher
from app.algohub.algorithms.ciphers.caesar import CaesarCipher
from flask import request, jsonify, Blueprint, Flask, Response
from flask_json_schema import JsonSchema
from app.routes.schemas import caesar_schema, vigenere_schema, text_schema, morse_decryption_schema

import logging

logging.basicConfig(level=logging.INFO)

ciphers_blueprint = Blueprint('ciphers', __name__, url_prefix='/api/algorithms/ciphers')
schema = JsonSchema()


def configure_ciphers(app: Flask) -> None:
    schema.init_app(app)
    app.register_blueprint(ciphers_blueprint)


@ciphers_blueprint.route('/caesar-encryption', methods=['POST'])
@schema.validate(caesar_schema)
def handle_caesar_encryption() -> Response:
    json_body = request.json
    text = json_body['text']
    shift = json_body.get('shift', 3)
    if not text.strip():
        return jsonify({'message': 'empty string'}), 400
    cs = CaesarCipher(shift=shift)
    encrypted_text = cs.encrypt(text)
    return jsonify({'encrypted': encrypted_text}), 200


@ciphers_blueprint.route('/caesar-decryption', methods=['POST'])
@schema.validate(caesar_schema)
def handle_caesar_decryption() -> Response:
    json_body = request.json
    text = json_body['text']
    shift = json_body.get('shift', 3)
    if not text.strip():
        return jsonify({'message': 'empty string'}), 400
    cs = CaesarCipher(shift=shift)
    decrypted_text = cs.decrypt(text)
    return jsonify({'decrypted': decrypted_text}), 200


@ciphers_blueprint.route('/vigenere-encryption', methods=['POST'])
@schema.validate(vigenere_schema)
def handle_vigenere_encryption() -> Response:
    json_body = request.json
    text = json_body['text']
    key = json_body.get('key', None)
    if not text.strip():
        return jsonify({'message': 'empty string'}), 400
    # domyslna wartosc, w roucie, czy  wklasie,
    vs = VigenereCipher() if key is None else VigenereCipher(key)
    encrypted_text = vs.encrypt(text)
    return jsonify({'encrypted': encrypted_text}), 200


@ciphers_blueprint.route('/vigenere-decryption', methods=['POST'])
@schema.validate(vigenere_schema)
def handle_vigenere_decryption() -> Response:
    json_body = request.json
    text = json_body['text']
    key = json_body.get('key', None)
    if not text.strip():
        return jsonify({'message': 'empty string'}), 400
    # default value for key
    vs = VigenereCipher() if key is None else VigenereCipher(key)
    decrypted_text = vs.decrypt(text)
    return jsonify({'decrypted': decrypted_text}), 200


@ciphers_blueprint.route('/morse-encryption', methods=['POST'])
@schema.validate(text_schema)
def handle_morse_encryption() -> Response:
    json_body = request.json
    text = json_body['text']
    if not text.strip():
        return jsonify({'message': 'empty string'}), 400

    morse_code = MorseCode()
    encrypted_text = morse_code.encrypt(text)
    return jsonify({'encrypted': encrypted_text}), 200


@ciphers_blueprint.route('/morse-decryption', methods=['POST'])
@schema.validate(morse_decryption_schema)
def handle_morse_decryption() -> Response:
    json_body = request.json
    text = json_body['text']
    if not text.strip():
        return jsonify({'message': 'empty string'}), 400

    morse_code = MorseCode()
    encrypted_text = morse_code.decrypt(text)
    return jsonify({'decrypted': encrypted_text}), 200
