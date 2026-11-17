def safe_divide(numerator: float, denominator: float) -> float | None:
    """Divide two numbers, returning None for a zero denominator."""
    if denominator == 0:
        return None  # Correct behavior: return None for zero denominator.
    return numerator / denominator
