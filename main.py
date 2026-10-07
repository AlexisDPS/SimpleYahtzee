# Group 10
# Alexis De Paz Salazar
# Broden Black
# A similar game to Yahtzee that uses 3 die instead of the regular 5. 
# The player rolls the die and they can land in a pair, series, or three of a kind. 
# Each give the player 1, 2, or 3 points respectively. If none of these are rolled then
# the player doesn't get any points. The player can choose to play again or quit the game.
# Every roll is random and the score is displayed after each turn. Once the player
# chooses to quit the game, the final score is displayed.

import check_input
import player

def take_turn(player):
    """Takes a turn for the player by rolling the dice and checking for pairs, series, or three of a kind.
    Args:
        player: The player object.
    Returns:
        None"""
    
    player.roll_dice()  # Rolls 3 die for the player
    print(player)  # Prints values of the 3 die

    if player.has_pair():  # Checks if the player has a pair with the same value
        print("You got a pair!")
    elif player.has_series():  # Checks if the player has a series with consecutive values
        print("You got a series of 3!")
    elif player.has_three_of_a_kind():  # Checks if the player has three die with the same value
        print("You got 3 of a kind!")
    else:  # If the player doesn't have a pair, series, or three of a kind
        print("Aww. Too Bad.")

    print(f"Score = {player.points}")  # Prints the player's score after their turn
    

def main():
    """Main function to run the Yahtzee game.
    Args:
        None
    Returns:
        None"""
    
    print("-Yahtzee-")
    current_player = player.Player()  # Create a player object
    playing_game = True  # Sets the playing_game variable to True for the game loop

    while playing_game:  # Loops the game until the player chooses to stop
        print()
        take_turn(current_player)  # Calls the take_turn function to roll the dice and check for points
        play_again = check_input.get_yes_no("Play again? (Y/N): ")  # Ask the player if they want to play again
        if not play_again:  # If the player does not want to play again, ends the loop with playing_game set to False
            playing_game = False

    print()
    print("Game Over.")  # Prints that the game is over
    print(f"Final Score = {current_player.points}")  # Prints the player's final score

if __name__ == "__main__":
    """Runs the main function to start the game."""
    main()
