from flask import Flask, Response, jsonify
from flask_restful import Api, Resource

from app.routes.numbers.digits import digits_blueprint
from app.routes.numbers.divisors import divisors_blueprint
# from app.routes.strings.string_manipulation import strings_manipulation_blueprint
from app.routes.strings.string_analysis import strings_analysis_blueprint
import logging
from app.algohub.algorithms.ciphers.caesar import CaesarCipher
from app.routes.ciphers import configure_ciphers
from app.routes.math.arithmetic_algorithms import configure_arithmetic_algorithms
from app.routes.math.geometric_algorithms import configure_geometric_algorithms
from app.routes.strings.string_analysis import configure_string_analysis
from app.routes.strings.configuration import configure_string_manipulation
from flask_json_schema import JsonSchema

logging.basicConfig(level=logging.INFO)


# api/algorithms/numbers/isprime
def main() -> Flask:
    app = Flask(__name__)
    with app.app_context():
        #
        #
        configure_ciphers(app)
        configure_arithmetic_algorithms(app)
        configure_geometric_algorithms(app)
        configure_string_analysis(app)
        configure_string_manipulation(app)

        # jsonschema = JsonSchema(app)

        @app.errorhandler(Exception)
        def handle_error(error: Exception):
            logging.info("---------------- ERROR START----------------")
            logging.error(error)
            logging.info("---------------- ERROR END----------------")

            return {'message': str(error)}, 500

        @app.route('/hello')
        def hello():
            cs = CaesarCipher()
            text = cs.encrypt('ABCD')
            return jsonify({'text': text})

        app.register_blueprint(digits_blueprint)
        app.register_blueprint(divisors_blueprint)
        app.register_blueprint(strings_analysis_blueprint)

        return app


if __name__ == '__main__':
    main()
