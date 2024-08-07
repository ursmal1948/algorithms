from app.algohub.algorithms.strings.analysis import (
    are_anagrams,
    is_pangram,
    is_palindrome,
    is_potential_palindrome,
    is_substring,
    is_subsequence
)
from flask import request, jsonify, Blueprint, Flask, Response
from flask_json_schema import JsonSchema

from app.routes.schemas import text_schema, anagrams_schema

schema2 = JsonSchema()
strings_analysis_blueprint = Blueprint('string_analysis', __name__,
                                       url_prefix='/api/algorithms/strings/analysis')


@strings_analysis_blueprint.route('/palindrome', methods=['POST'])
@schema2.validate(text_schema)
def handle_is_palindrome() -> Response:
    data = request.json
    text = data['text']
    result = is_palindrome(text)
    return jsonify({'palindrome': result}), 200


@strings_analysis_blueprint.route('/pangram', methods=['POST'])
@schema2.validate(text_schema)
def handle_is_pangram() -> Response:
    data = request.json
    text = data['text']
    result = is_pangram(text)
    return jsonify({'pangram': result}), 200


@strings_analysis_blueprint.route('/anagrams', methods=['POST'])
@schema2.validate(anagrams_schema)
def handle_are_anagrams() -> Response:
    data = request.json
    text1 = data['text1']
    text2 = data['text2']
    result = are_anagrams(text1, text2)
    return jsonify({'anagrams': result}), 200
