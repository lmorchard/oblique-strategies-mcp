# Oblique Strategies MCP Server

An MCP (Model Context Protocol) server that provides access to Brian Eno and Peter Schmidt's Oblique Strategies - a collection of prompts designed to help overcome creative blocks through lateral thinking.

## Why?

Why not?

## No, seriously, why?

Because I've built Oblique Strategies thingies for various devices & platforms and I wanted to make another one to play with the MCP protocol.

This is a very silly project and you should just go buy a real deck of cards.

## Quick Start

No installation required, if you have `uvx` and you trust my code from github. (Weirdo.)

Run directly from GitHub using uvx:
```bash
uvx --from git+https://github.com/lmorchard/oblique-strategies-mcp oblique-strategies-mcp
```

For Claude Desktop, add to your config file:
```json
{
  "mcpServers": {
    "oblique-strategies": {
      "command": "/path/to/uvx",
      "args": [
        "--from",
        "git+https://github.com/lmorchard/oblique-strategies-mcp",
        "oblique-strategies-mcp"
      ]
    }
  }
}
```

For Claude Code:
```bash
claude mcp add oblique-strategies -- /path/to/uvx --from git+https://github.com/lmorchard/oblique-strategies-mcp oblique-strategies-mcp
```

## Features

- Get random strategies from multiple editions (1975-1982)
- Search strategies by keyword
- Choose from 7 different collections including programming-specific adaptations
- Default: Edition 2 (1978) with 128 strategies

## MCP Tools

- **`get_strategy`** - Get a random strategy (optionally specify edition)
- **`search_strategies`** - Search strategies by keyword
- **`list_editions`** - List all available editions

## Available Collections

- **Edition 1-4**: Original Oblique Strategies (1975-1982)
- **Condensed**: Comprehensive collection (195 strategies)
- **Programmers**: Programming-specific adaptations (96 prompts)
- **Do It**: Action-oriented prompts (32 strategies)

## Installation

### For Development

```bash
# Clone the repository
git clone <repository-url>
cd oblique-strategies-mcp

# Install dependencies with uv
uv sync
```

## Running the Server

### Development Mode

From the project directory:
```bash
# Using the package entry point
uv run oblique-strategies-mcp

# Or using Python module syntax
uv run python -m oblique_strategies_mcp

# Or using the wrapper script
./run-server.sh
```

### After Global Installation

```bash
oblique-strategies-mcp
```

## Configuration

### For Claude Desktop

Add to your Claude Desktop config file (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

#### Development Setup
```json
{
  "mcpServers": {
    "oblique-strategies": {
      "command": "/path/to/uv",
      "args": [
        "--directory",
        "/path/to/oblique-strategies-mcp",
        "run",
        "oblique-strategies-mcp"
      ]
    }
  }
}
```

Note: Replace `/path/to/uv` with the full path to your uv executable (typically `~/.local/bin/uv` or use `which uv` to find it).

#### Global Installation Setup
```json
{
  "mcpServers": {
    "oblique-strategies": {
      "command": "oblique-strategies-mcp",
      "args": [],
      "env": {}
    }
  }
}
```

### For Claude Code

#### Development Setup
```bash
claude mcp add oblique-strategies -- uv --directory /path/to/oblique-strategies-mcp run oblique-strategies-mcp
```

#### Using Wrapper Script
```bash
claude mcp add oblique-strategies /path/to/oblique-strategies-mcp/run-server.sh
```

#### Global Installation
```bash
claude mcp add oblique-strategies oblique-strategies-mcp
```

After adding, restart Claude Desktop or reconnect in Claude Code.

## License

MIT

## Acknowledgments

- Brian Eno and Peter Schmidt for creating Oblique Strategies
- Strategy collections sourced from: https://github.com/zzkt/oblique-strategies