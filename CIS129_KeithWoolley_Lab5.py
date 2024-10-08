# Lab 5 The Bottle Return Program
# Keith Woolley
# 10/7/2024
# The program will track the number of bottles returned for the week.
# It will then calculate the total number of bottles returned and the amount paid out and display it to the user.
# Before ending it will ask the user if they want to enter data for another week.

import decimal
from decimal import Decimal

def main():
    # Declare and initialize variables
    total_bottles  = 0 # Total number of bottles this week
    counter = 1 # Day of the week
    today_bottles = 0 # Number of bottles today
    total_payout = 0 # Total payout this week
    keep_going = "y" # Determines if the loop continues to another week

    print(">>>")

    # Loop until the user does not input "y" to go to another week
    while keep_going == "y":
        # Reset variables
        total_payout = 0
        total_bottles = 0
        counter = 1

        # Loop 7 times for each day of the week
        while counter <= 7:
            today_bottles = getTodayBottles(counter)
            total_bottles += today_bottles # Calculate the total number of bottles 
            total_payout = calcTotalPayout(total_bottles)
            counter += 1 # Increment the counter by a day

        # Call to print totals and ask if the user wants to input another week's values
        printTotals(total_bottles, total_payout)
        keep_going = askKeepGoing()

    print(">>>")

# Determine the number of bottles today based on the user's input
def getTodayBottles(counter):
    while True:
        bottles_input = getBottlesInput(counter)
        if bottles_input < 0:
            print ("Value must be positive")
        else:
            return bottles_input

# Get the user to input the number of bottles today
def getBottlesInput(counter):
    while True:
            try:
                bottles_input = int(input(f'Enter number of bottles returned for day #{counter}: '))
            except ValueError:
                print("Value must be an integer")
            else:
                return bottles_input

# Calculate the total payout
def calcTotalPayout(total_bottles):
    total_payout = Decimal(total_bottles * .10)
    return total_payout

# Print the total number of bottles collected and the total paid out
def printTotals(total_bottles, total_payout):
    print("")
    print(f'Total number of bottles collected is {total_bottles}')
    print(f'The total paid out is $ {total_payout:.2f}')

# Ask the user if they want to input another week's values, sets keepGoing to y or n
def askKeepGoing():
    print("")
    while True:
        keep_going = input("Do you want to enter another week's worth of data?\n (Enter y or n): ")
        if keep_going != "y" and keep_going != "n":
            print (f'You must enter "y" or "n"')
        else:
            return keep_going
        
main()
    