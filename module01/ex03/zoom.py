import numpy as np
from matplotlib import pyplot as plt
from load_image import ft_load


def ft_zoom(data: np.array) -> np.array:
    """retruns zoomed array"""
    res = data[0:400, 0:400, 0:1]
    print(f"shape after slicing is {res.shape}")
    return res


def main():
    """main function"""
    arr = ft_load("animal.jpeg")
    print(arr)
    arr = ft_zoom(arr)
    print(arr)
    plt.imshow(arr, interpolation='nearest')
    plt.show()


if __name__ == "__main__":
    main()
