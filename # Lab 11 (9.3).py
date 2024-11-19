# Lab 11 (9.3)
# Keith Woolley
# 11/18/2024
# Allows the user to enter records into a text file, consisting of first name, last name, and exam grades.

import csv

def main():
    input_stage = 1
    
    # Main loop
    with open ('grades.csv', mode = 'w', newline = '') as grades:
        writer = csv.writer(grades)
        while True:
            while input_stage < 6: # Gets input for each value by calling getInput.
                if input_stage == 1:
                    first_name = getInput(input_stage)
                elif input_stage == 2:
                    last_name = getInput(input_stage)
                elif input_stage == 3:
                    exam_1_grade = getInput(input_stage)
                elif input_stage == 4:
                    exam_2_grade = getInput(input_stage)
                elif input_stage == 5:
                    exam_3_grade = getInput(input_stage)
                input_stage += 1

            # Create the record, reset the input stage, and ask if the user wants to stop the program.
            writer.writerow([first_name, last_name, exam_1_grade, exam_2_grade, exam_3_grade])
            input_stage = 1
            if input('Enter y to stop') == 'y':
                break

# Uses the input stage to determine which type of input is needed and returns the input.
def getInput(input_stage):
    if input_stage == 1:
        to_return = (input('Enter first name'))
        return to_return
    
    elif input_stage == 2:
        to_return = (input('Enter last name'))
        return to_return
    
    elif input_stage > 2 and input_stage < 6:
        exam_number = input_stage - 2
        while True:
            try:
                to_return = int(input(f'Enter exam {exam_number}'))
                if to_return < 0:
                    print('Enter a positive value')
                else:
                    return to_return
            except ValueError:
                print("Enter an integer")

main()