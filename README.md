# Oblique Strategies MCP Server

An MCP (Model Context Protocol) server implementation providing access to Brian Eno's Oblique Strategies - a collection of creative prompting cards designed to help overcome creative blocks through lateral thinking techniques.

## What are Oblique Strategies?

Oblique Strategies is a deck of cards created by Brian Eno and Peter Schmidt in 1975. Each card contains a cryptic remark or question intended to help creative people break out of creative blocks by encouraging lateral thinking. The cards have been used by musicians, artists, writers, and other creative professionals to approach problems from new angles.

## Features

This MCP server provides tools for:

- **Random Strategy Selection**: Get a random oblique strategy from multiple editions
- **Edition Selection**: Choose from original editions 1-4 or alternative collections
- **Strategy Search**: Search through strategies using keywords
- **Creative Workflow Integration**: Use strategies within AI-assisted creative processes

## Available Strategy Collections

The server includes several editions and variants of Oblique Strategies:

- **Edition 1** (1975): The original 112 strategies by Brian Eno and Peter Schmidt
- **Edition 2** (1978): Expanded to 127 strategies - **Default edition**
- **Edition 3** (1979): Refined to 121 strategies  
- **Edition 4** (1982): Streamlined to 100 strategies
- **Condensed Collection**: A comprehensive collection of 195 strategies
- **Prompts for Programmers**: 96 programming-specific adaptations
- **Do It (Abridged)**: 32 action-oriented prompts

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Clone the repository
git clone <repository-url>
cd oblique-strategies-mcp

# Install dependencies
uv sync
```

## Usage

### Running the MCP Server

Start the server for use with MCP clients:

```bash
uv run oblique-strategies-mcp
```

### Using with Claude Desktop

Add this server to your Claude Desktop configuration to access oblique strategies directly in your conversations.

## MCP Tools

The server provides these tools for MCP clients:

### `get_strategy`
Get a random oblique strategy from a selected edition.

**Parameters**:
- `edition` (string, optional): The edition/variant to use. Options:
  - `"edition-1"` - Original 1975 edition
  - `"edition-2"` - 1978 edition (default)
  - `"edition-3"` - 1979 edition
  - `"edition-4"` - 1982 edition
  - `"condensed"` - Comprehensive collection
  - `"programmers"` - Programming-specific prompts
  - `"do-it"` - Do It collection

**Returns**: A random strategy from the selected edition

### `search_strategies`
Search through strategies using keywords.

**Parameters**:
- `query` (string): Keywords to search for
- `edition` (string, optional): Limit search to specific edition (uses same values as `get_strategy`)

**Returns**: Strategies matching the search terms with their edition information

## Development

### Development Setup

```bash
# Install development dependencies
uv sync

# Run tests
uv run pytest

# Lint and format code
uv run ruff check .
uv run ruff format .

# Type checking
uv run mypy .
```

### Project Structure

```
oblique-strategies-mcp/
├── main.py                  # Entry point and MCP server implementation
├── strategies/              # Strategy text files
│   ├── oblique-strategies-edition-1.txt
│   ├── oblique-strategies-edition-2.txt (default)
│   ├── oblique-strategies-edition-3.txt
│   ├── oblique-strategies-edition-4.txt
│   ├── oblique-strategies-condensed.txt
│   ├── prompts-for-programmers.txt
│   └── do-it-abridged.txt
├── tests/                   # Test files
├── pyproject.toml          # Project configuration
├── CLAUDE.md               # Claude Code guidance
└── README.md               # This file
```

### Testing

Run the test suite:

```bash
uv run pytest
```

Run tests with coverage:

```bash
uv run pytest --cov=oblique_strategies_mcp
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite and linting
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Brian Eno and Peter Schmidt for creating the original Oblique Strategies
- The MCP community for the protocol specification
- Strategy collections sourced from: https://github.com/zzkt/oblique-strategies
- All contributors to this implementation