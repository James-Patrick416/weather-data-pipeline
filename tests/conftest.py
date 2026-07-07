"""
Shared pytest fixtures.

Fixtures defined here are automatically available
to every test module.
"""

import pytest

from src.models import WeatherResponse


@pytest.fixture
def sample_weather():
    """
    A reusable WeatherResponse object for tests.
    """

    return WeatherResponse.model_validate(
        {
            "name": "Nairobi",
            "dt": 1751800000,
            "main": {
                "temp": 22.5,
                "humidity": 68,
                "pressure": 1014,
            },
            "weather": [
                {
                    "main": "Clouds",
                    "description": "broken clouds",
                }
            ],
            "wind": {
                "speed": 4.2,
            },
            "sys": {
                "country": "KE",
            },
        }
    )