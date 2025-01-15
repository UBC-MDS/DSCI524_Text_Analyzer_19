from textanalyser.visualize_language_patterns import visualize_language_patterns

@pytest.mark.parametrize(
    "patterns, method",
    [
        (["en", "fr", "en"], "language"),
        ([('python package', 2), ('package example', 1)], "ngrams"),
        ([('a', 10), ('b', 5)], "char_patterns"),
    ]
)
def test_visualize_language_patterns(patterns, method):
    """
    """
    try:
        visualize_language_patterns(patterns, method)
    except Exception as e:
        pytest.fail(f"Visualization failed with error: {e}")