import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """returns a list of bmi values"""
    res = []
    matrix = np.column_stack((height, weight))
    for val in matrix:
        res.append(val.item(1) / (val.item(0) * val.item(0)))
    return res;

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """returns a list of bools"""
    res = []
    for val in bmi:
        res.append(True if val > limit else False)
    return res

height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
