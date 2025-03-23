"""
Main Flask Application Initialization
"""
from flask import Flask, render_template
from flask_migrate import Migrate
from application.database import db
from application.bp.homepage.app import bp as homepage_bp
import config



migrate = Migrate()


def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config.Config())

    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Register The Blueprints
        app.register_blueprint(homepage_bp)
        
        # Create database tables
        db.create_all()

        # Register error handlers
        @app.errorhandler(404)
        def page_not_found(e):
            return render_template('404.html'), 404

    return app
