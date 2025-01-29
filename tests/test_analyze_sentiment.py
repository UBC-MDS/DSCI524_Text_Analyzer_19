import pytest
from messageanalyzer.sentiment_analysis import analyze_sentiment

@pytest.mark.parametrize(
    "messages, model, expected",
    [
        # Default model detection
        (["I love this movie! It's amazing and so entertaining."], "Default", 
         [{'message': "I love this movie! It's amazing and so entertaining.", 'score': 0.5750000000000001, 'label': 'positive'}]),
        
        # Invalid input message detection
        ("I love this movie! It's amazing and so entertaining.", "Default", TypeError),

        # Invalid input message detection
        (["I love this movie! It's amazing and so entertaining.", 2], "Default", TypeError),
        
        # Multiple input message detection
        (["I love this movie! It's amazing and so entertaining.", "Hello! This is Tom!"], "Default",
        [{'message': "I love this movie! It's amazing and so entertaining.", 'score': 0.5750000000000001, 'label': 'positive'}, {'message': 'Hello! This is Tom!', 'score': 0.0, 'label': 'neutral'}]),

        # Invalid model detection
        (["Hello!"], "Model", ValueError)
    ]
)

def test_analyze_sentiment(messages, model, expected):
    """
    Tests the 'analyze_sentiment' function by verifying its behavior under different input conditions.
    
    This test function uses pytest's parameterized testing to run multiple test cases for the 
    sentiment analysis function. It checks both the expected behavior when the function runs 
    successfully and the handling of errors when invalid inputs are provided.
    
    Parameters:
    -----------
    messages : list of str
        A list of messages to be analyzed for sentiment by the 'analyze_sentiment' function.
        This parameter can also be a single string (to test the function's handling of invalid input).
        
    model : str
        The sentiment analysis model to use. In this test, the "Default" model is primarily tested, 
        but other model names like "Model" are used to test error handling.
        
    expected : object or Exception
        The expected result from the sentiment analysis function. If an exception is expected (such as 
        TypeError or ValueError), this parameter will be set to the corresponding exception type. 
        Otherwise, it will be set to the expected output of the 'analyze_sentiment' function (a list of 
        dictionaries containing the sentiment score and label for each message).
    
    Behavior:
    ---------
    - If the expected result is an exception type (TypeError or ValueError), 
      the function verifies that the 'analyze_sentiment' function raises the expected exception.
    - If the expected result is a dictionary or list (the function's expected output), 
      the function compares the actual result from 'analyze_sentiment' with the expected result to ensure the results are correct.
      
    Test cases include:
    -------------------
    1. **Default model detection**: Tests the output when valid input (a list of messages) is passed to the function.
       Expected result: A list with a positive sentiment label.
       
    2. **Invalid input message detection**: Tests the function’s error handling when the input is a single string, 
       not a list of strings.
       Expected result: TypeError.
       
    3. **Multiple input message detection**: Tests the function with multiple messages to ensure it processes each correctly.
       Expected result: A list with sentiment analysis results for each message (positive and neutral).
       
    4. **Invalid model detection**: Tests the function’s error handling when an unrecognized model name ("Model") is passed.
       Expected result: ValueError.
    
    Example Usage:
    --------------
    test_analyze_sentiment(["Hello!"], "Model", ValueError)
    """
    if isinstance(expected, type) and issubclass(expected, Exception):
        # Check for expected errors
        with pytest.raises(expected):
            analyze_sentiment(messages, model)
    else:
        # Check for expected usual outputs
        result = analyze_sentiment(messages, model)
        assert result == expected

def test_alert_on_highly_negative_message(capfd):
    """Test to verify that the 'analyze_sentiment' function correctly identifies and handles highly negative messages by triggering an alert."""
    messages = ["This is absolutely terrible."]
    results = analyze_sentiment(messages)
    out, _ = capfd.readouterr()
    assert "ALERT: Message is highly negative" in out
    assert results[0]["label"] == "negative"
    assert results[0]["alert"] is True