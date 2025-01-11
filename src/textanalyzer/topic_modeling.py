def topic_modeling(documents, n_topics=5, n_words=10, random_state=123):
    """
    Perform topic modeling using Non-negative Matrix Factorization (NMF).
    
    Parameters:
        documents (list of str): List of text documents for topic modeling.
        n_topics (int): Number of topics to extract. Optional, default set to 5.
        n_words (int): Number of top words to display per topic. Optional, default set to 10.
        random_state (int): Random seed for reproducibility. Optional, default set to 123.
        
    Returns:
        topics (list of list): A list of topics, where each topic is a list of top words.
    """