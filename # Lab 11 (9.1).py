# Lab 11 (9.1)
# Keith Woolley
# 11/18/2024
# Allows the user to enter any number of grades into a text file.

with open ('grades.txt', mode = 'w') as grades:
    while True:
        try:
            user_input = int(input('Enter grade, type -1 to end'))
            if user_input == -1:
                break
            else:
                grades.write(f'{user_input}\n')
        except ValueError:
            print("Enter an integer")