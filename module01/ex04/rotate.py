import numpy as np
from matplotlib import pyplot as plt
from load_image import ft_load


def ft_rotate(data: np.array) -> np.array:
    """returns zoomed array"""
    tmp = data[0:400, 0:400, 0:1]
    res = np.empty(tmp.shape, dtype=tmp.dtype)
    for i in range(tmp.shape[0]):
        for j in range(tmp.shape[1]):
            res[j, i, :] = tmp[i, j, :]
    print(f"shape after transpose is {res.shape}")
    return res


def main():
    """main function"""
    arr = ft_load("animal.jpeg")
    print(arr)
    arr = ft_rotate(arr)
    print(arr)
    plt.imshow(arr, interpolation='nearest')
    plt.show()


if __name__ == "__main__":
    main()
