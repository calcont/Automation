# Conventions to be followed:

- The file should be a json file.
- Try to follow the same structure as the example json file.
- For different strategies, you can use naming conventions like `test_cases_<strategy_name>` like below.

```json
{
  "test_cases": [
    {
      "input_expression": "1+2",
      "expected_output": "3"
    }
  ],
    "test_cases_<strategy_name>": [
        {
        "input_expression": "1+2",
        "expected_output": "3"
        }
    ]
}
```