class calculator:
    """Vector Calculator"""
    def __init__(self, values: list):
        """Constructor"""
        self.values = values

    def __add__(self, object) -> None:
        """Addition"""
        self.values = list(map(lambda x : x + object, self.values))
        print(self.values)

    def __mul__(self, object) -> None:
        """Multiplication"""
        self.values = list(map(lambda x : x * object, self.values))
        print(self.values)

    def __sub__(self, object) -> None:
        """Substraction"""
        self.values = list(map(lambda x : x - object, self.values))
        print(self.values)

    def __truediv__(self, object) -> None:
        """Division"""
        if (object != 0):
            self.values = list(map(lambda x : x / object, self.values))
        print(self.values)


v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5
