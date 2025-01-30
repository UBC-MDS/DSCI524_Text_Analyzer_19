import pytest
from messageanalyzer.extract_keywords import extract_keywords

@pytest.mark.parametrize(
    "messages, num_keywords, expected",
    [
        (
            ["Data Science is fun and Learning Data science at MDS is amazing!", "What is Python? Do you like learning Python? Learning it makes me crazy"],
            3,
            [['science', 'data', 'mds'], ['python', 'learning', 'makes']]
        )
    ]
)

def test_extract_keywords(messages, num_keywords, expected):
    """Test function with valid data"""
    result = extract_keywords(messages, num_keywords=num_keywords)
    assert result == expected

def test_invalid_message():
    """Test function with invalid message"""
    with pytest.raises(TypeError, match="messages must be a list of strings"):
        extract_keywords([123, "Valid message"], num_keywords=3)
