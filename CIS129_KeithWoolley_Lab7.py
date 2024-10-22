# Lab 7-3 The Dice Game
# Keith Woolley
# 10/21/2024
# The program simulates a dice game, both players are asked to enter their names, dice are simulated, and a winner is then determined

# add libraries as needed
import random

# the main function
def main():
    print()
 # initialize variables
    end_program = "no"
    player_one = "NO NAME"
    player_two = "NO NAME"

 # call to inputNames
    player_one, player_two = inputNames(player_one, player_two)

 # while loop to run program again
    while end_program == 'no':
         # populate variables
        winners_name = "NO NAME"
        p1_number = 0
        p2_number = 0
        # call to rollDice
        winners_name = rollDice(p1_number, p2_number, player_one, player_two, winners_name)
        # call to displayInfo
        displayInfo(winners_name)
        end_program = input('Do you want to end program? (yes/no): ')

#this function gets the players names
def inputNames(player_one, player_two):
    player_one = input("Enter player one's name")
    player_two = input("Enter player two's name")
    return player_one, player_two

#this function will get the random values
def rollDice(p1_number, p2_number, player_one, player_two, winners_name):
    p1_number = random.randint (1, 6)
    p2_number = random.randint (1, 6)
    if p1_number != p2_number:
        if p1_number > p2_number:
            winners_name = player_one
        if p1_number < p2_number:
           winners_name = player_two
    else:
       winners_name = "TIE"
    return winners_name

#this function displays the winner
def displayInfo(winners_name):
   if winners_name == "TIE":
       print (winners_name)
   else:
        print(f'{winners_name} wins!')

# calls
main()