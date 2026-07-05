from src.database import create_database
from src.ingest import ingest_weather
from src.transform import transform_and_load
from src.utils import logger


def main():

    logger.info("=" * 60)

    logger.info("Pipeline started.")

    try:

        create_database()

        file_path, weather = ingest_weather()

        transform_and_load(weather)

        logger.info("Pipeline completed successfully.")

    except Exception as err:

        logger.exception(f"Pipeline failed: {err}")

    finally:

        logger.info("=" * 60)


if __name__ == "__main__":
    main()