from selenium.webdriver.common.by import By


class HomePageLocators:
    MAIN_APP = (By.ID, "app")
    SORT_DATA_DROP_DOWN = (By.ID, "sort-select")
    FILTER_DATA_TEXT_BOX = (By.ID, "filter-input")

    @staticmethod
    def table_column_name_locator(col_value):
        return (By.CLASS_NAME, f"data-{col_value}")
