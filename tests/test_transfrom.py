"""
Unit tests for weather data transformation.
"""

from datetime import datetime

from src.models import WeatherResponse
from src.transform import transform_weather
from src.database import WeatherRecord


def create_sample_weather() -> WeatherResponse:
    """
    Create a reusable WeatherResponse object for tests.
    """

    return WeatherResponse.model_validate(
        {
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
    )


def test_transform_returns_weather_record():
    """
    The transform step should return a WeatherRecord instance.
    """

    weather = create_sample_weather()

    record = transform_weather(weather)

    assert isinstance(record, WeatherRecord)


def test_transform_copies_all_fields_correctly():
    """
    Every field should be copied correctly into the database model.
    """

    weather = create_sample_weather()

    record = transform_weather(weather)

    assert record.city == "Nairobi"
    assert record.country == "KE"
    assert record.temperature == 22.5
    assert record.humidity == 68
    assert record.pressure == 1014
    assert record.weather == "Clouds"
    assert record.description == "broken clouds"
    assert record.wind_speed == 4.2


def test_transform_converts_timestamp():
    """
    Unix timestamps should become datetime objects.
    """

    weather = create_sample_weather()

    record = transform_weather(weather)

    assert isinstance(record.recorded_at, datetime)