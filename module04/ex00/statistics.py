
def get_total(args: any) -> float:
    total = .0
    for val in args:
        total += val
    return total

def calc_mean(args: any) -> float:
    """calc mean"""
    return get_total(args) / len(args)

def calc_median(args: any) -> float:
    """calc median"""
    return args[len(args) // 2]

def calc_quartile(args: any) -> list:
    """calc quart"""
    pos = len(args) // 4
    return [args[pos], args[pos * 3]]

def dev_sqr(x: float, mean:  float) -> float:
    """for lambda"""
    return float((x - mean) ** 2)

def calc_var(args: any) -> float:
    """calc var"""
    mean = calc_mean(args);
    squares = list(map(lambda x : dev_sqr(x, mean), args))
    return get_total(squares) / (len(squares) - 1.)

def ft_statistics(*args: any, **kwargs: any) -> None:
    """calc arr"""
    sorted_ = sorted(args)
    if "toto" in kwargs:
        print(f"Mean: {calc_mean(sorted_)}")
    if "tutu" in kwargs:
        print(f"Median: {calc_median(sorted_)}")
    if "tata" in kwargs:
        print(f"Quartile: {calc_quartile(sorted_)}")
    if "world" in kwargs:
        print(f"Variance: {calc_var(sorted_)}")
    if "hello" in kwargs:
        print(f"Std dev: {calc_var(sorted_) ** .5}")


ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
