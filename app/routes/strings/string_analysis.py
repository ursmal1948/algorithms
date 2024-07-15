from app.algohub.algorithms.strings.string_analysis import (
    are_anagrams,
    is_pangram,
    is_palindrome,
    is_potential_palindrome,
    is_substring,
    is_subsequence
)
from flask import request, jsonify, Blueprint
strings_analysis_blueprint = Blueprint('string_analysis', __name__, url_prefix='/string-analysis')


# TODO PALINDROME VS PANGRAM MOZE JEDEN ROUTE, i rozbic na warunki w zaleznosci od query params
#   np type palindrome ?type=palindrome albo type=pangram
#    dokoknczyc string analysis routes. I moze zaczac  math czy ciphers.
@strings_analysis_blueprint.route('/valid-palindrome', methods=['GET'])
def check_palindrome():
    if not (text := request.args.get('text')):
        return jsonify({'message': 'No text provided'}), 400

    result = is_palindrome(text)
    return jsonify({f'Valid palindrome: {text}': result}), 200


@strings_analysis_blueprint.route('/valid-pangram', methods=['GET'])
def check_pangram():
    if not (text := request.args.get('text')):
        return jsonify({'message': 'No text provided'}), 400

    result = is_pangram(text)
    return jsonify({f'Valid pangram: {text}': result}), 200


# query params
@strings_analysis_blueprint.route('/valid-anagrams', methods=['GET'])
def check_anagrams():
    if not (text1 := request.args.get('text1')) or not (text2 := request.args.get('text2')):
        return jsonify({'message': 'Missing parameters'})
    
    result = are_anagrams(text1, text2)
    return jsonify({f'Valid anagrams: {text1} & {text2}': result}), 200
