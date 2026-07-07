"""
Unit tests for Pydantic weather models.
"""

from src.models import WeatherResponse


def test_valid_weather_response():
    """
    A valid API response should be successfully
    converted into a WeatherResponse model.
    """

    data = {
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

    weather = WeatherResponse.model_validate(data)

    assert weather.name == "Nairobi"
    assert weather.main.temp == 22.5
    assert weather.main.humidity == 68
    assert weather.wind.speed == 4.2
    assert weather.sys.country == "KE"