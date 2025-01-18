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
    result = detect_language_patterns(messages, method=method, n=n, top_n=top_n)
    assert result == expected


