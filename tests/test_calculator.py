from calculator import safe_divide


def test_divides_nonzero_values():
    assert safe_divide(8, 2) == 4


def test_zero_denominator_returns_none():
    assert safe_divide(8, 0) is None
