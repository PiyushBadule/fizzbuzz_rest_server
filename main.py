from flask_swagger_ui import get_swaggerui_blueprint
from app.constants import SWAGGER_URL, API_URL

from app import AppFactory, db
from logs.logger import logger


class FlaskAppRunner:
    def __init__(self):
        try:
            self.app = AppFactory.create_app()

            swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL,
                                                          config={'app_name': "FizzBuzz REST API"})
            self.app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

        except Exception as e:
            logger.error(f"Failed to create Flask app: {e}", exc_info=True)
            raise

    def run(self):
        with self.app.app_context():
            # Ensures that the database tables are created
            db.create_all()

        # Start the Flask application
        self.app.run(debug=False)


if __name__ == '__main__':
    runner = FlaskAppRunner()
    runner.run()
