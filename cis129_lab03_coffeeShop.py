# Allows the user to request a number of coffees and muffins and calculates the total cost with tax.
# Displays a recipt that shows the user a breakdown of their total cost.

# Sets the price of menu items
coffeePrice = 5.00
muffinPrice = 4.00
cookiePrice = 3.5
teaPrice = 3.00

# Welcomes and requests the user to input how many menu items they bought
print ("***************************************")
print ("My Coffee and Muffin Shop")
print ("Number of coffees bought?")
coffeesBoughtInput = input ("")
print ("Number of muffins bought?")
muffinsBoughtInput = input ("")
print ("Number of cookies bought?")
cookiesBoughtInput = input ("")
print ("Number of teas bought?")
teasBoughtInput = input ("")
print ("***************************************")
print (" ")

# Calculates the costs spent on each menu item and applies tax to a total cost
coffeesBought = int(coffeesBoughtInput)
muffinsBought = int(muffinsBoughtInput)
cookiesBought = int(cookiesBoughtInput)
teasBought = int(teasBoughtInput)
coffeesTotalCost = coffeesBought * coffeePrice
muffinsTotalCost = muffinsBought * muffinPrice
cookiesTotalCost = cookiesBought * cookiePrice
teasTotalCost = teasBought * teaPrice
totalCostBeforeTax = coffeesTotalCost + muffinsTotalCost + cookiesTotalCost + teasTotalCost
tax = totalCostBeforeTax * 0.06
totalCost = totalCostBeforeTax + tax

# Prints the recipt
print ("***************************************")
print ("My Coffee and Muffin Shop Receipt")
print (f"{coffeesBought} Coffee at ${coffeePrice:.2f} each: $ {coffeesTotalCost:.2f}")
print (f"{muffinsBought} Muffins at ${muffinPrice:.2f} each: $ {muffinsTotalCost:.2f}")
print (f"{cookiesBought} Cookies at ${cookiePrice:.2f} each: $ {cookiesTotalCost:.2f}")
print (f"{teasBought} Tea at ${teaPrice:.2f} each: $ {teasTotalCost:.2f}")
print (f"6% tax: $ {tax:.2f}")
print("---------")
print(f"Total: $ {totalCost:.2f}")
print ("***************************************")
print ("Thank you for your purchase!")
