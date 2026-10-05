# Group 10
# Alexis De Paz Salazar
# Broden Black
# Lab Assignment 1 - Description

import check_input
import die
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

if __name__ == "__main__":
    main()
