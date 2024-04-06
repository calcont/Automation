from pages.Base import BasePage
from locators.converters import PostfixToInfixPageLocators
from utils.endpoint import generateEndpoint
from constants.suite import CONVERTERS
from constants.tools import POSTFIX_TO_INFIX


class PostfixToInfix(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(generateEndpoint(CONVERTERS, POSTFIX_TO_INFIX))

    def enter_postfix(self, infix):
        self.enter_input(PostfixToInfixPageLocators.POSTFIX_INPUT, infix)

    def clear_postfix(self):
        self.clear_input(PostfixToInfixPageLocators.POSTFIX_INPUT)

    def click_convert(self):
        self.click(PostfixToInfixPageLocators.CONVERT_BUTTON)

    def get_infix(self):
        return self.get_output(PostfixToInfixPageLocators.INFIX_OUTPUT)
