import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(default=None)
    id: str = field(default=None)

    def __post_init__(self):
        if self.login is not None:
            raise TypeError("Student.__init__() got an unexpected keyword argument 'login'")
        if self.id is not None:
            raise TypeError("Student.__init__() got an unexpected keyword argument 'id'")
        self.id = generate_id()
        self.login = self.name[0] + self.surname


student = Student(name = "Edward", surname = "agle")
print(student)
student = Student(name = "Edward", surname = "agle", id = "toto")
print(student)
