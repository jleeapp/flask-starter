from flask import Flask
from .config import Config
from .extensions import db, migrate


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.config.from_pyfile("config.py", silent=True)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .routes import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
