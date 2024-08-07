from flask import Flask
from app.routes.computation.geometric import schema, geometric_algorithms_blueprint
from app.routes.computation.arithmetic import arithmetic_algorithms_blueprint, schema2
from app.routes.computation.function import function_algorithms_blueprint, schema_3
from app.routes.computation.numeric import numeric_algorithms_blueprint


def configure_computation(app: Flask) -> None:
    schema.init_app(app)
    schema2.init_app(app)
    schema_3.init_app(app)
    app.register_blueprint(geometric_algorithms_blueprint)
    app.register_blueprint(arithmetic_algorithms_blueprint)
    app.register_blueprint(function_algorithms_blueprint)
    app.register_blueprint(numeric_algorithms_blueprint)
