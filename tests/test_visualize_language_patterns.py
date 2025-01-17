# import pytest
# from textanalyzer.visualize_language_patterns import visualize_language_patterns

# @pytest.mark.parametrize(
#     "patterns, method",
#     [
#         # Language visualization
#         (["en", "fr", "en"], "language"),
        
#         # N-grams visualization
#         ([("python package", 2), ("package example", 1)], "ngrams"),
        
#         # Character patterns visualization
#         ([("a", 10), ("b", 5)], "char_patterns"),
#     ]
# )

# def test_visualize_language_patterns(patterns, method):
#     try:
#         visualize_language_patterns(patterns, method)
#     except Exception as e:
#         pytest.fail(f"Visualization failed with error: {e}")

