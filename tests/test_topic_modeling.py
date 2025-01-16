from typing import Literal
import pytest

from textanalyzer.topic_modeling import topic_modeling

sample_text = [
    "Artificial intelligence and machine learning are transforming industries around the globe.",
    "The basketball team secured a thrilling victory in the final seconds of the game.",
    "Yoga and meditation are excellent for reducing stress and improving mental health.",
    "Exploring the hidden beaches of Bali is an unforgettable experience for any traveler.",
    "Quantum computing is expected to revolutionize data processing and cryptography."
]

@pytest.mark.parametrize(
    "test_n_topics, test_n_words, expected",
    [
        (5, 3, {
            'Topic 1': ['hidden', 'experience', 'unforgettable'], 
            'Topic 2': ['revolutionize', 'quantum', 'computing'], 
            'Topic 3': ['intelligence', 'machine', 'globe'], 
            'Topic 4': ['yoga', 'stress', 'health'], 
            'Topic 5': ['basketball', 'victory', 'thrilling']
        }),
        (3, 7, {
            'Topic 1': ['quantum', 'computing', 'cryptography', 'data', 'expected', 'revolutionize', 'processing'], 
            'Topic 2': ['seconds', 'basketball', 'final', 'thrilling', 'team', 'secured', 'victory'], 
            'Topic 3': ['exploring', 'unforgettable', 'traveler', 'bali', 'beaches', 'hidden', 'experience']
        }),
        (15, 4, {
            'Topic 1': ['processing', 'data', 'quantum', 'expected'], 
            'Topic 2': ['beaches', 'unforgettable', 'bali', 'hidden'], 
            'Topic 3': ['excellent', 'health', 'yoga', 'mental'], 
            'Topic 4': ['learning', 'transforming', 'machine', 'globe'], 
            'Topic 5': ['exploring', 'hidden', 'unforgettable', 'traveler'], 
            'Topic 6': ['basketball', 'final', 'secured', 'victory'], 
            'Topic 7': ['computing', 'cryptography', 'revolutionize', 'expected'], 
            'Topic 8': ['artificial', 'industries', 'intelligence', 'transforming'], 
            'Topic 9': ['seconds', 'victory', 'team', 'final'], 
            'Topic 10': ['quantum', 'processing', 'data', 'cryptography'], 
            'Topic 11': ['yoga', 'industries', 'hidden', 'health'], 
            'Topic 12': ['game', 'thrilling', 'team', 'secured'], 
            'Topic 13': ['intelligence', 'globe', 'industries', 'artificial'], 
            'Topic 14': ['bali', 'experience', 'traveler', 'exploring'], 
            'Topic 15': ['reducing', 'stress', 'improving', 'meditation']
        })
    ]
)
# This suppress the runtime warning from NMF calculation
@pytest.mark.filterwarnings('ignore::RuntimeWarning')
def test_topic_modeling(test_n_topics, test_n_words, expected):
    """This test takes in the different arguments from the parametrization and checks that its output is the same as the expected"""
    assert topic_modeling(sample_text, test_n_topics, test_n_words) == expected

def test_topic_modeling_wrong_input():
    """This tests if the function throws a TypeError when the input is not a list of strings."""
    with pytest.raises(TypeError):
        topic_modeling(documents = -1)
    with pytest.raises(TypeError):
        topic_modeling(documents = 'Hello, this is a test.')
    with pytest.raises(TypeError):
        topic_modeling(documents = ['Hello, I am', ' ', 90, '.'])

def test_topic_modeling_bad_input():
    """This tests if the function throws a ValueError when the input is a list of empty strings or stop words"""
    with pytest.raises(ValueError):
        topic_modeling(documents = [' '])
    with pytest.raises(ValueError):
        topic_modeling(documents = ['is'])
    with pytest.raises(ValueError):
        topic_modeling(documents = [' ', '', 'is are'])
    
