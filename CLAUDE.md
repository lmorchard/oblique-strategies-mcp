# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an MCP (Model Context Protocol) server implementation for Oblique Strategies - Brian Eno's creative prompting system that provides lateral thinking techniques to help overcome creative blocks.

## Development Environment Setup

This is a Python project managed by uv. Common development commands:

```bash
# Install dependencies
uv sync

# Run the MCP server
uv run oblique-strategies-mcp

# Run tests
uv run pytest

# Lint and format code
uv run ruff check .
uv run ruff format .

# Type checking
uv run mypy .

# Add new dependencies
uv add <package-name>
uv add --dev <dev-package-name>
```

## MCP Architecture Considerations

When building this MCP server, follow these patterns:

### Server Structure
- Implement the MCP protocol handlers for tools, resources, and prompts
- Provide tools for:
  - `get_strategy` - Get a random oblique strategy from a selected edition (defaults to edition 2)
  - `search_strategies` - Search strategies by keywords across editions
- Resources should include the full collection of oblique strategies
- Prompts could provide creative workflow templates

### Strategy Data Management
- Strategy files are stored in `strategies/` directory, one strategy per line
- Available editions and variants:
  - `oblique-strategies-edition-1.txt` - First edition (112 strategies)
  - `oblique-strategies-edition-2.txt` - Second edition (127 strategies) **[DEFAULT]**
  - `oblique-strategies-edition-3.txt` - Third edition (121 strategies)
  - `oblique-strategies-edition-4.txt` - Fourth edition (100 strategies)
  - `oblique-strategies-condensed.txt` - Condensed collection (195 strategies)
  - `prompts-for-programmers.txt` - Programming-specific adaptation (96 prompts)
  - `do-it-abridged.txt` - Abridged "Do It" collection (32 strategies)

### Integration Patterns
- Follow MCP server specifications for Claude integration
- Ensure tools return structured, actionable responses
- Design for use in creative workflows and brainstorming sessions

## Testing Strategy

- Unit tests for strategy selection and filtering logic
- Integration tests for MCP protocol compliance
- Example usage scenarios for creative applications

## Common Development Tasks

The most frequently used commands will be:
- `uv run oblique-strategies-mcp` - Start the MCP server
- `uv run pytest` - Run test suite
- `uv run ruff check . && uv run ruff format .` - Lint and format code
- MCP client testing with Claude Desktop or other MCP clients

## Project Structure

Current project structure:
- `oblique_strategies_mcp/` - Package directory
  - `__init__.py` - Package initialization
  - `__main__.py` - Entry point and MCP server implementation
- `strategies/` - Directory containing strategy text files
  - Each file contains one strategy per line
  - Default edition is `oblique-strategies-edition-2.txt`
- `tests/` - Test files
- `pyproject.toml` - Project configuration and dependencies
- `CLAUDE.md` - This file
- `README.md` - User-facing documentation