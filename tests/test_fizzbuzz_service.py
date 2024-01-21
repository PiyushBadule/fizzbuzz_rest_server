import unittest

from app import AppFactory
from app.models_pydantic import FizzBuzzRequest, FizzBuzzResponse
from app.utils import FizzBuzzService
from database_handler.models import db, Statistics


class TestFizzBuzzService(unittest.TestCase):
    """
    Test cases for testing the FizzBuzzService logic.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up a test application and create a test database.
        """
        # Create app with testing configurations
        cls.app = AppFactory.create_app()
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.app.config['TESTING'] = True

        # Use the existing db instance
        with cls.app.app_context():
            db.create_all()

    def setUp(self):
        """
        Set up a clean database before each test.
        """
        with self.app.app_context():
            db.session.query(Statistics).delete()
            db.session.commit()

    def test_fizzbuzz_logic(self):
        """
        Test the execute_fizzbuzz method for correct FizzBuzz sequence generation.
        This test verifies that the method correctly processes a FizzBuzzRequest
        and returns the expected FizzBuzz sequence in a FizzBuzzResponse.
        """
        with self.app.app_context():
            request_data = FizzBuzzRequest(
                first_integer=3,
                second_integer=5,
                sequence_limit=15,
                first_string='Fizz',
                second_string='Buzz'
            )
            response = FizzBuzzService.execute_fizzbuzz(request_data)
            expected_result = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13',
                               '14', 'FizzBuzz']

            self.assertIsInstance(response, FizzBuzzResponse)
            self.assertEqual(response.result, expected_result)


if __name__ == '__main__':
    unittest.main()
