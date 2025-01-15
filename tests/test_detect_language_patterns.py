import pytest
from textanalyzer.detect_language_patterns import detect_language_patterns

def test_detect_language_patterns_language():
    messages = ["Hello World!", "Bonjour le monde!"]
    result = detect_language_patterns(messages, method="language")
    assert result == ["en", "fr"]

def test_detect_language_patterns_ngrams():
    messages = ["test data for ngrams"]
    result = detect_language_patterns(messages, method="ngrams", n=2, top_n=2)
    assert result == [("test data", 1), ("data for", 1)]

def test_detect_language_patterns_char_patterns():
    messages = ["hello hello hello"]
    result = detect_language_patterns(messages, method="char_patterns", top_n=2)
    assert result == [("l", 6), ("h", 3)]

