import logging

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


from pages.base_page import BasePage
from pages.home_page import HomePage

LOGGER = logging.getLogger(__name__)


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
    def expand_number(self, str_num):
        units = {"k": 1000, "M": 1000000, "B": 10000000}
        unit = str_num[-1]
        res = float(str_num[:-1])
        return res * units[unit]

    @pytest.mark.parametrize("sort_by", ["Number of cases", "Impact score"])
    def test_sorting(self, sort_by):
        home_page = HomePage(self.driver)
        home_page.open()
        col_value = home_page.sort_table_by_column_name(sort_by)
        col_data = home_page.get_column_data(col_value)
        for idx, value in enumerate(col_data):
            try:
                col_data[idx] = float(value)
            except ValueError:
                col_data[idx] = float(self.expand_number(value))
        assert all(
            col_data[i] <= col_data[i + 1] for i in range(len(col_data) - 1)
        ), LOGGER.error("Values are not sorted")

    @pytest.mark.parametrize(
        "filter_text", ["pass", "dlE", "PHI", "low", "high", "medium", " ", ""]
    )
    def test_filtering_postive_scenario(self, filter_text):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.filter_table_by_name(filter_text)
        names = home_page.get_column_data()
        assert names and all(
            filter_text.lower() in name.lower() for name in names
        ), LOGGER.error("No data captured from specified filters")

    @pytest.mark.parametrize("filter_text", ["non", "z", "!@#$%", "1"])
    def test_filtering_negative_scenario(self, filter_text):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.filter_table_by_name(filter_text)
        names = home_page.get_column_data()
        assert not names, LOGGER.error("Unexpected results from non-existent filters")

    @pytest.mark.parametrize("sort_by", ["Complexity"])
    def test_filtering_for_sorted_data(self, sort_by):
        pass
