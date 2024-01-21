import unittest
from app import AppFactory
from database_handler.models import db

class TestFlaskRoutes(unittest.TestCase):
    """
    Test cases for testing the Flask routes.
    These tests ensure that the application routes are correctly configured and
    are returning the expected HTTP responses.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up a test application with a separate test database.
        This method is called once before starting tests in this class.
        """
        cls.app = AppFactory.create_app()
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.app.config['TESTING'] = True
        cls.client = cls.app.test_client()

        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the test database after all tests have completed.
        This method is called once after all tests in this class have run.
        """
        with cls.app.app_context():
            db.drop_all()

    def setUp(self):
        """
        Set up a clean database state before each test.
        This method is called before each test method execution.
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            db.create_all()

    def test_home_route(self):
        """
        Test the home route to ensure it returns a 200 OK response.
        This test verifies that the home page is accessible and responsive.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_statistics_route(self):
        """
        Test the statistics route to ensure it returns a 200 OK response.
        This test checks the accessibility and responsiveness of the statistics page.
        """
        response = self.client.get('/statistics')
        self.assertEqual(response.status_code, 200)

    # Additional tests for other routes can be added here
    # ...

if __name__ == '__main__':
    unittest.main()
