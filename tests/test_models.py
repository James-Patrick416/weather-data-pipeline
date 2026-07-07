"""
Unit tests for Pydantic weather models.
"""

import pytest
from pydantic import ValidationError

from src.models import WeatherResponse


def test_valid_weather_response():
    """
    A valid API response should be successfully
    converted into a WeatherResponse model.
    """

    data = {
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

    weather = WeatherResponse.model_validate(data)

    assert weather.name == "Nairobi"
    assert weather.main.temp == 22.5
    assert weather.main.humidity == 68
    assert weather.main.pressure == 1014
    assert weather.weather[0].main == "Clouds"
    assert weather.weather[0].description == "broken clouds"
    assert weather.wind.speed == 4.2
    assert weather.sys.country == "KE"


def test_missing_required_field():
    """
    Validation should fail if a required field is missing.
    """

    data = {
        "name": "Nairobi",
        "dt": 1751800000,
        "main": {
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

    with pytest.raises(ValidationError):
        WeatherResponse.model_validate(data)


def test_invalid_temperature_type():
    """
    Validation should fail when temperature is not numeric.
    """

    data = {
        "name": "Nairobi",
        "dt": 1751800000,
        "main": {
            "temp": "hot",
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

    with pytest.raises(ValidationError):
        WeatherResponse.model_validate(data)


def test_missing_weather_list():
    """
    Validation should fail if the weather list is missing.
    """

    data = {
        "name": "Nairobi",
        "dt": 1751800000,
        "main": {
            "temp": 22.5,
            "humidity": 68,
            "pressure": 1014,
        },
        "wind": {
            "speed": 4.2,
        },
        "sys": {
            "country": "KE",
        },
    }

    with pytest.raises(ValidationError):
        WeatherResponse.model_validate(data)