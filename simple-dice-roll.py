''' simple-dice-roll.py by Devin Carter 08/18/2017
this program simulates rolling dice
'''
import random

# define main function
def rollTheDice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    totalValue = die1 + die2
    user = input("Would you like to roll again? Y/N ")

    if (user == "Y" or user == "y"):
        print("You rolled: ", totalValue)
        rollTheDice()
    elif (user == "N" or user == "n"):
        print("Thanks for rolling")


rollTheDice()




