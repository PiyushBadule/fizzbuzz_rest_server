from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Statistics(db.Model):
    """
    Model to store statistics for FizzBuzz requests.

    Attributes:
        id (int): Primary key.
        first_integer (int): First integer used in FizzBuzz calculation.
        second_integer (int): Second integer used in FizzBuzz calculation.
        sequence_limit (int): Limit for the FizzBuzz sequence.
        first_string (str): String to replace multiples of the first integer.
        second_string (str): String to replace multiples of the second integer.
        count (int): Number of times these parameters were used.
    """
    id = db.Column(db.Integer, primary_key=True)
    first_integer = db.Column(db.Integer, nullable=False)
    second_integer = db.Column(db.Integer, nullable=False)
    sequence_limit = db.Column(db.Integer, nullable=False)
    first_string = db.Column(db.String(50), nullable=False)
    second_string = db.Column(db.String(50), nullable=False)
    count = db.Column(db.Integer, default=1)

