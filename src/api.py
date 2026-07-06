"""
Functions for communicating with the OpenWeather API.
"""

import requests
from requests.exceptions import (
    HTTPError,
    ConnectionError,
    Timeout,
    RequestException,
)

from pydantic import ValidationError

from src.config import API_KEY, CITY, UNITS, BASE_URL
from src.models import WeatherResponse
from src.utils import logger


def fetch_weather() -> WeatherResponse:
    """
    Fetch weather data from the API and validate it.

    Returns:
        WeatherResponse:
            A validated Pydantic model.

    Raises:
        HTTPError
        ConnectionError
        Timeout
        RequestException
        ValidationError
    """

    params = {
        "q": CITY,
        "appid": API_KEY,
        "units": UNITS,
    }

    try:

        logger.info("Requesting weather data from API...")

        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10,
        )

        response.raise_for_status()

        logger.info("Weather data fetched successfully.")

        # Convert JSON -> validated Pydantic model
        weather = WeatherResponse.model_validate(
            response.json()
        )

        logger.info("Weather response validated.")

        return weather

    except ValidationError as err:

        logger.exception("Weather response failed validation.")

        raise

    except HTTPError as err:

        logger.exception(f"HTTP Error: {err}")

        raise

    except ConnectionError:

        logger.exception("No internet connection.")

        raise

    except Timeout:

        logger.exception("Request timed out.")

        raise

    except RequestException as err:

        logger.exception(f"Unexpected request error: {err}")

        raise