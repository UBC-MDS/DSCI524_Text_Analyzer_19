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
    result = extract_keywords(messages, method=method, num_keywords=num_keywords)
    assert result == expected


