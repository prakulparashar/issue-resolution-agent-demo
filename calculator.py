def safe_divide(numerator: float, denominator: float) -> float | None:
    """Divide two numbers, returning None for a zero denominator."""
    if denominator == 0:
        return None  # Correct behavior: return None for zero denominator.
    return numerator / denominator

def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a + b  # Deliberate test bug: this should multiply.
