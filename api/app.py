from typing import List
from flask import Blueprint, Flask, redirect, url_for, request
from alchemical.flask import Alchemical
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_mail import Mail
from apifairy import APIFairy
from config import Config
from dataclasses import dataclass, field

db = Alchemical()
migrate = Migrate()
ma = Marshmallow()
cors = CORS()
mail = Mail()
apifairy = APIFairy()


@dataclass
class Module:
    blueprint: Blueprint
    indexed: bool = field(default=True)


def create_app(models, modules: List[Module], config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # extensions
    db.init_app(app)
    migrate.init_app(app, db, directory=app.config["MIGRATION_DIR"])
    ma.init_app(app)
    if app.config["USE_CORS"]:  # pragma: no branch
        cors.init_app(app)
    mail.init_app(app)
    apifairy.init_app(app)

    # blueprints
    for module in modules:
        if module.indexed:
            app.register_blueprint(module.blueprint, url_prefix="/api")
        else:
            app.register_blueprint(module.blueprint)

    # define the shell context
    @app.shell_context_processor
    def shell_context():  # pragma: no cover
        ctx = {"db": db}
        for attr in dir(models):
            model = getattr(models, attr)
            if hasattr(model, "__bases__") and db.Model in getattr(model, "__bases__"):
                ctx[attr] = model
        return ctx

    @app.route("/")
    def index():  # pragma: no cover
        return redirect(url_for("apifairy.docs"))

    @app.after_request
    def after_request(response):
        # Werkzeu sometimes does not flush the request body so we do it here
        request.get_data()
        return response

    return app
