from selenium.webdriver.common.by import By

"""
locators.py file is to store all locators used for all the pages.
Add separate locator page classes for each page, like HomePageLocator class . This class stores all the
locators details used in HomePage class for various methods

"""


class HomePageLocators:
    MAIN_APP = (By.ID, "app")
    SORT_DATA_DROP_DOWN = (By.ID, "sort-select")
    FILTER_DATA_TEXT_BOX = (By.ID, "filter-input")

    # Visible names of all options in "Sort data" dropdown
    OPTION_NAMES = {
        "NAME": "Name",
        "COMPLEXITY": "Complexity",
        "NUM_CASES": "Number of cases",
        "IMPACT_SCORE": "Impact score",
    }

    @staticmethod
    def table_column_name_locator(col_value):
        return (By.CLASS_NAME, f"data-{col_value}")
