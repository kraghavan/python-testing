# Learning-L5 Project

## Introduction
This project demonstrates a simple Python application with a focus on testing practices using `pytest` and `hypothesis`. It includes examples of unit tests and coverage reports.

## Requirements
- Python 3.9+
- pytest
- pytest-cov
- hypothesis

## Installation
- Clone the repository and navigate into the project directory: ```git clone <repository-url> cd learning-L5```

- Install the required Python packages: ```pip3 install -r requirements.txt```

## Project Structure

learning-L5/
├── src/
│   └── converter.py
└── tests/
    └── test_converter.py

### Adding `__init__.py`
To make Python treat directories containing the file as packages, add an empty `__init__.py` file to both the `src` and `tests` directories.

## Running Tests
Execute the following command to run tests with coverage and hypothesis statistics:```python -m pytest --cov=src tests/ --hypothesis-show-statistics```

## Sample Output
The command above will produce an output similar to the following:
```
========================================================= test session starts=========================================================
platform darwin -- Python 3.9.10, pytest-8.3.2, pluggy-1.5.0
rootdir: /Users/kraghavan/KarthikaRepo/PycharmProjects/testing/unittesting/sample_testing5
plugins: cov-5.0.0, hypothesis-6.108.10
collected 2 items                                                                                                                     

tests/test_converter.py ..                                                                                                      [100%]

---------- coverage: platform darwin, python 3.9.10-final-0 ----------
Name               Stmts   Miss  Cover
--------------------------------------
src/__init__.py        0      0   100%
src/converter.py       5      0   100%
--------------------------------------
TOTAL                  5      0   100%

======================================================== Hypothesis Statistics ========================================================

tests/test_converter.py::TestConverter::test_ascii_to_str_to_ascii:

  - during generate phase (0.11 seconds):
    - Typical runtimes: < 1ms, of which < 1ms in data generation
    - 100 passing examples, 0 failing examples, 13 invalid examples

  - Stopped because settings.max_examples=100


tests/test_converter.py::TestConverter::test_str_to_ascii_to_str:

  - during generate phase (0.08 seconds):
    - Typical runtimes: < 1ms, of which < 1ms in data generation
    - 100 passing examples, 0 failing examples, 0 invalid examples

  - Stopped because settings.max_examples=100

```