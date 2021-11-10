#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 13:11:03 2021

@author: oliver
"""

#%% Import package dependencies

import requests
from urllib import request, response, error, parse
from urllib.request import urlopen
import csv
from bs4 import BeautifulSoup

#%% Declare Years

# for sake of simplicity, I want to see complete seasons

years_of_interest = [i for i in range(2008,2022,1)]


#%% find stastistical data for each year

for year in years_of_interest:
    source = requests.get(f'https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html').text
    
    soup = BeautifulSoup(source, 'lxml')
    
    article = soup.prettify()
    
    # Finding Steven Adams
    table = soup.find('table')
    table_rows = table.find_all('tr')
    table_headers = table.find_all('th')
    
    # Tried to retrieve headers, but failed at this. Will try to do better next time.
    """ headers =[] 
    for i in table_headers:
        column_id = i.text
        headers.append(column_id) """
    
    headers = ['Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
    
    csv_file = open(f'./data/pergame_stats_{year}.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)
    
    
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td] #nice list comprehension to get data into lists
        csv_writer.writerow(row)
    
    csv_file.close()
    
#%% find salary data for each player for each year
