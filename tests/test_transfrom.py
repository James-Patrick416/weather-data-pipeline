"""
Unit tests for weather data transformation.
"""

from datetime import datetime

from src.database import WeatherRecord
from src.transform import transform_weather


def test_transform_returns_weather_record(sample_weather):
    """
    The transform step should return a WeatherRecord instance.
    """

    record = transform_weather(sample_weather)

    assert isinstance(record, WeatherRecord)


def test_transform_copies_all_fields_correctly(sample_weather):
    """
    Every field should be copied correctly.
    """

    record = transform_weather(sample_weather)

    assert record.city == "Nairobi"
    assert record.country == "KE"
    assert record.temperature == 22.5
    assert record.humidity == 68
    assert record.pressure == 1014
    assert record.weather == "Clouds"
    assert record.description == "broken clouds"
    assert record.wind_speed == 4.2


def test_transform_converts_timestamp(sample_weather):
    """
    Unix timestamps should become datetime objects.
    """

    record = transform_weather(sample_weather)

    assert isinstance(record.recorded_at, datetime)