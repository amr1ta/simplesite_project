from selenium.webdriver.common.by import By


class HomePageLocators:
    MAIN_APP = (By.ID, "app")
    SORT_DATA_DROP_DOWN = (By.ID, "sort-select")
    FILTER_DATA_TEXT_BOX = (By.ID, "filter-input")
    TABLE_COL_NAME = (By.CLASS_NAME, "data-name")
    TABLE_COL_NUM_CASES = (By.CLASS_NAME, "data-cases")
    TABLE_COL_AVG_IMPACT_SCORE = (By.CLASS_NAME, "data-averageImpact")
    TABLE_COL_COMPLEXITY = (By.CLASS_NAME, "data-complexity")
    COLUMN_NAME_LOCATOR_LOOKUP = {
        "name": TABLE_COL_NAME,
        "number of cases": TABLE_COL_NUM_CASES,
        "average impact score": TABLE_COL_AVG_IMPACT_SCORE,
        "complexity": TABLE_COL_COMPLEXITY,
    }

    TABLE_ROWS = (By.CLASS_NAME, "table-row")
    TABLE_CONTENT = (By.CLASS_NAME, "//*[@id='app']/div[3]/div[2]/div[1]")
