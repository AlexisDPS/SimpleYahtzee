# Group 10
# Alexis De Paz Salazar
# Broden Black
# Lab Assignment 1 - Description

import check_input
import player

def take_turn(player):
    player.roll_dice()
    print(player)
    if player.has_pair():
        print("You got a pair!")
    elif player.has_series():
        print("You got a series of 3!")
    elif player.has_three_of_a_kind():
        print("You got 3 of a kind!")
    else:
        print("Aww. Too Bad.")
    print(f"Score = {player.points}")
    

def main():
    print("-Yahtzee-")
    current_player = player.Player()
    playing_game = True
    while playing_game:
        take_turn(current_player)
        play_again = check_input.get_yes_no("Play again? (Y/N): ")
        if not play_again:
            playing_game = False
    print("Game Over.")
    print(f"Final Score = {current_player.points}")

if __name__ == "__main__":
    main()
