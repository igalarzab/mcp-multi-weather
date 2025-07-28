## MCP Multi Weather Server ${{ needs.check-release.outputs.version }}

### Installation Options

**Python Package**
```bash
export WEATHER_PROVIDER=openweather
export OPENWEATHER_API_KEY=dummy
uvx mcp-multi-weather==${{ needs.check-release.outputs.version }}
```

**Docker Image**
```bash
docker run -e WEATHER_PROVIDER=openweather -e OPENWEATHER_API_KEY=dummy ghcr.io/igalarzab/mcp-multi-weather:${{ needs.check-release.outputs.version }}
```

**Claude Desktop**
```jsonc
// ~/Library/Application Support/Claude/claude_desktop_config.json
"mcpServers": {
  "mcp-multi-weather": {
    "command": "uvx",
    "transport": "stdio",
    "args": [
      "mcp-multi-weather"
    ],
    "env": {
      "WEATHER_PROVIDER": "openweather",
      "OPENWEATHER_API_KEY": "<<TOKEN>>"
    }
  }
}
```

**DXT Package**
Download the `.dxt` file from the assets below and install it using your preferred MCP client. You
can for example just drag and drop it into the Claude Desktop app
