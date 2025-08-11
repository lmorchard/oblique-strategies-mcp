#!/usr/bin/env python3
"""
Oblique Strategies MCP Server

An MCP server providing access to Brian Eno's Oblique Strategies
for creative problem-solving and lateral thinking.
"""

from typing import Optional, Dict, Any, Union
from mcp.server.fastmcp import FastMCP
from .strategies_core import StrategiesManager

# Initialize the MCP server
mcp = FastMCP("Oblique Strategies")

# Initialize the strategies manager
manager = StrategiesManager()


@mcp.tool()
def get_strategy(edition: Optional[str] = None) -> Dict[str, Union[str, int]]:
    """
    Get a random oblique strategy from the specified edition.

    Args:
        edition: The edition to use (edition-1, edition-2, edition-3, edition-4,
                condensed, programmers, do-it). Defaults to edition-2.

    Returns:
        A dictionary containing the strategy text and edition information.
    """
    return manager.get_random_strategy(edition)


@mcp.tool()
def search_strategies(query: str, edition: Optional[str] = None) -> Dict[str, Any]:
    """
    Search for strategies containing the specified keywords.

    Args:
        query: Keywords to search for (case-insensitive).
        edition: Optional edition to limit search to. If not specified,
                searches all editions.

    Returns:
        A dictionary containing matching strategies and their editions.
    """
    return manager.search_strategies(query, edition)


@mcp.tool()
def list_editions() -> Dict[str, Any]:
    """
    List all available editions and their descriptions.

    Returns:
        Information about all available editions.
    """
    return manager.list_editions()


def main() -> None:
    """Main entry point for the MCP server."""
    import sys

    # Print server info to stderr
    print("Starting Oblique Strategies MCP server...", file=sys.stderr)

    # Run the FastMCP server using stdio transport
    mcp.run()


# Entry point for running the server
if __name__ == "__main__":
    main()
