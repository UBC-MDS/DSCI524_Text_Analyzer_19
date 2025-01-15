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
    if method == "language":
        counts = Counter(patterns)
        plt.bar(counts.keys(), counts.values())
        plt.title("Detected Languages")
        plt.xlabel("Language")
        plt.ylabel("Frequency")

    elif method == "ngrams":
        labels, values = zip(*patterns)
        plt.bar(labels, values)
        plt.title("Top N-grams")
        plt.xlabel("N-gram")
        plt.ylabel("Frequency")
        plt.xticks(rotation=45)

    elif method == "char_patterns":
        labels, values = zip(*patterns)
        plt.bar(labels, values)
        plt.title("Common Character Patterns")
        plt.xlabel("Character")
        plt.ylabel("Frequency")
    else:
        raise ValueError("Unsupported method for visualization.")
    plt.tight_layout()
    plt.show()


    