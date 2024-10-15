# Lab 6 Hotdog Cookout Lab
# Keith Woolley
# 10/14/2024
# The program ask the user how many attendees will be at the cookout and how many hot dogs each attendee needs.
# It will then calculate the number of hot dogs and buns packages needed and how many hot dogs and buns will remain.
# Lastly, it will display that information.

# Calculate the total number of hot dogs needed by multiplying attendees by the number of hot dogs per attendee
def getTotalHotDogs():
    attendees = getAttendees()
    hotdogs_per_attendee = getHotDogsPerAttendee()
    total_hotdogs = attendees * hotdogs_per_attendee
    return total_hotdogs
            
# Get the amount of attendees from the user
def getAttendees():
     while True:
            try:
                attendees = int(input("How many attendees are coming to the cookout?"))
                if attendees > 0:
                     return attendees
                else:
                     print("You must enter a positive integer")
            except ValueError:
                print("Value must be an integer")

# Get the number of hot dogs per attendee from the user
def getHotDogsPerAttendee():
     while True:
            try:
                hotdogs_per_attendee = int(input("How many hot dogs should each attendee be given?"))
                if hotdogs_per_attendee > 0:
                     return hotdogs_per_attendee
                else:
                     print("You must enter a positive integer")
            except ValueError:
                print("Value must be an integer")
            
# Calculate the number of hot dogs and buns packages required and the amount of hot dogs and buns left.
# The results are then displayed to the user       
def showResults(total_hotdogs):
     DOGS = 10
     BUNS = 8

     hotdogs_left = (DOGS - total_hotdogs % DOGS) % DOGS
     min_hotdog_packages = (total_hotdogs / DOGS) + (0 ** (0 ** hotdogs_left))

     buns_left = (BUNS - total_hotdogs % BUNS) % BUNS
     min_bun_packages = (total_hotdogs / BUNS) + (0 ** (0 ** buns_left))

     print(f'Minumum packages of hot dogs needed: {int(min_hotdog_packages)}')
     print(f'Minumum packages of buns needed: {int(min_bun_packages)}')

     print(f'Hot dogs remaining: {hotdogs_left}')
     print(f'Buns remaining: {buns_left}')

total_hotdogs = getTotalHotDogs()

showResults(total_hotdogs)