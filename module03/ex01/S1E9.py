from abc import ABC, abstractmethod

class Character(ABC):
    """Character Class"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        pass

    def die(self):
        """Die Function"""
        self.is_alive = False

class Stark(Character):
    """Stark Class"""
    def __init__(self, first_name, is_alive=True):
        """Character Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive


# Ned = Stark("Ned")
# print(Ned.__dict__)
# print(Ned.is_alive)
# Ned.die()
# print(Ned.is_alive)
# print(Ned.__doc__)
# print(Ned.__init__.__doc__)
# print(Ned.die.__doc__)
# print("---")
# Lyanna = Stark("Lyanna", False)
# print(Lyanna.__dict__)
# hodor = Character("hodor")
