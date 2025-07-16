import argparse
import os

from mcp_weather.mcp import mcp


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

    return parser.parse_args()


def main() -> None:
    cli_args = args_parser()
    run_cmd_args = { 'transport': cli_args.transport }

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