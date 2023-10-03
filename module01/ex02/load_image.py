from PIL import Image
import numpy as np

def ft_load(path: str) -> np.array:
    """returns the image as numpy array"""
    img = Image.open(path)
    arr = np.asarray(img)
    print(f"the shape of the image is {arr.shape}")
    return arr;

print(ft_load("landscape.jpeg"))
