"""
Pipeline orchestration.

This module coordinates the ETL process without knowing
implementation details of each stage.
"""

from src.database import create_database
from src.ingest import ingest_weather
from src.transform import transform_and_load
from src.utils import logger


def run_pipeline() -> None:
    """
    Execute one complete ETL pipeline run.
    """

    logger.info("=" * 60)
    logger.info("Pipeline started.")

    try:
        create_database()

        file_path, weather = ingest_weather()

        logger.info(f"Snapshot saved to {file_path}")

        transform_and_load(weather)

        logger.info("Pipeline completed successfully.")

    except Exception as err:

        logger.exception(f"Pipeline failed: {err}")

        raise

    finally:

        logger.info("=" * 60)