import csv
import pandas as pd

# Define data path
WEATHER_DATA = './data/weather_data.csv'

'''
Method 1 to read CSV data: open -> readlines
'''
# Read each line into a list
with open(WEATHER_DATA, 'r') as file:
    weather_list = file.readlines()

# Strip the values in the list to get rid of \n
weather_list = [x.strip() for x in weather_list]
print('Method 1\n', weather_list)

'''
Method 2 to read CSV data: CSV library
'''
# Read folder and append each value into list (as soon as file is closed, csv object is not accessible)
with open(WEATHER_DATA, 'r') as file:
    reader = csv.reader(file)
    csv_data = [x for x in reader]
print('Method 2\n', csv_data)

#Challenge: put temperatures as integers in a list
temperatures = [int(x[1]) for x in csv_data[1:]] # Exclude header
print('\tTemperatures:\n', '\t', temperatures)

'''
Method 3 to read CSV data: PANDAS!!!!!!!
'''
# Read Pandas DataFrame
df = pd.read_csv(WEATHER_DATA)
print(df)

'''
Pandas functions
'''

# Convert DataFrame to dictionary
data_dict = df.to_dict()
print(data_dict)

# Convert Pandas Series to list
temp_list = df['temp'].to_list()
print(temp_list)

# Get mean and max value
print('Temp mean: ', df['temp'].mean())
print('Temp max: ', df['temp'].max())

# Get all the row with the data with max temperature
print(df[df['temp'] == df['temp'].max()])

# Convert Monday temp to Fahrenheit
print('Monday temperature in Fahrenheit: ', df[df['day'] == 'Monday']['temp'].values * 9/5 + 32)