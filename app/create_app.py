from flask import Flask, Response, jsonify
from flask_restful import Api, Resource

from app.routes.numbers.digits import digits_blueprint
from app.routes.strings.string_manipulation import strings_manipulation_blueprint
import logging

logging.basicConfig(level=logging.INFO)


def main() -> Flask:
    app = Flask(__name__)
    with app.app_context():
        #
        #

        @app.errorhandler(Exception)
        def handle_error(error: Exception):
            logging.info("---------------- ERROR START----------------")
            logging.error(error)
            logging.info("---------------- ERROR END----------------")

            return {'messagsse': str(error)}, 500

        app.register_blueprint(digits_blueprint)
        app.register_blueprint(strings_manipulation_blueprint)
    return app


if __name__ == '__main__':
    main()
