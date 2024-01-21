from .constants import frontend_bp, api_bp

from logs.logger import logger  # Import your custom logger
from .api_routes import FizzBuzzAPI, StatisticsAPI, ResetStatisticsAPI
from .frontend_routes import HomeView, StatisticsView, FizzBuzzView, NotFoundView

# Add URL rules for frontend routes
frontend_bp.add_url_rule('/', view_func=HomeView.as_view('home'))
frontend_bp.add_url_rule('/statistics', view_func=StatisticsView.as_view('statistics'), methods=['GET'])
frontend_bp.add_url_rule('/fizzbuzz', view_func=FizzBuzzView.as_view('fizzbuzz'), methods=['POST'])

# Registering NotFoundView as a catch-all for unmatched routes
frontend_bp.add_url_rule('/<path:unmatched>', view_func=NotFoundView.as_view('not_found'), methods=['GET', 'POST'])

# Add URL rules for API routes
api_bp.add_url_rule('/api/fizzbuzz', view_func=FizzBuzzAPI.as_view('api_fizzbuzz'), methods=['POST'])
api_bp.add_url_rule('/api/statistics', view_func=StatisticsAPI.as_view('api_statistics'), methods=['GET'])
api_bp.add_url_rule('/api/reset_statistics', view_func=ResetStatisticsAPI.as_view('reset_statistics'), methods=['POST'])

logger.info("Blueprints for frontend and API routes have been created and configured.")
