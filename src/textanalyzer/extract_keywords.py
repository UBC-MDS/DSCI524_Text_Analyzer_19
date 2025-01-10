def extract_keywords(messages, method="tfidf", num_keywords=5):
    """
    Extracts top keywords from the list of messages using the given methods.

    Parameters
    ----------
    messages : list of str
        A list of text messages to extract keywords.

    method : str, default="tfidf"
        The method to use for keyword extraction. Supported methods are:
        - "tfidf": Term Frequency-Inverse Document Frequency.
        - "rake": Rapid Automatic Keyword Extraction.

    num_keywords : int, default=5
        The number of keywords to extract from each message.

    Returns
    -------
    list of list of str
        A list containing sublists of extracted keywords for each message. 

    Examples
    --------
    >>> messages = ["Learning Data science at MDS is amazing!", "I prefer to work with Python than R"]
    >>> extract_keywords(messages, method="tfidf", num_keywords=3)
    [['data', 'science', 'amazing'], ['python', 'prefer', 'work']]

    """