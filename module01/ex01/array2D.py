import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """returns the list sliced"""
    arr = np.array(family)
    print(f"My shape is {arr.shape}")
    print(f"My new shape is ({len(arr) - abs(start - end)}, {arr.ndim})")
    x = slice(start, end)
    return (family[x])

family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, -2, 2))
print(slice_me(family, 1, -2))
