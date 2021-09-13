# Standard library imports
import time, logging

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
    def floatify_num_cases(self, col_data_list):
        """
        Convert a list of values like 5k , 1.2M to 5000, 1200000 in place
        """
        units = {"k": 1000, "M": 1000000, "B": 10000000}
        for idx, value in enumerate(col_data_list):
            try:
                col_data_list[idx] = float(value)
            except ValueError:
                unit = value[-1]
                res = float(value[:-1])
                col_data_list[idx] = float(res * units[unit])

    @pytest.mark.parametrize("sort_by", ["Number of cases", "Impact score"])
    def test_sorting(self, sort_by):
        """
        **Scenario 1**: Verify that a selected column is sorted from low to high
        """
        self.home_page.open()
        col_value = self.home_page.sort_table_by_column_name(sort_by)
        col_data = self.home_page.get_column_data(col_value)
        self.floatify_num_cases(col_data)
        assert sorted(col_data) == col_data, LOGGER.error("Values are not sorted")

    @pytest.mark.parametrize(
        "filter_text", ["pass", "dlE", "PHI", "low", "high", "medium", " ", ""]
    )
    def test_positive_filters(self, filter_text):
        """
        **Scenario 2**: Verify if a string matches values in the NAME and COMPLEXITY columns, the corresponding rows are returned and other rows are filtered out
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
        **Scenario 3**: Verify if a string does not match values in the NAME and COMPLEXITY columns, all  rows are filtered out
        """
        self.home_page.open()
        self.home_page.filter_table(filter_text)
        names = self.home_page.get_column_data(TABLE_COL_NAME_VALUE)
        assert not names, LOGGER.error(
            "Unexpected results from non-existing filter string"
        )

    @pytest.mark.parametrize(
        "sort_by,filter_text", [("Number of cases", "high"), ("Impact score", "low")]
    )
    def test_sort_then_filter(self, sort_by, filter_text):
        """
        **Scenario 4**: Verify combination of sorting first followed by filtering, the filtered columns should still be sorted
        """
        self.home_page.open()
        sort_col_value = self.home_page.sort_table_by_column_name(sort_by)
        self.home_page.filter_table(filter_text)
        sort_col_date = self.home_page.get_column_data(sort_col_value)
        filter_col_data = self.home_page.get_column_data(TABLE_COL_COMPLEXITY_VALUE)
        result = list()
        result.append(sorted(sort_col_date) == sort_col_date)
        result.append(
            all(filter_text.lower() in cell.lower() for cell in filter_col_data)
        )
        assert all(result), LOGGER.error(
            "Unexpected results after sorting and filtering"
        )

    @pytest.mark.parametrize(
        "filter_text,sort_by", [("ack", "Number of cases"), ("ack", "Impact score")]
    )
    def test_filter_then_sort(self, filter_text, sort_by):
        """
        **Scenario 5**: Verify combination of filtering first followed by sorting, the filtered columns should still be sorted
        """
        self.home_page.open()
        self.home_page.filter_table(filter_text)
        sort_col_value = self.home_page.sort_table_by_column_name(sort_by)
        sort_col_data = self.home_page.get_column_data(sort_col_value)
        filter_col_data = self.home_page.get_column_data(TABLE_COL_NAME_VALUE)
        result = list()
        self.floatify_num_cases(sort_col_data)
        result.append(sorted(sort_col_data) == sort_col_data)
        result.append(
            all(filter_text.lower() in cell.lower() for cell in filter_col_data)
        )
        assert all(result), LOGGER.error(
            "Unexpected results after filtering and sorting"
        )
