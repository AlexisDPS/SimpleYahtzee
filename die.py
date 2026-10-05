
import random

class Die:
    def __init__(self, sides=6):
        self._sides = sides
        self._value = 0

    def roll(self):
        self.value = random.randint(1, self._sides)

    def __str__(self):
        return str(self._value)

    def __lt__(self, other):
        if self._value < other._value:
            return True
        else:
            return False

    def __eq__(self, other):
        if self._value == other._value:
            return True
        else:
            return False

    def __sub__(self, other):
        if self._value > other._value:
            return self._value - other._value
        elif self._value < other._value:
            return other._value - self._value
        else:
            return 0