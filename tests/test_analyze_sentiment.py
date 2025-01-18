import pytest
from textanalyzer.sentiment_analysis import analyze_sentiment

@pytest.mark.parametrize(
    "messages, model, expected",
    [
        # Default model detection
        (["I love this movie! It's amazing and so entertaining."], "Default", 
         [{'message': "I love this movie! It's amazing and so entertaining.", 'score': 0.5750000000000001, 'label': 'positive'}]),
        
        # Invalid input message detection
        ("I love this movie! It's amazing and so entertaining.", "Default", TypeError),
        
        # Multiple input message detection
        (["I love this movie! It's amazing and so entertaining.", "Hello! This is Tom!"], "Default",
        [{'message': "I love this movie! It's amazing and so entertaining.", 'score': 0.5750000000000001, 'label': 'positive'}, {'message': 'Hello! This is Tom!', 'score': 0.0, 'label': 'neutral'}]),

        # Invalid model detection
        (["Hello!"], "Model", ValueError)
    ]
)

def test_analyze_sentiment(messages, model, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        # If the expected result is an exception, we need to check for that
        with pytest.raises(expected):
            analyze_sentiment(messages, model)
    else:
        # Otherwise, test for the expected result when no exception is expected
        result = analyze_sentiment(messages, model)
        assert result == expected