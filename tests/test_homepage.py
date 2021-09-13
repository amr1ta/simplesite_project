# Standard library imports
import logging

# Related third party imports
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Local application import
from pages.home_page import HomePage


LOGGER = logging.getLogger(__name__)
TABLE_COL_NAME_VALUE = "name"
TABLE_COL_COMPLEXITY_VALUE = "complexity"


@pytest.fixture(scope="class")
def setup_teardown(request, pytestconfig):
    """
    Run Setup and Teardown methods run before and after all test cases
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


@pytest.mark.usefixtures("setup_teardown")
class Test_SimpleSite:
    def expand_number(self, str_num):
        """
        Convert 5k , 1.2M to 5000, 1200000
        """
        units = {"k": 1000, "M": 1000000, "B": 10000000}
        unit = str_num[-1]
        res = float(str_num[:-1])
        return res * units[unit]

    @pytest.mark.parametrize("sort_by", ["Number of cases", "Impact score"])
    def test_sorting(self, sort_by):
        """
        **Scenario 1**: Verifying sorting on a particular column
        """
        self.home_page.open()
        col_value = self.home_page.sort_table_by_column_name(sort_by)
        col_data = self.home_page.get_column_data(col_value)
        for idx, value in enumerate(col_data):
            try:
                col_data[idx] = float(value)
            except ValueError:
                col_data[idx] = float(self.expand_number(value))
        assert sorted(col_data) == col_data, LOGGER.error("Values are not sorted")

    @pytest.mark.parametrize(
        "filter_text", ["pass", "dlE", "PHI", "low", "high", "medium", " ", ""]
    )
    def test_positive_filters(self, filter_text):
        """
        **Scenario 2**: Verifying matching rows are returned with existing text
        """
        self.home_page.open()
        self.home_page.filter_table(filter_text)
        names = self.home_page.get_column_data(TABLE_COL_NAME_VALUE)
        complexities = self.home_page.get_column_data(TABLE_COL_COMPLEXITY_VALUE)
        filtered_row_data = list(zip(names, complexities))
        assert filtered_row_data, LOGGER.error(
            "No data captured from specified filters"
        )
        for row in filtered_row_data:
            assert any(
                filter_text.lower() in cell.lower() for cell in row
            ), LOGGER.error("Unexpected results from existing filter string")

    @pytest.mark.parametrize("filter_text", ["non", "z", "!@#$%", "1"])
    def test_negative_filters(self, filter_text):
        """
        **Scenario 3**: Verifying no rows are returned with non-exisiting text
        """
        self.home_page.open()
        self.home_page.filter_table(filter_text)
        names = self.home_page.get_column_data(TABLE_COL_NAME_VALUE)
        assert not names, LOGGER.error(
            "Unexpected results from non-existing filter string"
        )
