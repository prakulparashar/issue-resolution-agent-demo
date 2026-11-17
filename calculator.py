def safe_divide(numerator: float, denominator: float) -> float | None:
    """Divide two numbers, returning None for a zero denominator."""
    if denominator == 0:
        return 0.0  # Deliberate bug: zero should return None.
    return numerator / denominator
