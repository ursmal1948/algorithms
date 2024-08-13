from app.algohub.algorithms.strings.analysis import (
    are_anagrams,
    is_pangram,
    is_palindrome,
    is_potential_palindrome,
    is_substring,
    is_subsequence,
    count_substring_occurences,
    contains_duplicates

)
from flask import request, jsonify, Blueprint, Flask, Response
from flask_json_schema import JsonSchema

from app.routes.schemas import (
    text_schema,
    anagrams_schema,
    text_and_subsequence,
    strings_list_schema
)

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


@strings_analysis_blueprint.route('/potential-palindrome', methods=['POST'])
@schema2.validate(text_schema)
def handle_is_potential_palindrome() -> Response:
    data = request.json
    text = data['text']
    result = is_potential_palindrome(text)
    return jsonify({'potential palindrome': result}), 200


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


@strings_analysis_blueprint.route('/subsequence', methods=['POST'])
@schema2.validate(text_and_subsequence)
def handle_is_subsequence() -> Response:
    data = request.json
    text = data['text']
    subsequence = data['sub_text']
    result = is_subsequence(text, subsequence)
    return jsonify({'subsequence': result}), 200


@strings_analysis_blueprint.route('/substring', methods=['POST'])
@schema2.validate(text_and_subsequence)
def handle_is_substring() -> Response:
    data = request.json
    text = data['text']
    substring = data['sub_text']
    result = is_substring(text, substring)
    return jsonify({'substring': result}), 200


@strings_analysis_blueprint.route('/substring-occurences', methods=['POST'])
@schema2.validate(text_and_subsequence)
def handle_count_substring_occurences() -> Response:
    data = request.json
    text = data['text']
    substring = data['sub_text']
    result = count_substring_occurences(text, substring)
    return jsonify({'substring occurences': result}), 200


@strings_analysis_blueprint.route('/duplicates', methods=['POST'])
@schema2.validate(strings_list_schema)
def handle_contains_duplicates() -> Response:
    data = request.json
    items = data["items"]
    result = contains_duplicates(items)
    return jsonify({'duplicates': result}), 200
