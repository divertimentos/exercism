import string
import random
from random import randint


class Robot(object):
    def __init__(self, char, num):
        self.char = char.upper()
        self.num = num

    def random_name(self, name_length=3):
        letters = string.ascii_uppercase
        return ''.join(random.choice(letters) for i in range(name_length))

    def random_num(self, num_length=3):
        lista = list()

        for i in range(num_length):
            x = randint(0, 9)
            lista.append(x)
        return ','.join(str(lista))

print(Robot.random_name(3))
print(Robot.random_num(3))