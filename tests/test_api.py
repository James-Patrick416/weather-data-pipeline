"""
Unit tests for the weather API client.
"""

from unittest.mock import Mock

import pytest
from pydantic import ValidationError
from requests.exceptions import HTTPError

from src.api import fetch_weather
from src.models import WeatherResponse


def sample_api_response():
    """
    A realistic API response used by multiple tests.
    """

    return {
        "name": "Nairobi",
        "dt": 1751800000,
        "main": {
            "temp": 22.5,
            "humidity": 68,
            "pressure": 1014,
        },
        "weather": [
            {
                "main": "Clouds",
                "description": "broken clouds",
            }
        ],
        "wind": {
            "speed": 4.2,
        },
        "sys": {
            "country": "KE",
        },
    }


def test_fetch_weather_success(mocker):
    """
    The API client should return a validated WeatherResponse.
    """

    fake_response = Mock()
    fake_response.json.return_value = sample_api_response()
    fake_response.raise_for_status.return_value = None

    mocker.patch(
        "src.api.requests.get",
        return_value=fake_response,
    )

    weather = fetch_weather()

    assert isinstance(weather, WeatherResponse)
    assert weather.name == "Nairobi"
    assert weather.main.temp == 22.5


def test_fetch_weather_http_error(mocker):
    """
    HTTP errors should be re-raised.
    """

    fake_response = Mock()
    fake_response.raise_for_status.side_effect = HTTPError()

    mocker.patch(
        "src.api.requests.get",
        return_value=fake_response,
    )

    with pytest.raises(HTTPError):
        fetch_weather()


def test_fetch_weather_validation_error(mocker):
    """
    Invalid API responses should raise ValidationError.
    """

    invalid_response = {
        "name": "Nairobi"
    }

    fake_response = Mock()
    fake_response.raise_for_status.return_value = None
    fake_response.json.return_value = invalid_response

    mocker.patch(
        "src.api.requests.get",
        return_value=fake_response,
    )

    with pytest.raises(ValidationError):
        fetch_weather()