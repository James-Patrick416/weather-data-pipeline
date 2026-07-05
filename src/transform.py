from datetime import datetime

from src.database import SessionLocal, WeatherRecord


def transform_and_load(weather_data: dict) -> None:
    """
    Transform raw weather JSON into a database record
    and save it to SQLite.
    """

    session = SessionLocal()

    try:
        record = WeatherRecord(
            city=weather_data["name"],
            country=weather_data["sys"]["country"],
            temperature=weather_data["main"]["temp"],
            humidity=weather_data["main"]["humidity"],
            pressure=weather_data["main"]["pressure"],
            weather=weather_data["weather"][0]["main"],
            description=weather_data["weather"][0]["description"],
            wind_speed=weather_data["wind"]["speed"],
            recorded_at=datetime.fromtimestamp(weather_data["dt"]),
        )

        session.add(record)

        session.commit()

        print("Weather record inserted successfully.")

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()