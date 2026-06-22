import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
        Load an image from a file and return an array.

        Params:
        path (str): the parth of the image file.

        return:
        np.ndarray: the image as a numpy array.
    """
    try:
        if not path.endswith('.jpg') and not path.endswith('.jpeg'):
            raise AssertionError(
                "Image extension is not correct. (ex: jpg|jpeg)")
        img = Image.open(path)
        return np.array(img)
    except Exception as e:
        print(f"Error: {e}")
        return None
