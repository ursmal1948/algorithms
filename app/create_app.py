from flask import Flask, Response, jsonify
from flask_restful import Api, Resource

import logging
from app.algohub.algorithms.ciphers.caesar import CaesarCipher
from app.routes.ciphers import configure_ciphers
from app.routes.strings.string_analysis import configure_string_analysis
from app.routes.strings.configuration import configure_string_manipulation
from app.routes.numbers.configuration import configure_digits
from app.routes.math.configuration import configure_math
# from app.routes.strings.string_analysis import strings_analysis_blueprint

logging.basicConfig(level=logging.INFO)


def main() -> Flask:
    app = Flask(__name__)
    with app.app_context():
        configure_ciphers(app)

        configure_string_analysis(app)
        configure_string_manipulation(app)
        configure_digits(app)
        configure_math(app)

        # app.register_blueprint(strings_analysis_blueprint)

        @app.errorhandler(Exception)
        def handle_error(error: Exception):
            logging.info("---------------- ERROR START----------------")
            logging.error(error)
            logging.info("---------------- ERROR END----------------")

            return {'message': str(error)}, 500

        return app


if __name__ == '__main__':
    main()
