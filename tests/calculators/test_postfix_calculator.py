import pytest
import os
from pages.calculators.postfix_calculator import PostfixCalculatorPage
from utils.File import read_json
from utils.testCases.spaceDecorator import SpaceDecor
from utils.testCases.removeComma import RemoveComma
from utils.testCases.base import BaseTest
from utils.testCases.transformer import BaseTransformer
from conf import ROOT_DIR

test_data = read_json(os.path.join(ROOT_DIR, "testData", "calculators/postfix_calculator.json"))
defaultDecor = BaseTransformer()
space_decor = SpaceDecor(defaultDecor)
comma_decor = RemoveComma(space_decor)
test_case = BaseTest(comma_decor)


@pytest.mark.usefixtures("setup")
class TestPostfixCalculator:

    def test_postfix_calculator(self):
        page = PostfixCalculatorPage(self.driver)
        data = test_data["test_cases"]
        test_case.run_test_cases(data, page.enter_postfix, page.click_calculate, page.get_result, page.clear_postfix)

    def test_postfix_calculator_with_spaces(self):
        page = PostfixCalculatorPage(self.driver)
        data = test_data["test_cases_with_spaces"]
        page.click_space_separator()
        test_case.run_test_cases(data, page.enter_postfix, page.click_calculate, page.get_result, page.clear_postfix)
