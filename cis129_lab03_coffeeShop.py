# Allows the user to request a number of coffees and muffins and calculates the total cost with tax.
# Displays a recipt that shows the user a breakdown of their total cost.

# Sets the price of menu items
coffeePrice = 5.00
muffinPrice = 4.00

# Welcomes and requests the user to input how many menu items they bought
print ("***************************************")
print ("My Coffee and Muffin Shop")
print ("Number of coffees bought?")
coffeesBoughtInput = input ("")
coffeesBought = int(coffeesBoughtInput)
print ("Number of muffins bought?")
muffinsBoughtInput = input ("")
print ("***************************************")
print (" ")

# Calculates the costs spent on each menu item and applies tax to a total cost
muffinsBought = int(muffinsBoughtInput)
coffeeTotalCost = coffeesBought * coffeePrice
muffinTotalCost = muffinsBought * muffinPrice
totalCostBeforeTax = coffeeTotalCost + muffinTotalCost
tax = totalCostBeforeTax * 0.06
totalCost = totalCostBeforeTax + tax

# Prints the recipt
print ("***************************************")
print ("My Coffee and Muffin Shop Receipt")
print (f"{coffeesBought} Coffee at ${coffeePrice:.2f} each: $ {coffeeTotalCost:.2f}")
print (f"{muffinsBought} Muffins at ${muffinPrice:.2f} each: $ {muffinTotalCost:.2f}")
print (f"6% tax: $ {tax}")
print("---------")
print(f"Total: $ {totalCost}")
print ("***************************************")

