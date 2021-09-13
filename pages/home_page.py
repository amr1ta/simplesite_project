from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage
from pages.locators import HomePageLocators


class HomePage(BasePage):
    def open(self):
        super().open()
        self.wait_for_element(*HomePageLocators.MAIN_APP)

    def filter_table_by_name(self, input_text):
        self.find_element(*HomePageLocators.FILTER_DATA_TEXT_BOX).send_keys(input_text)

    def sort_table_by_column_name(self, col_name):
        select = Select(self.find_element(*HomePageLocators.SORT_DATA_DROP_DOWN))
        select.select_by_visible_text(col_name)
        return select.first_selected_option.get_attribute("value")

    def get_column_data(self, col_value="name"):
        col_locator = HomePageLocators.table_column_name_locator(col_value)
        col_data = self.find_elements(*col_locator)
        data = [cell.text for cell in col_data]
        return data
