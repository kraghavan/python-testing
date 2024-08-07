# Learning-L6 Project

## Introduction
This project demonstrates a simple Python application with a focus on testing practices using `pytest` and `hypothesis`. It includes examples of unit tests and coverage reports.

## Requirements
- Python 3.9+
- pytest
- pytest-cov
- hypothesis

## Installation
- Clone the repository and navigate into the project directory: ```git clone <repository-url> cd learning-L6```

- Install the required Python packages: ```pip3 install -r requirements.txt```

## Project Structure
```
learning-L6/
├── src/
│   └── __init__.py
│   └── student.py
└── tests/
│   └── __init__.py
    └── test_student.py
```

### Adding `__init__.py`
To make Python treat directories containing the file as packages, add an empty `__init__.py` file to both the `src` and `tests` directories.

## Running Tests
Execute the following command to run tests with coverage and hypothesis statistics:```python -m pytest --cov=src tests/ --hypothesis-show-statistics```

## Sample Output
The command above will produce an output similar to the following:
```
========================================================================= test session starts ==========================================================================
platform darwin -- Python 3.9.10, pytest-8.3.2, pluggy-1.5.0 -- /Library/Frameworks/Python.framework/Versions/3.9/bin/python3
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase(PosixPath('/Users/kraghavan/KarthikaRepo/PycharmProjects/testing/unittesting/sample_testing6/.hypothesis/examples'))
rootdir: /Users/kraghavan/KarthikaRepo/PycharmProjects/testing/unittesting/sample_testing6
plugins: cov-5.0.0, hypothesis-6.108.10
collected 4 items                                                                                                                                                      

tests/test_student.py::TestStudent::test_get_average_grade_with_non_zero_grades PASSED                                                                           [ 25%]
tests/test_student.py::TestStudent::test_get_grade PASSED                                                                                                        [ 50%]
tests/test_student.py::TestStudent::test_non_zero_number_of_grades PASSED                                                                                        [ 75%]
tests/test_student.py::TestStudent::test_student_initialization PASSED                                                                                           [100%]

---------- coverage: platform darwin, python 3.9.10-final-0 ----------
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
src/__init__.py       0      0   100%
src/student.py        9      0   100%
-----------------------------------------------
TOTAL                 9      0   100%

======================================================================== Hypothesis Statistics =========================================================================

tests/test_student.py::TestStudent::test_get_average_grade_with_non_zero_grades:

  - during generate phase (0.69 seconds):
    - Typical runtimes: ~ 0-4 ms, of which ~ 0-4 ms in data generation
    - 100 passing examples, 0 failing examples, 86 invalid examples
    - Events:
      * 38.71%, Retried draw from text(characters(codec='utf-8', categories=('Zl', 'Zp', 'Co', 'Me', 'Pc', 'Zs', 'Lt', 'Pf', 'Pi', 'Nl', 'Pd', 'Cf', 'Sc', 'Sk', 'Lm', 'Nd', 'Sm', 'No', 'Pe', 'Ps', 'Mc', 'Po', 'So', 'Mn', 'Lo', 'Lu', 'Ll', 'Cn', 'Cc')), min_size=1).filter(not_yet_in_unique_list) to satisfy filter
      * 38.71%, invalid because: (internal) want a string but have a float
      * 4.84%, invalid because: (internal) want a string but have a boolean

  - Stopped because settings.max_examples=100


tests/test_student.py::TestStudent::test_get_grade:

  - during generate phase (0.53 seconds):
    - Typical runtimes: ~ 0-4 ms, of which ~ 0-4 ms in data generation
    - 100 passing examples, 0 failing examples, 69 invalid examples
    - Events:
      * 44.97%, Retried draw from text(characters(codec='utf-8', categories=('Zl', 'Zp', 'Co', 'Me', 'Pc', 'Zs', 'Lt', 'Pf', 'Pi', 'Nl', 'Pd', 'Cf', 'Sc', 'Sk', 'Lm', 'Nd', 'Sm', 'No', 'Pe', 'Ps', 'Mc', 'Po', 'So', 'Mn', 'Lo', 'Lu', 'Ll', 'Cn', 'Cc'))).filter(not_yet_in_unique_list) to satisfy filter
      * 35.50%, invalid because: (internal) want a string but have a float
      * 1.18%, invalid because: (internal) want a float but have a string

  - Stopped because settings.max_examples=100


tests/test_student.py::TestStudent::test_non_zero_number_of_grades:

  - during generate phase (0.57 seconds):
    - Typical runtimes: ~ 0-5 ms, of which ~ 0-4 ms in data generation
    - 100 passing examples, 0 failing examples, 72 invalid examples
    - Events:
      * 35.47%, Retried draw from text(characters(codec='utf-8', categories=('Zl', 'Zp', 'Co', 'Me', 'Pc', 'Zs', 'Lt', 'Pf', 'Pi', 'Nl', 'Pd', 'Cf', 'Sc', 'Sk', 'Lm', 'Nd', 'Sm', 'No', 'Pe', 'Ps', 'Mc', 'Po', 'So', 'Mn', 'Lo', 'Lu', 'Ll', 'Cn', 'Cc')), min_size=1).filter(not_yet_in_unique_list) to satisfy filter
      * 35.47%, invalid because: (internal) want a string but have a float
      * 2.91%, invalid because: (internal) want a string but have a boolean

  - Stopped because settings.max_examples=100


tests/test_student.py::TestStudent::test_student_initialization:

  - during generate phase (0.62 seconds):
    - Typical runtimes: ~ 0-4 ms, of which ~ 0-3 ms in data generation
    - 100 passing examples, 0 failing examples, 100 invalid examples
    - Events:
      * 44.00%, Retried draw from text(characters(codec='utf-8', categories=('Zl', 'Zp', 'Co', 'Me', 'Pc', 'Zs', 'Lt', 'Pf', 'Pi', 'Nl', 'Pd', 'Cf', 'Sc', 'Sk', 'Lm', 'Nd', 'Sm', 'No', 'Pe', 'Ps', 'Mc', 'Po', 'So', 'Mn', 'Lo', 'Lu', 'Ll', 'Cn', 'Cc')), min_size=1).filter(not_yet_in_unique_list) to satisfy filter
      * 44.00%, invalid because: (internal) want a string but have a float
      * 5.00%, invalid because: (internal) want a string but have a boolean
      * 0.50%, invalid because: (internal) got a string but outside the valid range

  - Stopped because settings.max_examples=100
  ```