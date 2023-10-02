def ft_filter(str: str, number: int) -> list:
    ls  = str.split(" ")
    res = []
    for element in ls:
        if len(element) >= number:
            res.append(element);
    return res
