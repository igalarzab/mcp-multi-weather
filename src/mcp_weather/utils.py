import argparse


def args_parser():
    parser = argparse.ArgumentParser(description='Run the mcp-weather service')

    parser.add_argument(
        '--transport',
        choices=['http', 'stdio'],
        default='http',
        help='Transport to use: http or stdio (default: http)'
    )

    parser.add_argument(
        '--host',
        default='127.0.0.1',
        help='Host to use (default: 127.0.0.1)'
    )

    parser.add_argument(
        '--port',
        default=4200,
        help='Port to use (default: 4200)'
    )

    return parser.parse_args()