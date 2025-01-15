import pytest
from textanalyzer.visualize_language_patterns import visualize_language_patterns

def test_visualize_language_patterns_language():
    try:
        visualize_language_patterns(["en", "fr", "en"], method="language")
    except Exception as e:
        pytest.fail(f"Visualization failed with error: {e}")

def test_visualize_language_patterns_ngrams():
    try:
        visualize_language_patterns([('python package', 2), ('package example', 1)], method="ngrams")
    except Exception as e:
        pytest.fail(f"Visualization failed with error: {e}")

def test_visualize_language_patterns_char_patterns():
    try:
        visualize_language_patterns([('a', 10), ('b', 5)], method="char_patterns")
    except Exception as e:
        pytest.fail(f"Visualization failed with error: {e}")
