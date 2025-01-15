import pytest
from textanalyzer.sentiment_analysis import analyze_sentiment

@pytest.mark.parametrize(
    "messages, model",
    [
        # Default model detection
        (["Hello World!", "Bonjour le monde!"], "default"),
        
        # Simple model detection - VADER
        (["testing for test model"], "VADER"),
        
        # Simple model detection - pretrained transformer models
        (["hello hello hello"], "BERT"),
    ]
)

def test_analyze_sentiment(messages, model, expected):
    result = analyze_sentiment(messages, model)
    assert result == expected