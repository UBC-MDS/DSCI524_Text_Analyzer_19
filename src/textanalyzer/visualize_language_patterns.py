import matplotlib.pyplot as plt
from collections import Counter

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

    Raises
    ------
    TypeError
        If patterns is not a list or method is not a string.

    ValueError
        If method is not one of the supported types.
    """
    if not isinstance(patterns, list):
        raise TypeError("Patterns must be a list.")

    if not isinstance(method, str):
        raise TypeError("Method must be a string.")

    if not patterns:
        raise ValueError("Patterns list is empty. Cannot generate visualization.")

    if method == "language":
        # Filter out empty or whitespace-only strings
        cleaned_patterns = [p for p in patterns if p.strip()]
        if not cleaned_patterns:
            raise ValueError("No language data to visualize.")
        counts = Counter(cleaned_patterns)
        plt.bar(counts.keys(), counts.values(), color='skyblue', edgecolor='black')
        plt.title("Detected Languages")
        plt.xlabel("Language")
        plt.ylabel("Frequency")

    elif method in ["ngrams", "char_patterns"]:
        if not all(isinstance(pair, tuple) and len(pair) == 2 for pair in patterns):
            raise ValueError("For 'ngrams' and 'char_patterns', patterns must be a list of (label, value) tuples.")
        labels, values = zip(*patterns)
        plt.bar(labels, values, color='skyblue', edgecolor='black')
        plt.title("Top N-grams" if method == "ngrams" else "Common Character Patterns")
        plt.xlabel("N-gram" if method == "ngrams" else "Character")
        plt.ylabel("Frequency")
        plt.xticks(rotation=45)

    else:
        raise ValueError("Unsupported method for visualization.")

    plt.tight_layout()
    plt.show()
