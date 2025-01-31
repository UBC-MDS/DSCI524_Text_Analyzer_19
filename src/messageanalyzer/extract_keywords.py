from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(messages: List[str], num_keywords: int = 5) -> List[List[str]]:
    
    """
    Extracts top keywords from the list of messages using the given methods.

    Parameters
    ----------
    messages : List[str]
        A list of text messages to extract keywords.

    method : str, default = "tfidf"
        The method to use for keyword extraction.
        - "tfidf": Term Frequency-Inverse Document Frequency.

    num_keywords : int, default = 5
        The number of keywords to extract from each message.
    
    Raises
    ------
    TypeError
        If `messages` is not a list of strings.

    Returns
    -------
    List[List[str]]
        A list containing sublists of extracted keywords for each message. 

    Examples
    --------
    >>> messages = ["Learning Data science at MDS is amazing!", "I prefer to work with Python than R"]
    >>> extract_keywords(messages, method="tfidf", num_keywords=3)
    [['data', 'science', 'amazing'], ['python', 'prefer', 'work']]
    """

    if not isinstance(messages, list) or not all(isinstance(msg, str) for msg in messages):
        raise TypeError("messages must be a list of strings")
    
    
    tf_idf_vectorizer = TfidfVectorizer(stop_words='english')

    tf_idf_vector = tf_idf_vectorizer.fit_transform(messages)

    feature_names = tf_idf_vectorizer.get_feature_names_out()

    top_keywords = []

    for i in range(len(messages)):
                
        msg_vector = tf_idf_vector[i].toarray().flatten()

        keywords = sorted(zip(msg_vector, feature_names), reverse= True)

        n_keywords = [word for _, word in keywords[:num_keywords]]
                
        top_keywords.append(n_keywords)
    
    return top_keywords