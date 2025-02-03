# messageanalyzer

[![Documentation Status](https://readthedocs.org/projects/dsci524-text-analyzer-19/badge/?version=latest)](https://dsci524-text-analyzer-19.readthedocs.io/en/latest/?badge=latest) [![ci-cd](https://github.com/UBC-MDS/DSCI524_Text_Analyzer_19/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/DSCI524_Text_Analyzer_19/actions/workflows/ci-cd.yml) [![codecov](https://codecov.io/gh/UBC-MDS/DSCI524_Text_Analyzer_19/graph/badge.svg?token=V1vuzkqQXg)](https://codecov.io/gh/UBC-MDS/DSCI524_Text_Analyzer_19)

`messageanalyzer` is a Python package designed for performing comprehensive Natural Language Processing (NLP) tasks on text messages. This package provides tools for sentiment analysis, keyword extraction, topic modeling, and language patterns detection, making it ideal for text mining and content analysis projects. Full documentation and tutorial is hosted on [ReadtheDocs](https://dsci524-text-analyzer-19.readthedocs.io/en/latest/?badge=latest).

`messageanalyzer`is built for developers, data scientists, and researchers working in text mining, social media analysis, and customer feedback evaluation. Its easy-to-use design makes it a great fit for both NLP beginners who want straightforward solutions and experienced professionals seeking a quick, efficient way to draw insights from text data. Whether you’re analyzing customer reviews, survey responses, or social media content, this package offers a reliable tool to support business decisions, sentiment monitoring, and academic research in a practical and user-friendly way.

## Installation

``` bash
$ pip install messageanalyzer
```

## Usage

### **Activate Python**
Ensure you have Python installed on your system. To get started, activate it by running:

```bash
python
```

Here’s a sample text list that will be used in the examples below:

```python
sample_text = [
    "Artificial intelligence and machine learning are transforming industries around the globe.",
    "The basketball team secured a thrilling victory in the final seconds of the game.",
    "Yoga and meditation are excellent for reducing stress and improving mental health.",
    "Exploring the hidden beaches of Bali is an unforgettable experience for any traveler.",
    "Quantum computing is expected to revolutionize data processing and cryptography."
]
```

You can now test the package with the examples below.

-   **`analyze_sentiment(messages: List[str], model: str = "Default") -> List[dict]`**:\
    This function analyzes the sentiment of a list of given messages and returns the sentiment scores and labels for each message.

    #### Example:
    ```python
    from messageanalyzer.sentiment_analysis import analyze_sentiment

    result = analyze_sentiment(sample_text)

    print(result)
    ```

-   **`topic_modeling(messages: List[str], n_topics: int = 5, n_words: int = 10, random_state: int = 123) -> dict`**:\
    This function extracts topics from a list of messages and returns the words that represent the extracted topics using Nonnegative Matrix Factorization.

    #### Example:
    ```python
    from messageanalyzer.topic_modeling import topic_modeling

    topics = topic_modeling(sample_text, n_topics=2, n_words=3)

    print(topics)
    ```

-   **`extract_keywords(messages: List[str], num_keywords: int = 5) -> list`**:\
    This function extracts the top keywords from a list of messages.

    #### Example:
    ```python
    from messageanalyzer.extract_keywords import extract_keywords

    keywords = extract_keywords(sample_text, num_keywords=3)

    print(keywords)
    ```

-   **`detect_language_patterns(messages: List[str], method: str = "language", n: int = 2, top_n: int = 5) -> list`**:\
    This function detects language patterns such as detected languages, common n-grams, or character usage patterns from a list of messages.

    #### Example:
    ```python
    from messageanalyzer.detect_language_patterns import detect_language_patterns

    patterns = detect_language_patterns(sample_text, method="language")

    print(patterns)
    ```

## Running Test

Here is the code we’ve written for testing using pytest. Under the project root, run this following code :
```bash
poetry run pytest tests
```
    
## Ecosystem Fit

`messageanalyzer` integrates into the Python NLP ecosystem by offering a simple yet powerful toolkit for analyzing text data. While other Python libraries like [NLTK](https://www.nltk.org/) and [spaCy](https://spacy.io/) provide extensive NLP functionalities, `messageanalyzer` focuses on making sentiment analysis, keyword extraction, and language pattern visualization more accessible and user-friendly.

For keyword extraction, packages like [YAKE](https://github.com/LIAAD/yake) and [RAKE-NLTK](https://pypi.org/project/rake-nltk/) provide similar functionality. However, `messageanalyzer` combines these tasks into a unified and streamlined workflow.

## Contributing

Interested in contributing? Check out the [contributing](CONTRIBUTING.md) guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## Dependencies

-   [`TextBlob`](https://textblob.readthedocs.io/): For sentiment analysis.
-   [`langdetect`](https://pypi.org/project/langdetect/): For language detection.
-   [`scikit-learn`](https://scikit-learn.org/): For keyword extraction, n-gram analysis (`CountVectorizer`), and topic modeling.
-   [`collections.Counter`](https://docs.python.org/3/library/collections.html): For frequency analysis.

## License

`messageanalyzer` was created by Quanhua Huang, Adrian Leung, Anna Nandar, Colombe Tolokin. It is licensed under the terms of the MIT license.

## Credits

`messageanalyzer` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
