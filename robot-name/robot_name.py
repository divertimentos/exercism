import string
import random
from random import randint


class Robot(object):
    def __init__(self):
        self.name = f"{self.random_name()}{self.random_num()}"

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
        self.name2 = self.random_name() + self.random_num()
        return self.name2
    
        # self.name2 = self.random_name() + self.random_num()
        # if self.name2 != self.name:
        #     self.name = self.name2
        #     return self.name



robot = Robot()
print(f"Instância robot | Nome do robô: {robot.get_name()}")
print(f"Instância robot | Novo nome: {robot.reset()}")
print(f"Método get name: {robot.get_name()}")

print("\n")

droid = Robot()
print(f"Instância droid | Nome do robô: {droid.get_name()}")
print(f"Método get_name: {droid.get_name()}")
print(f"Instância robot | Novo nome: {droid.reset()}")

print(droid.name == droid.name2)