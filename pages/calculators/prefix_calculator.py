from pages.Base import BasePage
from locators.calculators import PrefixCalculatorLocators
from utils.endpoint import generateEndpoint
from constants.suite import CALCULATORS
from constants.tools import PREFIX_CALCULATOR


class PrefixCalculatorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(generateEndpoint(CALCULATORS, PREFIX_CALCULATOR))

    def enter_prefix(self, prefix):
        self.enter_input(PrefixCalculatorLocators.PREFIX_INPUT, prefix)

    def clear_prefix(self):
        self.clear_input(PrefixCalculatorLocators.PREFIX_INPUT)

    def click_calculate(self):
        self.click(PrefixCalculatorLocators.CALCULATE_BUTTON)

    def click_space_separator(self):
        self.click(PrefixCalculatorLocators.SPACE_SEPARATION_CHECKBOX)

    def get_result(self):
        return self.get_output(PrefixCalculatorLocators.ANS)
