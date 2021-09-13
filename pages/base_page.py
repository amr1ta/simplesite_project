from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(
        self, driver, base_url="https://mystifying-beaver-ee03b5.netlify.app/"
    ):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30
        self.driver_wait = WebDriverWait(self.driver, self.timeout)

    def open(self, url=""):
        url = self.base_url + url
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def wait_for_element(self, *locator):
        self.driver_wait.until(EC.visibility_of_element_located(locator))

    def quit(self):
        self.driver.quit()
