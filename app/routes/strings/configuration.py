from flask import Flask, Blueprint
from app.routes.strings.string_manipulation import schema, string_manipulation_blueprint

# todo dwa sposoby konfiguracji.

def configure_string_manipulation(app: Flask) -> None:
    schema.init_app(app)
    app.register_blueprint(string_manipulation_blueprint)


def configure_string_analysis(app: Flask) -> None:
    pass
