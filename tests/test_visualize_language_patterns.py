import pytest
from textanalyzer.visualize_language_patterns import visualize_language_patterns

@pytest.mark.parametrize(
    "patterns, method",
    [
        (["en", "fr", "en"], "language"),
        ([("python package", 2), ("package example", 1)], "ngrams"),
        ([("a", 10), ("b", 5)], "char_patterns"),
    ]
)
def test_visualize_language_patterns(patterns, method):
    """
    Test visualize_language_patterns with supported methods.
    """
    try:
        visualize_language_patterns(patterns, method)
    except Exception as e:
        pytest.fail(f"Visualization failed with error: {e}")

def test_visualize_language_patterns_invalid_method():
    """
    Test that an unsupported method raises ValueError.
    """
    with pytest.raises(ValueError, match="Unsupported method for visualization."):
        visualize_language_patterns(["en", "fr"], method="invalid_method")

def test_visualize_language_patterns_empty_data():
    """
    Test that empty data does not break the function.
    """
    try:
        visualize_language_patterns([], method="language")
    except Exception as e:
        pytest.fail(f"Visualization failed with empty data: {e}")

def test_visualize_language_patterns_non_list_input():
    """
    Test that non-list input raises TypeError.
    """
    with pytest.raises(TypeError, match="Patterns must be a list."):
        visualize_language_patterns("invalid_input", method="language")

def test_visualize_language_patterns_malformed_patterns():
    """
    Test that malformed pattern data raises ValueError.
    """
    with pytest.raises(ValueError, match="patterns must be a list of \(label, value\) tuples."):
        visualize_language_patterns(["invalid", "data"], method="ngrams")

def test_visualize_language_patterns_non_string_method():
    """
    Test that non-string method input raises TypeError.
    """
    with pytest.raises(TypeError, match="Method must be a string."):
        visualize_language_patterns(["en", "fr"], method=123)
