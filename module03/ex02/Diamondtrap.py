from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """GameofThrones BS"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def set_eyes(self, newEyes):
        self.eyes = newEyes

    def set_hairs(self, newHairs):
        self.hairs = newHairs

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs


Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)
