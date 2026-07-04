import requests
from requests.exceptions import (
    HTTPError,
    ConnectionError,
    Timeout,
    RequestException,
)

from src.config import API_KEY, CITY, UNITS, BASE_URL


def fetch_weather():
    """
    Fetch current weather data from OpenWeatherMap API.

    Returns:
        dict: JSON response from the API.

    Raises:
        Exception: If the request fails.
    """

    params = {
        "q": CITY,
        "appid": API_KEY,
        "units": UNITS,
    }

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10,
        )

        response.raise_for_status()

        return response.json()

    except HTTPError as err:
        raise Exception(f"HTTP Error: {err}")

    except ConnectionError:
        raise Exception("No internet connection.")

    except Timeout:
        raise Exception("Request timed out.")

    except RequestException as err:
        raise Exception(f"Unexpected error: {err}")