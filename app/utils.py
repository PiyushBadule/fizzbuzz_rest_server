from typing import Optional

from database_handler.models import db, Statistics
from logs.logger import logger
from .models_pydantic import FizzBuzzRequest, FizzBuzzResponse


class FizzBuzzService:
    """
    Service class for handling FizzBuzz logic and database interactions.
    Provides methods to execute FizzBuzz logic, update and retrieve statistics,
    and reset statistics in the database.
    """

    _instance = None

    @classmethod
    def get_instance(cls) -> object:
        """
        Singleton pattern implementation. Returns the existing instance of the class
        or creates a new one if it doesn't exist.

        Returns:
            FizzBuzzService: Instance of the FizzBuzzService class.
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @staticmethod
    def execute_fizzbuzz(request: FizzBuzzRequest) -> FizzBuzzResponse:
        """
        Executes the FizzBuzz logic based on the given request parameters.

        Args:
            request (FizzBuzzRequest): The request parameters for FizzBuzz.

        Returns:
            FizzBuzzResponse: The result of the FizzBuzz calculation.
        """
        try:
            result = []
            for i in range(1, request.sequence_limit + 1):
                if i % request.first_integer == 0 and i % request.second_integer == 0:
                    result.append(request.first_string + request.second_string)
                elif i % request.first_integer == 0:
                    result.append(request.first_string)
                elif i % request.second_integer == 0:
                    result.append(request.second_string)
                else:
                    result.append(str(i))

            # Update statistics
            FizzBuzzService.update_statistics(request)

            logger.info("FizzBuzz logic executed")
            return FizzBuzzResponse(result=result)
        except Exception as e:
            logger.error(f"Error executing FizzBuzz logic: {e}")
            raise

    @staticmethod
    def update_statistics(request: FizzBuzzRequest) -> None:
        """
        Update the statistics in the database based on the FizzBuzz request.

        Args:
            request (FizzBuzzRequest): The request parameters used for FizzBuzz.
        """
        try:
            entry = Statistics.query.filter_by(
                first_integer=request.first_integer,
                second_integer=request.second_integer,
                sequence_limit=request.sequence_limit,
                first_string=request.first_string,
                second_string=request.second_string
            ).first()

            if entry:
                entry.count += 1
            else:
                new_entry = Statistics(
                    first_integer=request.first_integer,
                    second_integer=request.second_integer,
                    sequence_limit=request.sequence_limit,
                    first_string=request.first_string,
                    second_string=request.second_string,
                    count=1
                )
                db.session.add(new_entry)

            db.session.commit()
            logger.info("Statistics updated in the database")
        except Exception as e:
            logger.error(f"Error updating statistics: {e}")
            raise

    @staticmethod
    def get_statistics() -> Optional[dict]:
        """
        Retrieve the most frequent set of parameters used in FizzBuzz requests.

        Returns:
            Optional[dict]: A dictionary containing the most frequently used parameters and their count.
                            Returns None if there are no statistics.
        """
        try:
            most_frequent = Statistics.query.order_by(Statistics.count.desc()).first()

            if not most_frequent:
                return None

            return {
                'first_int': most_frequent.first_integer,
                'second_int': most_frequent.second_integer,
                'limit_val': most_frequent.sequence_limit,
                'first_str': most_frequent.first_string,
                'second_str': most_frequent.second_string,
                'count': most_frequent.count
            }
        except Exception as e:
            logger.error(f"Error retrieving statistics: {e}")
            raise

    @staticmethod
    def reset_statistics() -> None:
        """
        Reset the statistics in the database, removing all existing entries.
        """
        try:
            db.session.query(Statistics).delete()
            db.session.commit()
            logger.info("Statistics reset successfully")
        except Exception as e:
            logger.error(f"Error resetting statistics: {e}")
            raise
