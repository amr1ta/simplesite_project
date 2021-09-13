import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--mode", action="store", default="")
    parser.addoption(
        "--base_url",
        action="store",
        default="https://mystifying-beaver-ee03b5.netlify.app/",
    )
