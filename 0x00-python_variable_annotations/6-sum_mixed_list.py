import typing

def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    Sums a list of integers and floats and returns their total.

    Args:
        mxd_lst: A list of integers and floats to sum.

    Returns:
        The sum of the input list as a float.

    """
    return sum(mxd_lst)