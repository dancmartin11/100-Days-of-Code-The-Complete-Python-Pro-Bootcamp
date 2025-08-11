'''
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 

You are going to create a list called result which contains the numbers that are common in both files. 

e.g. if file1.txt contained: 

1 

2 

3

and file2.txt contained: 

2

3

4

result = [2, 3]



IMPORTANT:  The output should be a list of integers and not strings!

Try to use List Comprehension instead of a Loop. 
'''

# Read data from txt files into lists
with open('./file1.txt', 'r') as file:
    list1 = [int(num.strip()) for num in file.readlines()]
    
with open('./file2.txt', 'r') as file:
    list2 = [int(num.strip()) for num in file.readlines()]

result = [num for num in list1 if num in list2]

print(result)