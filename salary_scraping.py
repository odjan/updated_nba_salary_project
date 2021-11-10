# author: Oliver Jan
# objective: scrapes salary data from hoopshype.com

#%% Import dependencies
import requests
from urllib import request, response, error, parse
from urllib.request import urlopen
import csv
from bs4 import BeautifulSoup

#%% Years of Interest, 2008 to 2021

start_year = [i for i in range(2008, 2022)]
end_year = [i for i in range(2009,2023)]
years_to_observe = []

for i in range(len(start_year)):
    new_string = f"{start_year[i]}" + "-" + f"{end_year[i]}"
    years_to_observe.append(new_string)

#%% Scraping Each Year

for year in years_to_observe:
    source = requests.get(f'https://hoopshype.com/salaries/players/{year}/').text
    soup = BeautifulSoup(source, 'lxml')
    article = soup.prettify()
    
    table = soup.find('table')
    table_rows = table.find_all('tr')
    table_headers = table.find_all('thead')
    
    headers = ["Player", year]
    csv_file = open(f'./data/salary_{year}.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)
    
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td] #nice list comprehension to get data into lists
        csv_writer.writerow(row)
        
    csv_file.close()
#%% formatting for current year (2021-2022) is off, so must run this manually
current_year = requests = requests.get("https://hoopshype.com/salaries/players/").text
soup = BeautifulSoup(current_year, 'lxml')
article = soup.prettify()

table = soup.find('table')
table_rows = table.find_all('tr')
table_headers = table.find_all('thead')

headers = ["Player", "2021/2022"]
csv_file = open(f'./data/salary_2021_2022.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(headers)

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td] #nice list comprehension to get data into lists
    csv_writer.writerow(row)
    
csv_file.close()
# %%
