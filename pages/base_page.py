from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class basePage:
    def __init__(self, driver):
        self.driver = driver
    def find_element(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_elements(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def wait_for_element(self, locator: tuple, timeout: int = 2):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click_on_element(self, locator: tuple, timeout: int = 2):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def choose_from_select(self, selector: tuple, value: str):
        dropdown = Select(self.driver.find_element(*selector))
        dropdown.select_by_value(value)

    def get_image_src(self, locator: tuple, timeout: int = 2) -> str:
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return self.find_element(locator).get_attribute("src")