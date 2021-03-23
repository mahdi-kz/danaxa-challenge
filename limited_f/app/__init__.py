from os import makedirs
from flask import (
    Flask,
    render_template,
)

from . import api
from .environment import Config


def create_app():
    app = Flask(
        import_name=__name__,
        instance_relative_config=True,
    )
    app.config.from_object(Config)
    makedirs(
        name=app.instance_path,
        exist_ok=True,
    )
    app.register_blueprint(api.bp)

    # @app.route("/", methods=["GET", ])
    # def index():
    #     return render_template("base.html")

    # @app.shell_context_processor
    # def load_data():
    #     a = authentication.models.User.query.get(1)
    #     m = authentication.models.User.query.get(2)
    #     u = authentication.models.User.query.get(3)
    #     return dict(
    #         app=app,
    #         User=authentication.models.User,
    #         Role=authentication.models.Role,
    #         u=u,
    #         db=db,
    #         m=m,
    #         a=a,
    #     )

    return app
