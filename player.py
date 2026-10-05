
import die

class Player:
    def __init__(self):
        self._die = [die.Die(), die.Die(), die.Die()]
        self._die.sort()
        self._points = 0

    @property
    def points(self):
        return self._points

    def roll_dice(self):
        for dice in self._die:
            dice.roll()
        self._die.sort()

    def has_pair(self):
        if self._die[0] == self._die[1] == self._die[2]:
            return False
        elif self._die[0] == self._die[1] or self._die[1] == self._die[2] or self._die[0] == self._die[2]:
            self._points += 1
            return True
        else:
            return False

    def has_three_of_a_kind(self):
        if self._die[0] == self._die[1] == self._die[2]:
            self._points += 3
            return True
        else:
            return False

    def has_series(self):
        if self._die[1] - self._die[0] == 1 and self._die[2] - self._die[1] == 1:
            self._points += 2
            return True
        else:
            return False

    def __str__(self):
        return "D1=" + str(self._die[0]) + ", D2=" + str(self._die[1]) + ", D3=" + str(self._die[2])



    