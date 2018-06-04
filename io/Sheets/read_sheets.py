from get_service import service


SPREADSHEET_ID = '1tEL896ULhVv0hs_lVLztYJgXxA0A2cOdtB6flwiduUM'
RANGE_NAME = 'Test!A2:B2'
s = service()
result = s.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()

values = result.get('values', [])
print(values)
