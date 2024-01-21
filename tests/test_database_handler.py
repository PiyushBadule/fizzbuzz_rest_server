import unittest

from flask import Flask

from database_handler.models import db, Statistics


class TestStatisticsModel(unittest.TestCase):
    """
    Test cases for testing interactions with the Statistics model in the database.
    This includes testing the addition and deletion of records.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up a test application and create a test database.
        This method is called once before running all tests.
        """
        cls.app = Flask(__name__)
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        cls.app.config['TESTING'] = True
        db.init_app(cls.app)
        with cls.app.app_context():
            db.create_all()

    def setUp(self):
        """
        Set up a clean database before each test.
        This method is called before each test method.
        """
        with self.app.app_context():
            db.session.query(Statistics).delete()
            db.session.commit()

    def test_add_statistics(self):
        """
        Test adding a new statistics record to the database.
        Ensures that a new record is correctly added to the Statistics table.
        """
        with self.app.app_context():
            new_stat = Statistics(first_integer=3, second_integer=5, sequence_limit=100,
                                  first_string='Fizz', second_string='Buzz', count=1)
            db.session.add(new_stat)
            db.session.commit()

            added_stat = Statistics.query.first()
            self.assertIsNotNone(added_stat)
            self.assertEqual(added_stat.first_integer, 3)
            self.assertEqual(added_stat.second_integer, 5)
            self.assertEqual(added_stat.sequence_limit, 100)
            self.assertEqual(added_stat.first_string, 'Fizz')
            self.assertEqual(added_stat.second_string, 'Buzz')
            self.assertEqual(added_stat.count, 1)

    def test_reset_statistics(self):
        """
        Test clearing all records from the statistics table.
        Ensures that the Statistics table is empty after deletion.
        """
        with self.app.app_context():
            # Add a dummy statistic to ensure the table is not empty
            db.session.add(Statistics(first_integer=2, second_integer=3, sequence_limit=50,
                                      first_string='Test', second_string='Test', count=1))
            db.session.commit()

            # Clear the statistics table
            db.session.query(Statistics).delete()
            db.session.commit()

            stats_count = Statistics.query.count()
            self.assertEqual(stats_count, 0)


if __name__ == '__main__':
    unittest.main()
