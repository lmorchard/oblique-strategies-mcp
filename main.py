#!/usr/bin/env python3
"""
Oblique Strategies MCP Server

An MCP server providing access to Brian Eno's Oblique Strategies
for creative problem-solving and lateral thinking.
"""

import random
from pathlib import Path
from typing import Optional, List, Dict, Any, Union

from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("Oblique Strategies")

# Define available editions and their corresponding files
STRATEGIES_DIR = Path(__file__).parent / "strategies"
EDITIONS = {
    "edition-1": "oblique-strategies-edition-1.txt",
    "edition-2": "oblique-strategies-edition-2.txt",  # Default
    "edition-3": "oblique-strategies-edition-3.txt",
    "edition-4": "oblique-strategies-edition-4.txt",
    "condensed": "oblique-strategies-condensed.txt",
    "programmers": "prompts-for-programmers.txt",
    "do-it": "do-it-abridged.txt",
}

DEFAULT_EDITION = "edition-2"


def load_strategies(edition: str = DEFAULT_EDITION) -> List[str]:
    """Load strategies from the specified edition file."""
    if edition not in EDITIONS:
        edition = DEFAULT_EDITION

    file_path = STRATEGIES_DIR / EDITIONS[edition]

    if not file_path.exists():
        raise FileNotFoundError(f"Strategy file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        # Filter out empty lines and strip whitespace
        strategies = [line.strip() for line in f if line.strip()]

    return strategies


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
    if edition is None:
        edition = DEFAULT_EDITION

    try:
        strategies = load_strategies(edition)
        if not strategies:
            return {
                "error": f"No strategies found in edition: {edition}",
                "edition": edition,
            }

        strategy = random.choice(strategies)
        return {
            "strategy": strategy,
            "edition": edition,
            "total_in_edition": len(strategies),
        }
    except FileNotFoundError as e:
        return {"error": str(e), "edition": edition}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}", "edition": edition}


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
    query_lower = query.lower()
    results = []

    # Determine which editions to search
    editions_to_search = (
        [edition] if edition and edition in EDITIONS else EDITIONS.keys()
    )

    for ed in editions_to_search:
        try:
            strategies = load_strategies(ed)
            for strategy in strategies:
                if query_lower in strategy.lower():
                    results.append({"strategy": strategy, "edition": ed})
        except FileNotFoundError:
            # Skip editions that can't be loaded
            continue
        except Exception:
            # Skip editions with errors
            continue

    return {
        "query": query,
        "matches": results,
        "count": len(results),
        "searched_editions": list(editions_to_search),
    }


@mcp.tool()
def list_editions() -> Dict[str, Any]:
    """
    List all available editions and their descriptions.

    Returns:
        Information about all available editions.
    """
    edition_info = []

    for key, filename in EDITIONS.items():
        file_path = STRATEGIES_DIR / filename
        if file_path.exists():
            try:
                strategies = load_strategies(key)
                count = len(strategies)
            except Exception:
                count = 0

            edition_info.append(
                {
                    "key": key,
                    "filename": filename,
                    "strategy_count": count,
                    "is_default": key == DEFAULT_EDITION,
                }
            )

    return {"editions": edition_info, "default_edition": DEFAULT_EDITION}


def main():
    """Main entry point for the MCP server."""
    from mcp.server.stdio import stdio_server

    # Run the server using stdio transport
    stdio_server(mcp)


# Entry point for running the server
if __name__ == "__main__":
    main()
