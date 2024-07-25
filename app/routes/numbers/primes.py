from flask import request, jsonify, Blueprint, Response
from flask_restful import reqparse

from flask_json_schema import JsonSchema
from app.routes.schemas import eratosthenes_schema
from app.algohub.algorithms.numbers.primes import (
    ErastothenesSieve,
    is_prime_basic,
    get_prime_factors,
    is_perfect_number
)
import logging

logging.basicConfig(level=logging.INFO)

primes_blueprint = Blueprint('primes', __name__, url_prefix='/api/algorithms/numbers/primes')
schema2 = JsonSchema()


@primes_blueprint.route('/erastosthenes-sieve', methods=['POST'])
@schema2.validate(eratosthenes_schema)
def handle_erastothenes_sieve():
    json_body = request.json
    sieve_upper_limit = json_body['sieve_upper_limit']
    looked_number = json_body['looked_number']
    sieve = ErastothenesSieve(sieve_upper_limit)
    result = sieve.is_prime(looked_number)
    return {'result': result}, 200


@primes_blueprint.route('/is-prime/<int:number>', methods=['GET'])
def handle_is_prime(number: int) -> Response:
    result = is_prime_basic(number)
    if result:
        return jsonify({'message': 'Number is prime', "number": number}), 200
    return jsonify({'message': 'Number is not prime', "number": number}), 200


@primes_blueprint.route('/prime-factors/<int:number>', methods=['GET'])
def handle_get_prime_factors(number: int) -> Response:
    prime_factors = get_prime_factors(number)
    return jsonify({'prime factors': prime_factors}), 200


@primes_blueprint.route('/perfect-number/<int:number>', methods=['GET'])
def handle_is_perfect_number(number: int) -> Response:
    is_perfect = is_perfect_number(number)
    if is_perfect:
        return jsonify({'message': 'Number is perfect', "number": number}), 200
    return jsonify({'message': 'Number is not perfect', "number": number}), 200
