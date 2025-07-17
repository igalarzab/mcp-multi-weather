import argparse
import os

from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import PlainTextResponse

from mcp_weather.components.weather import WeatherComponent

mcp: FastMCP[None] = FastMCP(
    name='mcp-weather',
    dependencies=['aiohttp[speedups]']
)

weather_component = WeatherComponent()
weather_component.register_all(mcp_server=mcp)


@mcp.custom_route('/health', methods=['GET'])
async def health(_request: Request) -> PlainTextResponse:
    return PlainTextResponse('OK')


def args_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Run the mcp-weather service')

    parser.add_argument(
        '--transport',
        choices=['http', 'stdio'],
        default=os.environ.get('MCP_TRANSPORT', 'http'),
        help='Transport to use: http or stdio (default: http)'
    )

    parser.add_argument(
        '--host',
        default=os.environ.get('MCP_HOST', '127.0.0.1'),
        help='Host to use (default: 127.0.0.1)'
    )

    parser.add_argument(
        '--port',
        default=int(os.environ.get('MCP_PORT', 4200)),
        help='Port to use (default: 4200)'
    )

    parser.add_argument(
        '--log-level',
        default=os.environ.get('MCP_LOG_LEVEL', 'INFO'),
        help='Log level to use (default INFO)'
    )

    parser.add_argument(
        '--show-banner',
        default=os.environ.get('MCP_SHOW_BANNER', 'True'),
        help='Show the FastMCP banner (default True)'
    )

    return parser.parse_args()


def main() -> None:
    cli_args = args_parser()
    run_cmd_args = {
        'transport': cli_args.transport,
        'show_banner': cli_args.show_banner.lower() == 'true',
    }

    match cli_args.transport:
        case 'http':
            run_cmd_args.update({
                'log_level': cli_args.log_level,
                'host': cli_args.host,
                'port': cli_args.port,
            })
        case _:
            pass

    mcp.run(**run_cmd_args)


if __name__ == '__main__':
    main()