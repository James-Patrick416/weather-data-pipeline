"""
Application entry point.

This file should stay intentionally small.
Its only responsibility is to start the pipeline.
"""

from src.pipeline import run_pipeline


def main() -> None:
    """
    Start the ETL pipeline.
    """
    run_pipeline()


if __name__ == "__main__":
    main()