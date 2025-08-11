#!/usr/bin/env python3
"""
Core logic for Oblique Strategies operations.
Separated from MCP framework for easier testing.
"""

import random
from pathlib import Path
from typing import Optional, List, Dict, Any, Union


class StrategiesManager:
    """Manager for loading and searching Oblique Strategies."""

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

    def __init__(self, strategies_dir: Optional[Path] = None):
        """Initialize with optional custom strategies directory."""
        if strategies_dir is None:
            strategies_dir = Path(__file__).parent / "strategies"
        self.strategies_dir = strategies_dir
        self._cache: Dict[str, List[str]] = {}

    def load_strategies(self, edition: str = DEFAULT_EDITION) -> List[str]:
        """Load strategies from the specified edition file."""
        # Use cached version if available
        if edition in self._cache:
            return self._cache[edition]

        if edition not in self.EDITIONS:
            edition = self.DEFAULT_EDITION

        file_path = self.strategies_dir / self.EDITIONS[edition]

        if not file_path.exists():
            raise FileNotFoundError(f"Strategy file not found: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            # Filter out empty lines and strip whitespace
            strategies = [line.strip() for line in f if line.strip()]

        # Cache the loaded strategies
        self._cache[edition] = strategies
        return strategies

    def get_random_strategy(
        self, edition: Optional[str] = None
    ) -> Dict[str, Union[str, int]]:
        """Get a random strategy from the specified edition."""
        if edition is None:
            edition = self.DEFAULT_EDITION

        try:
            strategies = self.load_strategies(edition)
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

    def search_strategies(
        self, query: str, edition: Optional[str] = None
    ) -> Dict[str, Any]:
        """Search for strategies containing the specified keywords."""
        query_lower = query.lower()
        results = []

        # Determine which editions to search
        editions_to_search = (
            [edition] if edition and edition in self.EDITIONS else self.EDITIONS.keys()
        )

        for ed in editions_to_search:
            try:
                strategies = self.load_strategies(ed)
                for strategy in strategies:
                    if query_lower in strategy.lower():
                        results.append({"strategy": strategy, "edition": ed})
            except (FileNotFoundError, Exception):
                # Skip editions that can't be loaded
                continue

        return {
            "query": query,
            "matches": results,
            "count": len(results),
            "searched_editions": list(editions_to_search),
        }

    def list_editions(self) -> Dict[str, Any]:
        """List all available editions and their descriptions."""
        edition_info = []

        for key, filename in self.EDITIONS.items():
            file_path = self.strategies_dir / filename
            if file_path.exists():
                try:
                    strategies = self.load_strategies(key)
                    count = len(strategies)
                except Exception:
                    count = 0

                edition_info.append(
                    {
                        "key": key,
                        "filename": filename,
                        "strategy_count": count,
                        "is_default": key == self.DEFAULT_EDITION,
                    }
                )

        return {"editions": edition_info, "default_edition": self.DEFAULT_EDITION}
