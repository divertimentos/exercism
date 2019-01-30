import string
import random


class Robot(object):
    def __init__(self):
        self.reset()
    
    def random_name(self, name_length=2):
        letters = string.ascii_uppercase
        name = ''.join(random.choice(letters) for i in range(name_length))
        return name

    def random_num(self, num_length=3):
        num = list()
        for i in range(num_length):
            x = random.randint(0, 9)
            num.append(x)
        num = ''.join(map(str, num))
        return num

    def reset(self):
        self.name = f"{self.random_name()}{self.random_num()}"
        return self.name


robot = Robot()

print(f"Nome original: {robot.name}")

robot.reset()

name2 = robot.name

print(f"Novo nome: {name2}")
