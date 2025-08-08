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
  - `get_strategy` - Get a random oblique strategy
  - `get_strategy_by_category` - Get strategies filtered by creative domain
  - `search_strategies` - Search strategies by keywords
- Resources should include the full collection of oblique strategies
- Prompts could provide creative workflow templates

### Strategy Data Management
- Store strategies in a structured format (JSON/YAML)
- Include metadata like categories, contexts, and usage guidance
- Consider providing both original strategies and modern interpretations

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

Expected Python package structure:
- `src/oblique_strategies_mcp/` - Main package directory
- `src/oblique_strategies_mcp/__main__.py` - Entry point for `uv run oblique-strategies-mcp`
- `src/oblique_strategies_mcp/server.py` - MCP server implementation
- `src/oblique_strategies_mcp/strategies.py` - Strategy data and logic
- `tests/` - Test files
- `pyproject.toml` - Project configuration and dependencies