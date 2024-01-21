import requests
from flask import render_template, request
from flask.views import MethodView
from typing import Any, Tuple, Optional

from logs.logger import logger
from .constants import api_statistics_url, api_fizzbuzz_url


class HomeView(MethodView):
    """
    View for the home page.
    """

    def get(self) -> str:
        """
        Renders the home page template.
        """
        return render_template('home.html')


class StatisticsView(MethodView):
    """
    View for the statistics page.
    """

    def get(self) -> str:
        """
        Fetches statistics from the API and renders the statistics page template.
        """

        try:
            stats_data = requests.get(api_statistics_url)
            stats_data.raise_for_status()
            return render_template('statistics.html', stats=stats_data.json())
        except requests.exceptions.RequestException as e:
            logger.error(f"StatisticsView error: {e}")
            return render_template('error.html', error=str(e))


class FizzBuzzView(MethodView):
    """
    View for processing FizzBuzz requests.
    """

    def post(self) -> str:
        """
        Sends a FizzBuzz request to the API and renders the result page template.
        """

        try:
            response = requests.post(api_fizzbuzz_url, data=request.form)
            response.raise_for_status()

            if response.content:
                stats_data = response.json()
                return render_template('result.html', stats=stats_data)
            else:
                return render_template('error.html', error="Empty response from API")
        except (requests.exceptions.RequestException) as e:
            logger.error(f"FizzBuzzView error: {e}")
            return render_template('error.html', error=str(e))


class NotFoundView(MethodView):
    """
    View for handling 404 Not Found errors.
    """

    def get(self, unmatched) -> Tuple[str, int]:
        """
        Renders the 404 error page template.
        """
        return render_template('404.html'), 404

    def post(self, unmatched) -> Tuple[str, int]:
        """
        Renders the 404 error page template for POST requests.
        """
        return render_template('404.html'), 404
