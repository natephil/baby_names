import pandas as pd
from pathlib import Path

# set path to directory with all names files
p = Path('/Users/nathancahn/baby_names/0_data/names_national/')

# all .csv files in path are now callable
files = [file for file in p.iterdir() if file.suffix == '.csv']

big_dataframe_list = [] # create an empty list to put your dataframes in

# iterate over each file and load into pandas
# create list of dataframes
for filename in files:
    big_dataframe_list.append(pd.read_csv(filename, header=None))

# add column names to each dataframe in dataframe list
for i in range(len(big_dataframe_list)):
    big_dataframe_list[i].columns=['name','gender','frequency']

# add a new column named year
# populate it with the year that dataframe's data is from
for i in range(len(big_dataframe_list)):
    year = 1880 + i
    big_dataframe_list[i]['year'] = year