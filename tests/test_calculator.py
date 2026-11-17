from calculator import multiply, safe_divide


def test_divides_nonzero_values():
    assert safe_divide(8, 2) == 4


def test_zero_denominator_returns_none():
    assert safe_divide(8, 0) is None


def test_multiply_multiplies_values():
    assert multiply(3, 4) == 12
