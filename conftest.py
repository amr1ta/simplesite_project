import pytest

"""
The conftest.py file serves as a means of providing fixtures for an entire directory.
Fixtures defined in a conftest.py can be used by any test in that package without needing 
to import them (pytest will automatically discover them).

"""


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--mode", action="store", default="")
    parser.addoption(
        "--base_url",
        action="store",
        default="https://mystifying-beaver-ee03b5.netlify.app/",
    )
