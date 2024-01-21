from pathlib import Path

from flask import Flask

from database_handler.models import db
from logs.logger import logger
from .urls import frontend_bp, api_bp
from .utils import FizzBuzzService
from typing import NoReturn


class AppFactory:
    """
    A factory class responsible for creating, configuring, and initializing
    an instance of a Flask application with necessary components like database,
    logging, and blueprints.

    This class encapsulates the setup logic for the Flask app, ensuring that
    all components are correctly initialized and configured before the app starts.
    """

    @staticmethod
    def create_app():
        """
        Create and configure an instance of the Flask application. This includes
        initializing the database, setting up logging, and registering blueprints.

        The method handles exceptions during the app creation process and logs
        appropriate error messages.

        Returns:
            Flask: The created and configured Flask app.

        Raises:
            Exception: Propagates exceptions that occur during app initialization.
        """
        try:
            app = Flask(__name__, template_folder='../templates', static_folder='../static')

            # Locate the base directory (two levels up from this file)
            base_dir = Path(__file__).resolve().parent.parent

            # Construct the path to the database
            db_path = base_dir / 'database_handler' / 'fizzbuzz.db'

            app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
            app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

            db.init_app(app)

            # Initialize FizzBuzzService without needing to pass the app instance
            FizzBuzzService.get_instance()

            # Setup logging
            AppFactory.setup_logging(app)

            # Register blueprints
            AppFactory.register_blueprints(app)

            logger.info('FizzBuzz app initialized')
            return app
        except Exception as e:
            logger.error(f"Error in creating Flask app: {e}", exc_info=True)
            raise

    @staticmethod
    def setup_logging(app: Flask):
        """
        Set up logging for the application using the custom logger.

        Integrates the custom logger with the Flask app, enabling unified logging
        throughout the application.

        Args:
            app (Flask): The Flask app instance to configure logging for.
        """
        app.logger = logger

    @staticmethod
    def register_blueprints(app: Flask) -> NoReturn:
        """
        Register blueprints for the application. This method is responsible for
        adding the blueprints to the Flask app, which defines routes and views.

        Args:
            app (Flask): The Flask app instance to register blueprints on.
        """
        app.register_blueprint(frontend_bp)
        app.register_blueprint(api_bp)
