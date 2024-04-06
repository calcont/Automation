from pages.Base import BasePage
from locators.calculators import PostfixCalculatorLocators
from utils.endpoint import generateEndpoint
from constants.suite import CALCULATORS
from constants.tools import POSTFIX_CALCULATOR


class PostfixCalculatorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(generateEndpoint(CALCULATORS, POSTFIX_CALCULATOR))

    def enter_postfix(self, postfix):
        self.enter_input(PostfixCalculatorLocators.POSTFIX_INPUT, postfix)

    def clear_postfix(self):
        self.clear_input(PostfixCalculatorLocators.POSTFIX_INPUT)

    def click_calculate(self):
        self.click(PostfixCalculatorLocators.CALCULATE_BUTTON)

    def click_space_separator(self):
        self.click(PostfixCalculatorLocators.SPACE_SEPARATION_CHECKBOX)

    def get_result(self):
        return self.get_output(PostfixCalculatorLocators.ANS)
