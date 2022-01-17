from __future__ import annotations
from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Arguments must be of either int or float.")
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Arguments must be of either int or float.")
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Arguments must be of either int or float.")
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Arguments must be of either int or float.")
    return a / b
