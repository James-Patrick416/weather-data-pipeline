"""
Unit tests for the database loader.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.database import Base, WeatherRecord
from src.loader import load_weather
from src.transform import transform_weather


def test_load_weather(sample_weather):
    """
    A transformed WeatherRecord should be successfully
    inserted into the database.
    """

    # Create an in-memory SQLite database.
    engine = create_engine("sqlite:///:memory:")

    Base.metadata.create_all(engine)

    TestingSessionLocal = sessionmaker(bind=engine)

    session = TestingSessionLocal()

    try:
        # Transform API model into database model.
        record = transform_weather(sample_weather)

        # Save it.
        load_weather(record, session)

        # Read it back.
        saved = session.query(WeatherRecord).first()

        assert saved is not None
        assert saved.city == "Nairobi"
        assert saved.country == "KE"
        assert saved.temperature == 22.5
        assert saved.humidity == 68
        assert saved.pressure == 1014
        assert saved.weather == "Clouds"
        assert saved.description == "broken clouds"
        assert saved.wind_speed == 4.2

    finally:
        session.close()