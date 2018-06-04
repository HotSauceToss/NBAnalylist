from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import client, file, tools

## Return Google Sheets API service
def service():
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    store = file.Storage('res/credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('res/client_key_google_sheets_api.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))
    return service

