import pytest
import os
from pages.converters.infix_to_prefix import InfixToPrefixPage
from utils.File import read_json
from utils.testCases.spaceDecorator import SpaceDecor
from utils.testCases.base import BaseTest
from utils.testCases.transformer import BaseTransformer
from conf import ROOT_DIR

test_data = read_json(os.path.join(ROOT_DIR, "testData", "converters/infix_to_prefix.json"))
defaultDecor = BaseTransformer()


@pytest.mark.usefixtures("setup")
class TestInfixToPrefix:

    def test_infix_to_prefix(self):
        page = InfixToPrefixPage(self.driver)
        data = test_data["test_cases"]
        space_decor = SpaceDecor(defaultDecor)
        BaseTest(space_decor).run_test_cases(data, page.enter_infix, page.click_convert, page.get_prefix,
                                             page.clear_infix)
