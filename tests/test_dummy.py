"""Basic dummy test to ensure testing infrastructure works."""


def test_addition():
    """Test that basic math works - dummy test for setup verification."""
    assert 2 + 2 == 4


def test_string_operations():
    """Test basic string operations - another dummy test."""
    text = "oblique strategies"
    assert text.title() == "Oblique Strategies"
    assert len(text.split()) == 2


def test_list_operations():
    """Test basic list operations."""
    strategies = ["Use an old idea", "What would your closest friend do?", "Honor thy error as a hidden intention"]
    assert len(strategies) == 3
    assert strategies[0] == "Use an old idea"