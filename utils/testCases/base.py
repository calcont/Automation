import pytest
from utils.testCases.transformer import Transformer


class BaseTest:
    def __init__(self, transformer: Transformer = None) -> None:
        self.transformer = transformer

    def run_test_cases(self, data, input_method, submit, get_output, clear_method) -> None:
        for test_case in data:
            input_exp = test_case["input_expression"]
            expected_output = test_case["expected_output"]
            expected_output = self.transformer.execute(expected_output)
            input_method(input_exp)
            submit()
            output = get_output()
            if output != expected_output:
                pytest.fail(f"Expected: {expected_output}, Got: {output} for input: {input_exp}")
            assert output == expected_output
            clear_method()
