from pages.Base import BasePage
from locators.converters import InfixToPrefixPageLocators
from utils.endpoint import generateEndpoint
from constants.suite import CONVERTERS
from constants.tools import INFIX_TO_PREFIX


class InfixToPrefixPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(generateEndpoint(CONVERTERS, INFIX_TO_PREFIX))

    def enter_infix(self, infix):
        self.enter_input(InfixToPrefixPageLocators.INFIX_INPUT, infix)

    def clear_infix(self):
        self.clear_input(InfixToPrefixPageLocators.INFIX_INPUT)

    def click_convert(self):
        self.click(InfixToPrefixPageLocators.CONVERT_BUTTON)

    def get_prefix(self):
        return self.get_output(InfixToPrefixPageLocators.PREFIX_OUTPUT)
