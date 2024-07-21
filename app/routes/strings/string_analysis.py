from app.algohub.algorithms.strings.string_analysis import (
    are_anagrams,
    is_pangram,
    is_palindrome,
    is_potential_palindrome,
    is_substring,
    is_subsequence
)
from flask import request, jsonify, Blueprint, Flask, Response
from flask_json_schema import JsonSchema


strings_analysis_blueprint = Blueprint('string_analysis', __name__, url_prefix='/string-analysis')

from app.routes.schemas import text_schema, anagrams_schema


def configure_string_analysis(app: Flask) -> None:
    schema = JsonSchema(app)

    @app.route('/api/algorithms/string-analysis/palindrome', methods=['POST'])
    @schema.validate(text_schema)
    def handle_is_palindrome() -> Response:
        data = request.json
        text = data['text']
        if not text.strip():
            return jsonify({'palindrome': False, 'message': 'empty string'}), 400
        result = is_palindrome(text)
        return jsonify({'palindrome': result}), 200

    @app.route('/api/algorithms/string-analysis/pangram', methods=['POST'])
    @schema.validate(text_schema)
    def handle_is_pangram() -> Response:
        data = request.json
        text = data['text']
        result = is_pangram(text)
        return jsonify({'pangram': result}), 200

    @app.route('/api/algorithms/string-analysis/anagrams', methods=['POST'])
    @schema.validate(anagrams_schema)
    def handle_are_anagrams() -> Response:
        data = request.json
        text1 = data['text1']
        text2 = data['text2']
        result = are_anagrams(text1, text2)
        return jsonify({'anagrams': result}), 200

