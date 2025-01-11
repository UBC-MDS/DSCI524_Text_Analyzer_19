# textanalyzer

This package includes powerful tools to perform natural language processing on English texts.

## Installation

```bash
$ pip install textanalyzer
```

## Usage


- `analyze_sentiment(message, model="default")`: This function analyzes the sentiment of a given message and prints alert message if it's highly negative. 
- `topic_modeling()`: This function performs topic extraction from a text or a list of texts by using Nonnegative Matrix Factorization. 
- `extract_keywords(messages, method="tfidf", num_keywords=5)`: This function extracts the top keywords from a list of messages using specified methods like TF-IDF or RAKE.


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`textanalyzer` was created by Quanhua Huang, Adrian Leung, Anna Nandar, Colombe Tolokin. It is licensed under the terms of the MIT license.

## Credits

`textanalyzer` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
