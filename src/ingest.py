"""
Extract weather data from the API and save the validated
response as raw JSON.
"""

from pathlib import Path
from datetime import datetime
import json

from src.api import fetch_weather
from src.models import WeatherResponse
from src.utils import logger

RAW_DATA_DIR = Path("data/raw")


def ingest_weather() -> tuple[Path, WeatherResponse]:
    """
    Fetch validated weather data and save a raw JSON snapshot.

    Returns:
        tuple:
            Path -> saved JSON file
            WeatherResponse -> validated weather model
    """

    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    weather = fetch_weather()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    file_path = RAW_DATA_DIR / f"{timestamp}.json"

    # Convert the Pydantic model back into a normal dictionary
    # before saving it as JSON.
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            weather.model_dump(),
            file,
            indent=4,
        )

    logger.info(f"Raw JSON saved: {file_path}")

    return file_path, weather