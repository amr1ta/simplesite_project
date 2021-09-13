from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage
from pages.locators import HomePageLocators

"""
HomePage class : Page class which is a subclass of BasePage class and contains all the methods
of the home page.
These methods are used in test class to validate various test scenarios
"""


class HomePage(BasePage):
    def open(self):
        super().open()
        self.wait_for_element(*HomePageLocators.MAIN_APP)

    def filter_table(self, input_text):
        self.find_element(*HomePageLocators.FILTER_DATA_TEXT_BOX).send_keys(input_text)

    def sort_table_by_column_name(self, col_name):
        """
        Select the :col_name parameter in the "Sort data" selector
        and return corresponding value of selection
        """
        select = Select(self.find_element(*HomePageLocators.SORT_DATA_DROP_DOWN))
        select.select_by_visible_text(col_name)
        return select.first_selected_option.get_attribute("value")

    def get_column_data(self, col_value):
        """
        Using the value of column that is selected, find all the "data" elements
        of that column and return the text value
        """
        col_locator = HomePageLocators.table_column_name_locator(col_value)
        col_data = self.find_elements(*col_locator)
        data = [cell.text for cell in col_data]
        return data
