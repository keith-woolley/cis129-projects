# Lab 11 (9.2)
# Keith Woolley
# 11/18/2024
# Reads grades.txt and displays the grades, their total, count, and average.

count = 0
total = 0

# Prints each grade and increments count and total.
with open ('grades.txt', mode = 'r') as grades:
    for record in grades:
        grade = int(record)
        print(grade)
        count += 1
        total += grade

# Prints the total, count, and average
print(f'Total of grades: {total}')
print(f'Count of grades: {count}')
print(f'Average of grades: {total/count}')