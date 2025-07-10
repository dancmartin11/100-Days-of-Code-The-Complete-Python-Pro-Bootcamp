# Read letter and store template into string variable
with open('./Input/Letters/starting_letter.txt', mode = 'r') as letter_file:
    starting_letter = letter_file.read()

print(starting_letter)

# Read names and store each line into a list (each name as an item)
with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

# Remove \n from all names
names = [name.strip() for name in names]

# Iterate over names and generate personalized letters in Output/ReadyToSend folder
for name in names:
    with open(f'./Output/ReadyToSend/{name}_letter.txt', mode = 'w') as output_letter:
        output_letter.write(starting_letter.replace('[name]', name))
        
print('All letters have been generated.')