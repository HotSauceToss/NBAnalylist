from bs4 import BeautifulSoup as bs
import requests
from mongo.write_to_db import writeToMongo

page = requests.get('https://basketball.realgm.com/nba/stats')
page_data = bs(page.content, 'html.parser')
# Get table
table = page_data.find('table', {'class': 'tablesaw compact'})
# Create a list of the table headers
headers = list(map(lambda a: a.get_text(), table.find_all('th')))
# List of documents to append to the mongoDB
documents = []
# Get all the table rows
table_rows = table.find_all('tr')
for row in table_rows:
  # Break up the row into a list of the column entries
  row_list = list(map(lambda a: a.get_text(), row.find_all('td')))
  if(len(row_list) == 0): continue
  doc = {}
  # Create the document
  for i in range(len(row_list)):
    doc[str(headers[i])] = row_list[i]
  # Add the doc to the list
  documents.append(doc)

writeToMongo(documents)