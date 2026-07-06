"""
Transform validated weather data into a database model.

This module is responsible ONLY for transformation.
It does not interact with the database.
"""

from datetime import datetime

from src.database import WeatherRecord
from src.models import WeatherResponse
from src.utils import logger


def transform_weather(weather: WeatherResponse) -> WeatherRecord:
    """
    Transform a validated WeatherResponse into a WeatherRecord.

    Args:
        weather:
            Validated weather data from the API.

    Returns:
        WeatherRecord:
            SQLAlchemy model ready to be saved.
    """

    logger.info("Transforming validated weather data.")

    record = WeatherRecord(
        city=weather.name,
        country=weather.sys.country,
        temperature=weather.main.temp,
        humidity=weather.main.humidity,
        pressure=weather.main.pressure,
        weather=weather.weather[0].main,
        description=weather.weather[0].description,
        wind_speed=weather.wind.speed,
        recorded_at=datetime.fromtimestamp(weather.dt),
    )

    logger.info("Transformation completed successfully.")

    return record