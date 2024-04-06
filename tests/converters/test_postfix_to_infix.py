import pytest
import os
from pages.converters.postfix_to_infix import PostfixToInfix
from utils.File import read_json
from utils.testCases.spaceDecorator import SpaceDecor
from utils.testCases.base import BaseTest
from utils.testCases.transformer import BaseTransformer
from conf import ROOT_DIR

test_data = read_json(os.path.join(ROOT_DIR, "testData", "converters/postfix_to_infix.json"))
defaultDecor = BaseTransformer()


@pytest.mark.usefixtures("setup")
class TestPostfixToInfix:

    def test_postfix_to_infix(self):
        page = PostfixToInfix(self.driver)
        data = test_data["test_cases"]
        space_decor = SpaceDecor(defaultDecor)
        BaseTest(space_decor).run_test_cases(data, page.enter_postfix, page.click_convert, page.get_infix,
                                             page.clear_postfix)
