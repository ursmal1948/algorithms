from flask import Flask

import logging
from app.routes.ciphers import configure_ciphers
from app.routes.strings.configuration import configure_strings
from app.routes.numbers.configuration import configure_digits
from app.routes.computation.configuration import configure_computation

logging.basicConfig(level=logging.INFO)


def configure_routes(app: Flask) -> None:
    configure_ciphers(app)
    configure_strings(app)
    configure_digits(app)
    configure_computation(app)


def main() -> Flask:
    app = Flask(__name__)
    with app.app_context():
        configure_routes(app)

        @app.errorhandler(Exception)
        def handle_error(error: Exception):
            logging.info("---------------- ERROR START----------------")
            logging.error(error)
            logging.info("---------------- ERROR END----------------")

            return {'message': str(error)}, 500

    return app


if __name__ == '__main__':
    main()
