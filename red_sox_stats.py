# -*- coding: utf-8 -*-
"""
Get Red Sox batting statisticss from baseball-reference.com

"""
import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd

# Get a page from the web
url = 'https://www.baseball-reference.com/teams/BOS/2018.shtml'
# Save local copy for testing:
# url_to_scrape = '2018.shtml'

response = requests.get(url)
# print(response.status_code)

# Process page from the web.
soup = BeautifulSoup(response.text, 'lxml')

# Or process local file.
# with open('2018.shtml', 'r') as f:
#     soup = BeautifulSoup(f, 'lxml')

table = soup.find('table', id='team_batting')

outer_list = []
for row in table.find_all('tr'):
    inner_list = []
    for cell in row.find_all('td'):
        text = cell.text
        inner_list.append(''.join(text) if text else 'null')
    outer_list.append(inner_list)
    
df = pd.DataFrame(outer_list)
df.columns = ['Pos', 'Name', 'Age', 'G', 'PA', 'AB', 'R', 'H', '2B', \
    '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'SO', 'BA', 'OBP', 'SLG', 'OPS', \
    'OPS+', 'TB', 'GDP', 'HBP', 'SH', 'SF', 'IBB']

df = df[~df['Pos'].isin(['null'])]
df = df.dropna()

# TODO: Remove text in parantheses in Name column.
# Example: (10-day dl)
# var regExp = /\(([^)]+)\)/;

print(df.to_string())







