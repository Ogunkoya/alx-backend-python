import typing

def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    Takes a string k and an int or float v, returns a tuple with the string k
    as the first element and the square of v as a float as the second element.

    Args:
        k: A string key.
        v: An integer or float value to be squared.

    Returns:
        A tuple containing the string key k as the first element and the square of v
        as a float as the second element.
    """
    return (k, float(v**2))