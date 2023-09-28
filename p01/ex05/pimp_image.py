import numpy as np


def ft_invert(array) -> np.array:
    """Inverts the color of the image received."""
    inverted_image = np.invert(array)
    return (inverted_image)


def ft_red(array) -> np.array:
    """Retain the red color part of the image received."""
    array[:, :, 1] = 0
    array[:, :, 2] = 0
    return array


def ft_green(array) -> np.array:
    """Retain the green color part of the image received."""
    array[:, :, 0] = 0
    array[:, :, 2] = 0
    return array


def ft_blue(array) -> np.array:
    """Retain the blue color part of the image received."""
    array[:, :, 1] = 0
    array[:, :, 0] = 0
    return array


def ft_grey(array) -> np.array:
    """Greyscale the image received."""
    gray_array_chn1 = np.mean(array,
                              axis=2, keepdims=True).astype(np.uint8)
    gray_array_chn3 = np.repeat(gray_array_chn1, 3, axis=2)
    return gray_array_chn3
