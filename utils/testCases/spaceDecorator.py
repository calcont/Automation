from utils.testCases.baseDecorator import TestCaseDecor


class SpaceDecor(TestCaseDecor):
    def execute(self, data):
        return self._wrapper.execute(data).replace(" ", "")
