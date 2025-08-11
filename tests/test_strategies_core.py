#!/usr/bin/env python3
"""Tests for the Oblique Strategies core logic."""

import pytest
from pathlib import Path
from unittest.mock import patch
from oblique_strategies_mcp.strategies_core import StrategiesManager


@pytest.fixture
def temp_strategies_dir(tmp_path):
    """Create a temporary directory with test strategy files."""
    strategies_dir = tmp_path / "strategies"
    strategies_dir.mkdir()

    # Create test strategy files
    (strategies_dir / "oblique-strategies-edition-1.txt").write_text(
        "Strategy 1\nStrategy 2\nStrategy 3\n"
    )
    (strategies_dir / "oblique-strategies-edition-2.txt").write_text(
        "Default strategy 1\nDefault strategy 2\n"
    )
    (strategies_dir / "prompts-for-programmers.txt").write_text(
        "Debug it\nRefactor it\nTest it\n"
    )

    return strategies_dir


@pytest.fixture
def manager(temp_strategies_dir):
    """Create a StrategiesManager with test data."""
    return StrategiesManager(temp_strategies_dir)


class TestStrategiesManager:
    """Tests for the StrategiesManager class."""

    def test_load_strategies(self, manager):
        """Test loading strategies from a file."""
        strategies = manager.load_strategies("edition-1")
        assert len(strategies) == 3
        assert "Strategy 1" in strategies
        assert "Strategy 2" in strategies
        assert "Strategy 3" in strategies

    def test_load_strategies_default(self, manager):
        """Test loading default edition."""
        strategies = manager.load_strategies()
        assert len(strategies) == 2
        assert "Default strategy 1" in strategies

    def test_load_strategies_caching(self, manager):
        """Test that strategies are cached after first load."""
        # First load
        strategies1 = manager.load_strategies("edition-1")
        # Second load should use cache
        strategies2 = manager.load_strategies("edition-1")
        assert strategies1 is strategies2  # Same object reference

    def test_load_strategies_invalid_edition(self, manager):
        """Test loading with invalid edition falls back to default."""
        strategies = manager.load_strategies("nonexistent")
        assert len(strategies) == 2  # Default edition

    def test_get_random_strategy(self, manager):
        """Test getting a random strategy."""
        result = manager.get_random_strategy("edition-1")
        assert "strategy" in result
        assert result["edition"] == "edition-1"
        assert result["total_in_edition"] == 3
        assert result["strategy"] in ["Strategy 1", "Strategy 2", "Strategy 3"]

    def test_get_random_strategy_default(self, manager):
        """Test getting a random strategy with default edition."""
        result = manager.get_random_strategy()
        assert "strategy" in result
        assert result["edition"] == "edition-2"
        assert result["total_in_edition"] == 2

    def test_get_random_strategy_missing_file(self, manager):
        """Test error handling for missing strategy file."""
        # Remove one of the expected files
        manager.strategies_dir = Path("/nonexistent")
        result = manager.get_random_strategy("edition-1")
        assert "error" in result
        assert "not found" in result["error"]

    def test_search_strategies(self, manager):
        """Test searching for strategies."""
        result = manager.search_strategies("strategy")
        assert result["query"] == "strategy"
        assert result["count"] > 0
        matches = result["matches"]
        assert any(m["edition"] == "edition-1" for m in matches)
        assert any(m["edition"] == "edition-2" for m in matches)

    def test_search_strategies_specific_edition(self, manager):
        """Test searching within a specific edition."""
        result = manager.search_strategies("Debug", "programmers")
        assert result["count"] == 1
        assert result["matches"][0]["strategy"] == "Debug it"
        assert result["matches"][0]["edition"] == "programmers"

    def test_search_strategies_case_insensitive(self, manager):
        """Test that search is case-insensitive."""
        result = manager.search_strategies("STRATEGY")
        assert result["count"] > 0

    def test_search_no_matches(self, manager):
        """Test searching with no matches."""
        result = manager.search_strategies("xyzabc123")
        assert result["count"] == 0
        assert result["matches"] == []

    def test_list_editions(self, manager):
        """Test listing all available editions."""
        result = manager.list_editions()
        assert "editions" in result
        assert "default_edition" in result
        assert result["default_edition"] == "edition-2"

        editions = result["editions"]
        assert len(editions) >= 3

        # Find edition-1 info
        edition_1 = next(e for e in editions if e["key"] == "edition-1")
        assert edition_1["strategy_count"] == 3
        assert not edition_1["is_default"]

        # Find default edition
        default = next(e for e in editions if e["is_default"])
        assert default["key"] == "edition-2"
        assert default["strategy_count"] == 2


class TestRandomness:
    """Test randomness-related functionality."""

    @patch("random.choice")
    def test_random_strategy_uses_random_choice(self, mock_choice, manager):
        """Test that get_random_strategy actually uses random.choice."""
        mock_choice.return_value = "Strategy 2"
        result = manager.get_random_strategy("edition-1")
        assert result["strategy"] == "Strategy 2"
        mock_choice.assert_called_once()
        # Verify it was called with the correct list
        call_args = mock_choice.call_args[0][0]
        assert "Strategy 2" in call_args
