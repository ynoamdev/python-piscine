import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Calculate the shape of the 2D array and truncate it.

    params:
        family: 2D array
        start: starting truncating index
        end: ending truncating index

    return:
        list: truncated 2D array
    """
    try:
        if not type(family) is list:
            raise TypeError("family must be a list")
        if not type(start) is int or not type(end) is int:
            raise TypeError("start and end must be integers")

        print("My shape is : " + str(np.array(family).shape))
        print("My new shape is : " + str(np.array(family[start:end]).shape))
        return family[start:end]

    except Exception as e:
        print("Error:", e)
        return None
