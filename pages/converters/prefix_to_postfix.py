from pages.Base import BasePage
from locators.converters import PrefixToPostfixPageLocators
from utils.endpoint import generateEndpoint
from constants.suite import CONVERTERS
from constants.tools import PREFIX_TO_POSTFIX


class PrefixToPostfix(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(generateEndpoint(CONVERTERS, PREFIX_TO_POSTFIX))

    def enter_prefix(self, infix):
        self.enter_input(PrefixToPostfixPageLocators.PREFIX_INPUT, infix)

    def clear_prefix(self):
        self.clear_input(PrefixToPostfixPageLocators.PREFIX_INPUT)

    def click_convert(self):
        self.click(PrefixToPostfixPageLocators.CONVERT_BUTTON)

    def get_postfix(self):
        return self.get_output(PrefixToPostfixPageLocators.POSTFIX_OUTPUT)
