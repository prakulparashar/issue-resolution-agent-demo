# Issue Resolution Agent demo fixture

A tiny Python repository for testing the issue-resolution workflow.

## Bug for the demo issue

`safe_divide(numerator, denominator)` is documented to return `None` when the denominator is zero, but currently returns `0.0`. The regression test in `tests/test_calculator.py` captures the expected behavior.

Run tests with `python -m pytest -q` (requires Python and pytest).
