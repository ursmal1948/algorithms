from flask import Blueprint, Flask
from app.routes.numbers.digits import schema, digits_blueprint
from app.routes.numbers.divisors import divisors_blueprint


def configure_digits(app: Flask) -> None:
    schema.init_app(app)
    app.register_blueprint(digits_blueprint)
    app.register_blueprint(divisors_blueprint)
