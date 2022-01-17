import pytest
import math
from calculator import calculator


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (1, 1, 2),
        (-1, -1, -2),
        (-1, 1, 0),
        (1, -1, 0),
        (0.0, 0.0, 0.0),
        (1.0, 1.0, 2.0),
        (-1.0, -1.0, -2.0),
        (-1.0, 1.0, 0.0),
        (1.0, -1.0, 0.0),
        (0.3, 0.3, 0.6),
    ],
)
def test_add(a, b, expected):
    result = calculator.add(a, b)
    assert math.isclose(result, expected, rel_tol=1e-09, abs_tol=0.0)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (1, 1, 0),
        (-1, -1, 0),
        (-1, 1, -2),
        (1, -1, 2),
        (0.0, 0.0, 0.0),
        (1.0, 1.0, 0.0),
        (-1.0, -1.0, 0.0),
        (-1.0, 1.0, -2.0),
        (1.0, -1.0, 2.0),
        (0.6, 0.3, 0.3),
    ],
)
def test_subtract(a, b, expected):
    result = calculator.subtract(a, b)
    assert math.isclose(result, expected, rel_tol=1e-09, abs_tol=0.0)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, -1),
        (1, -1, -1),
        (5, 5, 25),
        (0.0, 0.0, 0.0),
        (1.0, 1.0, 1.0),
        (-1.0, -1.0, 1.0),
        (-1.0, 1.0, -1.0),
        (1.0, -1.0, -1.0),
        (5.0, 5.0, 25.0),
        (0.3, 0.3, 0.09),
    ],
)
def test_multiply(a, b, expected):
    result = calculator.multiply(a, b)
    assert math.isclose(result, expected, rel_tol=1e-09, abs_tol=0.0)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, -1),
        (1, -1, -1),
        (25, 5, 5),
        (1.0, 1.0, 1.0),
        (-1.0, -1.0, 1.0),
        (-1.0, 1.0, -1.0),
        (1.0, -1.0, -1.0),
        (25.0, 5.0, 5.0),
        (0.09, 0.3, 0.3),
    ],
)
def test_divide(a, b, expected):
    result = calculator.divide(a, b)
    assert math.isclose(result, expected, rel_tol=1e-09, abs_tol=0.0)


@pytest.mark.parametrize(
    "a,b",
    [
        (0, 0),
        (1, 0),
        (2, 0),
        (-1, 0),
        (-2, 0),
        (0.0, 0.0),
        (1.0, 0.0),
        (2.0, 0.0),
        (-1.0, 0.0),
        (-2.0, 0.0),
        (1, 0.0),
        (1.0, 0),
    ],
)
def test_divide_by_0(a, b):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(a, b)


@pytest.mark.parametrize(
    "a,b",
    [
        ("string", 1),
        ("string", 1.0),
        (1, "string"),
        (1.0, "string"),
        ([], 1),
        ([], 1.0),
        (1, []),
        (1.0, []),
        (tuple(), 1),
        (tuple(), 1.0),
        (1, tuple()),
        (1.0, tuple()),
        ({}, 1),
        ({}, 1.0),
        (1, {}),
        (1.0, {}),
        (set(), 1),
        (set(), 1.0),
        (1, set()),
        (1.0, set()),
        ("string", "string"),
        ([], []),
        (tuple(), tuple()),
        ({}, {}),
        (set(), set()),
    ],
)
def test_invalid_args(a, b):
    with pytest.raises(TypeError):
        calculator.add(a, b)
        calculator.subtract(a, b)
        calculator.multiply(a, b)
        calculator.divide(a, b)
