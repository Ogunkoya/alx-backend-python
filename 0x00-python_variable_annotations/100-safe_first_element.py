from typing import Any, List, Union

def safe_first_element(lst: List) -> Union[Any, None]:
    """
    Returns the first element of a list, or None if the list is empty.

    Parameters:
    lst (List): A list of elements of unknown type.

    Returns:
    Union[Any, None]: The first element of the list, or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None