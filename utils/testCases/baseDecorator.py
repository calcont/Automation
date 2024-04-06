from utils.testCases.transformer import Transformer
from abc import abstractmethod


class TestCaseDecor(Transformer):
    _wrapper: Transformer = None

    def __init__(self, wrapper: Transformer) -> None:
        self._wrapper = wrapper

    @abstractmethod
    def execute(self, data):
        pass
