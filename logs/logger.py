import logging
import os

"""
This module sets up custom logging for the application.

It configures logging to write messages to both a file and the console, with different
levels of verbosity for each output. Debug and more severe messages are logged to the
file, while error and more severe messages are logged to the console.

Attributes:
    logger (Logger): The configured logger instance for the application.
"""

# Path to the directory containing this file
log_dir = os.path.dirname(os.path.abspath(__file__))

# Log file path
log_file_path = os.path.join(log_dir, 'app.log')

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler which logs even debug messages
fh = logging.FileHandler(log_file_path)
fh.setLevel(logging.DEBUG)

# Create a console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
