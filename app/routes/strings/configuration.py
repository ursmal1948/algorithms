from flask import Flask, Blueprint
from app.routes.strings.manipulation import schema, string_manipulation_blueprint
from app.routes.strings.analysis import schema2, strings_analysis_blueprint


def configure_strings(app: Flask) -> None:
    schema.init_app(app)
    schema2.init_app(app)
    app.register_blueprint(string_manipulation_blueprint)
    app.register_blueprint(strings_analysis_blueprint)
