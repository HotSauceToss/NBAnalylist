from bs4 import BeautifulSoup as bs
import requests
from Sheets.write_sheets import SheetsWriter
from Sheets import get_service

SPREADSHEETS = {'Test': '1tEL896ULhVv0hs_lVLztYJgXxA0A2cOdtB6flwiduUM'}
page = requests.get('https://basketball.realgm.com/nba/stats')
page_data = bs(page.content, 'html.parser')
table = page_data.find('table', {'class': 'tablesaw compact'})
# table_data = table.find('tbody')
table_rows = table.find_all('tr')
writer = SheetsWriter(SPREADSHEETS['Test'])
writes = []
writes.append(list(map(lambda a: str(a.get_text()), table.find_all('th'))))
for row in table_rows:
  row_list = list(map(lambda a: str(a.get_text()), row.find_all('td')))
  writes.append(row_list)
writer.append_to_sheet(writes)