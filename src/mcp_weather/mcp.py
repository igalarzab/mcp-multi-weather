from fastmcp import FastMCP, Context
from pydantic import PastDate
from starlette.requests import Request
from starlette.responses import PlainTextResponse


mcp: FastMCP[None] = FastMCP(
    name='mcp-weather',
    dependencies=['aiohttp[speedups]']
)


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
    await ctx.info(f'Checking weather of {address} for {day}')
    return 'Sunny'