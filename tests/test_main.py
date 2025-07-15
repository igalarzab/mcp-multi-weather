import pytest

from datetime import date, timedelta

from fastmcp import Client
from fastmcp.exceptions import ToolError

from mcp_weather.main import mcp


async def test_get_weather_with_good_arguments():
    async with Client(mcp) as client:
        result = await client.call_tool('get_weather', {'city': 'London, UK', 'day': '2025-01-01'})
        assert result.data == 'Sunny'


async def test_get_weather_with_future_day():
    future_day = (date.today() + timedelta(days=1)).isoformat()

    async with Client(mcp) as client:
        with pytest.raises(ToolError, match='Date should be in the past') as e:
            await client.call_tool('get_weather', {'city': 'London, UK', 'day': future_day})