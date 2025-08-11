#!/bin/bash
# Run the Oblique Strategies MCP server from anywhere
cd "$(dirname "$0")"
exec uv run oblique-strategies-mcp "$@"