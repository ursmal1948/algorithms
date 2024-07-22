from flask import Flask
from app.routes.math.geometric_algorithms import schema, geometric_algorithms_blueprint
from app.routes.math.arithmetic_algorithms import arithmetic_algorithms_blueprint, schema2


def configure_math(app: Flask) -> None:
    schema.init_app(app)
    schema2.init_app(app)
    app.register_blueprint(geometric_algorithms_blueprint)
    app.register_blueprint(arithmetic_algorithms_blueprint)
