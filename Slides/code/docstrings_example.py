def rms_error(n: int, actual: list[int], expected: list[int]) -> float:
    """
    Compute and return the root mean square (rms) error between
    an expected value and the actual value.
    Args:
        n: Length of the vectors
        actual: Computed values to compare
        expected: Values expected from the computation

    Returns:
      Root mean square error
    """
    error: float = 0  # Running total of errors
    # Add contributions from each index to error
    for i in range(n):
        error_i = actual[i] - expected[i]
        error += error_i * error_i / n
    return sqrt(error)
