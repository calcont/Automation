from pages.Base import BasePage
from locators.converters import PrefixToInfixPageLocators
from utils.endpoint import generateEndpoint
from constants.suite import CONVERTERS
from constants.tools import PREFIX_TO_INFIX


class PrefixToInfix(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(generateEndpoint(CONVERTERS, PREFIX_TO_INFIX))

    def enter_prefix(self, infix):
        self.enter_input(PrefixToInfixPageLocators.PREFIX_INPUT, infix)

    def clear_prefix(self):
        self.clear_input(PrefixToInfixPageLocators.PREFIX_INPUT)

    def click_convert(self):
        self.click(PrefixToInfixPageLocators.CONVERT_BUTTON)

    def get_infix(self):
        return self.get_output(PrefixToInfixPageLocators.INFIX_OUTPUT)
