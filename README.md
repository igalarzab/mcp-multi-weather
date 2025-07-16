# mcp-weather

## Description

MCP server for checking the weather history and forecast. This Model Context Protocol (MCP) server provides weather data functionality through a FastMCP-based service that integrates with weather providers to deliver historical weather information.

The server exposes a `get_weather` tool that allows checking weather conditions for specific cities on past dates, making it useful for applications that need historical weather data.

## How to run

Install the package in your claude-desktop using uv:

```
$ uv run fastmcp install claude-desktop src/mcp_weather/mcp.py --env-file .env --env PYTHONPATH=$PWD/src/
```
