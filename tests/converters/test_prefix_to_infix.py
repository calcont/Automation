import pytest
import os
from pages.converters.prefix_to_infix import PrefixToInfix
from utils.File import read_json
from utils.testCases.spaceDecorator import SpaceDecor
from utils.testCases.base import BaseTest
from utils.testCases.transformer import BaseTransformer
from conf import ROOT_DIR

test_data = read_json(os.path.join(ROOT_DIR, "testData", "converters/prefix_to_infix.json"))
defaultDecor = BaseTransformer()


@pytest.mark.usefixtures("setup")
class TestPrefixToInfix:

    def test_prefix_to_infix(self):
        page = PrefixToInfix(self.driver)
        data = test_data["test_cases"]
        space_decor = SpaceDecor(defaultDecor)
        BaseTest(space_decor).run_test_cases(data, page.enter_prefix, page.click_convert, page.get_infix,
                                             page.clear_prefix)
