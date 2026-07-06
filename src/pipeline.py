"""
Pipeline orchestration.

This module coordinates the ETL process.
Each stage has exactly one responsibility.
"""

from src.database import create_database
from src.ingest import ingest_weather
from src.transform import transform_weather
from src.loader import load_weather
from src.utils import logger


def run_pipeline() -> None:
    """
    Execute one complete ETL pipeline.

    Flow:
        Extract
            ↓
        Validate
            ↓
        Transform
            ↓
        Load
    """

    logger.info("=" * 60)
    logger.info("Pipeline started.")

    try:
        # Ensure the database and tables exist.
        create_database()

        # Extract + Validate
        file_path, weather = ingest_weather()

        logger.info(f"Snapshot saved to {file_path}")

        # Transform
        record = transform_weather(weather)

        # Load
        load_weather(record)

        logger.info("Pipeline completed successfully.")

    except Exception as err:

        logger.exception(f"Pipeline failed: {err}")

        raise

    finally:

        logger.info("=" * 60)