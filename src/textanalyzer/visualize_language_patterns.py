def visualize_language_patterns(patterns, method="language"):
    """
    Visualizes detected language patterns.

    Parameters
    ----------
    patterns : list
        The output from `detect_language_patterns` function.

    method : str, default="language"
        The method used for pattern detection. Supported methods are:
        - "language": Displays a bar chart of detected languages.
        - "ngrams": Displays a bar chart of top n-grams.
        - "char_patterns": Displays a bar chart of common characters.
    """
    