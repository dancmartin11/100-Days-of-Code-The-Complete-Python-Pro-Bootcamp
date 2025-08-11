import random
import pandas as pd

'''
LIST COMPREHENSION
'''

# Create a new list with list comprehension from a list
numbers = [1,2,3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

# Create a new list with list comprehension from a string
name = 'daniel'
new_list = [letter for letter in name]
print(new_list)

# Create a new list with list comprehension from a range
doubled_range = [x * 2 for x in range(1,5)]
print(doubled_range)

'''
CONDITIONAL LIST COMPREHENSION
'''

# Get all names whose length is less or equal than 4 characters
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)

# Get all UPPERCASE names whose length is more than 4 characters
long_upper_names = [name.upper() for name in names if len(name) > 4]
print(long_upper_names)

'''
DICTIONARY COMPREHENSION
'''

# Generate a dictionary with random scores for each student using the names list
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

# Generate a dictionary with students that passed (scores above or equal to 60) from students_scores dictionary
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)

'''
ITERATE OVER PANDAS DATAFRAME
'''

 # Iterate through DataFrame and get Alex score
df = pd.DataFrame(list(student_scores.items()), columns=['student', 'score'])
print(df)

for (index, row) in df.iterrows(): # Iterate row by row
    if row.student == 'Alex':
        print(row.score)