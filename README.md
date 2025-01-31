# messageanalyzer

[![Documentation Status](https://readthedocs.org/projects/dsci524-text-analyzer-19/badge/?version=latest)](https://dsci524-text-analyzer-19.readthedocs.io/en/latest/?badge=latest) [![ci-cd](https://github.com/UBC-MDS/DSCI524_Text_Analyzer_19/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/DSCI524_Text_Analyzer_19/actions/workflows/ci-cd.yml) [![codecov](https://codecov.io/gh/UBC-MDS/DSCI524_Text_Analyzer_19/graph/badge.svg?token=V1vuzkqQXg)](https://codecov.io/gh/UBC-MDS/DSCI524_Text_Analyzer_19)

`messageanalyzer` is a Python package designed for performing comprehensive Natural Language Processing (NLP) tasks on text messages. This package provides tools for sentiment analysis, keyword extraction, topic modeling, and language patterns detection, making it ideal for text mining and content analysis projects. Full documentation and tutorial is hosted on [ReadtheDocs](https://dsci524-text-analyzer-19.readthedocs.io/en/latest/?badge=latest).

## Installation

``` bash
$ pip install messageanalyzer
```

## Usage

-   **`analyze_sentiment(messages: List[str], model: str = "Default")  -> List[dict]`**:\
    This function analyzes the sentiment of a list of given messages and returns the sentiment scores and labels for each messange and prints alert message if it's highly negative.
-   **`topic_modeling(messages: List[str], n_topics: int = 5, n_words: int = 10, random_state: int = 123) -> dict`**:\
    This function extracts topics from a list of messages and returns the words that represent the extracted topics by using Nonnegative Matrix Factorization.
-   **`extract_keywords(messages: List[str], num_keywords: int = 5) -> list`**:\
    This function extracts the top keywords from a list of messages.
-   **`detect_language_patterns(messages: List[str], method: str = "language", n: int = 2, top_n: int = 5) -> list`**:\
    This function detects language patterns such as detected languages, common n-grams, or character usage patterns from a list of messages.

## Ecosystem Fit

`messageanalyzer` integrates into the Python NLP ecosystem by offering a simple yet powerful toolkit for analyzing text data. While other Python libraries like [NLTK](https://www.nltk.org/) and [spaCy](https://spacy.io/) provide extensive NLP functionalities, `messageanalyzer` focuses on making sentiment analysis, keyword extraction, and language pattern visualization more accessible and user-friendly.

For keyword extraction, packages like [YAKE](https://github.com/LIAAD/yake) and [RAKE-NLTK](https://pypi.org/project/rake-nltk/) provide similar functionality. However, `messageanalyzer` combines these tasks into a unified and streamlined workflow.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## Dependencies

-   [`TextBlob`](https://textblob.readthedocs.io/): For sentiment analysis.
-   [`langdetect`](https://pypi.org/project/langdetect/): For language detection.
-   [`scikit-learn`](https://scikit-learn.org/): For keyword extraction, n-gram analysis (`CountVectorizer`), and topic modeling.
-   [`collections.Counter`](https://docs.python.org/3/library/collections.html): For frequency analysis.

## License

`messageanalyzer` was created by Quanhua Huang, Adrian Leung, Anna Nandar, Colombe Tolokin. It is licensed under the terms of the MIT license.

## Credits

`messageanalyzer` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
