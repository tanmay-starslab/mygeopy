import numbers

def hypot(a: float, b: float) -> float:
    """Calculate the hypotenuse of a right triangle given legs a and b.

    Args:
        a (float): Length of one leg.
        b (float): Length of the other leg.

    Raises:
        ValueError: If either leg is not a positive real number.

    Returns:
        float: Length of the hypotenuse.
    
    Example:
        >>> hypot(3, 4)
        5.0
        >>> hypot(5, 12)
        13.0
        >>> hypot(8, 15)
        17.0
        >>> hypot(7, 24)
        25.0
    """
    if not isinstance(a, numbers.Real) or not isinstance(b, numbers.Real):
        raise ValueError("`a` and `b` must be real numbers")
    if a < 0 or b < 0:
        raise ValueError("`a` and `b` must be non-negative")
    return (a**2 + b**2)**0.5
