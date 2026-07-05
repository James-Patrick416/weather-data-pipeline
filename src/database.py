from pathlib import Path

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    Float,
    String,
    DateTime,
)
from sqlalchemy.orm import declarative_base, sessionmaker

DB_PATH = Path("database/weather.db")

DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class WeatherRecord(Base):
    __tablename__ = "weather_records"

    id = Column(Integer, primary_key=True)

    city = Column(String)

    country = Column(String)

    temperature = Column(Float)

    humidity = Column(Integer)

    pressure = Column(Integer)

    weather = Column(String)

    description = Column(String)

    wind_speed = Column(Float)

    recorded_at = Column(DateTime)


def create_database():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    Base.metadata.create_all(engine)