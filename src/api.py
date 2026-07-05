import requests
from requests.exceptions import (
    HTTPError,
    ConnectionError,
    Timeout,
    RequestException,
)

from src.config import API_KEY, CITY, UNITS, BASE_URL
from src.utils import logger


def fetch_weather():
    """
    Fetch weather data from OpenWeather API.

    Returns:
        dict: Weather JSON.
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

        return response.json()

    except HTTPError as err:

        logger.error(f"HTTP Error: {err}")

        raise

    except ConnectionError:

        logger.error("No internet connection.")

        raise

    except Timeout:

        logger.error("Request timed out.")

        raise

    except RequestException as err:

        logger.error(f"Unexpected request error: {err}")

        raise