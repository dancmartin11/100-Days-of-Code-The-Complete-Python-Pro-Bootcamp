# Import required modules
import pandas as pd

# Define constants
DATA_PATH = './data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
OUTPUT_PATH = './data/squirrel_count.csv'

# Read squirel data
df = pd.read_csv(DATA_PATH, parse_dates = True)
print(df.head())

# See DataFrame information
df.info()

# Group values by fur color and format DataFrame
df_color_count = df.groupby('Primary Fur Color', as_index = False)['Unique Squirrel ID'].count()
df_color_count.rename(columns = {'Primary Fur Color': 'Fur Color', 'Unique Squirrel ID': 'Count'}, inplace = True)
df_color_count.sort_values(by = 'Count', ascending = False, inplace = True)

print(df_color_count)

#Export DataFrame to csv file
df_color_count.to_csv(OUTPUT_PATH)