from bs4 import BeautifulSoup as bs
import requests

# page = requests.get('https://basketball.realgm.com/nba/stats')
page = requests.get('http://www.nbaminer.com/nbaminer_nbaminer/basic_stats_pl.php?operation=eexcel&partitionpage=&partition2page=&page=1')
page_data = bs(page.content, 'html.parser')
table = page_data.find('table', {'class': 'tablesaw compact'})
# table_data = table.find('tbody')
table = page_data.find('table')
table_rows = table.find_all('tr')
for row in table_rows:
table_headers = table_rows[0]
for row in table_rows[1:]:
  row_list = list(map(lambda a: a.get_text(), row.find_all('td')))
