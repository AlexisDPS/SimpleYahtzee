
import random

class Die:
    """Creates a die object with a set amount of sides such as 6. 
    Args:
        sides: The number of sides on the die. Default is 6.
    Returns:
        A die object with a random value between 1 and the number of sides."""
    
    def __init__(self, sides=6):
        """Initializes the die object with a set number of sides and a value of 0.
        Args:
            sides: The number of sides on the die. Default is 6.
        Returns:
            None"""
        
        self._sides = sides  # Set the number of sides on the die to the value passed in as an argument
        self._value = 0  # Set the value of the die to 0

    def roll(self):
        """Rolls the die and sets the value to a random integer between 1 and the number of sides.
        Returns:
            The value of the die."""
        
        self._value = random.randint(1, self._sides)  # Set the value of the die to a random integer between 1 and the number of sides
        return self._value

    def __str__(self):
        """Returns a string representation of the die's value.
        Returns:
            A string representation of the die's value."""
        
        return str(self._value)

    def __lt__(self, other):
        """Returns True if the value of this die is less than the value of another die.
        Returns:
            True if the value of this die is less than the value of another die, False otherwise."""
        
        if self._value < other._value:  # If the value of this die is less than the value of another die, return True
            return True
        else:  # If the value of this die is not less than the value of another die, return False
            return False

    def __eq__(self, other):
        """Returns True if the value of this die is equal to the value of another die."""
        
        if self._value == other._value:  # If the value of this die is equal to the value of another die, return True
            return True
        else:  # If the value of this die is not equal to the value of another die, return False
            return False

    def __sub__(self, other):
        """Returns the difference between the value of this die and the value of another die.
        Returns:
            The difference between the value of this die and the value of another die."""
        
        if self._value > other._value:  # If the value of this die is greater than the value of another die, return the difference between the two values
            return self._value - other._value
        elif self._value < other._value:  # If the value of this die is less than the value of another die, return the difference between the two values
            return other._value - self._value
        else:  # returns 0 if the value of this die is equal to the value of another die.
            return 0