from flask import request, jsonify, Response
from flask.views import MethodView
from pydantic import ValidationError

from logs.logger import logger
from .models_pydantic import FizzBuzzRequest
from .utils import FizzBuzzService
from typing import Tuple, Union

class FizzBuzzAPI(MethodView):
    """
    API endpoint for processing FizzBuzz requests.
    """

    def post(self) -> Union[Tuple[Response, int], Response]:
        """
        Handles POST request to execute the FizzBuzz logic.
        Returns the FizzBuzz result as JSON.
        """
        try:
            data = request.form or request.json
            fizzbuzz_request = FizzBuzzRequest(**data)
            response = FizzBuzzService().execute_fizzbuzz(fizzbuzz_request)
            return jsonify(response.dict())
        except ValidationError as e:
            logger.error(f"Validation Error {e.errors()}")
            return jsonify({"error": str(e.errors())}), 400
        except Exception as e:
            logger.error(f"Error in FizzBuzzAPI: {e}")
            return jsonify({"error": str(e)}), 500


class StatisticsAPI(MethodView):
    """
    API endpoint for retrieving FizzBuzz statistics.
    """

    def get(self) -> Union[Tuple[Response, int], Response]:
        """
        Handles GET request to retrieve statistics.
        Returns the statistics as JSON.
        """
        try:
            fizzbuzzservice = FizzBuzzService.get_instance()
            stats = fizzbuzzservice.get_statistics()
            return jsonify(stats)
        except Exception as e:
            logger.error(f"Error in StatisticsAPI: {e}")
            return jsonify({"error": str(e)}), 500


class ResetStatisticsAPI(MethodView):
    """
    API endpoint for resetting FizzBuzz statistics.
    """

    def post(self) -> Union[Tuple[Response, int], Response]:
        """
        Handles POST request to reset the statistics.
        Returns success message as JSON.
        """
        try:
            FizzBuzzService.reset_statistics()
            return jsonify(message="Statistics reset successfully")
        except Exception as e:
            logger.error(f"Error in ResetStatisticsAPI: {e}")
            return jsonify({"error": str(e)}), 500
