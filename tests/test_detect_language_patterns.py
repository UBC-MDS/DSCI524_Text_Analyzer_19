from textanalyser.detect_language_patterns import detect_language_patterns

@pytest.mark.parametrize(
    "messages, method, n, top_n, expected",
    [
        (["Hello World!", "Bonjour le monde!"], "language", 2, 5, ["en", "fr"]),
        (["test data for ngrams"], "ngrams", 2, 2, [("test data", 1), ("data for", 1)]),
        (["hello hello hello"], "char_patterns", 2, 2, [("h", 3), ("e", 3)]),
    ]
)

def test_detect_language_patterns(messages, method, n, top_n, expected):
    """
    """
    result = detect_language_patterns(messages, method, n, top_n)
    assert result == expected


    