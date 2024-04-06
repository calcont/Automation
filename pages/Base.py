import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

WAIT_TIME = 5


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        element = WebDriverWait(self.driver, WAIT_TIME).until(EC.presence_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].click();", element)

    def enter_input(self, by_locator, text):
        return WebDriverWait(self.driver, WAIT_TIME).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def clear_input(self, by_locator):
        return WebDriverWait(self.driver, WAIT_TIME).until(EC.visibility_of_element_located(by_locator)).clear()

    # TODO: make this method more generic to handle different type of attributes
    def get_output(self, by_locator):
        return WebDriverWait(self.driver, WAIT_TIME).until(EC.visibility_of_element_located(by_locator)).get_attribute(
            "value")
