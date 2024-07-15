from app.algohub.algorithms.ciphers.caesar import CaesarCipher
from app.algohub.algorithms.ciphers.morse import MorseCode
from app.algohub.algorithms.ciphers.vigenere import VigenereCipher
from app.algohub.algorithms.ciphers.caesar import CaesarCipher
from flask import request, jsonify, Blueprint

from flask_restful import reqparse

from flask import Flask
import logging

logging.basicConfig(level=logging.INFO)


def configure_caesar_cipher(app: Flask) -> None:
    caesar_cipher = CaesarCipher()

    @app.route('/ciphers/caesar-ecnryption', methods=['POST'])
    def encrypt_text():
        text = request.args.get('text', type=str)
        if not text:
            return jsonify({'message': 'No text provided'}), 400
        shift = request.args.get('shift', type=int)
        if shift:
            caesar_cipher.shift = shift

        encrypted_text = caesar_cipher.encrypt(text)
        return jsonify({'Encrypted_text': f'{encrypted_text}'}), 200

    @app.route('/ciphers/caesar-decryption', methods=['POST'])
    def decrypt_text():
        text = request.args.get('text', type=str)
        if not text:
            return jsonify({'message': 'No text provided'}), 400

        shift = request.args.get('shift', type=int)
        if shift:
            caesar_cipher.shift = shift

        encrypted_text = caesar_cipher.decrypt(text)
        return jsonify({'Encrypted_text': f'{encrypted_text}'}), 200
