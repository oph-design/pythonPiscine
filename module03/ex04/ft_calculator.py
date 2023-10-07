class calculator:
    """Vector calculator"""

    @classmethod
    def dotproduct(cls, V1: list[float], V2: list[float]) -> None:
        """Calculate Dot product"""
        res = 0
        for x, y in zip(V1, V2):
            res = res + x * y
        print(f"Dot Product is {res}")

    @classmethod
    def add_vec(cls, V1: list[float], V2: list[float]) -> None:
        """Calculate Addition"""
        res = []
        for x, y in zip(V1, V2):
            res.append(x + y)
        print(f"Add is {res}")

    @classmethod
    def sous_vec(cls, V1: list[float], V2: list[float]) -> None:
        """Calculate Substraction"""
        res = []
        for x, y in zip(V1, V2):
            res.append(x - y)
        print(f"Add is {res}")


a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a,b)
calculator.add_vec(a,b)
calculator.sous_vec(a,b)
