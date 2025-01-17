import pytest
from textanalyzer.extract_keywords import extract_keywords

@pytest.mark.parametrize(
    "messages, method, num_keywords, expected",
    [
        (
            ["Data Science is fun and Learning Data science at MDS is amazing!", "What is Python? Do you like learning Python? Learning it makes me crazy"],
            "tfidf",
            3,
            [['science', 'data', 'mds'], ['python', 'learning', 'makes']]
        )
    ]
)

def test_extract_keywords(messages, method, num_keywords, expected):
    """Test function with valid data"""
    result = extract_keywords(messages, method=method, num_keywords=num_keywords)
    assert result == expected

def test_invalid_message():
    """Test function with invalid message"""
    with pytest.raises(TypeError, match="messages must be a list of strings"):
        extract_keywords([123, "Valid message"], method="tfidf", num_keywords=3)

def test_invalid_method():
    """Test function with invalid method"""
    with pytest.raises(ValueError, match="Unsupported method"):
        extract_keywords(["Valid message"], method="unsupported", num_keywords=3)


