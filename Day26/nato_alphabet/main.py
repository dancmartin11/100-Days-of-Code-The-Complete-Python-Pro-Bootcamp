# Import required modules
import pandas as pd

# Declare constants
DATA_PATH = './data/nato_phonetic_alphabet.csv'

# Import NATO alphabet data from csv file
df = pd.read_csv(DATA_PATH)
    
# Convert the extracted DataFrame to a dictionary
nato_dict = {row.letter:row.code for index, row in df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
user_input = input('Enter a word:\n').strip().upper()
user_input = [letter for letter in user_input]

# Extract from dictionary and print result
result = [nato_dict[letter] for letter in user_input if letter in nato_dict]
print(result)