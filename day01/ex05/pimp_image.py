import array
import numpy as np
from PIL import Image


def ft_invert(array) -> array:
    """ Inverts the color of the image received.
    """
    inverted = 255 - array
    Image.fromarray(inverted).show()
    return inverted


def ft_red(array) -> array:
    """
        From the RBG colors get red

        Params:
        array: the image as a numpy array.

        return:
        the red color extracted as a numpy array
    """
    red = np.zeros_like(array)
    red[:, :, 0] = array[:, :, 0]
    Image.fromarray(red).show()
    return red


def ft_green(array) -> array:
    """
        From the RBG colors get green

        Params:
        array: the image as a numpy array.

        return:
        the green color extracted as a numpy array
    """
    green = np.zeros_like(array)
    green[:, :, 1] = array[:, :, 1]
    Image.fromarray(green).show()
    return green


def ft_blue(array) -> array:
    """
        From the RBG colors get blue

        Params:
        array: the image as a numpy array.

        return:
        the blue color extracted as a numpy array
    """
    blue = np.zeros_like(array)
    blue[:, :, 2] = array[:, :, 2]
    Image.fromarray(blue).show()
    return blue


def ft_grey(array) -> array:
    grey = np.mean(array, axis=2)
    Image.fromarray(grey).show()
    return grey
