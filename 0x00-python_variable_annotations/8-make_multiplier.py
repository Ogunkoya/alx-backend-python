import typing

def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    Returns a function that multiplies a float by the provided multiplier.

    Args:
        multiplier: A float value to use as a multiplier.

    Returns:
        A function that takes a single float argument and returns its product
        with the multiplier.

    """
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func