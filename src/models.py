"""
Pydantic models used to validate weather API responses.

Instead of trusting that the API always returns the expected
structure, we define exactly what our application expects.
"""

from pydantic import BaseModel


class WeatherInfo(BaseModel):
    """
    Represents the first item inside the 'weather' list.
    """

    main: str
    description: str


class MainWeather(BaseModel):
    """
    Represents the 'main' section of the API response.
    """

    temp: float
    humidity: int
    pressure: int


class Wind(BaseModel):
    """
    Represents wind information.
    """

    speed: float


class System(BaseModel):
    """
    Represents country information.
    """

    country: str


class WeatherResponse(BaseModel):
    """
    Represents the subset of the OpenWeather response
    that our pipeline actually uses.

    Notice that we don't model every field returned by the API,
    only the ones our application needs.
    """

    name: str
    dt: int

    main: MainWeather
    weather: list[WeatherInfo]
    wind: Wind
    sys: System