# Module 4 Lab
# Keith Woolley
# 9/30/2024
# The program asks for the monthly sales and increase.
# It then calculates store and employee bonuses.

# The main function
def main():
    # declare local variables and run functions to get their values
    monthlySales = getSales('Enter monthly sales: $ ') # monthly sales amount
    salesIncrease = getIncrease('Enter percent of sales increase: ') # percent of sales increase
    storeAmount = calcStoreBonus(monthlySales) # store bonus amount
    empAmount = calcEmpBonus(salesIncrease)  # employee bonus amount

    # call to printBonus()
    printBonus(storeAmount, empAmount)

# This function gets the monthly sales
def getSales(prompt):
 monthlySales = float(input(prompt))
 return monthlySales

# This function gets the percent of increase in sales
def getIncrease(prompt):
    salesIncrease = float(input(prompt))
    salesIncrease = salesIncrease / 100
    return salesIncrease

# This function determines the storeAmount bonus
def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
       storeAmount = 5000
    elif monthlySales >= 90000:
       storeAmount = 4000
    elif monthlySales >= 80000:
       storeAmount = 3000
    else:
       storeAmount = 0
    return storeAmount

# This function determines the empAmount bonus
def calcEmpBonus(salesIncrease):
    if salesIncrease >= .05:
        empAmount = 75
    elif salesIncrease >= .04:
        empAmount = 50
    elif salesIncrease >= .03:
        empAmount = 40
    else: empAmount = 0
    return empAmount

# This function prints the bonus information
def printBonus(storeAmount, empAmount):
    print("The store bonus amount is $", storeAmount )
    print("The employee bonus amount is $", empAmount)
    if (storeAmount == 6000 ) and (empAmount == 75):
        print('Congrats! You have reached the highest bonus amounts possible!')

# calls main
main()