import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from pages.home_page import HomePage

"""
This is the conftest specific to tests. Here we define fixtures which will be reused across all tests.
"""


@pytest.fixture(scope="class")
def homepage_setup_teardown(request, pytestconfig):
    """
    Initialize base class using Selenium webdriver.
    Run all testcases
    Teardown: close the browser
    """
    browser = pytestconfig.getoption("browser")
    mode = pytestconfig.getoption("mode")
    base_url = pytestconfig.getoption("base_url")
    options = Options()
    if mode == "headless":
        options.headless = True
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    home_page = HomePage(driver, base_url)
    request.cls.home_page = home_page
    yield
    home_page.quit()
