from flask import Blueprint

# Create a Blueprint for frontend routes
frontend_bp = Blueprint('frontend', __name__, template_folder='templates')

# Create a Blueprint for API routes
api_bp = Blueprint('api', __name__)

# Swagger UI configuration
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI
API_URL = '/static/openapi.yaml'  # URL for the OpenAPI specification

api_statistics_url = "http://127.0.0.1:5000/api/statistics"

api_fizzbuzz_url = "http://127.0.0.1:5000/api/fizzbuzz"
