import random
from os import system


class Engine:
    def roll_d20(self):
        return random.randint(1, 20)

    def roll_d10(self):
        return random.randint(1, 10)

    def roll_d6(self):
        return random.randint(1, 6)
