import pytest
from textanalyzer.visualize_language_patterns import visualize_language_patterns

sample_text = [
    "Artificial intelligence and machine learning are transforming industries around the globe.",
    "The basketball team secured a thrilling victory in the final seconds of the game.",
    "Yoga and meditation are excellent for reducing stress and improving mental health.",
    "Exploring the hidden beaches of Bali is an unforgettable experience for any traveler.",
    "Quantum computing is expected to revolutionize data processing and cryptography."
]

@pytest.mark.parametrize(
    "patterns, method",
    [
        ([sample_text[1]], "language"),
        ([("machine learning", 3), ("artificial intelligence", 2)], "ngrams"),
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
    with pytest.raises(ValueError, match=r"Unsupported method for visualization."):
        visualize_language_patterns(["en", "fr"], method="invalid_method")

def test_visualize_language_patterns_empty_data():
    """
    Test that empty data raises a ValueError.
    """
    with pytest.raises(ValueError, match=r"Patterns list is empty. Cannot generate visualization."):
        visualize_language_patterns([], method="language")

def test_visualize_language_patterns_empty_ngrams():
    """
    Test that empty n-grams data raises a ValueError.
    """
    with pytest.raises(ValueError, match=r"Patterns list is empty. Cannot generate visualization."):
        visualize_language_patterns([], method="ngrams")

def test_visualize_language_patterns_empty_char_patterns():
    """
    Test that empty character pattern data raises a ValueError.
    """
    with pytest.raises(ValueError, match=r"Patterns list is empty. Cannot generate visualization."):
        visualize_language_patterns([], method="char_patterns")

def test_visualize_language_patterns_non_list_input():
    """
    Test that non-list input raises TypeError.
    """
    with pytest.raises(TypeError, match=r"Patterns must be a list."):
        visualize_language_patterns("invalid_input", method="language")

def test_visualize_language_patterns_malformed_patterns():
    """
    Test that malformed pattern data raises ValueError.
    """
    with pytest.raises(ValueError, match=r"patterns must be a list of \(label, value\) tuples."):
        visualize_language_patterns(["invalid", "data"], method="ngrams")

def test_visualize_language_patterns_invalid_tuple_structure():
    """
    Test that invalid tuple structure raises a ValueError for 'ngrams' and 'char_patterns'.
    """
    with pytest.raises(ValueError, match=r"patterns must be a list of \(label, value\) tuples."):
        visualize_language_patterns([("valid", 1), ("invalid",)], method="ngrams")

def test_visualize_language_patterns_non_string_method():
    """
    Test that non-string method input raises TypeError.
    """
    with pytest.raises(TypeError, match=r"Method must be a string."):
        visualize_language_patterns(["en", "fr"], method=123)

def test_visualize_language_patterns_unsupported_data_structure():
    """
    Test that passing a tuple instead of a list raises a TypeError for 'language' method.
    """
    with pytest.raises(TypeError, match=r"Patterns must be a list."):
        visualize_language_patterns(("en", "fr"), method="language")

def test_visualize_language_patterns_empty_language_counter():
    """
    Test that an empty Counter in 'language' method raises a ValueError.
    """
    with pytest.raises(ValueError, match=r"No language data to visualize."):
        visualize_language_patterns(["", ""], method="language")
