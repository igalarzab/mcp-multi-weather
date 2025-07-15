from fastmcp import FastMCP, Context
from pydantic import PastDate
from starlette.requests import Request
from starlette.responses import PlainTextResponse

from .utils import args_parser


mcp = FastMCP(name='mcp-weather')


@mcp.custom_route('/health', methods=['GET'])
async def health(_request: Request) -> PlainTextResponse:
    return PlainTextResponse('OK')


@mcp.tool
async def get_weather(city: str, day: PastDate, ctx: Context) -> str:
    '''
    Checks the weather a specific city had in a specific day in the past
    '''

    await ctx.info(f'Checking weather of {city} for {day}')

    return 'Sunny'


def main() -> None:
    cli_args = args_parser()
    run_cmd_args = { 'transport': cli_args.transport }

    match cli_args.transport:
        case 'http':
            run_cmd_args.update({
                'log_level': 'INFO',
                'host': cli_args.host,
                'port': cli_args.port,
            })

    mcp.run(**run_cmd_args)


if __name__ == '__main__':
    main()