from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
def topic_modeling(messages, n_topics=5, n_words=10, random_state=123):
    """
    Perform topic modeling using Non-negative Matrix Factorization (NMF).
    
    Parameters:
        messages (list of str): List of text for topic modeling.
        n_topics (int): Number of topics to extract. Optional, default set to 5.
        n_words (int): Number of top words to display per topic. Optional, default set to 10.
        random_state (int): Random seed for reproducibility. Optional, default set to 123.
        
    Returns:
        topics (list of list): A list of topics, where each topic is a list of its top representative words.
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