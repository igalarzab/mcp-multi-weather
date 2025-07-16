from fastmcp import FastMCP, Context
from pydantic import PastDate
from starlette.requests import Request
from starlette.responses import PlainTextResponse

from mcp_weather.providers.openweather import OpenWeather


mcp: FastMCP[None] = FastMCP(
    name='mcp-weather',
    dependencies=['aiohttp[speedups]']
)

openweather_client = OpenWeather.from_env()


@mcp.custom_route('/health', methods=['GET'])
async def health(_request: Request) -> PlainTextResponse:
    return PlainTextResponse('OK')


@mcp.tool
async def get_weather(address: str, day: PastDate, ctx: Context) -> str:
    '''
    Checks the weather a specific city had in a specific day in the past

    Args:
        address: City name and Country name, separated by a comma
        day: ISO8601 formatted date (without the time part)
    '''
    await ctx.debug(f'Checking weather of {address} for {day}')
    result = await openweather_client.daily_weather(address, day)

    if not result:
        return f'There is no information for {address}'

    return result.explain()