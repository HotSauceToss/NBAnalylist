from bs4 import BeautifulSoup as bs
import requests

page = requests.get('https://basketball.realgm.com/nba/stats')
page_data = bs(page.content, 'html.parser')
table = page_data.find('table', {'class': 'tablesaw compact'})
# table_data = table.find('tbody')
table_rows = table.find_all('tr')
for row in table_rows:
  row_list = list(map(lambda a: a.get_text(), row.find_all('td')))
  print(','.join(row_list[1:])) 