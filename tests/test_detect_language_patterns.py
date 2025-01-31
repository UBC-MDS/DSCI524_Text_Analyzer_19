import pytest
from messageanalyzer.detect_language_patterns import detect_language_patterns

sample_text = [
    "Artificial intelligence and machine learning are transforming industries around the globe.",
    "The basketball team secured a thrilling victory in the final seconds of the game.",
    "Yoga and meditation are excellent for reducing stress and improving mental health.",
    "Exploring the hidden beaches of Bali is an unforgettable experience for any traveler.",
    "Quantum computing is expected to revolutionize data processing and cryptography."
]

# Test for valid language detection
def test_detect_language_patterns_language():
    """
    Test the 'language' method with valid input.
    
    This test verifies that the language detection method identifies all
    sample messages as English ('en') using the `detect_language_patterns` function.
    
    Input:
    - A list of English sentences (sample_text)
    
    Expected Result:
    - All detected languages should be 'en'.
    """

    result = detect_language_patterns(sample_text, method="language")
    assert all(lang == "en" for lang in result)

# Test for valid n-gram detection
def test_detect_language_patterns_ngrams():
    """
    Test the 'ngrams' method with valid input.
    
    This test checks that the `detect_language_patterns` function correctly identifies 
    the top 3 most frequent 2-grams in the provided sample text.
    
    Input:
    - Sample messages (sample_text)
    - n = 2 (bigrams)
    - top_n = 3 (return the top 3 frequent n-grams)
    
    Expected Result:
    - A list of 3 tuples representing the most common bigrams and their counts.
    """


    result = detect_language_patterns(sample_text, method="ngrams", n=2, top_n=3)
    assert len(result) == 3

# Test for valid character pattern detection
def test_detect_language_patterns_char_patterns():
    """
    Test the 'char_patterns' method with valid input.
    
    This test checks if the `detect_language_patterns` function returns the top 3
    most common characters from the provided sample text.
    
    Input:
    - Sample messages (sample_text)
    - top_n = 3 (return the top 3 common characters)
    
    Expected Result:
    - A list of 3 tuples representing characters and their frequencies.
    """

    result = detect_language_patterns(sample_text, method="char_patterns", top_n=3)
    assert len(result) == 3

# Test for unsupported method (should raise ValueError)
def test_detect_language_patterns_invalid_method():
    """
    Test that providing an unsupported method raises a ValueError.
    
    This test ensures that if a user specifies a method that is not 'language', 'ngrams', 
    or 'char_patterns', the `detect_language_patterns` function raises a ValueError.
    
    Input:
    - Sample messages (sample_text)
    - Invalid method name ('invalid_method')
    
    Expected Result:
    - A ValueError is raised with an appropriate error message.
    """
    with pytest.raises(ValueError, match="Unsupported method."):
        detect_language_patterns(sample_text, method="invalid_method")

# Test for non-list input (should raise TypeError)
def test_detect_language_patterns_non_list_input():
    """
    Test that a non-list input raises a TypeError.
    
    This test checks if the `detect_language_patterns` function raises a TypeError when 
    the input is a string instead of a list of strings.
    
    Input:
    - A single string ("This is a string, not a list.")
    
    Expected Result:
    - A TypeError is raised with the message "messages must be a list of strings".
    """

    with pytest.raises(TypeError, match="messages must be a list of strings"):
        detect_language_patterns("This is a string, not a list.", method="language")

# Test for non-string elements in the list (should raise TypeError)
def test_detect_language_patterns_non_string_elements():
    """
    Test that a list containing non-string elements raises a TypeError.
    
    This test ensures that the `detect_language_patterns` function correctly identifies
    a list with non-string elements and raises an appropriate TypeError.
    
    Input:
    - A list containing a mix of valid text and a non-string element ["Valid text", 42]
    
    Expected Result:
    - A TypeError is raised with the message "messages must be a list of strings".
    """

    with pytest.raises(TypeError, match="messages must be a list of strings"):
        detect_language_patterns(["Valid text", 42], method="language")

# Test for empty input list
def test_detect_language_patterns_empty_input():
    """
    Test that an empty list as input returns an empty result.
    
    This test verifies that the `detect_language_patterns` function handles empty 
    input correctly and returns an empty list.
    
    Input:
    - An empty list []
    
    Expected Result:
    - The function should return an empty list.
    """

    result = detect_language_patterns([], method="language")
    assert result == []

def test_detect_language_patterns_invalid_n_value():
    """
    Test that providing an invalid 'n' value for n-grams raises a ValueError.
    
    This test checks if the `detect_language_patterns` function raises a ValueError 
    when 'n' is set to 0 or a negative value.
    
    Input:
    - A valid message list ["test data"]
    - n = 0 (invalid n-gram size)
    
    Expected Result:
    - A ValueError is raised with the message "Parameter 'n' must be a positive integer."
    """

    with pytest.raises(ValueError, match="Parameter 'n' must be a positive integer."):
        detect_language_patterns(["test data"], method="ngrams", n=0)
        
def test_detect_language_patterns_unsupported_method():
    """
    Test that providing an unsupported method raises a ValueError.
    
    This test verifies that any method not explicitly defined ('language', 'ngrams', 
    or 'char_patterns') results in a ValueError being raised.
    
    Input:
    - A valid message list ["test data"]
    - An unsupported method name ('invalid_method')
    
    Expected Result:
    - A ValueError is raised with the message: 
      "Unsupported method. Choose from 'language', 'ngrams', or 'char_patterns'."
    """

    with pytest.raises(ValueError, match="Unsupported method. Choose from 'language', 'ngrams', or 'char_patterns'."):
        detect_language_patterns(["test data"], method="invalid_method")
