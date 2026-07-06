"""
Load transformed weather records into the database.
"""

from src.database import SessionLocal, WeatherRecord
from src.utils import logger


def load_weather(record: WeatherRecord) -> None:
    """
    Save a WeatherRecord to the database.

    Args:
        record:
            SQLAlchemy WeatherRecord object.
    """

    session = SessionLocal()

    try:

        logger.info("Loading weather record into database.")

        session.add(record)

        session.commit()

        logger.info("Weather record inserted successfully.")

    except Exception as err:

        session.rollback()

        logger.exception(f"Database transaction failed: {err}")

        raise

    finally:

        session.close()