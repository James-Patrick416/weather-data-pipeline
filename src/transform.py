"""
Transform validated weather data and load it into the database.
"""

from datetime import datetime

from src.database import SessionLocal, WeatherRecord
from src.models import WeatherResponse
from src.utils import logger


def transform_and_load(weather: WeatherResponse) -> None:
    """
    Transform a validated WeatherResponse object into
    a WeatherRecord database row.

    Args:
        weather:
            Validated weather data from the API.
    """

    session = SessionLocal()

    try:

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

        session.add(record)

        session.commit()

        logger.info("Weather record inserted into database.")

    except Exception as err:

        session.rollback()

        logger.exception(f"Database transaction failed: {err}")

        raise

    finally:

        session.close()