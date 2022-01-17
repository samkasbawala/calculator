# Calculator
[![Tests](https://github.com/samkasbawala/calculator/actions/workflows/tests.yaml/badge.svg)](https://github.com/samkasbawala/calculator/actions/workflows/tests.yaml)

Project to test out git actions, `poetry`, and `tox`. Created a **very** simple calculator package in Python. Focus is not on the code, but instead automating tests and checks on different Python envs on different OSs. Trying to learn the `poetry` package manager.

## Packaging
Using `Poetry` as package manager. Find more info about Poetry [here](https://python-poetry.org/).

## GitHub Actions
There are definitely some improvements that can be made for the workflow to use caching instead of downloding all of the packages over and over again. Also there are no clear instructions on how to have `tox` and `poetry` to behave nicely with one another.
