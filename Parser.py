from bs4 import BeautifulSoup as bs
import requests
from postgres.connect import connect

conn = connect('player-stats', 'nba-dev', 'nba-dev')
cur = conn.cursor()

# page = requests.get('https://basketball.realgm.com/nba/stats')
page = requests.get('http://www.nbaminer.com/nbaminer_nbaminer/basic_stats_pl.php?operation=eexcel&partitionpage=&partition2page=&page=1')
page_data = bs(page.content, 'html.parser')
table = page_data.find('table')
table_rows = table.find_all('tr')
# Table stores headers as a table row
table_headers = table_rows[0]
# Iterate index 1..rows
for row in table_rows[1:]:
  row_list = list(map(lambda a: a.get_text(), row.find_all('td')))
  # Col 1 is First + Last name
  # Needs to be split before inserting into the db 
  print(row_list)
