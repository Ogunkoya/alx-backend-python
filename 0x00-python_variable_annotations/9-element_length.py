import typing

def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an element from the input list and its length.

    Parameters:
    lst (List[str]): A list of strings.

    Returns:
    List[Tuple[str, int]]: A list of tuples, where each tuple contains a string and its length.
    """
    return [(i, len(i)) for i in lst]