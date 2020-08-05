This is a simple calculator python script with a unit test to test the implementation
of the Travis CI unit testing.

To run the unit tests, where ``<root>`` is the top level directory:
```
cd <root>/tests
python  test_simple_calculator.py
```
For more verbose output:
```
python  test_simple_calculator.py -v
```
If you have `coverage` installed, to get test coverage:
```
coverage run test_simple_calculator.py
coverage report -m
```
To check source code quality with pylint:
```
cd <root>
env PYTHONPATH=scripts:${PYTHONPATH} pylint --rcfile ./tests/.pylintrc ./tests/test_simple_calculator.py
```
