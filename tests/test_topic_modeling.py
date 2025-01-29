import pytest

from messageanalyzer.topic_modeling import topic_modeling

sample_text = [
    "Artificial intelligence and machine learning are transforming industries around the globe.",
    "The basketball team secured a thrilling victory in the final seconds of the game.",
    "Yoga and meditation are excellent for reducing stress and improving mental health.",
    "Exploring the hidden beaches of Bali is an unforgettable experience for any traveler.",
    "Quantum computing is expected to revolutionize data processing and cryptography."
]

# This suppress the runtime warning from NMF calculation
@pytest.mark.filterwarnings('ignore::RuntimeWarning')
def test_topic_modeling():
    """This tests if the function returns the correct number of topics and representative words"""
    topics = topic_modeling(sample_text, 5, 10)
    assert len(topics) == 5
    assert len(topics['Topic 1']) == 10
    assert len(topics['Topic 2']) == 10
    assert len(topics['Topic 3']) == 10
    assert len(topics['Topic 4']) == 10
    assert len(topics['Topic 5']) == 10

def test_topic_modeling_wrong_input():
    """This tests if the function throws a TypeError when the input is not a list of strings."""
    with pytest.raises(TypeError):
        topic_modeling(messages = -1)
    with pytest.raises(TypeError):
        topic_modeling(messages = 'Hello, this is a test.')
    with pytest.raises(TypeError):
        topic_modeling(messages = ['Hello, I am', ' ', 90, '.'])

def test_topic_modeling_bad_input():
    """This tests if the function throws a ValueError when the input is a list of empty strings or stop words"""
    with pytest.raises(ValueError):
        topic_modeling(messages = [' '])
    with pytest.raises(ValueError):
        topic_modeling(messages = ['is'])
    with pytest.raises(ValueError):
        topic_modeling(messages = [' ', '', 'is are'])
    