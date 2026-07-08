"""
Load transformed weather records into the database.
"""

from sqlalchemy.orm import Session

from src.database import SessionLocal, WeatherRecord
from src.utils import logger


def load_weather(
    record: WeatherRecord,
    session: Session | None = None,
) -> None:
    """
    Save a WeatherRecord to the database.

    Args:
        record:
            SQLAlchemy WeatherRecord object.

        session:
            Optional SQLAlchemy session.
            If omitted, a new session is created.
    """

    created_session = False

    if session is None:
        session = SessionLocal()
        created_session = True

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

        if created_session:
            session.close()