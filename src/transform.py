from datetime import datetime

from src.database import SessionLocal, WeatherRecord
from src.utils import logger


def transform_and_load(weather_data):

    session = SessionLocal()

    try:

        logger.info("Transforming weather data.")

        record = WeatherRecord(
            city=weather_data["name"],
            country=weather_data["sys"]["country"],
            temperature=weather_data["main"]["temp"],
            humidity=weather_data["main"]["humidity"],
            pressure=weather_data["main"]["pressure"],
            weather=weather_data["weather"][0]["main"],
            description=weather_data["weather"][0]["description"],
            wind_speed=weather_data["wind"]["speed"],
            recorded_at=datetime.fromtimestamp(
                weather_data["dt"]
            ),
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