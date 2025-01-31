from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
def topic_modeling(messages: List[str], n_topics: int = 5, n_words: int = 10, random_state: int = 123) -> Dict[str, List[str]]:
    """
    Perform topic modeling using Non-negative Matrix Factorization (NMF).

    Parameters
    ----------
    messages : List[str]
        List of messages for topic modeling.
    n_topics : int, optional
        Number of topics to extract, by default 5.
    n_words : int, optional
        Number of top words to display per topic, by default 10.
    random_state : int, optional
        Random seed for reproducibility, by default 123.

    Returns
    -------
    Dict[str, List[str]]
        A dictionary where each key is a topic label (e.g., "Topic 1") and each value is a list of the most representative words for that topic.

    Raises
    ------
    TypeError
        If `messages` is not a list of strings.

    Examples
    --------
    >>> messages = ["Learning Data science at MDS is amazing!", "I prefer to work with Python than R"]
    >>> topic_modeling(messages, n_topics = 3, n_words = 3)
    {'Topic 1': ['mds', 'science', 'learning'], 'Topic 2': ['work', 'python', 'prefer'], 'Topic 3': ['amazing', 'data', 'learning']}
    """
   
    if not isinstance(messages, list):
        raise TypeError("Input messages should be a list of strings.")
    for doc in messages:
        if not isinstance(doc, str):
            raise TypeError("Input messages should be a list of strings.")

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(messages)
    
    nmf_model = NMF(n_components=n_topics, random_state=random_state, init='random')
    W = nmf_model.fit_transform(tfidf_matrix)
    H = nmf_model.components_
    
    feature_names = vectorizer.get_feature_names_out()
    topics = {}
    
    for topic_idx, topic_weights in enumerate(H):
        top_word_indices = topic_weights.argsort()[:-n_words - 1:-1]
        top_words = [feature_names[i] for i in top_word_indices]
        topics[f"Topic {topic_idx + 1}"] = top_words
    return topics