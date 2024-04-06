from pages.Base import BasePage
from locators.converters import InfixToPostfixPageLocators
from utils.endpoint import generateEndpoint
from constants.suite import CONVERTERS
from constants.tools import INFIX_TO_POSTFIX


class InfixToPostfixPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(generateEndpoint(CONVERTERS, INFIX_TO_POSTFIX))

    def enter_infix(self, infix):
        self.enter_input(InfixToPostfixPageLocators.INFIX_INPUT, infix)

    def clear_infix(self):
        self.clear_input(InfixToPostfixPageLocators.INFIX_INPUT)

    def click_convert(self):
        self.click(InfixToPostfixPageLocators.CONVERT_BUTTON)

    def get_postfix(self):
        return self.get_output(InfixToPostfixPageLocators.POSTFIX_OUTPUT)
