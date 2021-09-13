import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from pages.base_page import BasePage
from pages.home_page import HomePage
import time


@pytest.fixture(scope="class")
def setup_teardown(request, pytestconfig):
    browser = pytestconfig.getoption("browser")
    mode = pytestconfig.getoption("mode")
    base_url = pytestconfig.getoption("base_url")
    options = Options()
    if mode == "headless":
        options.headless = True
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    base_page = BasePage(driver, base_url)
    request.cls.driver = driver
    yield
    base_page.quit()


@pytest.mark.usefixtures("setup_teardown")
class Test_SimpleSite:
    def test_sorting(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.sort_table_by_column_name("Number of cases")
        data = home_page.get_table_column_by_name("Number of cases")
        print(data)
        # home_page.sort_table_by_column_name(1)
        time.sleep(5)
