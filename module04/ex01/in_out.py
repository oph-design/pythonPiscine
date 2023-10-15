def square(x: int | float) -> int | float:
    """squares the arguments"""
    return x * x

def pow(x: int | float) -> int | float:
    """returns power of itself"""
    return x ** x

def outer(x: int | float, function) -> object:
    count = 0
    def inner() -> float:
        class InnerClass:
            def __init__(self, num, func):
                self.num = num
                self.func = func

            def __call__(self):
                self.num = self.func(self.num)
                return self.num

        return InnerClass
    instance = inner();
    return instance(x, function)


my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())
