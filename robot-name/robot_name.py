import string
import random
from random import randint


class Robot(object):
    def __init__(self):
        self.name = self.random_name() + self.random_num()

    def random_name(self, name_length=2):
        letters = string.ascii_uppercase
        name = ''.join(random.choice(letters) for i in range(name_length))
        return name

    def random_num(self, num_length=3):
        num = list()

        for i in range(num_length):
            x = randint(0, 9)
            num.append(x)

        num = ''.join(map(str, num))
        return num

    def get_name(self):
        return self.name

    def reset(self):
        name = Robot.__init__(self)
        return self.name


robot = Robot()

print(f"Nome da instância: {robot.__class__.__name__} | Nome do robô: {robot.get_name()}")

print(f"Nome da instância: {robot.__class__.__name__} | Novo nome: {robot.reset()}")

print(robot.get_name())