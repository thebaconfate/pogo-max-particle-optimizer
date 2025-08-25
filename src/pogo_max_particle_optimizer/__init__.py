from flask import Flask
from ..routes.index import blueprint as indexRoute


def create_app() -> Flask:
    app = Flask(__name__, template_folder="../templates/")
    app.register_blueprint(indexRoute)
    return app
