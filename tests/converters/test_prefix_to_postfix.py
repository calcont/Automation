import pytest
import os
from pages.converters.prefix_to_postfix import PrefixToPostfix
from utils.File import read_json
from utils.testCases.spaceDecorator import SpaceDecor
from utils.testCases.base import BaseTest
from utils.testCases.transformer import BaseTransformer
from conf import ROOT_DIR

test_data = read_json(os.path.join(ROOT_DIR, "testData", "converters/prefix_to_postfix.json"))
defaultDecor = BaseTransformer()


@pytest.mark.usefixtures("setup")
class TestPrefixToPostfix:

    def test_prefix_to_postfix(self):
        page = PrefixToPostfix(self.driver)
        data = test_data["test_cases"]
        space_decor = SpaceDecor(defaultDecor)
        BaseTest(space_decor).run_test_cases(data, page.enter_prefix, page.click_convert, page.get_postfix,
                                             page.clear_prefix)
