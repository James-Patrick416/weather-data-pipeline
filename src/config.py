"""
Application configuration.
"""

import os

from dotenv import load_dotenv

# Load variables from the .env file.
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = os.getenv("CITY", "Nairobi")
UNITS = os.getenv("UNITS", "metric")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def validate_config() -> None:
    """
    Validate that all required configuration values exist.

    Raises:
        ValueError:
            If a required environment variable is missing.
    """

    if not API_KEY:
        raise ValueError(
            "OPENWEATHER_API_KEY not found. "
            "Create a .env file and add your API key."
        )