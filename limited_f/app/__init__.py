from flask import Flask

from . import api
from .environment import Config


def create_app():
    app = Flask(
        import_name=__name__,
        instance_relative_config=True,
    )
    app.config.from_object(Config)
    app.register_blueprint(api.bp)

    return app
