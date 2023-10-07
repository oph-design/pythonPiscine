from S1E9 import Character


class Baratheon(Character):
    """Baratheon Class"""
    def __init__(self, first_name, is_alive=True):
        """Character Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f"<('{self.first_name}', '{self.eyes}', '{self.hairs}')>"

    def __repr__(self):
        return f"<('{self.first_name}', '{self.eyes}', '{self.hairs}')>"

class Lannister(Character):
    """Lannister Class"""
    def __init__(self, first_name, is_alive=True):
        """Character Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return f"<('{self.first_name}', '{self.eyes}', '{self.hairs}')>"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        lannister = cls(first_name,is_alive)
        return lannister


# Robert = Baratheon("Robert")
# print(Robert.__dict__)
# print(Robert.__str__)
# print(Robert.__repr__)
# print(Robert.is_alive)
# Robert.die()
# print(Robert.is_alive)
# print(Robert.__doc__)
# print("---")
# Cersei = Lannister("Cersei")
# print(Cersei.__dict__)
# print(Cersei.__str__)
# print(Cersei.is_alive)
# print("---")
# Jaine = Lannister.create_lannister("Jaine", True)
# print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")
