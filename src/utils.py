"""
Utility functions shared across the project.

Right now this file only contains logging, but in larger projects
it may also contain helper functions for formatting dates,
validating data, etc.
"""

from pathlib import Path
import logging

# Ensure the logs directory exists before creating the log file.
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "pipeline.log"

# Create one logger for the entire application.
logger = logging.getLogger("weather_pipeline")

# Prevent duplicate log messages if this module is imported multiple times.
logger.propagate = False

# Only configure the logger once.
if not logger.handlers:

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # Write logs to a file.
    file_handler = logging.FileHandler(LOG_FILE)

    file_handler.setFormatter(formatter)

    # Also display logs in the terminal.
    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)