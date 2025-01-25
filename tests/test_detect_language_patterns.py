import pytest
from txtanalyzer.detect_language_patterns import detect_language_patterns

sample_text = [
    "Artificial intelligence and machine learning are transforming industries around the globe.",
    "The basketball team secured a thrilling victory in the final seconds of the game.",
    "Yoga and meditation are excellent for reducing stress and improving mental health.",
    "Exploring the hidden beaches of Bali is an unforgettable experience for any traveler.",
    "Quantum computing is expected to revolutionize data processing and cryptography."
]

# Test for valid language detection
def test_detect_language_patterns_language():
    """
    Test language detection method with valid input.
    """
    result = detect_language_patterns(sample_text, method="language")
    assert all(lang == "en" for lang in result)

# Test for valid n-gram detection
def test_detect_language_patterns_ngrams():
    """
    Test n-grams detection method with valid input.
    """
    result = detect_language_patterns(sample_text, method="ngrams", n=2, top_n=3)
    assert len(result) == 3

# Test for valid character pattern detection
def test_detect_language_patterns_char_patterns():
    """
    Test character pattern detection with valid input.
    """
    result = detect_language_patterns(sample_text, method="char_patterns", top_n=3)
    assert len(result) == 3

# Test for unsupported method (should raise ValueError)
def test_detect_language_patterns_invalid_method():
    """
    Test that an unsupported method raises a ValueError.
    """
    with pytest.raises(ValueError, match="Unsupported method."):
        detect_language_patterns(sample_text, method="invalid_method")

# Test for non-list input (should raise TypeError)
def test_detect_language_patterns_non_list_input():
    """
    Test that non-list input raises a TypeError.
    """
    with pytest.raises(TypeError, match="messages must be a list of strings"):
        detect_language_patterns("This is a string, not a list.", method="language")

# Test for non-string elements in the list (should raise TypeError)
def test_detect_language_patterns_non_string_elements():
    """
    Test that a list with non-string elements raises a TypeError.
    """
    with pytest.raises(TypeError, match="messages must be a list of strings"):
        detect_language_patterns(["Valid text", 42], method="language")

# Test for empty input list
def test_detect_language_patterns_empty_input():
    """
    Test that an empty list returns an empty result.
    """
    result = detect_language_patterns([], method="language")
    assert result == []

def test_detect_language_patterns_invalid_n_value():
    """
    Test that an invalid 'n' value in n-grams raises a ValueError.
    """
    with pytest.raises(ValueError, match="Parameter 'n' must be a positive integer."):
        detect_language_patterns(["test data"], method="ngrams", n=0)
        
def test_detect_language_patterns_unsupported_method():
    """
    Test that using an unsupported method raises a ValueError.
    """
    with pytest.raises(ValueError, match="Unsupported method. Choose from 'language', 'ngrams', or 'char_patterns'."):
        detect_language_patterns(["test data"], method="invalid_method")
