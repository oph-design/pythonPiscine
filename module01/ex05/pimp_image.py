import numpy as np
from matplotlib import pyplot as plt
from load_image import ft_load


def ft_invert(array) -> np.array:
    """inverts rgb color values"""
    return 255 - array


def ft_red(array) -> np.array:
    """applies red filter"""
    res = array.copy()
    res[:, :, 0] = 180
    return res


def ft_green(array) -> np.array:
    """applies green filter"""
    res = array.copy()
    res[:, :, 1] = 180
    return res


def ft_blue(array) -> np.array:
    """applies blue filter"""
    res = array.copy()
    res[:, :, 2] = 180
    return res


def ft_grey(array) -> np.array:
    copy = array.copy()
    copy = np.sum(copy, axis=2) // 3
    copy = np.stack([copy, copy, copy], axis=2)
    return copy

arr = ft_load("landscape.jpeg")
plt.imshow(arr, interpolation='nearest')
plt.show()
arr = ft_invert(ft_load("landscape.jpeg"))
plt.imshow(arr, interpolation='nearest')
plt.show()
arr = ft_red(ft_load("landscape.jpeg"))
plt.imshow(arr, interpolation='nearest')
plt.show()
arr = ft_green(ft_load("landscape.jpeg"))
plt.imshow(arr, interpolation='nearest')
plt.show()
arr = ft_blue(ft_load("landscape.jpeg"))
plt.imshow(arr, interpolation='nearest')
plt.show()
arr = ft_grey(ft_load("landscape.jpeg"))
plt.imshow(arr, interpolation='nearest')
plt.show()
