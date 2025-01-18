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
        # Check for expected errors
        with pytest.raises(expected):
            analyze_sentiment(messages, model)
    else:
        # Check for expected usual outputs
        result = analyze_sentiment(messages, model)
        assert result == expected