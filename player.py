
import die

class Player:
    """Creates a player object with 3 die and a score of 0.
    Args:
        None
    Returns:
        A player object with 3 die and a score of 0."""
    def __init__(self):
        """Initializes the player object with 3 die and a score of 0.
        Args:
            None
        Returns:
            None"""
        
        self._die = [die.Die(), die.Die(), die.Die()]  # Create a list of 3 die objects for the player
        self._die.sort()  # Sort the list of die objects in ascending order
        self._points = 0  # Set the player's score to 0

    @property
    def points(self):
        """Returns the points of the player.
        Returns:
            The points of the player."""
        
        return self._points

    def roll_dice(self):
        """Rolls the 3 die and sorts them in ascending order.
        Args:
            None
        Returns:
            None"""
        
        for dice in self._die:  # Roll each die in the list of die objects for the player
            dice.roll()
        self._die.sort()

    def has_pair(self):
        """Checks if the player has a pair of die with the same value.
        Args:
            None
        Returns:
            True if the player has a pair of die with the same value, False otherwise."""
        
        if self._die[0] == self._die[1] == self._die[2]:  # If the player has three of a kind, return False because it is not a pair
            return False
        elif self._die[0] == self._die[1] or self._die[1] == self._die[2] or self._die[0] == self._die[2]:  # If the player has a pair of die with the same value, return True
            self._points += 1
            return True
        else:  # If the player does not have a pair of die with the same value, return False
            return False

    def has_three_of_a_kind(self):
        """Checks if the player has three of a kind of die with the same value.
        Args:
            None
        Returns:
            True if the player has three of a kind of die with the same value, False otherwise"""
        
        if self._die[0] == self._die[1] == self._die[2]:  # If the player has three of a kind of die with the same value, return True
            self._points += 3
            return True
        else:  # If the player does not have three of a kind of die with the same value, return False
            return False

    def has_series(self):
        """Checks if the player has a series of 3 die with consecutive values.
        Args:
            None
        Returns:
            True if the player has a series of 3 die with consecutive values, False otherwise"""
        
        if self._die[1] - self._die[0] == 1 and self._die[2] - self._die[1] == 1:  # If the player has a series of 3 die with consecutive values, return True
            self._points += 2
            return True
        else:  # If the player does not have a series of 3 die with consecutive values, return False
            return False

    def __str__(self):
        """Returns a string representation of the player's die values.
        Args:
            None
        Returns:
            A string representation of the player's die values."""
        
        return "D1=" + str(self._die[0]) + ", D2=" + str(self._die[1]) + ", D3=" + str(self._die[2])



    