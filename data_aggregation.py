# Main research objective: is NBA salary be modeled as a function of player performance?

# Performance and Salary stats have already been extracted using a handy script
# Data spans from 2008 to 2021
# Load data into SQL tables
# Extract data to answer questions using SQL

#%% Set directory
# import os
# path = os.getcwd()
# print(path)

#%% File dependencies
import pandas as pd
import numpy as np

#%% Creating pandas dataframes

years = [i for i in range(2008, 2022, 1)]
dataframes = []
print(years)
for year in years:
    name = f"salary_{year}"
    name = pd.read_csv(f'./data/pergame_stats_{year}.csv', skipinitialspace=True)
    dataframes.append(name)
    
#%% Viewing dataframe
print(dataframes[0].head())

#%% Define class to handle data

class SalaryData:
    
    def __init__(self, data):
        self.data = data
        
    def data_cleanse(self):
        pass
    
    def remove_dollar_signs(self):
        pass