from src.database import create_database
from src.ingest import ingest_weather
from src.transform import transform_and_load


def main():
    create_database()

    file_path, weather_data = ingest_weather()

    print(f"Raw data saved to: {file_path}")

    transform_and_load(weather_data)

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()