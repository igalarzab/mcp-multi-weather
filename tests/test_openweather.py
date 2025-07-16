import pytest

from datetime import date
from unittest.mock import patch, AsyncMock

from mcp_weather.providers.openweather import OpenWeather
from mcp_weather.providers.types import Weather, GeoCode


LONDON_MOCK = GeoCode(name='London', country='GB', lat=51.5, lon=0)
WEATHER_MOCK = lambda t, d: {'data': [{'temp': t, 'weather': [{'description': d}]}]} # pyright: ignore # noqa: E731


async def test_daily_weather_success():
    ow = OpenWeather(api_key='dummy')
    day = date(2023, 1, 1)

    with patch.object(ow, '_find_geocode', AsyncMock(return_value=LONDON_MOCK)):
        with patch.object(ow, '_call', AsyncMock(return_value=WEATHER_MOCK(20, 'clear sky'))):
            weather = await ow.daily_weather('London', day)

            assert isinstance(weather, Weather)
            assert weather.address == 'London, GB'
            assert weather.temperature == 20
            assert weather.description == 'clear sky'


async def test_daily_weather_geocode_no_results():
    ow = OpenWeather(api_key='dummy')
    day = date(2023, 1, 1)

    with patch.object(ow, '_find_geocode', AsyncMock(return_value=None)):
        weather = await ow.daily_weather('London', day)
        assert weather is None


async def test_daily_weather_api_no_results():
    ow = OpenWeather(api_key='dummy')
    day = date(2023, 1, 1)

    with patch.object(ow, '_find_geocode', AsyncMock(return_value=LONDON_MOCK)):
        with patch.object(ow, '_call', AsyncMock(return_value=None)):
            weather = await ow.daily_weather('London', day)
            assert weather is None


async def test_daily_weather_real_api(ow_api_key: str | None):
    if not ow_api_key:
        pytest.skip('No OpenWeather API key provided via --ow-api-key')

    ow = OpenWeather(api_key=ow_api_key)
    day = date(2023, 1, 1)

    weather = await ow.daily_weather('London', day)

    assert isinstance(weather, Weather)
    assert weather.address == 'London, GB'
    assert weather.temperature == 12.54
    assert weather.description == 'light rain'