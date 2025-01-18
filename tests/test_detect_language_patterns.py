import pytest
from textanalyzer.detect_language_patterns import detect_language_patterns

@pytest.mark.parametrize(
    "messages, method, n, top_n, expected",
    [
        # Language detection
        (["Hello World!", "Bonjour le monde!"], "language", 2, 5, ["en", "fr"]),
        
        # N-grams detection
        (["test data for ngrams"], "ngrams", 2, 2, [("test data", 1), ("data for", 1)]),
        
        # Character pattern detection 
        (["hello hello hello"], "char_patterns", 2, 2, [("l", 6), ("h", 3)]),
    ]
)
def test_detect_language_patterns(messages, method, n, top_n, expected):
    """
    Test detect_language_patterns with supported methods.
    """
    result = detect_language_patterns(messages, method=method, n=n, top_n=top_n)
    assert result == expected

def test_detect_language_patterns_invalid_method():
    """
    Test that an unsupported method raises a ValueError.
    """
    with pytest.raises(ValueError, match="Unsupported method. Choose from 'language', 'ngrams', or 'char_patterns'."):
        detect_language_patterns(["Hello World!"], method="invalid_method")

def test_detect_language_patterns_invalid_messages_type():
    """
    Test that a non-list input raises a TypeError.
    """
    with pytest.raises(TypeError, match="messages must be a list of strings"):
        detect_language_patterns("Hello World!", method="language")

def test_detect_language_patterns_non_string_in_list():
    """
    Test that a list with non-string elements raises a TypeError.
    """
    with pytest.raises(TypeError, match="messages must be a list of strings"):
        detect_language_patterns(["Hello", 123], method="language")
