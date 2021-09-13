from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage
from pages.locators import HomePageLocators


class HomePage(BasePage):
    def open(self):
        super().open()
        self.wait_for_element(*HomePageLocators.MAIN_APP)

    def filter_table_by_column_name(self, col_name):
        self.find_element(*HomePageLocators.FILTER_DATA_TEXT_BOX).send_keys(col_name)

    def sort_table_by_column_name(self, col_name):
        select = Select(self.find_element(*HomePageLocators.SORT_DATA_DROP_DOWN))
        select.select_by_visible_text(col_name)

    def get_table_column_by_name(self, col_name):
        col_locator = HomePageLocators.COLUMN_NAME_LOCATOR_LOOKUP[col_name.lower()]
        col_data = self.find_elements(*col_locator)
        data = [cell.text for cell in col_data]
        return data
