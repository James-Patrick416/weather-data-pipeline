from pathlib import Path
from datetime import datetime
import json

from src.api import fetch_weather


RAW_DATA_DIR = Path("data/raw")


def ingest_weather():
    """
    Fetch weather data and save it as a timestamped JSON file.

    Returns:
        Path: Path to the saved JSON file.
    """

    # Create directory if it doesn't exist
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    weather_data = fetch_weather()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    file_path = RAW_DATA_DIR / f"{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(weather_data, file, indent=4)

    return file_path